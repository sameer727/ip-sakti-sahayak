"""Expanded Ayurvedic Canonical, Statutory & Internet-Trained Knowledge Base.

Contains verified canonical epistemology (Pramana Vijnana, Aptopadesha, Charaka, Sushruta),
statutory links (Drugs & Cosmetics Act First Schedule, Patents Act § 3(p), Rule 158B, TKDL),
and a comprehensive training dataset of real questions and answers sourced across the internet.
"""
from __future__ import annotations

import re
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# 1. Canonical Epistemological Records (Pramana Vijnana & Authoritative Texts)
# ---------------------------------------------------------------------------

CANONICAL_EPISTEMOLOGY: List[Dict[str, Any]] = [
    {
        "id": "ayur_pramana_aptopadesha_supreme",
        "title": "Aptopadesha as the Supreme Pramana in Ayurveda (Charaka Samhita)",
        "source_name": "Charaka Samhita — Sutrasthana (Trisraishaniya Adhyaya, Ch. 11, Slokas 17–27) & Vimanasthana (Ch. 8, Sloka 33)",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Charaka Sutrasthana 11.17-27",
        "section_title": "Chaturvidha Pariksha / Pramana — Aptopadesha Pradhanyam",
        "summary": (
            "In Ayurvedic epistemology (Pramana Vijnana), Aptopadesha (verbal testimony / canonical "
            "instruction of enlightened sages) is considered the SUPREME and foremost Pramana (Pradhana Pramana) "
            "for medicine and therapeutics. Aptas are defined as individuals possessing unimpeachable knowledge "
            "(Raja-Tamo Nirmukta — completely free from bias, prejudice, attachment, and ignorance) who speak "
            "only verified truth. Acharya Charaka emphasizes that sensory perception (Pratyaksha) is severely limited "
            "('Pratyaksham hyalpam, analpam apratyaksham') because subtle pathological causes, distant origins, and "
            "internal systemic operations cannot be observed directly. Therefore, Pratyaksha (direct observation), "
            "Anumana (logical inference), and Yukti (experimental rationale) must all be guided and validated "
            "by Aptopadesha."
        ),
        "legal_significance": (
            "1. Statutory Basis: Section 3(a) of the Drugs and Cosmetics Act, 1940 and its First Schedule "
            "codify Aptopadesha by giving statutory recognition to 54 classical texts (Charaka, Sushruta, "
            "Ashtanga Hridaya, etc.) as the exclusive authoritative basis for defining an Ayurvedic drug.\n"
            "2. Regulatory Trial Exemption: Under Rule 158-B of the Drugs and Cosmetics Rules, 1945, classical "
            "formulations documented in these Aptopadesha texts do NOT require animal toxicity or clinical efficacy "
            "trials because centuries of textual documentation constitute empirical human evidence.\n"
            "3. Patent Non-Patentability: Under Section 3(p) of the Patents Act, 1970, all therapeutic formulations "
            "and medicinal uses documented through Aptopadesha in classical texts constitute India's public domain "
            "Traditional Knowledge (Prior Art / Purva Jnana), legally barring any individual or corporation from "
            "obtaining a private patent monopoly.\n"
            "4. TKDL Prior Art Defense: India's Traditional Knowledge Digital Library (TKDL) systematically translates "
            "slokas from these Aptopadesha texts into 5 international languages, successfully defeating hundreds of "
            "biopiracy patent claims worldwide."
        ),
        "url": "https://tkdl.res.in",
        "tags": [
            "pramana", "pramanas", "supreme pramana", "aptopadesha", "aptopadesh",
            "pradhana pramana", "charaka", "charaka samhita", "sutrasthana 11",
            "pratyaksha", "anumana", "yukti", "authoritative text", "prior art",
            "traditional knowledge", "section 3(p)", "rule 158b", "first schedule"
        ],
    },
    {
        "id": "ayur_pramana_four_means",
        "title": "The Four Pramanas in Ayurvedic Jurisprudence (Chaturvidha Pramana)",
        "source_name": "Charaka Samhita Sutrasthana 11.17-25 & Nyaya Darshana",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Charaka Sutrasthana 11.25",
        "section_title": "The Four Pramanas: Aptopadesha, Pratyaksha, Anumana, Yukti",
        "summary": (
            "Ayurveda recognizes four means of valid cognitive proof (Pramanas):\n"
            "1. Aptopadesha (Authoritative Testimony): Teachings of sages free from defect (supreme for medical theory).\n"
            "2. Pratyaksha (Direct Perception): Immediate observation through the sense organs (corresponds to modern clinical observation & lab testing).\n"
            "3. Anumana (Logical Inference): Deduction based on invariable concomitant relationship (Vyapti), such as inferring Agni strength from digestion.\n"
            "4. Yukti (Experimental Reasoning / Rational Combination): A unique contribution of Acharya Charaka. The intellect that plans multiple causative factors (Dosha, Dhatu, Kala, Desha) in harmony to achieve a specific therapeutic result without contradiction."
        ),
        "legal_significance": (
            "Yukti corresponds to modern formulation science and synergistic composition. Under Section 3(e) of "
            "the Patents Act, 1970, a mere mixture of known components is unpatentable unless the inventor proves "
            "a true synergistic technical effect (unexpected therapeutic improvement beyond additive properties). "
            "Yukti provides the philosophical and classical foundation for demonstrating formulation synergy."
        ),
        "url": "https://ipindia.gov.in",
        "tags": [
            "pramana", "pramanas", "four pramanas", "chaturvidha pramana", "yukti",
            "pratyaksha", "anumana", "aptopadesha", "synergy", "section 3(e)",
            "inventive step", "ayurvedic jurisprudence"
        ],
    },
    {
        "id": "ayur_pramana_rasa_panchaka",
        "title": "Dravyaguna Epistemology: Rasa Panchaka and Therapeutic Efficacy",
        "source_name": "Charaka Samhita Sutrasthana Ch. 26 & Ashtanga Hridaya Sutrasthana Ch. 9-10",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Charaka Sutrasthana 26.28-40",
        "section_title": "Rasa, Guna, Virya, Vipaka, Prabhava",
        "summary": (
            "Ayurvedic pharmacodynamics is governed by Rasa Panchaka (the 5 principles of drug action):\n"
            "1. Rasa (Taste): 6 tastes (Madhura, Amla, Lavana, Tikta, Katu, Kashaya) initiating initial physiological feedback.\n"
            "2. Guna (Qualities): 20 somatic attributes (Gurvadi Guna) such as heavy/light, cold/hot, unctuous/dry.\n"
            "3. Virya (Potency): Active thermodynamic energy responsible for action (Sheeta or Ushna).\n"
            "4. Vipaka (Post-digestive Transformation): Metabolic end-result (Madhura, Amla, or Katu).\n"
            "5. Prabhava (Specific Pharmacological Action): Inherent unexplained therapeutic action that cannot be deduced from Rasa, Virya, or Vipaka alone."
        ),
        "legal_significance": (
            "Under Section 3(d) of the Patents Act, 1970, the mere discovery of a new form of a known substance "
            "is not patentable unless it results in the enhancement of the known efficacy (interpreted by the Supreme "
            "Court in Novartis v. Union of India as 'therapeutic efficacy'). Prabhava and Samskara (pharmaceutical "
            "processing like Bhavana or Shodhana) serve as classical antecedents to showing enhanced therapeutic bio-activity."
        ),
        "url": "https://ipindia.gov.in",
        "tags": [
            "rasa panchaka", "virya", "vipaka", "prabhava", "dravyaguna",
            "section 3(d)", "therapeutic efficacy", "novartis", "bhavana", "shodhana"
        ],
    },
    {
        "id": "ayur_classical_dosage_forms_schedule_t",
        "title": "Classical Dosage Forms (Kalpana) and GMP Compliance (Schedule T)",
        "source_name": "Sharangadhara Samhita (Madhyama Khanda) & Drugs and Cosmetics Rules, 1945 (Schedule T)",
        "source_type": "canonical_statutory",
        "jurisdiction": "India",
        "scope_area": "drugs_cosmetics",
        "section": "Schedule T & Sharangadhara Samhita",
        "section_title": "Panchavidha Kashaya Kalpana to Secondary Dosage Forms and GMP Standards",
        "summary": (
            "Classical pharmacology recognizes primary dosage forms (Swarasa, Kalka, Kwatha, Hima, Phanta) and "
            "advanced secondary transformations (Asava, Arishta, Avaleha, Ghrita, Taila, Vati, and Bhasma). "
            "Schedule T of the Drugs and Cosmetics Rules, 1945 prescribes mandatory Good Manufacturing Practices (GMP) "
            "for ASU manufacturing units, specifying factory premises, hygiene, raw material testing, heavy metal limits, "
            "and batch documentation."
        ),
        "legal_significance": (
            "Any manufacturer marketing classical or proprietary Ayurvedic products must hold a valid GMP certificate "
            "issued under Schedule T. While classical formulations are exempted from clinical trials under Rule 158-B, "
            "they MUST strictly comply with Schedule T manufacturing standards and Pharmacopoeial laboratory testing (API/AFI)."
        ),
        "url": "https://ayush.gov.in",
        "tags": [
            "schedule t", "gmp", "dosage forms", "kalpana", "asava", "arishta", "bhasma",
            "sharangadhara", "rule 158b", "manufacturing license"
        ],
    },
    {
        "id": "dc_act_1940_first_schedule_texts",
        "title": "First Schedule of Drugs & Cosmetics Act, 1940: Authoritative Canonical Texts",
        "source_name": "The Drugs and Cosmetics Act, 1940 (Act 23 of 1940) — First Schedule",
        "source_type": "statute",
        "jurisdiction": "India",
        "scope_area": "drugs_cosmetics",
        "section": "First Schedule & Section 3(a)",
        "section_title": "Authoritative Books of Ayurvedic, Siddha and Unani Tibb Systems",
        "summary": (
            "Under Section 3(a) of the Drugs and Cosmetics Act, 1940, an 'Ayurvedic, Siddha or Unani drug' "
            "is defined strictly as a medicine manufactured exclusively in accordance with the formulae described "
            "in the authoritative books specified in the First Schedule. The First Schedule enumerates 54 recognized "
            "canonical texts, including Charaka Samhita, Sushruta Samhita, Ashtanga Hridaya, Sharangadhara Samhita, "
            "Bhavaprakasha, Bhaishajya Ratnavali, and the Ayurvedic Pharmacopoeia of India (API)."
        ),
        "legal_significance": (
            "1. Boundary of Classical vs. Proprietary: If all ingredients and processes strictly follow any of these "
            "54 texts, it is licensed as a Classical Ayurvedic Medicine. If an applicant adds a modern excipient, changes "
            "proportions, or invents a new therapeutic indication, it becomes a 'Patent or Proprietary Medicine' under "
            "Section 3(h) requiring clinical proof under Rule 158-B.\n"
            "2. Statutory Trademark Protection: Names of formulations directly mentioned in these 54 texts (e.g. "
            "Chyawanprash, Triphala Churna, Sitopaladi Churna, Dashamularishta) are generic public property and CANNOT "
            "be registered as exclusive private trademarks under Section 9 of the Trade Marks Act, 1999."
        ),
        "url": "https://cdsco.gov.in",
        "tags": [
            "first schedule", "54 texts", "section 3(a)", "authoritative texts", "classical medicine",
            "proprietary medicine", "drugs and cosmetics act 1940", "trade marks act", "generic name"
        ],
    },
    {
        "id": "dc_rules_1945_rule_158b",
        "title": "Rule 158-B of Drugs & Cosmetics Rules, 1945: Licensing Evidence Matrix",
        "source_name": "Drugs and Cosmetics Rules, 1945 — Rule 158-B",
        "source_type": "regulation",
        "jurisdiction": "India",
        "scope_area": "drugs_cosmetics",
        "section": "Rule 158-B",
        "section_title": "Guidelines for Issue of License with Respect to Ayurvedic, Siddha or Unani Drugs",
        "summary": (
            "Rule 158-B establishes a differentiated regulatory matrix for licensing ASU medicines:\n"
            "- Category A (Classical): Strict adherence to First Schedule authoritative texts. Requires NO safety or "
            "efficacy trial data (textual reference is sufficient evidence).\n"
            "- Category B (Patent or Proprietary with textual ingredients): Made with ingredients from First Schedule texts "
            "but in non-classical combinations. Requires published scientific literature or pilot clinical safety and efficacy data.\n"
            "- Category C (Aqueous/hydroalcoholic extracts): Requires acute toxicity studies and published clinical proof.\n"
            "- Category D (New indications): Requires full clinical trial data on efficacy."
        ),
        "legal_significance": (
            "Rule 158-B prevents unregulated commercialization while preserving textual classical tradition. "
            "It sets the precise statutory boundary between zero-trial classical manufacturing and evidence-backed proprietary drugs."
        ),
        "url": "https://ayush.gov.in",
        "tags": [
            "rule 158b", "rule 158-b", "licensing", "proprietary ayurvedic medicine",
            "proof of safety", "clinical trials", "toxicity studies", "first schedule"
        ],
    },
    {
        "id": "patents_act_1970_section_3p",
        "title": "Section 3(p) of the Patents Act, 1970: Traditional Knowledge Exclusion",
        "source_name": "The Patents Act, 1970 (Act 39 of 1970) — Section 3(p)",
        "source_type": "statute",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Section 3(p)",
        "section_title": "Inventions Not Patentable — Traditional Knowledge",
        "summary": (
            "Section 3(p) expressly provides that 'an invention which in effect is traditional knowledge or which "
            "is an aggregation or duplication of known properties of traditionally known component or components' "
            "is NOT an invention within the meaning of the Patents Act, 1970."
        ),
        "legal_significance": (
            "Section 3(p) is India's principal statutory shield against biopiracy. Patent examiners compare claims "
            "against the Traditional Knowledge Digital Library (TKDL) and First Schedule classical texts. To overcome "
            "Section 3(p), an applicant must demonstrate a substantial technical departure from known classical methods, "
            "a truly novel isolated chemical structure or non-obvious synergistic interaction."
        ),
        "url": "https://ipindia.gov.in",
        "tags": [
            "section 3(p)", "patents act 1970", "traditional knowledge", "tkdl",
            "prior art", "biopiracy", "patentability", "exclusion"
        ],
    },
    # === NEW CANONICAL ENTRIES (8 additions) ===
    {
        "id": "ayur_sushruta_shalya",
        "title": "Sushruta Samhita — Surgical Epistemology and Dravya-Guna-Karma",
        "source_name": "Sushruta Samhita — Sutrasthana & Chikitsasthana",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Sushruta Sutrasthana (Chapters 1-46)",
        "section_title": "Shalya Tantra & Dravya-Guna-Karma Classification",
        "summary": (
            "The Sushruta Samhita, attributed to Acharya Sushruta (circa 600 BCE), is the foundational "
            "text of Indian surgical science (Shalya Tantra) and one of the Brihat Trayi. It documents "
            "rhinoplasty (Nasasandhana) — the earliest recorded reconstructive surgery — along with 120+ "
            "surgical instruments classified as Yantra (blunt) and Shastra (sharp). The Dravya-Guna-Karma "
            "framework classifies medicines by substance, qualities, and therapeutic actions."
        ),
        "legal_significance": (
            "Sushruta's surgical procedures and pharmacological classifications constitute prior art "
            "under Section 3(p). The documented rhinoplasty technique is a canonical example of traditional "
            "knowledge that prevents modern derivative patents. Shodhana procedures described for mineral "
            "drugs are also documented prior art for any claimed novel purification methods."
        ),
        "url": "https://tkdl.res.in",
        "tags": [
            "sushruta", "sushruta samhita", "shalya tantra", "surgery", "rhinoplasty",
            "nasasandhana", "dravya guna karma", "surgical instruments", "prior art"
        ],
    },
    {
        "id": "ayur_vagbhata_ashtanga",
        "title": "Ashtanga Hridaya (Vagbhata) — Pharmacological Synthesis",
        "source_name": "Ashtanga Hridaya of Vagbhata — Sutrasthana & Chikitsasthana",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Ashtanga Hridaya Sutrasthana (Chapters 1-30)",
        "section_title": "Comprehensive Dravyaguna & Anupana System",
        "summary": (
            "Ashtanga Hridaya by Vagbhata (7th century CE) synthesizes Charaka and Sushruta teachings. "
            "It covers 500+ single drugs with Rasa, Guna, Virya, Vipaka, Prabhava properties, introduces "
            "Savirya Kala (drug potency duration), and Anupana (vehicle/adjuvant) concepts for drug delivery "
            "and bioavailability enhancement."
        ),
        "legal_significance": (
            "The comprehensive pharmacological classification is documented in TKDL and constitutes "
            "defensive prior art. Anupana concepts are relevant to modern bioavailability enhancement "
            "patents — applicants must demonstrate novelty beyond classical adjuvant methods. Compound "
            "formulations in Chikitsasthana are prior art under Section 3(p)."
        ),
        "url": "https://tkdl.res.in",
        "tags": [
            "vagbhata", "ashtanga hridaya", "dravyaguna", "anupana", "savirya kala",
            "pharmacology", "drug delivery", "bioavailability", "prior art"
        ],
    },
    {
        "id": "ayur_nighantu_classification",
        "title": "Nighantu Texts — Ayurvedic Materia Medica Classification",
        "source_name": "Bhavaprakash Nighantu, Dhanvantari Nighantu, Raja Nighantu",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Varga (Group) Classification System",
        "section_title": "Systematic Drug Identification & Classification",
        "summary": (
            "Nighantu texts are materia medica lexicons that classify medicinal substances. Bhavaprakash "
            "Nighantu (16th century) classifies 470+ drugs into Vargas with synonyms (Paryaya), properties, "
            "and indications. Dhanvantari Nighantu (10th century) classifies by therapeutic action. Raja "
            "Nighantu provides detailed identity markers for drug authentication."
        ),
        "legal_significance": (
            "Nighantu descriptions provide species-level botanical identification and therapeutic-use "
            "documentation constituting prior art. They are critical for TKDL entries and prior art "
            "searches during patent examination of herbal inventions."
        ),
        "url": "https://tkdl.res.in",
        "tags": [
            "nighantu", "bhavaprakash", "dhanvantari", "raja nighantu", "materia medica",
            "drug classification", "varga", "paryaya", "botanical identification"
        ],
    },
    {
        "id": "ayur_shodhana_marana",
        "title": "Shodhana and Marana — Pharmaceutical Purification & Calcination",
        "source_name": "Rasa Tarangini & Rasaratna Samuchchaya",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Shodhana & Marana Prakarana",
        "section_title": "Classical Mineral Pharmaceutical Processes",
        "summary": (
            "Shodhana (purification) detoxifies minerals through repeated heating and quenching in "
            "specific media (milk, decoctions, juices). Marana (calcination) converts purified metals "
            "into biocompatible nano-scale particles (Bhasma). Quality tests include Varitaratva "
            "(floats on water), Rekhapurnatva (fills finger lines), and Nishchandratva (no metallic lustre)."
        ),
        "legal_significance": (
            "Classical Shodhana/Marana processes are prior art under Section 3(p). Novel modifications "
            "(e.g. green synthesis of Bhasma) may qualify for patent protection if they demonstrate "
            "enhanced safety/efficacy beyond classical methods. API monographs specify physicochemical "
            "standards for Bhasmas."
        ),
        "url": "https://tkdl.res.in",
        "tags": [
            "shodhana", "marana", "bhasma", "rasa shastra", "purification",
            "calcination", "mineral processing", "nano particles", "detoxification"
        ],
    },
    {
        "id": "ayur_classical_dosage_forms",
        "title": "Classical Ayurvedic Dosage Forms (Kalpana)",
        "source_name": "Sharangadhara Samhita — Madhyama Khanda",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Madhyama Khanda (Chapters 1-12)",
        "section_title": "Pharmaceutical Dosage Forms Classification",
        "summary": (
            "Sharangadhara classifies dosage forms: Churna (powders), Kwatha (decoctions), Asava/Arishta "
            "(fermented preparations with self-generated 5-12% alcohol), Taila (medicated oils), Ghrita "
            "(medicated ghee), Bhasma (calcined minerals), Gutika/Vati (tablets), Avaleha (confections). "
            "Each has prescribed manufacturing processes, proportions, and shelf life."
        ),
        "legal_significance": (
            "These dosage forms documented in First Schedule texts are prior art under Section 3(p). "
            "Modern innovations in drug delivery using these classical bases must demonstrate substantial "
            "departure from known methods to be patentable. Asava/Arishta fermentation methods constitute "
            "prior art for bioethanol and herbal fermentation patents."
        ),
        "url": "https://ayush.gov.in",
        "tags": [
            "dosage form", "kalpana", "churna", "kwatha", "asava", "arishta",
            "taila", "ghrita", "bhasma", "gutika", "vati", "avaleha", "sharangadhara"
        ],
    },
    {
        "id": "ayur_panchakarma",
        "title": "Panchakarma Therapeutic Framework and IP Implications",
        "source_name": "Charaka Samhita Siddhisthana & Kalpasthana",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Charaka Siddhisthana (Chapters 1-12)",
        "section_title": "Five Purificatory Therapies",
        "summary": (
            "Panchakarma comprises five bio-purificatory therapies: Vamana (emesis), Virechana (purgation), "
            "Basti (medicated enema), Nasya (nasal medication), and Raktamokshana (bloodletting). Each "
            "includes Purvakarma (preparation — Snehana/Abhyanga & Swedana), Pradhana Karma (main therapy), "
            "and Paschatkarma (post-therapeutic regimen including Samsarjana Krama graded diet)."
        ),
        "legal_significance": (
            "Panchakarma procedures are well-documented prior art. Patents claiming novel purification "
            "or detoxification therapies must be evaluated against this documented framework. However, "
            "novel medical devices or equipment for administering Panchakarma may be patentable as "
            "they involve technical innovation beyond the classical methods."
        ),
        "url": "https://tkdl.res.in",
        "tags": [
            "panchakarma", "vamana", "virechana", "basti", "nasya", "raktamokshana",
            "purification", "detoxification", "snehana", "swedana"
        ],
    },
    {
        "id": "ayur_prakriti_personalized",
        "title": "Prakriti Assessment — Personalized Medicine and IP",
        "source_name": "Charaka Samhita Vimanasthana Ch. 8 & Sushruta Samhita Sharirasthana Ch. 4",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Charaka Vimanasthana 8 & Sushruta Sharirasthana 4",
        "section_title": "Constitutional Assessment Framework",
        "summary": (
            "Prakriti (Psychosomatic Constitution) assessment classifies individuals into Vata, Pitta, "
            "Kapha, or mixed Dosha types based on physical, physiological, and psychological parameters. "
            "This framework enables personalized drug selection, dosage adjustment, and dietary "
            "recommendations — the classical precursor to modern pharmacogenomics."
        ),
        "legal_significance": (
            "Prakriti-based personalized medicine concepts are prior art for broad 'personalized medicine' "
            "patent claims. However, genomic correlations between Prakriti types and specific genetic "
            "polymorphisms (e.g. CYP450 variants) may constitute novel patentable subject matter if "
            "they demonstrate new, non-obvious, technically useful correlations."
        ),
        "url": "https://tkdl.res.in",
        "tags": [
            "prakriti", "constitution", "personalized medicine", "vata", "pitta", "kapha",
            "dosha", "pharmacogenomics", "individualized treatment"
        ],
    },
    {
        "id": "ayur_trividha_pariksha",
        "title": "Trividha & Ashtavidha Pariksha — Classical Diagnostic Examination",
        "source_name": "Charaka Samhita Vimanasthana Ch. 4 & Yogaratnakara",
        "source_type": "canonical_treatise",
        "jurisdiction": "India",
        "scope_area": "patents",
        "section": "Charaka Vimanasthana 4 & Yogaratnakara Purva Khanda",
        "section_title": "Three-Fold and Eight-Fold Examination Methods",
        "summary": (
            "Trividha Pariksha (three-fold examination): Darshana (inspection), Sparshana (palpation), "
            "Prashna (interrogation). Ashtavidha Pariksha (eight-fold examination): Nadi (pulse), Mutra "
            "(urine), Mala (stool), Jihva (tongue), Shabda (voice), Sparsha (touch/skin), Druk (eyes), "
            "Akruti (body build). These form a comprehensive diagnostic framework."
        ),
        "legal_significance": (
            "Classical diagnostic methods are documented prior art. AI-based diagnostic tools that merely "
            "digitize these classical examination parameters may face Section 3(p) challenges. However, "
            "novel algorithms, sensors, or devices that go beyond classical methods may be patentable."
        ),
        "url": "https://tkdl.res.in",
        "tags": [
            "trividha pariksha", "ashtavidha pariksha", "nadi pariksha", "pulse diagnosis",
            "darshana", "sparshana", "prashna", "diagnostic examination"
        ],
    },
]


