"""Bhashini (National Language Translation Mission - MeitY) integration.

Provides official Government of India AI4Bharat / ULCA translation (NMT)
pipeline connectivity for 22 scheduled Indian languages, enabling high-quality
bilingual and multilingual legal and regulatory assistance across English, Hindi,
Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, and more.
"""
from __future__ import annotations

import json
import logging
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger("ipsakti.bhashini")

BHASHINI_PIPELINE_URL = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"
DEFAULT_PIPELINE_ID = "64392f96daac500b55c543cd"

DATA_DIR = Path(__file__).resolve().parent / "data"
I18N_CACHE_DIR = DATA_DIR / "i18n_cache"

# Standard Bhashini / ISO language code mapping with native script names
# Supporting all 22 official Indian languages (Eighth Schedule of Constitution of India) + English
SUPPORTED_LANGUAGES: Dict[str, Dict[str, str]] = {
    "en": {"name": "English", "native": "English", "script": "Latn"},
    "as": {"name": "Assamese", "native": "অসমীয়া", "script": "Beng"},
    "bn": {"name": "Bengali", "native": "বাংলা", "script": "Beng"},
    "brx": {"name": "Bodo", "native": "बड़ो", "script": "Deva"},
    "doi": {"name": "Dogri", "native": "डोगरी", "script": "Deva"},
    "gom": {"name": "Konkani", "native": "कोंकणी", "script": "Deva"},
    "gu": {"name": "Gujarati", "native": "ગુજરાતી", "script": "Gujr"},
    "hi": {"name": "Hindi", "native": "हिन्दी", "script": "Deva"},
    "kn": {"name": "Kannada", "native": "ಕನ್ನಡ", "script": "Knda"},
    "ks": {"name": "Kashmiri", "native": "कॉशुर / کٲشُر", "script": "Arab"},
    "mai": {"name": "Maithili", "native": "मैथिली", "script": "Deva"},
    "ml": {"name": "Malayalam", "native": "മലയാളം", "script": "Mlym"},
    "mni": {"name": "Manipuri", "native": "মৈতৈলোন্", "script": "Beng"},
    "mr": {"name": "Marathi", "native": "मराठी", "script": "Deva"},
    "ne": {"name": "Nepali", "native": "नेपाली", "script": "Deva"},
    "or": {"name": "Odia", "native": "ଓଡ଼ିଆ", "script": "Orya"},
    "pa": {"name": "Punjabi", "native": "ਪੰਜਾਬੀ", "script": "Guru"},
    "sa": {"name": "Sanskrit", "native": "संस्कृतम्", "script": "Deva"},
    "sat": {"name": "Santali", "native": "संताली / ᱥᱟᱱᱛᱟᱲᱤ", "script": "Olck"},
    "sd": {"name": "Sindhi", "native": "सिन्धी / سنڌي", "script": "Arab"},
    "ta": {"name": "Tamil", "native": "தமிழ்", "script": "Taml"},
    "te": {"name": "Telugu", "native": "తెలుగు", "script": "Telu"},
    "ur": {"name": "Urdu", "native": "اُردُو", "script": "Arab"},
}