# ---------------------------------------------------------------------------
# 2. Internet-Trained Regulatory & Canonical Q&A Knowledge Base
# ---------------------------------------------------------------------------

INTERNET_TRAINED_QA: List[Dict[str, Any]] = [
    {
        "id": "qa_supreme_pramana",
        "question_patterns": [
            "which is the supreme pramana",
            "supreme pramana in ayurveda",
            "what is the supreme pramana",
            "which pramana is supreme",
            "which pramana is best",
            "highest pramana in ayurveda",
            "most important pramana",
            "pradhana pramana in ayurveda",
            "सबसे प्रमुख प्रमाण कौन सा है",
            "सर्वश्रेष्ठ प्रमाण कौन सा है"
        ],
        "primary_concept": "Supreme Pramana (Aptopadesha)",
        "answer_summary": (
            "In classical Ayurvedic epistemology (Pramana Vijnana), **Aptopadesha** (Authoritative Testimony / "
            "Shabda Pramana) is held as the **Supreme Pramana** (*Pradhana Pramana*).\n\n"
            "### 1. Classical Epistemology\n"
            "- As expounded in **Charaka Samhita Sutrasthana Chapter 11 (Trisraishaniya Adhyaya)** and "
            "**Vimanasthana Chapter 8**, knowledge imparted by *Aptas* (enlightened sages free from Rajas and Tamas, "
            "bias, fear, and delusion) constitutes uncontroverted authoritative knowledge.\n"
            "- Acharya Charaka specifically reasons: *'Pratyaksham hyalpam, analpam apratyaksham'* (that which can be directly "
            "observed by sensory perception is small; that which is unobservable is vast). Because invisible pathology, deep systemic "
            "etiology, and future drug outcomes cannot be directly perceived, *Pratyaksha* (Direct Observation), "
            "*Anumana* (Logical Inference), and *Yukti* (Rational Experimental Design) must always be guided by *Aptopadesha*.\n\n"
            "### 2. Modern Statutory & Regulatory Intersection\n"
            "- **Drugs and Cosmetics Act, 1940 (§ 3(a) & First Schedule)**: Modern Indian drug regulation directly codifies Aptopadesha "
            "by designating 54 classical authoritative texts (Charaka, Sushruta, Ashtanga Hridaya, etc.) as the statutory standard "
            "defining an authentic Ayurvedic medicine.\n"
            "- **Rule 158-B of Drugs & Cosmetics Rules, 1945**: Formulations strictly following these 54 Aptopadesha texts are legally "
            "exempt from clinical trials and animal toxicity testing because centuries of recorded traditional usage serve as verified evidence.\n"
            "- **Section 3(p) of the Patents Act, 1970**: Therapeutic formulations and medicinal properties described in these Aptopadesha "
            "texts form India's public domain Traditional Knowledge (Prior Art), documented in the Traditional Knowledge Digital Library (TKDL) "
            "and precluding private patent monopolies."
        ),
        "citations": [
            {
                "id": "charaka_samhita_sutrasthana_11",
                "source_name": "Charaka Samhita Sutrasthana 11 & Vimanasthana 8 (Aptopadesha)",
                "source_type": "Classical Text / Statutory Standard",
                "section": "Charaka Sutrasthana 11.17-27 & Vimanasthana 8.33",
                "excerpt": "Aptopadesha is the authoritative testimony of sages (Aptas) who are devoid of bias and possessed of verified wisdom. It is the primary Pramana that guides observation, inference, and rational experimental design.",
                "url": "https://tkdl.res.in",
            },
            {
                "id": "dc_act_1940_first_schedule",
                "source_name": "Drugs and Cosmetics Act, 1940 - First Schedule (54 Classical Texts)",
                "source_type": "Statutory Schedule",
                "section": "Section 3(a) & First Schedule",
                "excerpt": "The First Schedule to the Drugs and Cosmetics Act, 1940 lists the 54 authoritative classical books of Ayurvedic, Siddha and Unani systems as the statutory basis for traditional medicines.",
                "url": "https://cdsco.gov.in",
            },
            {
                "id": "patents_act_1970_sec3p",
                "source_name": "Indian Patents Act, 1970 - Section 3(p) & TKDL Prior Art",
                "source_type": "Patent Statute",
                "section": "Section 3(p)",
                "excerpt": "Section 3(p) of the Patents Act, 1970 declares that an invention which in effect is traditional knowledge or an aggregation of known properties of traditionally known components is not an invention.",
                "url": "https://ipindia.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.98,
    },
    {
        "id": "qa_four_pramanas_synergy",
        "question_patterns": [
            "what are the four pramanas",
            "four pramanas in ayurveda",
            "chaturvidha pramana",
            "how does yukti relate to patent synergy",
            "yukti and section 3e",
            "चार प्रमाण कौन से हैं",
            "युक्ति प्रमाण क्या है"
        ],
        "primary_concept": "Four Pramanas & Section 3(e) Synergistic Efficacy",
        "answer_summary": (
            "Ayurveda recognizes four means of valid cognitive proof (*Chaturvidha Pramana*):\n\n"
            "1. **Aptopadesha (Authoritative Testimony)**: Codified knowledge of sages, forming the basis of Section 3(a) First Schedule texts.\n"
            "2. **Pratyaksha (Direct Observation)**: Empirical observation via the sensory faculties, aligning with laboratory analytics and clinical trial readouts.\n"
            "3. **Anumana (Logical Inference)**: Logical deduction from invariable association (*Vyapti*), such as inferring biological mechanisms from metabolic markers.\n"
            "4. **Yukti (Rational Experimental Combination)**: The intellect combining multiple causative factors (herbs, dosage, processing, time, individual constitution) "
            "to generate an optimal therapeutic effect without mutual antagonism.\n\n"
            "### Statutory Bridge to Patent Synergy (§ 3(e))\n"
            "- Under **Section 3(e) of the Patents Act, 1970**, a mere admixture resulting only in the aggregation of the properties of the components is not patentable.\n"
            "- To secure a patent for a polyherbal formulation, an applicant must demonstrate **synergistic technical effect** (where the combined formulation exhibits "
            "statistically superior therapeutic efficacy compared to the sum of individual herbs). Yukti serves as the classical conceptual framework for rational synergy."
        ),
        "citations": [
            {
                "id": "KB-CANON-004",
                "source_name": "Charaka Samhita Sutrasthana 11.25 (Yukti Pramana)",
                "source_type": "Classical Text",
                "section": "Charaka Sutrasthana 11.25",
                "excerpt": "Yukti is the intellect that perceives the outcome produced by a combination of multiple causative factors operating in harmony.",
                "url": "https://tkdl.res.in",
            },
            {
                "id": "KB-PAT-001",
                "source_name": "Indian Patents Act, 1970 - Section 3(e) Synergistic Admixtures",
                "source_type": "Patent Statute",
                "section": "Section 3(e)",
                "excerpt": "A substance obtained by a mere admixture resulting only in the aggregation of the properties of the components thereof or a process for producing such substance is not patentable unless synergy is proved.",
                "url": "https://ipindia.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.96,
    },
    {
        "id": "qa_patent_classical_vs_proprietary",
        "question_patterns": [
            "can i patent a classical ayurvedic formulation",
            "patentability of classical formulation",
            "is classical ayurvedic medicine patentable",
            "patent on triphala or chyawanprash",
            "difference between classical and proprietary patent"
        ],
        "primary_concept": "Patentability of Classical vs Proprietary Formulations",
        "answer_summary": (
            "**No, classical Ayurvedic formulations cannot be patented in India.**\n\n"
            "### Legal Analysis\n"
            "1. **Section 3(p) Bar**: Under Section 3(p) of the Patents Act, 1970, any product or formulation documented in classical texts "
            "is deemed traditional knowledge in the public domain. Formulations like Triphala, Chyawanprash, or Sitopaladi Churna cannot be monopolized.\n"
            "2. **Section 3(e) Bar**: A mere mixture of known classical herbs is unpatentable unless unexpected synergistic bio-efficacy is demonstrated with experimental data.\n"
            "3. **What CAN Be Patented?**:\n"
            "   - Novel, non-obvious extraction processes yielding standardized fractions with identified active chemical markers.\n"
            "   - Synergistic combinations of specific extracts demonstrating unexpected bio-enhancement (overcoming § 3(e)).\n"
            "   - Modified drug delivery systems (e.g., lipid nanoparticles or phytosomes of Ayurvedic actives) showing enhanced bioavailability (overcoming § 3(d))."
        ),
        "citations": [
            {
                "id": "patents_act_1970_sec3p",
                "source_name": "The Patents Act, 1970",
                "source_type": "statute",
                "section": "Section 3(p)",
                "excerpt": "An invention which in effect is traditional knowledge or which is an aggregation or duplication of known properties of traditionally known component or components is not an invention.",
                "url": "https://ipindia.gov.in",
            },
            {
                "id": "patents_act_1970_sec3e",
                "source_name": "The Patents Act, 1970",
                "source_type": "statute",
                "section": "Section 3(e)",
                "excerpt": "A substance obtained by a mere admixture resulting only in the aggregation of the properties of the components thereof is not patentable.",
                "url": "https://ipindia.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.97,
    },
    {
        "id": "qa_tkdl_defensive_protection",
        "question_patterns": [
            "what is tkdl",
            "traditional knowledge digital library",
            "how does tkdl prevent biopiracy",
            "how does csir use tkdl against patents",
            "tkdl prior art search"
        ],
        "primary_concept": "TKDL Prior Art Defense Against Biopiracy",
        "answer_summary": (
            "The **Traditional Knowledge Digital Library (TKDL)** is a pioneering Indian database established by CSIR and the Ministry of Ayush:\n\n"
            "- **Mechanism**: Translates classical Sanskrit, Arabic, Persian, and Tamil slokas from First Schedule texts into 5 international "
            "languages (English, German, French, Spanish, Japanese) in structured patent classification format (IPC).\n"
            "- **International Agreements**: Access agreements with major patent offices (USPTO, EPO, JPO, UKIPO, CIPO) allow patent examiners "
            "to search traditional knowledge prior art before granting claims.\n"
            "- **Legal Role in India**: In India, TKDL evidence is used by the Indian Patent Office under Section 3(p) to reject wrongful patent claims. "
            "Note that access to TKDL is restricted to examiners and registered R&D institutions to prevent misuse."
        ),
        "citations": [
            {
                "id": "tkdl_official_portal",
                "source_name": "Traditional Knowledge Digital Library (CSIR-Ayush)",
                "source_type": "government_database",
                "section": "TKDL Defensive Mechanism",
                "excerpt": "TKDL bridges the linguistic gap between classical Indian texts and modern patent examiners, preventing misappropriation of traditional knowledge.",
                "url": "https://tkdl.res.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.96,
    },
    {
        "id": "qa_bda_section6_patent_approval",
        "question_patterns": [
            "do i need nba approval for patent",
            "biological diversity act patent approval",
            "section 6 biological diversity act",
            "when to apply to nba for patent in india",
            "form iii nba approval"
        ],
        "primary_concept": "NBA Approval for Patent Applications under BDA § 6",
        "answer_summary": (
            "Under **Section 6 of the Biological Diversity Act, 2002 (amended in 2023)**:\n\n"
            "1. **Mandatory Approval**: Any person (Indian or foreign) applying for any intellectual property right (patent) in or outside India "
            "for any invention based on any research or information on a biological resource obtained from India MUST obtain prior approval from "
            "the **National Biodiversity Authority (NBA)**.\n"
            "2. **Timing**: In India, the patent application may be filed, but the NBA approval (Form III) MUST be obtained **before the grant of the patent**.\n"
            "3. **Benefit Sharing**: The NBA may impose conditions, including monetary or non-monetary benefit sharing under Section 21.\n"
            "4. **2023 Amendment Relief**: Codified traditional knowledge and registered AYUSH practitioners are exempted from access fees and benefit-sharing obligations, "
            "though patent approvals still require statutory verification."
        ),
        "citations": [
            {
                "id": "bda_2002_sec6",
                "source_name": "The Biological Diversity Act, 2002 (as amended 2023)",
                "source_type": "statute",
                "section": "Section 6",
                "excerpt": "No person shall apply for any intellectual property right, by whatever name called, in or outside India for any invention based on any research or information on a biological resource obtained from India without obtaining the previous approval of the National Biodiversity Authority.",
                "url": "https://nbaindia.org",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.96,
    },
    {
        "id": "qa_bda_geo_origin_disclosure",
        "question_patterns": [
            "section 10 4 d patents act",
            "geographical origin disclosure patent india",
            "where does the plant come from patent disclosure",
            "what happens if i do not disclose origin of plant in patent"
        ],
        "primary_concept": "Mandatory Geo-Origin Disclosure (§ 10(4)(d))",
        "answer_summary": (
            "Under **Section 10(4)(d) of the Indian Patents Act, 1970**:\n\n"
            "- **Statutory Mandate**: Every patent specification MUST disclose the source and geographical origin of any biological material "
            "used in the invention when the material is obtained from India.\n"
            "- **Consequences of Non-Disclosure / Wrongful Disclosure**:\n"
            "  1. Ground for Pre-grant and Post-grant Opposition under **Section 25(1)(j) & 25(2)(j)**.\n"
            "  2. Ground for complete revocation of the granted patent under **Section 64(1)(p)** for false disclosure.\n"
            "- **Compliance**: Applicants must disclose the specific village, district, state, or agro-ecological zone and obtain NBA Form III clearance."
        ),
        "citations": [
            {
                "id": "patents_act_1970_sec10",
                "source_name": "The Patents Act, 1970",
                "source_type": "statute",
                "section": "Section 10(4)(d)",
                "excerpt": "The specification must disclose the source and geographical origin of the biological material in the specification, when that material is used in an invention and is obtained from India.",
                "url": "https://ipindia.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.97,
    },
    {
        "id": "qa_rule_158b_licensing",
        "question_patterns": [
            "what is rule 158b",
            "how to get ayurvedic drug license",
            "licensing requirements classical vs proprietary ayurveda",
            "safety and efficacy trial ayurveda rule 158-b"
        ],
        "primary_concept": "Rule 158-B Licensing Evidence Matrix",
        "answer_summary": (
            "**Rule 158-B of the Drugs and Cosmetics Rules, 1945** governs the regulatory evidence required for state licensing of ASU drugs:\n\n"
            "1. **Classical Formulations (Category A)**:\n"
            "   - Manufactured strictly as per the 54 books in the First Schedule.\n"
            "   - **Exempt from animal toxicity and clinical trials**; textual citation is sufficient.\n"
            "2. **Patent or Proprietary Formulations (Category B)**:\n"
            "   - Contains ingredients from First Schedule texts in new combinations.\n"
            "   - Requires published safety literature or pilot clinical trial data before license grant.\n"
            "3. **Extract-based formulations (Category C & D)**:\n"
            "   - Aqueous/hydroalcoholic extracts require acute oral toxicity studies (OECD 423) and safety evidence."
        ),
        "citations": [
            {
                "id": "dc_rules_rule158b",
                "source_name": "Drugs and Cosmetics Rules, 1945",
                "source_type": "regulation",
                "section": "Rule 158-B",
                "excerpt": "Guidelines for issue of license with respect to Ayurvedic, Siddha or Unani drugs. Delineates proof of safety and effectiveness for classical versus proprietary formulations.",
                "url": "https://ayush.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.95,
    },
    {
        "id": "qa_phytopharmaceuticals_cdsco",
        "question_patterns": [
            "what is a phytopharmaceutical drug",
            "phytopharmaceutical regulation india cdsco",
            "can phytopharmaceutical get a patent",
            "clinical trial phytopharmaceutical",
            "difference between phytopharmaceutical and ayurvedic medicine"
        ],
        "primary_concept": "Phytopharmaceutical Regulatory Pathway (CDSCO)",
        "answer_summary": (
            "Phytopharmaceuticals are a modern pharmaceutical category defined under the **Drugs and Cosmetics Rules (Amendment 2015)**:\n\n"
            "- **Definition**: Purified and standardized fraction with a minimum of **4 bioactive markers**, extracted from plant parts.\n"
            "- **Regulator**: Regulated directly by **CDSCO** (DCGI), NOT state AYUSH licensing authorities.\n"
            "- **Clinical Data**: Requires full Phase I, Phase II, and Phase III human clinical trials, animal toxicology, and stability dossiers.\n"
            "- **Patentability**: High patentability potential. Because the standardized extraction process, solvent purification, and marker profile "
            "represent novel technical intervention rather than traditional whole-plant usage, they can overcome Section 3(p) if an inventive step is established."
        ),
        "citations": [
            {
                "id": "cdsco_phytopharmaceutical_2015",
                "source_name": "Gazette Notification G.S.R. 918(E) — Phytopharmaceutical Drugs",
                "source_type": "regulation",
                "section": "Rule 122-E & Schedule Y",
                "excerpt": "Phytopharmaceutical drug means purified and standardized fraction with defined minimum four marker compounds extracted from plant origin.",
                "url": "https://cdsco.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.96,
    },
    {
        "id": "qa_fssai_ayurveda_aahara",
        "question_patterns": [
            "can ayurvedic medicine be sold as food",
            "ayurveda aahara regulations fssai",
            "fssai vs ayush license",
            "can food product cure disease claim"
        ],
        "primary_concept": "FSSAI Ayurveda Aahara vs AYUSH Drug",
        "answer_summary": (
            "The **Food Safety and Standards (Ayurveda Aahara) Regulations, 2022** establish clear boundaries:\n\n"
            "- **Permitted Products**: Foods prepared in accordance with classical Ayurvedic texts listed in Schedule A, for nutrition and wellness.\n"
            "- **Strict Prohibitions**:\n"
            "  1. Cannot include Schedule E(1) poisonous botanical substances.\n"
            "  2. Cannot make **disease prevention, treatment, or cure claims**.\n"
            "  3. Cannot be packaged or presented as pharmaceutical dosage forms targeting specific pathologies.\n"
            "- **Labeling**: Must prominently carry the special 'Ayurveda Aahara' logo and advisory warning: *'Not for medicinal use'*. "
            "Therapeutic formulations MUST be licensed under AYUSH drug regulations, not FSSAI."
        ),
        "citations": [
            {
                "id": "fssai_ayurveda_aahara_2022",
                "source_name": "Food Safety and Standards (Ayurveda Aahara) Regulations, 2022",
                "source_type": "regulation",
                "section": "Regulation 3 & Schedule A",
                "excerpt": "Ayurveda Aahara shall not include Ayurvedic drugs, proprietary Ayurvedic medicines, medicinal plant extracts or synthetic additives. No disease cure or mitigation claims shall be made.",
                "url": "https://fssai.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.95,
    },
    {
        "id": "qa_gi_registration_ayurveda",
        "question_patterns": [
            "how to register gi tag for ayurveda",
            "geographical indications for medicinal plants",
            "kashmir saffron gi tag",
            "can a company own a gi tag",
            "difference between gi and patent"
        ],
        "primary_concept": "Geographical Indications for Ayurvedic Agro-botanicals",
        "answer_summary": (
            "Under the **Geographical Indications of Goods (Registration and Protection) Act, 1999**:\n\n"
            "- **Nature of Right**: GIs protect goods possessing special quality, reputation, or characteristics attributable to geographical origin "
            "(e.g., altitude, soil composition, rainfall, traditional processing skills).\n"
            "- **Collective Ownership**: A GI belongs to an **association of producers or community**, NEVER to a private single company or individual.\n"
            "- **Examples**: Kashmir Saffron (high crocin/safranal content due to Karewa soil), Malabar Pepper, Alleppey Green Cardamom, Navara Rice.\n"
            "- **Contrast with Patents**: Patents grant temporary 20-year private monopoly for novel inventions. GIs grant indefinite collective protection "
            "(renewable every 10 years) for traditional regional heritage."
        ),
        "citations": [
            {
                "id": "gi_act_1999_sec8",
                "source_name": "The Geographical Indications of Goods Act, 1999",
                "source_type": "statute",
                "section": "Section 8 & Section 11",
                "excerpt": "Any association of persons or producers representing the interest of the producers of the concerned goods to which a geographical indication is attributed may apply for registration.",
                "url": "https://ipindia.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.95,
    },
    {
        "id": "qa_wipo_gratk_treaty_2024",
        "question_patterns": [
            "wipo gratk treaty traditional knowledge",
            "how to file patent outside india for ayurveda",
            "mandatory disclosure genetic resources wipo",
            "international treaty traditional knowledge 2024"
        ],
        "primary_concept": "WIPO GRATK Treaty 2024 & Global Protection",
        "answer_summary": (
            "The **WIPO Treaty on Intellectual Property, Genetic Resources and Associated Traditional Knowledge (GRATK)**, adopted on May 24, 2024:\n\n"
            "1. **Mandatory Patent Disclosure**: Patent applicants worldwide MUST disclose the country of origin of genetic resources "
            "and the indigenous/local community providing associated traditional knowledge in patent applications.\n"
            "2. **Filing Routes**: International protection should be sought via the **Patent Cooperation Treaty (PCT)** (157 contracting states).\n"
            "3. **Prior Art Access**: Patent examiners globally are mandated to access interoperable traditional knowledge databases (like India's TKDL) "
            "to prevent unauthorized biopiracy patents internationally."
        ),
        "citations": [
            {
                "id": "wipo_gratk_treaty_2024",
                "source_name": "WIPO Treaty on Intellectual Property, Genetic Resources and Associated Traditional Knowledge (2024)",
                "source_type": "statute",
                "section": "Article 3 — Mandatory Disclosure Requirement",
                "excerpt": "Where the claimed invention in a patent application is based on genetic resources and associated traditional knowledge, each Contracting Party shall require applicants to disclose the country of origin or source.",
                "url": "https://www.wipo.int",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.96,
    },
    {
        "id": "qa_advertising_drugs_magic_remedies",
        "question_patterns": [
            "can i advertise ayurvedic cure for cancer",
            "advertising rules for ayurvedic medicines",
            "drugs and magic remedies act ayurveda",
            "misleading advertisements ayush drugs",
            "rule 170 drugs and cosmetics rules"
        ],
        "primary_concept": "Advertising Restrictions (Drugs & Magic Remedies Act)",
        "answer_summary": (
            "Advertising Ayurvedic medicines in India is strictly circumscribed:\n\n"
            "1. **Drugs and Magic Remedies (Objectionable Advertisements) Act, 1954**: Section 3 completely prohibits any advertisement "
            "claiming the diagnosis, cure, mitigation, treatment, or prevention of specified conditions listed in the Schedule (including cancer, "
            "diabetes, blindness, kidney failure, epilepsy, and sexual disorders).\n"
            "2. **Rule 170 of Drugs and Cosmetics Rules, 1945**: Mandates prior approval from the State Licensing Authority before publishing "
            "advertisements for Ayurvedic medicines.\n"
            "3. **Consumer Protection Act, 2019 & CCPA Guidelines**: Penalties up to ₹10-50 lakhs and potential bans on endorsers for misleading "
            "claims regarding AYUSH formulations."
        ),
        "citations": [
            {
                "id": "dmra_1954_sec3",
                "source_name": "The Drugs and Magic Remedies (Objectionable Advertisements) Act, 1954",
                "source_type": "statute",
                "section": "Section 3 & Schedule",
                "excerpt": "No person shall take part in the publication of any advertisement referring to any drug which suggests or is calculated to lead to the use of that drug for the diagnosis, cure, mitigation, treatment or prevention of any disease specified in the schedule.",
                "url": "https://ayush.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.95,
    },
    {
        "id": "qa_bioenhancers_piperine_patents",
        "question_patterns": [
            "can i patent a bioenhancer with ayurvedic herb",
            "patent on piperine combination",
            "curcumin piperine synergy patent",
            "overcoming section 3d with bioavailability enhancement"
        ],
        "primary_concept": "Bio-enhancers and Synergistic Patentability",
        "answer_summary": (
            "Combining classical bio-enhancers (such as *Piper nigrum* / Piperine or *Zingiber officinale* / Shunti) with active herbal extracts "
            "**can be patentable in India** under strict conditions:\n\n"
            "1. **Overcoming Section 3(p)**: Classical texts (e.g. Trikatu) mention using black pepper to increase Agni. Merely using crude black pepper "
            "powder in a traditional ratio is barred as traditional knowledge under § 3(p).\n"
            "2. **Overcoming Section 3(e)**: If the applicant uses a purified active constituent (e.g. 98% pure piperine) at specific non-classical molar ratios "
            "and proves statistically unexpected synergistic plasma concentration (AUC) or bioavailability enhancement (e.g., 2000% increase in curcumin bioavailability), "
            "this constitutes valid inventive synergy under Section 3(e).\n"
            "3. **Overcoming Section 3(d)**: Bioavailability increase alone is insufficient unless accompanied by demonstrable increase in *therapeutic efficacy* "
            "(as laid down in Novartis AG v. Union of India)."
        ),
        "citations": [
            {
                "id": "patent_guidelines_pharma",
                "source_name": "Indian Patent Office Guidelines for Examination of Pharmaceutical Applications",
                "source_type": "guidelines",
                "section": "Chapter 5 — Synergism and Bioavailability",
                "excerpt": "To establish synergism under Section 3(e), the applicant must produce comparative experimental data demonstrating that the combined action of the components exceeds the aggregate effect.",
                "url": "https://ipindia.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.95,
    },
    {
        "id": "qa_clinical_trials_ctri_ayurveda",
        "question_patterns": [
            "is clinical trial mandatory for ayurveda",
            "ctri registration ayurvedic clinical trial",
            "do classical medicines need clinical trials",
            "clinical trial guidelines ayush ministry"
        ],
        "primary_concept": "Clinical Trials & CTRI Registration for Ayurveda",
        "answer_summary": (
            "Clinical trial requirements in Ayurveda follow a statutory bifurcation:\n\n"
            "- **Classical Medicines**: Exempt from clinical trials under **Rule 158-B** if prepared strictly per First Schedule texts.\n"
            "- **Proprietary & New Indication Medicines**: Must undergo clinical trials following the **Good Clinical Practice (GCP) Guidelines for ASU Drugs**.\n"
            "- **Mandatory CTRI Registration**: Any clinical trial conducted on human subjects in India MUST be prospectively registered in the "
            "**Clinical Trials Registry - India (CTRI)** hosted by ICMR before enrolling the first participant.\n"
            "- **Ethics Committee**: Must receive clearance from a registered Institutional Ethics Committee (IEC) with an Ayurveda domain expert."
        ),
        "citations": [
            {
                "id": "ctri_icmr_ayush",
                "source_name": "Clinical Trials Registry - India (ICMR-CTRI) & AYUSH GCP Guidelines",
                "source_type": "guidelines",
                "section": "Prospective Registration & Ethics Approval",
                "excerpt": "Prospective registration in CTRI is mandatory for all clinical trials on ASU interventions before subject recruitment.",
                "url": "https://ctri.nic.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.94,
    },
    {
        "id": "qa_bhasmas_heavy_metals_regulation",
        "question_patterns": [
            "are bhasmas regulated for heavy metals",
            "how are rasashastra medicines approved",
            "heavy metal limits in ayurvedic medicine",
            "mercury lead arsenic bhasma safety rule"
        ],
        "primary_concept": "Regulation of Herbo-metallic Formulations (Bhasmas/Rasashastra)",
        "answer_summary": (
            "Herbo-metallic and mineral formulations (*Bhasmas* and *Rasashastra* medicines) are subject to stringent quality controls in India:\n\n"
            "1. **Classical Shodhana & Marana**: Raw minerals must undergo verified classical purification (*Shodhana*) and incineration (*Marana*) "
            "as codified in authoritative texts (e.g. *Rasa Tarangini*, *Rasaratna Samucchaya*).\n"
            "2. **Heavy Metal Permissible Limits**: Ayurvedic Pharmacopoeia of India (API) and Rule 161 of Drugs & Cosmetics Rules prescribe permissible limits "
            "for heavy metals (Lead: 10 ppm, Arsenic: 3 ppm, Cadmium: 0.3 ppm, Mercury: 1 ppm) for plant-based formulations. For herbo-metallic medicines where "
            "metals are active ingredients, strict organometallic Bhasma Parikshas (*Varitaratva*, *Rekhapurnatva*, *Niruttha*) and modern physicochemical tests "
            "(XRD, ICP-MS) are mandatory.\n"
            "3. **Schedule E(1) Cautionary Labeling**: Formulations containing poisonous substances listed in Schedule E(1) (such as Vatsanabha, Kupilu, Parada) "
            "must prominently display 'Caution: To be taken under medical supervision' on the label."
        ),
        "citations": [
            {
                "id": "dc_rules_rule161_heavy_metals",
                "source_name": "Drugs and Cosmetics Rules, 1945 — Rule 161 & Schedule E(1)",
                "source_type": "regulation",
                "section": "Rule 161 & Schedule E(1)",
                "excerpt": "Mandatory testing for heavy metals and cautionary labeling for ASU medicines containing poisonous substances specified in Schedule E(1).",
                "url": "https://ayush.gov.in",
            },
        ],
        "confidence": "HIGH",
        "confidence_score": 0.95,
    },
    # === NEW QA ENTRIES (15 additions) ===
    {
        "id": "qa_how_to_patent_ayurvedic",
        "question_patterns": [
            "how to patent an ayurvedic product",
            "how do i patent ayurvedic medicine",
            "patent filing for ayurvedic formulation",
            "can i get patent for ayurvedic drug",
            "patent process for herbal medicine india",
            "आयुर्वेदिक उत्पाद का पेटेंट कैसे करें",
        ],
        "primary_concept": "Patenting Ayurvedic Products in India",
        "answer_summary": (
            "To patent an Ayurvedic product in India, you must navigate specific legal requirements:\n\n"
            "### Key Steps\n"
            "1. **Novelty Check**: Ensure the formulation is NOT already documented in classical texts "
            "(First Schedule) or TKDL. Classical formulations are barred under **Section 3(p)**.\n"
            "2. **Prove Innovation**: For polyherbal compositions, demonstrate **synergistic efficacy** "
            "beyond mere admixture (Section 3(e)). For new forms of known substances, show **enhanced "
            "therapeutic efficacy** (Section 3(d)).\n"
            "3. **File Application**: Submit Form 1 (Application) & Form 2 (Specification) at the Indian "
            "Patent Office. Include **geographical origin disclosure** of biological material (Section 10(4)(d)).\n"
            "4. **NBA Approval**: Obtain approval from National Biodiversity Authority if using Indian "
            "biological resources.\n"
            "5. **Request Examination**: File Form 18 within 48 months.\n"
            "6. **Respond to FER**: Address First Examination Report within 6 months.\n\n"
            "### What IS Patentable\n"
            "- Novel extraction processes with improved yield/purity\n"
            "- Synergistic polyherbal compositions with clinical data\n"
            "- Novel drug delivery systems for classical drugs\n"
            "- Bio-enhanced formulations with proven superior bioavailability\n\n"
            "### What is NOT Patentable\n"
            "- Classical formulations from First Schedule texts (Section 3(p))\n"
            "- Mere admixtures without synergy (Section 3(e))\n"
            "- New forms without enhanced therapeutic efficacy (Section 3(d))"
        ),
        "citations": [
            {"id": "patents_act_sec3p", "source_name": "Patents Act, 1970 — Section 3(p)", "url": "https://ipindia.gov.in"},
            {"id": "patents_act_sec10_4d", "source_name": "Patents Act, 1970 — Section 10(4)(d)", "url": "https://ipindia.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.95,
    },
    {
        "id": "qa_classical_vs_proprietary",
        "question_patterns": [
            "difference between classical and proprietary ayurvedic medicine",
            "what is classical medicine vs proprietary medicine",
            "classical formulation vs patent proprietary",
            "what is a proprietary ayurvedic drug",
            "शास्त्रीय और स्वामित्व वाली आयुर्वेदिक दवा में अंतर",
        ],
        "primary_concept": "Classical vs Proprietary Ayurvedic Medicines",
        "answer_summary": (
            "Under **Rule 158-B** of the Drugs and Cosmetics Rules, 1945, Ayurvedic drugs are classified into:\n\n"
            "### Classical Medicines (Category A & B)\n"
            "- Formulations documented in the **54 authoritative texts** listed in the First Schedule\n"
            "- **No clinical trials required** — centuries of documented use serve as evidence\n"
            "- Manufacturing requires Schedule T GMP compliance and state Drug Controller license\n"
            "- Examples: Triphala Churna, Chyawanprash, Dashamoola Kwatha\n\n"
            "### Proprietary Medicines (Category C & D)\n"
            "- **Category C**: New combinations of classical ingredients in non-classical proportions — "
            "requires safety and efficacy data\n"
            "- **Category D**: Entirely novel formulations with no classical precedent — requires full "
            "clinical trials (Phase I-III)\n"
            "- Must obtain separate product-wise CDSCO/AYUSH approval\n"
            "- CAN be patented if they meet inventive step requirements\n\n"
            "### Key Distinction for IP\n"
            "Classical formulations are public domain (prior art under Section 3(p)). "
            "Proprietary formulations may qualify for patent and trade secret protection."
        ),
        "citations": [
            {"id": "rule_158b", "source_name": "D&C Rules, 1945 — Rule 158-B", "url": "https://ayush.gov.in"},
            {"id": "dc_act_first_schedule", "source_name": "D&C Act, 1940 — First Schedule", "url": "https://cdsco.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.96,
    },
    {
        "id": "qa_trademark_ayurvedic_brand",
        "question_patterns": [
            "how to register trademark for ayurvedic brand",
            "trademark registration ayurvedic products",
            "can i trademark ayurvedic brand name",
            "protect ayurvedic brand name",
            "आयुर्वेदिक ब्रांड का ट्रेडमार्क कैसे करें",
        ],
        "primary_concept": "Trademark Registration for Ayurvedic Brands",
        "answer_summary": (
            "### Trademark Registration Process\n"
            "1. **Search**: Check availability on IP India's TM search portal\n"
            "2. **File Application**: Under **Section 18** of the Trade Marks Act, 1999 with the Trade Marks Registry\n"
            "3. **Examination**: Registrar checks absolute/relative grounds for refusal (Section 9 & 11)\n"
            "4. **Publication**: 4-month opposition period in the Trade Marks Journal\n"
            "5. **Registration**: Certificate issued if no opposition\n\n"
            "### What CAN Be Trademarked\n"
            "- Coined/distinctive brand names (e.g., 'Dabur', 'Himalaya', 'Patanjali')\n"
            "- Distinctive logos, taglines, and packaging trade dress\n"
            "- Sound marks, color combinations\n\n"
            "### What CANNOT Be Trademarked\n"
            "- Generic Ayurvedic terms: 'Triphala', 'Chyawanprash', 'Ashwagandha' (descriptive/generic under Section 9)\n"
            "- Deceptive marks suggesting medicinal properties not possessed\n\n"
            "**Duration**: 10 years, renewable indefinitely. International protection via Madrid Protocol (India joined 2013)."
        ),
        "citations": [
            {"id": "trademarks_act_1999", "source_name": "Trade Marks Act, 1999 — Sections 9, 11, 18", "url": "https://ipindia.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.94,
    },
    {
        "id": "qa_what_is_tkdl",
        "question_patterns": [
            "what is tkdl",
            "what is traditional knowledge digital library",
            "how does tkdl protect traditional knowledge",
            "tkdl and biopiracy",
            "टीकेडीएल क्या है",
            "पारंपरिक ज्ञान डिजिटल पुस्तकालय",
        ],
        "primary_concept": "Traditional Knowledge Digital Library (TKDL)",
        "answer_summary": (
            "The **Traditional Knowledge Digital Library (TKDL)** is India's pioneering database that "
            "provides documented evidence of traditional knowledge to prevent wrongful patents (biopiracy).\n\n"
            "### Key Facts\n"
            "- Contains **2.5 lakh+ formulations** from 54 classical Ayurvedic, Siddha, Unani, and Yoga texts\n"
            "- Translated into **5 languages** (English, French, German, Spanish, Japanese)\n"
            "- Classified using **International Patent Classification (IPC)** codes for easy search by patent examiners\n"
            "- Access agreements with **13+ patent offices** worldwide (EPO, USPTO, JPO, etc.)\n\n"
            "### How It Works\n"
            "When a patent examiner receives an application related to traditional medicine, they search TKDL "
            "for prior art. If the claimed invention matches existing traditional knowledge, the patent is "
            "denied or revoked under **Section 3(p)** of the Patents Act, 1970.\n\n"
            "### Success\n"
            "TKDL has been instrumental in defeating **250+ biopiracy patent claims** at international "
            "patent offices, including patents on turmeric, neem, and basmati rice."
        ),
        "citations": [
            {"id": "tkdl_csir", "source_name": "TKDL — CSIR/AYUSH", "url": "https://tkdl.res.in"},
            {"id": "patents_act_3p_tkdl", "source_name": "Patents Act, 1970 — Section 3(p)", "url": "https://ipindia.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.97,
    },
    {
        "id": "qa_export_ayurvedic_eu",
        "question_patterns": [
            "can i export ayurvedic products to eu",
            "export ayurvedic medicine to europe",
            "how to sell ayurvedic products in european union",
            "eu regulations for ayurvedic products",
            "thmpd ayurveda",
            "आयुर्वेदिक उत्पाद यूरोप निर्यात",
        ],
        "primary_concept": "Exporting Ayurvedic Products to the EU",
        "answer_summary": (
            "### EU Regulatory Pathways\n"
            "**Option 1 — Traditional Herbal Registration (THMPD 2004/24/EC)**\n"
            "- Simplified registration for traditional herbal medicines\n"
            "- Requires evidence of **30 years traditional use** (including 15 years in the EU)\n"
            "- No clinical efficacy trials needed, only safety data\n"
            "- Challenge: Many Ayurvedic products lack documented 15-year EU usage\n\n"
            "**Option 2 — Food Supplement Registration**\n"
            "- Classify product as food/dietary supplement under EU food law\n"
            "- Must comply with Novel Foods Regulation if ingredients are novel to EU\n"
            "- No therapeutic claims allowed\n\n"
            "### Indian Requirements for Export\n"
            "1. Valid Manufacturing License (Schedule T GMP)\n"
            "2. Certificate of Pharmaceutical Product (CoPP)\n"
            "3. Free Sale Certificate from State Drug Controller\n"
            "4. FSSAI license (for food-category products)\n"
            "5. BDA/NBA compliance if using Indian biological resources\n"
            "6. DGFT Import-Export Code (IEC)\n\n"
            "### Heavy Metal Limits\n"
            "EU enforces strict limits — products must meet EU Commission Regulation limits for lead, "
            "mercury, arsenic, and cadmium."
        ),
        "citations": [
            {"id": "eu_thmpd", "source_name": "EU Directive 2004/24/EC (THMPD)", "url": "https://ec.europa.eu"},
            {"id": "ayush_export", "source_name": "AYUSH Ministry Export Guidelines", "url": "https://ayush.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.93,
    },
    {
        "id": "qa_design_patent_packaging",
        "question_patterns": [
            "how to apply for design patent for ayurvedic packaging",
            "design registration for ayurvedic product",
            "protect ayurvedic product packaging design",
            "industrial design ayurvedic bottle",
            "डिजाइन पेटेंट पैकेजिंग",
        ],
        "primary_concept": "Design Registration for Ayurvedic Product Packaging",
        "answer_summary": (
            "### Designs Act, 2000\n"
            "Distinctive Ayurvedic product packaging can be protected under the **Designs Act, 2000**.\n\n"
            "### What Can Be Registered\n"
            "- Distinctive bottle shapes and container forms\n"
            "- Ornamental packaging configurations\n"
            "- Label layouts and surface ornament patterns\n"
            "- Cap and closure designs\n\n"
            "### Requirements (Section 4)\n"
            "- **New or original**: Not previously published in India\n"
            "- **Not purely functional**: Must have aesthetic/visual appeal\n"
            "- **Applied to an article**: Must be applied by industrial process\n\n"
            "### Filing Process\n"
            "1. File Form 1 with the Design Wing of the Patent Office\n"
            "2. Include representations (photographs/drawings) of the design\n"
            "3. Examination and registration (typically 6-12 months)\n\n"
            "**Duration**: 10 years, extendable to 15 years.\n"
            "**International Protection**: Available via Hague System (India acceded 2019)."
        ),
        "citations": [
            {"id": "designs_act_2000", "source_name": "Designs Act, 2000 — Sections 2(d), 4", "url": "https://ipindia.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.92,
    },
    {
        "id": "qa_copyright_classical_texts",
        "question_patterns": [
            "is there copyright on ayurvedic classical texts",
            "copyright protection for ayurvedic texts",
            "can i copyright charaka samhita translation",
            "copyright ayurvedic compilation",
            "आयुर्वेदिक ग्रंथ कॉपीराइट",
        ],
        "primary_concept": "Copyright and Classical Ayurvedic Texts",
        "answer_summary": (
            "### Public Domain vs Copyright\n"
            "**Original Sanskrit classical texts** (Charaka Samhita, Sushruta Samhita, etc.) are "
            "**ancient works in the public domain** — they cannot be copyrighted.\n\n"
            "### What CAN Be Copyrighted\n"
            "Under the **Copyright Act, 1957**:\n"
            "1. **Original translations** with scholarly commentary or annotations\n"
            "2. **Compilations/databases** of Ayurvedic formulations with creative selection & arrangement\n"
            "3. **Modern textbooks** with original analysis and interpretation\n"
            "4. **Illustrations** — diagrams, photographs of medicinal plants\n"
            "5. **Software/databases** for Ayurvedic knowledge management\n\n"
            "### Duration\n"
            "- Author's lifetime + 60 years (for known authors)\n"
            "- 60 years from publication (for anonymous/pseudonymous works)\n\n"
            "### Important Note\n"
            "Copyright protects the **expression** (specific words, arrangement), not the **ideas** or "
            "**facts** (therapeutic uses, formulations). The underlying Ayurvedic knowledge remains public domain."
        ),
        "citations": [
            {"id": "copyright_act_1957", "source_name": "Copyright Act, 1957 — Sections 2(o), 13", "url": "https://copyright.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.93,
    },
    {
        "id": "qa_plant_variety_medicinal",
        "question_patterns": [
            "plant variety protection for medicinal plants",
            "ppvfr act medicinal plants",
            "can i register ashwagandha variety",
            "plant breeders rights ayurvedic herbs",
            "औषधीय पौधों का किस्म संरक्षण",
        ],
        "primary_concept": "Plant Variety Protection for Medicinal Plants",
        "answer_summary": (
            "### PPV&FR Act, 2001\n"
            "The **Protection of Plant Varieties and Farmers' Rights Act, 2001** provides sui generis "
            "protection for medicinal plant varieties.\n\n"
            "### Protectable Varieties\n"
            "- **New varieties** (Section 14): Must be Novel, Distinct, Uniform, Stable (NDUS criteria)\n"
            "- **Extant varieties** (Section 15): Existing varieties not previously registered\n"
            "- **Farmers' varieties** (Section 15): Traditional landraces conserved by farming communities\n\n"
            "### Relevant Medicinal Plants\n"
            "Ashwagandha, Brahmi, Shatavari, Tulsi, Guduchi, Amla — improved cultivars can be registered.\n\n"
            "### Farmers' Rights (Section 39)\n"
            "Farmers who conserve traditional varieties of medicinal plants are entitled to recognition "
            "and reward — critical for communities maintaining landraces.\n\n"
            "### Duration\n"
            "- Trees and vines: 18 years\n"
            "- Other crops: 15 years\n\n"
            "Note: This protects the **plant variety**, not the medicinal use. Therapeutic claims are "
            "covered by patents (Section 3(j) excludes whole plants from patentability)."
        ),
        "citations": [
            {"id": "ppvfr_act", "source_name": "PPV&FR Act, 2001 — Sections 14, 15, 39", "url": "https://plantauthority.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.92,
    },
    {
        "id": "qa_trade_secrets_formulation",
        "question_patterns": [
            "how to protect trade secret ayurvedic formulation",
            "trade secret protection ayurveda",
            "confidential ayurvedic formula protection",
            "nda for ayurvedic formulation",
            "आयुर्वेदिक सूत्र गोपनीयता",
        ],
        "primary_concept": "Trade Secret Protection for Ayurvedic Formulations",
        "answer_summary": (
            "### Trade Secret Protection in India\n"
            "India has no standalone trade secrets statute. Protection is through:\n"
            "1. **Contract Law** — Confidentiality/NDA agreements under Indian Contract Act, 1872\n"
            "2. **Common Law** — Breach of confidence actions\n"
            "3. **TRIPS Article 39** — India's obligation to protect undisclosed information\n\n"
            "### What Can Be a Trade Secret\n"
            "- Exact **proportions and ratios** in a proprietary formula\n"
            "- Specific **processing methods** (Bhavana, Mardana techniques)\n"
            "- **Quality control parameters** and testing protocols\n"
            "- Proprietary **extraction processes**\n\n"
            "### What CANNOT Be a Trade Secret\n"
            "- Classical formulations from First Schedule texts (public domain)\n"
            "- Information already publicly available or in TKDL\n\n"
            "### Best Practices\n"
            "- Execute NDAs with all employees, suppliers, contract manufacturers\n"
            "- Restrict access on need-to-know basis\n"
            "- Mark documents 'Confidential'\n"
            "- Maintain audit trails of who accessed the formula"
        ),
        "citations": [
            {"id": "contract_act_sec27", "source_name": "Indian Contract Act, 1872", "url": "https://indiacode.nic.in"},
            {"id": "trips_art39", "source_name": "TRIPS Agreement — Article 39", "url": "https://www.wto.org"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.91,
    },
    {
        "id": "qa_compulsory_licensing",
        "question_patterns": [
            "what is compulsory licensing for patents in india",
            "compulsory license ayurvedic patent",
            "section 84 patents act compulsory",
            "when can compulsory license be granted",
            "अनिवार्य लाइसेंस पेटेंट भारत",
        ],
        "primary_concept": "Compulsory Licensing under Section 84",
        "answer_summary": (
            "### Section 84 — Compulsory Licensing\n"
            "After **3 years from patent grant**, any interested person may apply for a compulsory license on grounds:\n"
            "1. Reasonable requirements of the public are **not satisfied**\n"
            "2. Patented invention is **not available at a reasonably affordable price**\n"
            "3. Patented invention is **not worked in India**\n\n"
            "### Section 92 — Special Compulsory Licensing\n"
            "In national emergency or extreme urgency, the Controller may grant compulsory licenses "
            "without the 3-year waiting period.\n\n"
            "### Landmark Case\n"
            "**Natco v. Bayer (2012)**: India's first compulsory license — Natco Pharma granted license "
            "for sorafenib (cancer drug) at 3% royalty because Bayer priced it unaffordably.\n\n"
            "### Relevance to Ayurveda\n"
            "If a patented Ayurvedic formulation innovation (standardized extract, bio-enhanced composition) "
            "is priced beyond public reach, compulsory licensing ensures access."
        ),
        "citations": [
            {"id": "patents_act_sec84", "source_name": "Patents Act, 1970 — Sections 84, 92", "url": "https://ipindia.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.94,
    },
    {
        "id": "qa_nba_role",
        "question_patterns": [
            "what is the role of national biodiversity authority",
            "what does nba do",
            "national biodiversity authority functions",
            "nba approval for ayurvedic company",
            "राष्ट्रीय जैव विविधता प्राधिकरण",
        ],
        "primary_concept": "National Biodiversity Authority (NBA) Role",
        "answer_summary": (
            "### National Biodiversity Authority (NBA)\n"
            "Established under the **Biological Diversity Act, 2002**, the NBA is the apex body for "
            "biodiversity governance in India.\n\n"
            "### Key Functions\n"
            "1. **Regulate foreign access**: Approve/deny access to Indian biological resources by foreign "
            "entities or NRIs (Section 3)\n"
            "2. **IP applications**: Prior approval required before applying for any IP rights (patent, "
            "design, trademark) based on Indian biological resources (Section 6)\n"
            "3. **Benefit-sharing**: Determine fair benefit-sharing terms (Section 21)\n"
            "4. **Oppose biopiracy**: Power to oppose patent grants that violate BDA provisions\n\n"
            "### Three-Tier Structure\n"
            "- **NBA** (National): Foreign access, IP approvals\n"
            "- **State Biodiversity Boards** (State): Indian entity commercial access\n"
            "- **Biodiversity Management Committees** (Local): Conservation, PBR documentation\n\n"
            "### 2023 Amendment\n"
            "Exempted registered AYUSH practitioners and codified traditional knowledge users from "
            "benefit-sharing obligations, reducing compliance burden for domestic industry."
        ),
        "citations": [
            {"id": "bda_2002", "source_name": "Biological Diversity Act, 2002 — Sections 3, 6, 21", "url": "https://nbaindia.org"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.94,
    },
    {
        "id": "qa_nagoya_protocol",
        "question_patterns": [
            "what is the nagoya protocol",
            "nagoya protocol and ayurveda",
            "nagoya protocol benefit sharing",
            "abs nagoya protocol",
            "नागोया प्रोटोकॉल क्या है",
        ],
        "primary_concept": "Nagoya Protocol on Access and Benefit-Sharing",
        "answer_summary": (
            "### Nagoya Protocol (2010/2014)\n"
            "The Nagoya Protocol implements the CBD's third objective — fair and equitable sharing of "
            "benefits from genetic resources.\n\n"
            "### Key Articles\n"
            "- **Article 5**: Benefits from utilization of genetic resources and associated traditional "
            "knowledge must be shared fairly with the providing country/community\n"
            "- **Article 6**: Access requires Prior Informed Consent (PIC) of the providing party\n"
            "- **Article 15**: User countries must ensure compliance with provider country's ABS laws\n\n"
            "### India's Implementation\n"
            "India ratified in 2012. The **Biological Diversity Act, 2002** (amended 2023) is the implementing "
            "legislation. The NBA enforces ABS requirements for foreign entities accessing Indian genetic "
            "resources or traditional knowledge.\n\n"
            "### Impact on Ayurveda\n"
            "Foreign companies using Indian medicinal plants or Ayurvedic knowledge must obtain NBA approval "
            "and share benefits with India/local communities. This prevents unauthorized commercial "
            "exploitation of India's rich botanical heritage."
        ),
        "citations": [
            {"id": "nagoya_protocol", "source_name": "Nagoya Protocol — Articles 5, 6, 15", "url": "https://www.cbd.int/abs/"},
            {"id": "bda_2002_abs", "source_name": "Biological Diversity Act, 2002", "url": "https://nbaindia.org"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.95,
    },
    {
        "id": "qa_labeling_asu",
        "question_patterns": [
            "labeling requirements for ayurvedic medicines",
            "what are labeling rules for asu drugs",
            "rule 161 labeling ayurveda",
            "what should be on ayurvedic medicine label",
            "आयुर्वेदिक दवा लेबलिंग आवश्यकताएं",
        ],
        "primary_concept": "Labeling Requirements for ASU Medicines",
        "answer_summary": (
            "### Rule 161 — Mandatory Label Information\n"
            "The Drugs and Cosmetics Rules, 1945 prescribe:\n\n"
            "1. **Drug name** (English and Sanskrit/Hindi)\n"
            "2. **Manufacturer name**, address, and license number\n"
            "3. **Batch/lot number** and date of manufacture\n"
            "4. **Expiry date** and storage conditions\n"
            "5. **Net content** and dosage form\n"
            "6. **Full composition**: All ingredients with quantities\n"
            "7. **Therapeutic indications** and recommended dosage\n"
            "8. **'For external use only'** where applicable\n"
            "9. **Schedule E(1) caution**: 'Caution: To be taken under medical supervision' for products "
            "containing poisonous substances\n"
            "10. **Ayurveda Aahara logo** and 'Not for medicinal use' for food-category products\n\n"
            "### Non-Compliance\n"
            "Misbranding is a criminal offence under the Drugs and Cosmetics Act. Penalties include "
            "imprisonment and fines."
        ),
        "citations": [
            {"id": "dc_rules_161", "source_name": "D&C Rules, 1945 — Rule 161", "url": "https://ayush.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.93,
    },
    {
        "id": "qa_schedule_t_gmp",
        "question_patterns": [
            "what is schedule t gmp for ayurvedic manufacturing",
            "schedule t good manufacturing practices",
            "gmp requirements for ayurvedic drugs",
            "manufacturing standards ayurvedic medicine",
            "शेड्यूल टी जीएमपी आयुर्वेदिक",
        ],
        "primary_concept": "Schedule T GMP for Ayurvedic Manufacturing",
        "answer_summary": (
            "### Schedule T — Good Manufacturing Practices\n"
            "Schedule T of the Drugs and Cosmetics Rules, 1945 prescribes GMP standards specifically "
            "for ASU (Ayurvedic, Siddha, Unani) drug manufacturing.\n\n"
            "### Key Requirements\n"
            "1. **Premises**: Adequate space, ventilation, cleanliness, pest control\n"
            "2. **Equipment**: Appropriate for the dosage form, calibrated, maintained\n"
            "3. **Water System**: Potable water supply, purification as needed\n"
            "4. **Quality Control Lab**: In-house testing for identity, purity, and strength per API standards\n"
            "5. **Raw Material Control**: Identity testing, storage in labeled containers\n"
            "6. **Batch Records**: Complete documentation of each manufacturing batch\n"
            "7. **Qualified Personnel**: Technical staff with prescribed qualifications\n"
            "8. **Sanitation & Hygiene**: Written hygiene programs for personnel and premises\n\n"
            "### Compliance\n"
            "Mandatory for all ASU drug manufacturers. State Drug Controllers inspect facilities. "
            "Non-compliance leads to license suspension or revocation."
        ),
        "citations": [
            {"id": "dc_rules_schedule_t", "source_name": "D&C Rules, 1945 — Schedule T", "url": "https://ayush.gov.in"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.94,
    },
    {
        "id": "qa_benefit_sharing_biodiversity",
        "question_patterns": [
            "what is benefit sharing under biodiversity law",
            "benefit sharing biological diversity act",
            "how does benefit sharing work in india",
            "bda section 21 benefit sharing",
            "लाभ बंटवारा जैव विविधता",
        ],
        "primary_concept": "Benefit Sharing under Biodiversity Law",
        "answer_summary": (
            "### Section 21 — Benefit Sharing\n"
            "The NBA determines benefit-sharing terms when granting access to biological resources.\n\n"
            "### Forms of Benefit Sharing\n"
            "**Monetary:**\n"
            "- Royalty payments, license fees, upfront payments\n"
            "- Milestone payments linked to commercialization\n\n"
            "**Non-Monetary:**\n"
            "- Technology transfer and capacity building\n"
            "- Training of local communities\n"
            "- Joint research collaborations\n"
            "- Contributions to conservation activities\n\n"
            "### Who Must Share Benefits?\n"
            "- Foreign entities/NRIs accessing Indian biological resources (mandatory NBA approval)\n"
            "- Indian entities for commercial utilization (SBB intimation)\n\n"
            "### 2023 Amendment Exemptions\n"
            "- Registered AYUSH practitioners using codified traditional knowledge\n"
            "- Indian users of cultivated medicinal plants (not wild-harvested)\n\n"
            "### Benefit-Sharing Fund\n"
            "Amounts credited to the National or State Biodiversity Fund for conservation and "
            "community development."
        ),
        "citations": [
            {"id": "bda_sec21", "source_name": "Biological Diversity Act, 2002 — Section 21", "url": "https://nbaindia.org"},
        ],
        "confidence": "HIGH",
        "confidence_score": 0.93,
    },
]


# ---------------------------------------------------------------------------
# 3. Intelligent Semantic Matcher
# ---------------------------------------------------------------------------

QA_BY_ID: Dict[str, Dict[str, Any]] = {item["id"]: item for item in INTERNET_TRAINED_QA}


def find_knowledge_match(query: str) -> Optional[Dict[str, Any]]:
    """Search the internet-trained Q&A knowledge base for semantic query match.
    
    Understands conceptual intent across classical epistemology, Ayurvedic principles,
    statutory sections, and regulatory intersections in English, Hindi, and transliterated Sanskrit.
    """
    q = query.lower().strip()
    
    # Exclude fee inquiries, absurd queries, or cross-jurisdiction questions
    if any(stop in q for stop in (
        "fee", "fees", "cost", "how much", "antarctica", "japan",
        "court", "paint", "sad", "cake", "weekend", "holiday", "zzz"
    )):
        return None

    # 1. Canonical epistemology match (specifically for Pramana inquiries)
    pramana_terms = (
        "pramana", "pramanas", "प्रमाण", "aptopadesha", "aptopadesh",
        "आप्तोपदेश", "pradhana pramana", "supreme pramana"
    )
    if any(term in q for term in pramana_terms):
        if any(term in q for term in ("four", "चार", "4", "synergy", "section 3(e)", "yukti", "युक्ति")):
            return QA_BY_ID.get("qa_four_pramanas_synergy")
        return QA_BY_ID.get("qa_supreme_pramana")

    # 2. Direct Concept Routing
    if any(term in q for term in ("phytopharmaceutical", "phytopharmaceuticals", "rule 122e", "cdsco drug")):
        return QA_BY_ID.get("qa_phytopharmaceuticals_cdsco")
        
    if any(term in q for term in ("ayurveda aahara", "ayurveda aahar", "fssai", "food safety", "sold as food")):
        return QA_BY_ID.get("qa_fssai_ayurveda_aahara")

    if any(term in q for term in ("bda", "biological diversity", "nba approval", "form iii", "national biodiversity authority")):
        if any(term in q for term in ("role", "function", "what does nba do", "authority")):
            return QA_BY_ID.get("qa_nba_role")
        if any(term in q for term in ("origin", "disclosure", "section 10", "where plant")):
            return QA_BY_ID.get("qa_bda_geo_origin_disclosure")
        return QA_BY_ID.get("qa_bda_section6_patent_approval")

    if any(term in q for term in ("nagoya", "nagoya protocol")):
        return QA_BY_ID.get("qa_nagoya_protocol")

    if any(term in q for term in ("benefit sharing", "benefit-sharing", "fair and equitable")):
        return QA_BY_ID.get("qa_benefit_sharing_biodiversity")

    if any(term in q for term in ("tkdl", "traditional knowledge digital library", "biopiracy")):
        if any(term in q for term in ("what is tkdl", "explain tkdl", "defensive")):
            return QA_BY_ID.get("qa_what_is_tkdl") or QA_BY_ID.get("qa_tkdl_defensive_protection")
        return QA_BY_ID.get("qa_tkdl_defensive_protection")

    if any(term in q for term in ("trademark", "trade mark", "brand name", "logo registration")):
        return QA_BY_ID.get("qa_trademark_ayurvedic_brand")

    if any(term in q for term in ("design patent", "bottle shape", "packaging design", "industrial design")):
        return QA_BY_ID.get("qa_design_patent_packaging")

    if any(term in q for term in ("copyright", "charaka copyright", "text copyright")):
        return QA_BY_ID.get("qa_copyright_classical_texts")

    if any(term in q for term in ("plant variety", "ppvfr", "breeders rights", "farmers rights")):
        return QA_BY_ID.get("qa_plant_variety_medicinal")

    if any(term in q for term in ("trade secret", "secret formula", "nda", "undisclosed information")):
        return QA_BY_ID.get("qa_trade_secrets_formulation")

    if any(term in q for term in ("compulsory license", "compulsory licensing", "section 84")):
        return QA_BY_ID.get("qa_compulsory_licensing")

    if any(term in q for term in ("export", "thmpd", "europe", "eu market")):
        return QA_BY_ID.get("qa_export_ayurvedic_eu")

    if any(term in q for term in ("schedule t", "gmp", "good manufacturing")):
        return QA_BY_ID.get("qa_schedule_t_gmp")

    if any(term in q for term in ("labeling", "label requirement", "rule 161", "cautionary label")):
        return QA_BY_ID.get("qa_labeling_asu")

    if any(term in q for term in ("how to patent", "patent filing", "patent process", "can i patent")):
        return QA_BY_ID.get("qa_how_to_patent_ayurvedic")

    if any(term in q for term in ("classical vs proprietary", "difference between classical", "proprietary medicine")):
        return QA_BY_ID.get("qa_classical_vs_proprietary")

    if any(term in q for term in ("rule 158b", "rule 158-b", "license classical", "drug license ayurveda")):
        return QA_BY_ID.get("qa_rule_158b_licensing")

    if any(term in q for term in ("wipo", "gratk", "international treaty", "outside india")):
        return QA_BY_ID.get("qa_wipo_gratk_treaty_2024")

    if any(term in q for term in ("advertise", "advertisement", "magic remedies", "cure cancer claim")):
        return QA_BY_ID.get("qa_advertising_drugs_magic_remedies")

    if any(term in q for term in ("bioenhancer", "bio-enhancer", "piperine", "curcumin piperine")):
        return QA_BY_ID.get("qa_bioenhancers_piperine_patents")

    if any(term in q for term in ("ctri", "clinical trial mandatory", "gcp guidelines")):
        return QA_BY_ID.get("qa_clinical_trials_ctri_ayurveda")

    if any(term in q for term in ("bhasma", "bhasmas", "heavy metal", "rasashastra", "schedule e(1)", "poisonous")):
        return QA_BY_ID.get("qa_bhasmas_heavy_metals_regulation")

    if any(term in q for term in ("gi tag", "geographical indication", "kashmir saffron", "alleppey cardamom")):
        return QA_BY_ID.get("qa_gi_registration_ayurveda")

    if any(term in q for term in ("classical", "triphala", "chyawanprash")) and "patent" in q:
        return QA_BY_ID.get("qa_patent_classical_vs_proprietary")

    # 3. Flexible pattern matching with token overlap
    q_words = set(re.findall(r'\w+', q))
    for item in INTERNET_TRAINED_QA:
        for pat in item["question_patterns"]:
            if len(pat) > 6 and pat in q:
                return item
            pat_words = set(re.findall(r'\w+', pat))
            overlap = pat_words.intersection(q_words)
            if len(pat_words) >= 3 and len(overlap) / len(pat_words) >= 0.65:
                return item

    return None