UI_BUNDLE_EN: Dict[str, str] = {
    "brandSub": "AI Assistant for Ayurvedic IP & Regulatory Guidance",
    "navChat": "Chat Assistant",
    "navClassifier": "Formulation Classifier",
    "navGis": "GIS & Geo-Origin",
    "navGraph": "Knowledge Graph",
    "navForms": "Forms & Registries",
    "navAudit": "DPDP Audit Trail",
    "navAbout": "About",
    "navHelp": "Help",
    "tagline": "Traditional Knowledge. Protected Future.",
    "healthChecking": "Checking service…",
    "healthOk": "Service online",
    "healthDown": "Service offline",
    "jurisdiction": "Jurisdiction",
    "formulation": "Formulation class",
    "language": "Language",
    "autoDetect": "Auto-detect",
    "chatHint": "Ask an India or International IP / regulatory question about an Ayurvedic product.",
    "classifierHint": "Answer the guided questions — the classifier sorts your product into its regulatory category.",
    "gisHint": "Ayurveda Geographical Indications (GI), BDA §10(4)(d) origin disclosure and remote sensing habitat analysis.",
    "graphHint": "Interactive relational knowledge graph: Formulations → Statutes → Case Law → International Treaties.",
    "formsHint": "Official IP India, NBA, FoSCoS and WIPO statutory forms, fee calculators and portal links.",
    "auditHint": "Tamper-evident audit trail aligned with Digital Personal Data Protection Act 2023.",
    "aboutHint": "What IP-SAKTI Sahayak does and how it stays safe.",
    "helpHint": "How to use the assistant, and how to read its answers.",
    "escalateBtn": "Escalate to Human Facilitator",
    "voiceInput": "Voice Input",
    "readAloud": "Read Aloud",
    "jurisdictionNoteIndia": "India jurisdiction — answers stay within Indian law and never blend with international guidance.",
    "jurisdictionNoteIntl": "International jurisdiction — answers cover treaties and international filing routes only, never Indian procedure.",
    "demoTitle": "Quick demo scenarios",
    "demo1": "Classical Patent",
    "demo1sub": "Section 3(p) & TKDL for classical formulations",
    "demo2": "ABS / Plant Approvals",
    "demo2sub": "Biological Diversity Act route for plant-based products",
    "demo3": "Formulation Classification",
    "demo3sub": "Guided M2 questionnaire — food vs medicine",
    "demo4": "GI Registration",
    "demo4sub": "Geographical Indication for a region-tied product",
    "demo5": "International Patent",
    "demo5sub": "PCT route for filing outside India",
    "welcomeTitle": "Namaste. How can I help with your Ayurvedic product?",
    "welcomeSub": "Every answer is grounded in a curated corpus of real legal sources, with citations and a confidence level. When evidence is insufficient, I say so instead of guessing.",
    "askPlaceholder": "Ask an Ayurvedic IP / regulatory question…",
    "composerHint": "Information only — not legal advice. Answers cite their sources; insufficient evidence is declined, not guessed.",
    "answerLabel": "Answer",
    "confidenceLabel": "Confidence",
    "sourcesLabel": "Sources",
    "abstainTitle": "Insufficient verified evidence",
    "abstainNote": "The assistant declines rather than guess. You may rephrase the question or consult the official sources shown in Help.",
    "openClassifier": "Open the Formulation Classifier",
    "errNetwork": "Could not reach the IP-SAKTI service. Check that the backend is running, then try again.",
    "errValidation": "The request could not be processed. Please adjust your input and try again.",
    "errProcessing": "A temporary processing error occurred while preparing this answer. Nothing was answered — please try again.",
    "errUnavailable": "This capability is not available in the current build. Please try again later.",
    "errGeneric": "Something went wrong while handling the request. Please try again.",
    "newChat": "New conversation",
    "responseMeta": "Response",
    "noResponseYet": "No response yet — ask a question to see confidence, status and routing details.",
    "specialists": "Connected specialists",
    "loading": "Loading…",
    "sourcesTitle": "Sources & citations",
    "noSources": "Citations from the latest answer will appear here.",
    "disclaimerTitle": "Disclaimer",
    "disclaimerBody": "IP-SAKTI Sahayak provides general information, not legal advice. Answers are generated from a curated corpus of public sources and may be incomplete or outdated. Verify against official sources and consult a qualified IP professional before acting.",
    "statusAnswered": "Answered",
    "statusAbstained": "Abstained",
    "statusError": "Error",
    "answeredIn": "Answered in {s} s",
    "abstainedIn": "Declined in {s} s",
    "rowJurisdiction": "Jurisdiction",
    "rowLanguage": "Language",
    "rowFormulation": "Formulation class",
    "rowSources": "Sources",
    "rowTime": "Response time",
    "rowConfidence": "Confidence",
    "rowStatus": "Status",
    "specIndia": "India IP & Regulatory",
    "specAbs": "ABS / TKDL / Traditional Knowledge",
    "specIntl": "International IP",
    "specCls": "Formulation Classifier",
    "specCentral": "Central assistant (routing & assembly)",
    "classifierTitle": "Formulation Classifier",
    "classifierIntro": "Answer the guided questions below. The deterministic classifier sorts your product into a regulatory category — medicine, food (Ayurveda-Aahar), cosmetic and more — and maps the relevant regimes. Incomplete or contradictory answers safely yield Uncertain rather than a guess.",
    "loadingQuestions": "Loading guided questions…",
    "classifyBtn": "Classify formulation",
    "resetBtn": "Reset",
    "relevantRegimes": "Relevant regimes",
    "clarificationNeeded": "Clarification needed",
    "suggestedQuestions": "Suggested follow-up questions",
    "reasoningTrace": "Classification reasoning trace",
    "tkdlHeading": "TKDL pointer",
    "noClassification": "Answer the questions and press “Classify formulation” — the result will appear here.",
    "resultConfidence": "Confidence",
    "clsFormulation": "Formulation class",
    "aboutTitle": "About IP-SAKTI Sahayak",
    "aboutLead": "A source-cited assistant for Ayurvedic intellectual property and regulatory guidance — across national and international regimes, in English and Hindi.",
    "aboutHow": "What the system does",
    "aboutSafety": "Safety principles",
    "aboutBuild": "How it is built",
    "helpTitle": "Help",
    "helpAsk": "Asking a question",
    "helpAskBody": "Pick a jurisdiction and language in the top bar, then ask in plain language — or start from a Quick demo scenario card. Follow-up questions work: keep them short and the assistant resolves them against the previous turn.",
    "helpJurisdiction": "Jurisdiction",
    "helpIndia": "answers Indian law: Patents Act, GI Act, Trade Marks, D&C Act, FSSAI, Biological Diversity Act.",
    "helpIntl": "answers treaties and routes: TRIPS, WIPO GRATK, PCT, Madrid, Hague. The two answer-sets are never conflated — the toggle is authoritative.",
    "helpMap": "System reminder:",
    "helpConfidence": "Confidence & abstention",
    "helpConfBody": "Every answer carries a confidence level (HIGH / MEDIUM / LOW) computed from evidence strength. When the curated corpus cannot support an answer, the assistant declines openly — you will see an “insufficient verified evidence” state with the reason. That is a safety feature, not an error.",
    "helpClassifier": "Formulation Classifier",
    "helpClsBody": "Open the Formulation Classifier and answer the guided questions (in English or Hindi). The classifier is deterministic — the same answers always produce the same category — and incomplete or contradictory answers yield Uncertain with a clarification prompt instead of a guess.",
    "helpSources": "Sources",
    "helpSourcesBody": "Citations link to official portals — India Code, IP India, the National Biodiversity Authority, CDSCO, FSSAI, WIPO and WTO. TKDL (tkdl.res.in) is referenced as a pointer: its detailed contents are available to patent offices, not the public.",
    "helpLimits": "Limitations",
    "helpLimitsBody": "This is a hackathon MVP over a small curated corpus. It provides general information, not legal advice — verify with the official sources or a qualified professional before acting. A human IP-facilitator escalation path is not part of this build."
}

UI_BUNDLE_HI: Dict[str, str] = {
    "brandSub": "आयुर्वेदिक IP एवं नियामक मार्गदर्शन हेतु AI सहायक",
    "navChat": "चैट सहायक",
    "navClassifier": "फॉर्मूलेशन वर्गीकरण",
    "navGis": "जीआईएस एवं भू-उत्पत्ति",
    "navGraph": "ज्ञान आलेख",
    "navForms": "वैधानिक प्रपत्र",
    "navAudit": "डीपीडीपी ऑडिट ट्रेल",
    "navAbout": "परिचय",
    "navHelp": "सहायता",
    "tagline": "पारंपरिक ज्ञान। सुरक्षित भविष्य।",
    "healthChecking": "सेवा जाँची जा रही है…",
    "healthOk": "सेवा ऑनलाइन है",
    "healthDown": "सेवा उपलब्ध नहीं",
    "jurisdiction": "क्षेत्राधिकार",
    "formulation": "फॉर्मूलेशन वर्ग",
    "language": "भाषा",
    "autoDetect": "स्वतः पहचान",
    "chatHint": "आयुर्वेदिक उत्पाद से जुड़े भारत या अंतरराष्ट्रीय IP / नियामक प्रश्न पूछें।",
    "classifierHint": "निर्देशित प्रश्नों के उत्तर दें — वर्गीकरण आपके उत्पाद को उसकी नियामक श्रेणी में रखता है।",
    "gisHint": "आयुर्वेदिक भौगोलिक संकेत (जीआई), बीडीए धारा १०(४)(घ) भू-उत्पत्ति घोषणा एवं उपग्रह पर्यावरण विश्लेषण।",
    "graphHint": "परस्पर संबंधित ज्ञान आलेख: फॉर्मूलेशन → विधियाँ → न्यायिक निर्णय → अंतरराष्ट्रीय संधियाँ।",
    "formsHint": "आईपी इंडिया, एनबीए, फोस्कोस एवं विपो के आधिकारिक वैधानिक प्रपत्र व शुल्क।",
    "auditHint": "डिजिटल व्यक्तिगत डेटा संरक्षण अधिनियम २०२३ के अनुरूप ऑडिट ट्रेल।",
    "aboutHint": "IP-SAKTI सहायक क्या करता है और कैसे सुरक्षित रहता है।",
    "helpHint": "सहायक का उपयोग कैसे करें और उत्तर कैसे पढ़ें।",
    "escalateBtn": "मानव विशेषज्ञ से परामर्श लें",
    "voiceInput": "आवाज़ से बोलें",
    "readAloud": "उत्तर सुनें",
    "jurisdictionNoteIndia": "भारत क्षेत्राधिकार — उत्तर केवल भारतीय कानून तक सीमित रहते हैं, अंतरराष्ट्रीय मार्गदर्शन के साथ मिश्रित नहीं होते।",
    "jurisdictionNoteIntl": "अंतरराष्ट्रीय क्षेत्राधिकार — उत्तर केवल संधियों और अंतरराष्ट्रीय दाखिला मार्गों को कवर करते हैं, भारतीय प्रक्रिया को नहीं।",
    "demoTitle": "त्वरित डेमो परिदृश्य",
    "demo1": "क्लासिकल पेटेंट",
    "demo1sub": "क्लासिकल फॉर्मूलेशन हेतु धारा 3(p) और TKDL",
    "demo2": "ABS / पौधा-अनुमतियाँ",
    "demo2sub": "पौधे-आधारित उत्पादों हेतु जैव विविधता अधिनियम मार्ग",
    "demo3": "फॉर्मूलेशन वर्गीकरण",
    "demo3sub": "निर्देशित प्रश्नावली — भोजन बनाम औषधि",
    "demo4": "GI पंजीकरण",
    "demo4sub": "क्षेत्र-बद्ध उत्पाद हेतु भौगोलिक संकेत",
    "demo5": "अंतरराष्ट्रीय पेटेंट",
    "demo5sub": "भारत के बाहर दाखिले हेतु PCT मार्ग",
    "welcomeTitle": "नमस्ते। आपके आयुर्वेदिक उत्पाद को लेकर कैसे मदद कर सकता हूँ?",
    "welcomeSub": "हर उत्तर वास्तविक कानूनी स्रोतों के चुनिंदा संग्रह पर आधारित होता है, साथ में उद्धरण और विश्वास स्तर। जब साक्ष्य अपर्याप्त होता है, मैं अनुमान लगाने के बजाय साफ़ कह देता हूँ।",
    "askPlaceholder": "आयुर्वेदिक IP / नियामक प्रश्न पूछें…",
    "composerHint": "केवल जानकारी — कानूनी सलाह नहीं। उत्तर अपने स्रोत बताते हैं; अपर्याप्त साक्ष्य पर अनुमान नहीं लगाया जाता।",
    "answerLabel": "उत्तर",
    "confidenceLabel": "विश्वास स्तर",
    "sourcesLabel": "स्रोत",
    "abstainTitle": "पर्याप्त सत्यापित साक्ष्य नहीं मिला",
    "abstainNote": "सहायक अनुमान लगाने के बजाय इंकार करता है। आप प्रश्न दूसरे शब्दों में पूछ सकते हैं या सहायता खंड में दिखाए आधिकारिक स्रोत देख सकते हैं।",
    "openClassifier": "फॉर्मूलेशन वर्गीकरण खोलें",
    "errNetwork": "IP-SAKTI सेवा तक नहीं पहुँच पा रहे हैं। कृपया जाँचें कि बैकएंड चल रहा है, फिर पुनः प्रयास करें।",
    "errValidation": "अनुरोध प्रोसेस नहीं हो सका। कृपया अपना इनपुट जाँचें और फिर प्रयास करें।",
    "errProcessing": "उत्तर तैयार करते समय एक अस्थायी त्रुटि हुई। कुछ भी उत्तर नहीं दिया गया — कृपया पुनः प्रयास करें।",
    "errUnavailable": "यह क्षमता वर्तमान बिल्ड में उपलब्ध नहीं है। कृपया बाद में पुनः प्रयास करें।",
    "errGeneric": "अनुरोध संभालते समय कुछ गड़बड़ हुई। कृपया पुनः प्रयास करें।",
    "newChat": "नई बातचीत",
    "responseMeta": "उत्तर",
    "noResponseYet": "अभी कोई उत्तर नहीं — विश्वास स्तर, स्थिति और विवरण देखने के लिए प्रश्न पूछें।",
    "specialists": "जुड़े विशेषज्ञ",
    "loading": "लोड हो रहा है…",
    "sourcesTitle": "स्रोत और उद्धरण",
    "noSources": "नवीनतम उत्तर के उद्धरण यहाँ दिखेंगे।",
    "disclaimerTitle": "अस्वीकरण",
    "disclaimerBody": "IP-SAKTI सहायक सामान्य जानकारी देता है, कानूनी सलाह नहीं। उत्तर सार्वजनिक स्रोतों के चुनिंदा संग्रह से तैयार होते हैं और अपूर्ण या पुराने हो सकते हैं। कोई कदम उठाने से पहले आधिकारिक स्रोतों से सत्यापित करें और योग्य IP पेशेवर से परामर्श लें।",
    "statusAnswered": "उत्तर मिला",
    "statusAbstained": "उत्तर नहीं दिया गया",
    "statusError": "त्रुटि",
    "answeredIn": "{s} सेकंड में उत्तरित",
    "abstainedIn": "{s} सेकंड में इंकार",
    "rowJurisdiction": "क्षेत्राधिकार",
    "rowLanguage": "भाषा",
    "rowFormulation": "फॉर्मूलेशन वर्ग",
    "rowSources": "स्रोत",
    "rowTime": "उत्तर समय",
    "rowConfidence": "विश्वास स्तर",
    "rowStatus": "स्थिति",
    "specIndia": "भारत IP एवं नियामक",
    "specAbs": "ABS / TKDL / पारंपरिक ज्ञान",
    "specIntl": "अंतरराष्ट्रीय IP",
    "specCls": "फॉर्मूलेशन वर्गीकरण",
    "specCentral": "केंद्रीय सहायक (राउटिंग और संयोजन)",
    "classifierTitle": "फॉर्मूलेशन वर्गीकरण",
    "classifierIntro": "नीचे निर्देशित प्रश्नों के उत्तर दें। निश्चयात्मक वर्गीकरण आपके उत्पाद को एक नियामक श्रेणी — औषधि, भोजन (आयुर्वेद आहार), कॉस्मेटिक आदि — में रखता है और संबंधित विधियाँ बताता है। अधूरे या विरोधाभासी उत्तर सुरक्षित रूप से अनिश्चित (Uncertain) देते हैं, अनुमान नहीं।",
    "loadingQuestions": "निर्देशित प्रश्न लोड हो रहे हैं…",
    "classifyBtn": "फॉर्मूलेशन वर्गीकृत करें",
    "resetBtn": "रीसेट",
    "relevantRegimes": "संबंधित विधियाँ",
    "clarificationNeeded": "स्पष्टीकरण आवश्यक",
    "suggestedQuestions": "सुझाए गया अगले प्रश्न",
    "reasoningTrace": "वर्गीकरण तर्क-ट्रेस",
    "tkdlHeading": "TKDL संकेत",
    "noClassification": "प्रश्नों के उत्तर देकर “फॉर्मूलेशन वर्गीकृत करें” दबाएँ — परिणाम यहाँ दिखेगा।",
    "resultConfidence": "विश्वास स्तर",
    "clsFormulation": "फॉर्मूलेशन वर्ग",
    "aboutTitle": "IP-SAKTI सहायक परिचय",
    "aboutLead": "आयुर्वेदिक बौद्धिक संपदा और नियामक मार्गदर्शन हेतु स्रोत-उद्धृत सहायक — राष्ट्रीय और अंतरराष्ट्रीय दोनों क्षेत्रों में, अंग्रेज़ी और हिन्दी में।",
    "aboutHow": "प्रणाली क्या करती है",
    "aboutSafety": "सुरक्षा सिद्धांत",
    "aboutBuild": "निर्माण कैसे हुआ है",
    "helpTitle": "सहायता",
    "helpAsk": "प्रश्न पूछना",
    "helpJurisdiction": "क्षेत्राधिकार",
    "helpConfidence": "विश्वास स्तर और इंकार",
    "helpClassifier": "फॉर्मूलेशन वर्गीकरण",
    "helpSources": "स्रोत",
    "helpLimits": "सीमाएँ",
    "helpAskBody": "शीर्ष पट्टी में क्षेत्राधिकार और भाषा चुनें, फिर सरल भाषा में प्रश्न पूछें — या त्वरित डेमो परिदृश्य कार्ड से प्रारंभ करें।",
    "helpIndia": "भारतीय कानूनों के उत्तर: पेटेंट अधिनियम, जीआई अधिनियम, ट्रेड मार्क्स, डी एंड सी अधिनियम, एफएसएसएआई, जैव विविधता अधिनियम।",
    "helpIntl": "अंतरराष्ट्रीय संधियों और मार्गों के उत्तर: ट्रिप्स (TRIPS), विपो (WIPO GRATK), पीसीटी (PCT), मैड्रिड, हेग।",
    "helpMap": "सिस्टम अनुस्मारक:",
    "helpConfBody": "प्रत्येक उत्तर साक्ष्य की शक्ति के आधार पर विश्वास स्तर (उच्च / मध्यम / निम्न) के साथ आता है। अपर्याप्त साक्ष्य पर सहायक इंकार करता है।",
    "helpClsBody": "फॉर्मूलेशन वर्गीकरण खोलें और निर्देशित प्रश्नों के उत्तर दें। वर्गीकरण निश्चयात्मक है और सदैव समान परिणाम देता है।",
    "helpSourcesBody": "उद्धरण आधिकारिक पोर्टल्स — इंडिया कोड, आईपी इंडिया, राष्ट्रीय जैव विविधता प्राधिकरण, सीडीएससीओ, एफएसएसएआई आदि से जुड़े हैं।",
    "helpLimitsBody": "यह सीमित क्यूरेटेड संग्रह पर आधारित एक प्रायोगिक प्रणाली है। यह सामान्य जानकारी प्रदान करता है, कानूनी सलाह नहीं।"
}


class BhashiniError(Exception):
    """Raised when Bhashini API returns an error or fails communication."""
    pass


class BhashiniClient:
    """Client for Bhashini MeitY / ULCA translation and Indic NLP services."""

    def __init__(
        self,
        user_id: Optional[str] = None,
        api_key: Optional[str] = None,
        inference_key: Optional[str] = None,
        pipeline_id: Optional[str] = None,
        timeout: float = 20.0,
    ) -> None:
        self._ensure_env_loaded()
        self.user_id = (user_id or os.environ.get("BHASHINI_USER_ID", "")).strip()
        self.api_key = (api_key or os.environ.get("BHASHINI_API_KEY", "")).strip()
        self.inference_key = (
            inference_key or os.environ.get("BHASHINI_INFERENCE_KEY", "")
        ).strip()
        self.pipeline_id = (
            pipeline_id
            or os.environ.get("BHASHINI_PIPELINE_ID", "")
            or DEFAULT_PIPELINE_ID
        ).strip()
        self.timeout = timeout
        self._pipeline_cache: Dict[Tuple[str, str], Dict[str, Any]] = {}

    def _ensure_env_loaded(self) -> None:
        if "pytest" in sys.modules:
            return
        try:
            from dotenv import load_dotenv
            cur = Path(__file__).resolve()
            for _ in range(5):
                cur = cur.parent
                env_file = cur / ".env"
                if env_file.is_file():
                    load_dotenv(env_file)
                    break
        except Exception:
            pass

    @property
    def is_configured(self) -> bool:
        """Return True if all required Bhashini credentials are present."""
        return bool(self.user_id and self.api_key and self.inference_key)

    def get_supported_languages(self) -> Dict[str, Dict[str, str]]:
        """Return the dictionary of supported Bhashini languages."""
        return dict(SUPPORTED_LANGUAGES)

    def get_ui_bundle(self, target_lang: str = "en") -> Dict[str, str]:
        """Retrieve UI string bundle for target language with disk caching."""
        return get_ui_bundle(target_lang=target_lang, client=self)

    def resolve_pipeline(self, source_lang: str, target_lang: str) -> Dict[str, Any]:
        """Call getModelsPipeline to obtain serviceId and inference callback URL for a language pair."""
        cache_key = (source_lang, target_lang)
        if cache_key in self._pipeline_cache:
            return self._pipeline_cache[cache_key]

        if not self.is_configured:
            raise BhashiniError("Bhashini credentials are not fully configured in environment.")

        payload = {
            "pipelineTasks": [
                {
                    "taskType": "translation",
                    "config": {
                        "language": {
                            "sourceLanguage": source_lang,
                            "targetLanguage": target_lang,
                        }
                    },
                }
            ],
            "pipelineRequestConfig": {
                "pipelineId": self.pipeline_id,
            },
        }

        headers = {
            "userID": self.user_id,
            "ulcaApiKey": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": "IP-SAKTI-Sahayak/1.0",
        }

        req = urllib.request.Request(
            BHASHINI_PIPELINE_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode("utf-8", errors="replace")
            raise BhashiniError(f"Bhashini pipeline resolution failed ({exc.code}): {err_body}") from exc
        except Exception as exc:
            raise BhashiniError(f"Bhashini pipeline network failure: {exc}") from exc

        endpoint_info = data.get("pipelineInferenceAPIEndPoint", {})
        callback_url = endpoint_info.get("callbackUrl")
        key_header = endpoint_info.get("inferenceApiKey", {}).get("name", "Authorization")
        key_val = endpoint_info.get("inferenceApiKey", {}).get("value") or self.inference_key

        service_id = None
        for task in data.get("pipelineResponseConfig", []):
            if task.get("taskType") == "translation":
                configs = task.get("config", [])
                if configs:
                    service_id = configs[0].get("serviceId")
                    break

        if not callback_url or not service_id:
            raise BhashiniError(
                f"Bhashini pipeline returned no service for pair {source_lang} -> {target_lang}"
            )

        resolved = {
            "callback_url": callback_url,
            "service_id": service_id,
            "header_name": key_header,
            "header_value": key_val,
        }
        self._pipeline_cache[cache_key] = resolved
        return resolved

    def translate(
        self,
        text: str,
        source_lang: str = "en",
        target_lang: str = "hi",
    ) -> str:
        """Translate text between Indian languages and English using Bhashini NMT."""
        if not text or not text.strip():
            return text

        if source_lang.lower() == target_lang.lower():
            return text

        if not self.is_configured:
            logger.warning("Bhashini not configured; returning original text.")
            return text

        results = self.translate_batch([text], source_lang=source_lang, target_lang=target_lang)
        return results[0] if results else text

    def translate_batch(
        self,
        texts: List[str],
        source_lang: str = "en",
        target_lang: str = "hi",
    ) -> List[str]:
        """Translate a batch of strings using Bhashini NMT inference."""
        if not texts:
            return []

        if source_lang.lower() == target_lang.lower() or not self.is_configured:
            return texts

        try:
            pipeline = self.resolve_pipeline(source_lang, target_lang)
        except Exception as exc:
            logger.error(f"Failed to resolve Bhashini pipeline: {exc}")
            return texts

        infer_payload = {
            "pipelineTasks": [
                {
                    "taskType": "translation",
                    "config": {
                        "language": {
                            "sourceLanguage": source_lang,
                            "targetLanguage": target_lang,
                        },
                        "serviceId": pipeline["service_id"],
                    },
                }
            ],
            "inputData": {
                "input": [{"source": t} for t in texts]
            },
        }

        infer_headers = {
            "Content-Type": "application/json",
            "User-Agent": "IP-SAKTI-Sahayak/1.0",
            pipeline["header_name"]: pipeline["header_value"],
        }

        req = urllib.request.Request(
            pipeline["callback_url"],
            data=json.dumps(infer_payload).encode("utf-8"),
            headers=infer_headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            logger.error(f"Bhashini inference failed: {exc}")
            return texts

        outputs: List[str] = []
        try:
            response_tasks = data.get("pipelineResponse", [])
            for task in response_tasks:
                if task.get("taskType") == "translation":
                    for item in task.get("output", []):
                        outputs.append(item.get("target", ""))
                    break
        except Exception as exc:
            logger.error(f"Failed to parse Bhashini output: {exc}")
            return texts

        if len(outputs) == len(texts):
            return outputs
        return texts


_CLIENT_INSTANCE: Optional[BhashiniClient] = None


def get_bhashini_client() -> BhashiniClient:
    """Get or instantiate the global Bhashini client singleton."""
    global _CLIENT_INSTANCE
    if _CLIENT_INSTANCE is None:
        _CLIENT_INSTANCE = BhashiniClient()
    return _CLIENT_INSTANCE


def translate_text(text: str, source_lang: str = "en", target_lang: str = "hi") -> str:
    """Convenience helper to translate text via Bhashini."""
    return get_bhashini_client().translate(text, source_lang=source_lang, target_lang=target_lang)


def get_ui_bundle(
    target_lang: str = "en",
    client: Optional[BhashiniClient] = None,
) -> Dict[str, str]:
    """Retrieve UI string bundle for target language with disk caching.

    - If target_lang == "en", returns English strings.
    - If target_lang == "hi", returns Hindi strings.
    - For any other language: checks local disk cache `src/ipsakti/core/data/i18n_cache/{target_lang}.json`.
      If exists, returns it immediately.
    - If not cached on disk: uses BhashiniClient.translate_batch() to translate the UI strings
      in batches, saves to `src/ipsakti/core/data/i18n_cache/{target_lang}.json`, and returns
      the translated dictionary.
    """
    lang = (target_lang or "en").strip().lower()

    if lang == "en":
        return dict(UI_BUNDLE_EN)
    if lang == "hi":
        return dict(UI_BUNDLE_HI)

    cache_file = I18N_CACHE_DIR / f"{lang}.json"
    if cache_file.is_file():
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
        except Exception as exc:
            logger.warning("Failed to read i18n disk cache from %s: %s", cache_file, exc)

    if client is None:
        client = get_bhashini_client()

    keys = list(UI_BUNDLE_EN.keys())
    values = [UI_BUNDLE_EN[k] for k in keys]

    batch_size = 25
    translated_values: List[str] = []

    for i in range(0, len(values), batch_size):
        batch = values[i : i + batch_size]
        translated_batch = client.translate_batch(batch, source_lang="en", target_lang=lang)
        if len(translated_batch) == len(batch):
            translated_values.extend(translated_batch)
        else:
            translated_values.extend(batch)

    bundle = dict(zip(keys, translated_values))

    try:
        I18N_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(bundle, f, ensure_ascii=False, indent=2)
    except Exception as exc:
        logger.warning("Failed to write i18n disk cache to %s: %s", cache_file, exc)

    return bundle
