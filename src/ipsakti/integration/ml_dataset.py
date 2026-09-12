"""Comprehensive Training Corpus for Ayurvedic IP & Epistemological Machine Learning Model.

Contains verified canonical treatises (Charaka, Sushruta, Nyaya), Indian statutory laws
(Patents Act 1970, Drugs & Cosmetics Act 1940, Biological Diversity Act 2002),
and regulatory guidelines (CDSCO, FSSAI, WIPO, CTRI, TKDL).
"""
from __future__ import annotations

from typing import Any, Dict, List

TRAINING_DOCUMENTS: List[Dict[str, Any]] = [
    {
        "doc_id": "doc_aptopadesha_core_characteristics",
        "title": "Aptopadesha: Core Defining Characteristics of an Apta and Epistemological Validation",
        "category": "canonical_epistemology",
        "source_name": "Charaka Samhita Vimanasthana 8.33 & Sutrasthana 11.18-19",
        "source_type": "Classical Treatise",
        "section": "Vimanasthana 8.33 & Sutrasthana 11.18-19",
        "url": "https://tkdl.res.in",
        "keywords_hi": "आप्तोपदेश प्रमाण आप्त चरक संहिता लक्षण विशेषता सर्वोच्च प्रमाण प्रत्यक्ष अनुमान युक्ति रजस्तमो निर्मुक्त त्रिकाल अमल ज्ञान",
        "content": (
            "In classical Ayurvedic epistemology (Pramana Vijnana), Aptopadesha (Authoritative Verbal Testimony) "
            "is the Supreme Pramana (Pradhana Pramana). Acharya Charaka defines the core characteristics of an Apta: "
            "'Aptas tu khalu Raja-Tamo Nirmukta Tapo-Jnana Balena Ye / Yesham Trikala-Amalam Jnanam Avyahatam Sada / "
            "Ete Hyapta Shishtas Vibuddhas Tesham Vakyam Asamshayam'.\n"
            "Core Defining Characteristics:\n"
            "1. Raja-Tamo Nirmuktatva (Complete Freedom from Passion, Greed, and Ignorance): Sages are entirely free "
            "from Rajas (attachment, self-interest, commercial bias) and Tamas (delusion, ignorance). In classical jurisprudence, "
            "falsehood arises solely from greed, malice, or ignorance. Because an Apta is devoid of both, their speech is "
            "inherently and incontrovertibly truthful (Avitatha Vachana).\n"
            "2. Trikala-Amala Jnana (Untainted Tri-Temporal Cognition): Their knowledge across past, present, and future is pure "
            "and unclouded, born of meditative penance (Tapas) and profound realization (Jnana-Bala).\n"
            "3. Avyahata Vachana and Avisamvada (Uncontradicted and Empirically Inviolable Speech): Their instructions are never "
            "refuted by subsequent empirical observation (Pratyaksha) or logical reasoning (Anumana).\n"
            "4. Sarvabhuta Hite Ratah (Universal Altruism): Their teachings are expounded solely for the compassionate alleviation "
            "of human disease and suffering (Dukha-Prashamana), devoid of private profit.\n"
            "Why it Validates as Supreme Pramana: Sensory perception is severely limited ('Pratyaksham hyalpam, analpam apratyaksham'). "
            "The physical senses cannot directly perceive subtle pathogenic mechanisms, hidden channels (Srotas), or unseen drug "
            "potencies (Virya/Prabhava). Inference (Anumana) requires a prior known concomitant relation (Vyapti), which cannot "
            "begin without an authoritative baseline. Therefore, Aptopadesha provides the self-validating baseline (Svatah-Pramanya) "
            "that guides and validates all clinical inquiry, observation, and experimentation."
        ),
        "citation_id": "charaka_samhita_sutrasthana_11",
        "excerpt": "Aptas are those who are freed from Rajas and Tamas by virtue of spiritual discipline and wisdom; their knowledge of past, present, and future is pure and their speech is perpetually uncontradicted.",
    },
    {
        "doc_id": "doc_supreme_pramana_general",
        "title": "Aptopadesha as Supreme Pramana in Epistemological Hierarchy",
        "category": "canonical_epistemology",
        "source_name": "Charaka Samhita Sutrasthana 11.17-27",
        "source_type": "Classical Treatise",
        "section": "Sutrasthana 11.17-27",
        "url": "https://tkdl.res.in",
        "keywords_hi": "सर्वोच्च प्रमाण आप्तोपदेश चरक संहिता सूत्रस्थान प्रथम अनुसूची ड्रग्स एंड कॉस्मेटिक्स एक्ट धारा 3(p) टीकेडीएल",
        "content": (
            "Acharya Charaka designates Aptopadesha as the foremost of the four Pramanas (Aptopadesha, Pratyaksha, "
            "Anumana, Yukti). Direct sensory observation (Pratyaksha) is tiny compared to the vast unperceived universe "
            "('Pratyaksham hyalpam, analpam apratyaksham'). Because unseen pathology, systemic etiology, and distant outcomes "
            "cannot be observed by the eyes, Pratyaksha and Anumana must be guided by Aptopadesha.\n"
            "Statutory Recognition: Modern Indian drug law codifies Aptopadesha in Section 3(a) of the Drugs and Cosmetics "
            "Act, 1940, recognizing 54 classical texts as authoritative. Under Rule 158-B, formulations from these texts are "
            "exempt from clinical trials. Under Section 3(p) of the Patents Act, 1970, formulations documented in these "
            "texts form India's public domain Traditional Knowledge (Prior Art), protected by the Traditional Knowledge "
            "Digital Library (TKDL)."
        ),
        "citation_id": "dc_act_1940_first_schedule",
        "excerpt": "The First Schedule to the Drugs and Cosmetics Act, 1940 lists the 54 authoritative classical books of Ayurvedic, Siddha and Unani systems as the statutory basis for traditional medicines.",
    },
    {
        "doc_id": "doc_four_pramanas_yukti_synergy",
        "title": "Chaturvidha Pramana and Yukti's Statutory Equivalence to Section 3(e) Patent Synergy",
        "category": "patent_epistemology",
        "source_name": "Charaka Samhita Sutrasthana 11.25 & Indian Patents Act Section 3(e)",
        "source_type": "Classical & Patent Statute",
        "section": "Sutrasthana 11.25 & Section 3(e)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "चार प्रमाण आप्तोपदेश प्रत्यक्ष अनुमान युक्ति धारा 3(e) सिनर्जी पेटेंट चरक संहिता",
        "content": (
            "Ayurveda recognizes four means of valid cognitive proof: Aptopadesha (authoritative testimony), Pratyaksha "
            "(direct sensory observation), Anumana (logical deduction based on Vyapti), and Yukti (rational experimental combination).\n"
            "Yukti is the intellect that plans multiple causative factors (Dosha, Dhatu, Kala, Desha, Dravya) in harmony to produce "
            "an optimal therapeutic effect without contradiction. In modern patent law, Section 3(e) of the Patents Act, 1970 bars "
            "patents on mere admixtures resulting only in the aggregation of the properties of the components. Yukti is the classical "
            "foundation for demonstrating inventive synergy — where combined polyherbal ingredients produce unexpected therapeutic "
            "superiority exceeding the sum of individual components."
        ),
        "citation_id": "patents_act_1970_sec3e",
        "excerpt": "A substance obtained by a mere admixture resulting only in the aggregation of the properties of the components thereof is not patentable unless synergistic efficacy is demonstrated.",
    },
    {
        "doc_id": "doc_patents_classical_vs_proprietary_3p",
        "title": "Patentability of Classical vs Proprietary Ayurvedic Formulations under Section 3(p)",
        "category": "patent_law",
        "source_name": "The Patents Act, 1970 (Section 3(p), 3(e), 3(d)) & TKDL",
        "source_type": "Patent Statute",
        "section": "Section 3(p)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "शास्त्रीय योग पेटेंट धारा 3(p) पारंपरिक ज्ञान त्रिफला च्यवनप्राश स्वामित्व औषधि",
        "content": (
            "Classical Ayurvedic formulations cannot be patented in India. Under Section 3(p) of the Patents Act, 1970, an "
            "invention which in effect is traditional knowledge or an aggregation of known properties of traditionally known components "
            "is not an invention. Formulations documented in First Schedule texts (e.g. Triphala, Chyawanprash, Trikatu) are public domain "
            "prior art.\n"
            "Patentable Proprietary Innovations: To obtain a patent, an Ayurvedic product must demonstrate:\n"
            "1. Novel, non-obvious extraction processes isolating standardized fractions.\n"
            "2. Synergistic compositions with statistical proof of unexpected efficacy overcoming Section 3(e).\n"
            "3. Novel formulations with enhanced bioavailability or therapeutic efficacy overcoming Section 3(d).\n"
            "4. Modified delivery systems such as nano-phytosomes or liposomal herbal delivery."
        ),
        "citation_id": "patents_act_1970_sec3p",
        "excerpt": "Section 3(p) of the Patents Act, 1970 declares that an invention which in effect is traditional knowledge or an aggregation of known properties of traditionally known components is not an invention.",
    },
    {
        "doc_id": "doc_tkdl_prior_art_defense",
        "title": "Traditional Knowledge Digital Library (TKDL) and International Biopiracy Defense",
        "category": "defensive_ip",
        "source_name": "Traditional Knowledge Digital Library (CSIR & Ministry of Ayush)",
        "source_type": "Government Repository",
        "section": "Defensive Prior Art",
        "url": "https://tkdl.res.in",
        "keywords_hi": "टीकेडीएल पारंपरिक ज्ञान डिजिटल लाइब्रेरी सीएसआईआर आयुष बायो-पायरेसी पूर्व कला",
        "content": (
            "The Traditional Knowledge Digital Library (TKDL) is a collaborative initiative between CSIR and the Ministry of Ayush. "
            "It translates classical Sanskrit, Urdu, Arabic, and Tamil formulations from 54 First Schedule texts into five international "
            "languages (English, French, German, Spanish, Japanese) structured according to the International Patent Classification (IPC).\n"
            "Through formal access agreements with patent offices globally (USPTO, EPO, JPO, UKIPO, CIPO), patent examiners search TKDL "
            "prior art before granting claims, successfully blocking hundreds of biopiracy patent attempts worldwide on Neem, Turmeric, "
            "and classical formulations."
        ),
        "citation_id": "tkdl_official_portal",
        "excerpt": "TKDL bridges the linguistic gap between classical Indian texts and modern patent examiners, preventing misappropriation of traditional knowledge.",
    },
    {
        "doc_id": "doc_bda_section_6_nba_approval",
        "title": "Mandatory Approval from National Biodiversity Authority under BDA Section 6",
        "category": "biodiversity_law",
        "source_name": "The Biological Diversity Act, 2002 (as amended 2023) — Section 6",
        "source_type": "Statute",
        "section": "Section 6 & Form III",
        "url": "https://nbaindia.org",
        "keywords_hi": "राष्ट्रीय जैव विविधता प्राधिकरण एनबीए अनुमोदन धारा 6 फॉर्म III जैव विविधता अधिनियम",
        "content": (
            "Under Section 6 of the Biological Diversity Act, 2002 (amended in 2023), any person or corporation applying for an "
            "Intellectual Property Right (patent) in India or abroad based on research or information on biological resources obtained from "
            "India MUST obtain prior approval from the National Biodiversity Authority (NBA).\n"
            "In India, the patent application may be filed at the patent office, but NBA approval (Form III) must be granted before the patent "
            "is issued. The NBA may impose benefit sharing conditions under Section 21. Under the 2023 Amendment, registered AYUSH practitioners "
            "and codified traditional knowledge formulations are exempted from commercial access benefit-sharing taxes."
        ),
        "citation_id": "bda_2002_sec6",
        "excerpt": "No person shall apply for any intellectual property right, by whatever name called, in or outside India for any invention based on any research or information on a biological resource obtained from India without obtaining the previous approval of the National Biodiversity Authority.",
    },
    {
        "doc_id": "doc_patents_section_10_4_d_origin",
        "title": "Mandatory Geographical Origin Disclosure under Section 10(4)(d) of Patents Act",
        "category": "patent_law",
        "source_name": "The Patents Act, 1970 — Section 10(4)(d)",
        "source_type": "Patent Statute",
        "section": "Section 10(4)(d)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "भौगोलिक मूल प्रकटीकरण धारा 10(4)(d) पेटेंट अधिनियम जैविक संसाधन स्रोत",
        "content": (
            "Section 10(4)(d) of the Patents Act, 1970 requires that every patent specification disclose the source and geographical origin "
            "of any biological material used in the invention when obtained from India.\n"
            "Consequences of Non-Disclosure: Failure to disclose or wrongful disclosure of geographical origin provides statutory grounds for:\n"
            "1. Pre-grant opposition under Section 25(1)(j).\n"
            "2. Post-grant opposition under Section 25(2)(j).\n"
            "3. Revocation of the granted patent under Section 64(1)(p)."
        ),
        "citation_id": "patents_act_1970_sec10",
        "excerpt": "The specification must disclose the source and geographical origin of the biological material in the specification, when that material is used in an invention and is obtained from India.",
    },
    {
        "doc_id": "doc_rule_158b_licensing_evidence",
        "title": "Rule 158-B of Drugs & Cosmetics Rules, 1945: Licensing Matrix and Trial Exemptions",
        "category": "drug_regulation",
        "source_name": "Drugs and Cosmetics Rules, 1945 — Rule 158-B",
        "source_type": "Regulation",
        "section": "Rule 158-B",
        "url": "https://ayush.gov.in",
        "keywords_hi": "नियम 158-बी औषधि लाइसेंस शास्त्रीय औषधि छूट नैदानिक परीक्षण सुरक्षा साक्ष्य",
        "content": (
            "Rule 158-B establishes the regulatory evidence matrix for licensing Ayurvedic, Siddha, and Unani (ASU) medicines:\n"
            "1. Category A (Classical Medicines): Formulations prepared strictly according to First Schedule authoritative books. "
            "Exempt from animal toxicity studies and clinical trials; classical textual documentation is recognized as empirical human evidence.\n"
            "2. Category B (Patent or Proprietary with classical ingredients): Ingredients from classical texts in non-classical proportions. "
            "Requires published safety literature or pilot clinical trial data.\n"
            "3. Category C & D (Aqueous/hydroalcoholic extracts & novel indications): Requires acute oral toxicity testing (OECD 423) and full clinical trial dossiers."
        ),
        "citation_id": "dc_rules_rule158b",
        "excerpt": "Guidelines for issue of license with respect to Ayurvedic, Siddha or Unani drugs. Delineates proof of safety and effectiveness for classical versus proprietary formulations.",
    },
    {
        "doc_id": "doc_cdsco_phytopharmaceuticals",
        "title": "CDSCO Regulatory Framework for Phytopharmaceutical Drugs (Rule 122E)",
        "category": "drug_regulation",
        "source_name": "Central Drugs Standard Control Organisation — Rule 122E & Schedule Y",
        "source_type": "Regulation",
        "section": "Rule 122E & Schedule Y",
        "url": "https://cdsco.gov.in",
        "keywords_hi": "फाइटोफार्मास्युटिकल ड्रग सीडीएससीओ नियम 122ई बायोएक्टिव मार्कर क्लिनिकल ट्रायल",
        "content": (
            "Phytopharmaceuticals are a modern pharmaceutical drug class defined under the Drugs and Cosmetics Rules (Amendment 2015). "
            "A phytopharmaceutical drug is a purified and standardized fraction with a minimum of four bioactive marker compounds extracted "
            "from plant parts.\n"
            "Regulatory Route: Regulated by CDSCO (DCGI), not state AYUSH licensing. Requires full Phase I, Phase II, and Phase III human clinical trials, "
            "toxicology, and stability dossiers.\n"
            "Patentability: High patentability potential because the standardized solvent fractionation and multi-marker fingerprint represent novel "
            "technical isolation rather than classical whole-herb preparation, overcoming Section 3(p) when inventive step is demonstrated."
        ),
        "citation_id": "cdsco_phytopharmaceutical_2015",
        "excerpt": "Phytopharmaceutical drug means purified and standardized fraction with defined minimum four marker compounds extracted from plant origin.",
    },
    {
        "doc_id": "doc_fssai_ayurveda_aahara",
        "title": "FSSAI Ayurveda Aahara Regulations (2022) vs AYUSH Drug Licensing",
        "category": "food_safety",
        "source_name": "Food Safety and Standards (Ayurveda Aahara) Regulations, 2022",
        "source_type": "Regulation",
        "section": "Regulation 3 & Schedule A",
        "url": "https://fssai.gov.in",
        "keywords_hi": "आयुर्वेद आहार एफएसएसएआई खाद्य सुरक्षा नियम 2022 पोषण दावा रोग निवारण निषेध",
        "content": (
            "The Food Safety and Standards (Ayurveda Aahara) Regulations, 2022 establish rules for foods prepared in accordance with classical "
            "Ayurvedic texts listed in Schedule A for nutritional purposes.\n"
            "Prohibitions:\n"
            "1. Must NOT make claims to prevent, treat, or cure any specific disease or pathology.\n"
            "2. Must NOT contain Schedule E(1) poisonous botanical substances.\n"
            "3. Must NOT be presented as pharmaceutical dosage forms targeting disease states.\n"
            "Labeling: Must carry the official 'Ayurveda Aahara' logo and declaration: 'Not for medicinal use'. Therapeutic formulations must be "
            "licensed under AYUSH drug rules, not FSSAI."
        ),
        "citation_id": "fssai_ayurveda_aahara_2022",
        "excerpt": "Ayurveda Aahara shall not include Ayurvedic drugs, proprietary Ayurvedic medicines, medicinal plant extracts or synthetic additives. No disease cure or mitigation claims shall be made.",
    },
    {
        "doc_id": "doc_geographical_indications_ayurveda",
        "title": "Geographical Indications of Goods Act, 1999 for Ayurvedic Botanicals",
        "category": "gi_law",
        "source_name": "The Geographical Indications of Goods Act, 1999 — Section 8 & Section 11",
        "source_type": "Statute",
        "section": "Section 8 & Section 11",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "भौगोलिक उपदर्शन जीआई टैग कश्मीर केसर नवारा चावल जीआई अधिनियम 1999",
        "content": (
            "Under the Geographical Indications of Goods (Registration and Protection) Act, 1999, GIs protect products whose special quality, "
            "reputation, or chemical profile is inextricably linked to geographical origin, climate, soil, or traditional community skills.\n"
            "Collective Right: A GI belongs to a collective association of producers or community, never to a single private corporate monopoly.\n"
            "Examples: Kashmir Saffron (high crocin/safranal due to Karewa soil), Alleppey Green Cardamom, Malabar Pepper, Navara Rice.\n"
            "Difference from Patents: Patents grant a 20-year temporary private monopoly for novel inventions. GIs grant indefinite, collectively "
            "held regional protection (renewable every 10 years) for cultural and agricultural heritage."
        ),
        "citation_id": "gi_act_1999_sec8",
        "excerpt": "Any association of persons or producers representing the interest of the producers of the concerned goods to which a geographical indication is attributed may apply for registration.",
    },
    {
        "doc_id": "doc_wipo_gratk_treaty_2024",
        "title": "WIPO GRATK Treaty 2024: Mandatory International Patent Disclosures",
        "category": "international_ip",
        "source_name": "WIPO Treaty on Intellectual Property, Genetic Resources and Associated Traditional Knowledge (2024)",
        "source_type": "International Treaty",
        "section": "Article 3",
        "url": "https://www.wipo.int",
        "keywords_hi": "विपो जीआरएटीके संधि 2024 अनिवार्य प्रकटीकरण आनुवंशिक संसाधन पारंपरिक ज्ञान पीसीटी",
        "content": (
            "Adopted on May 24, 2024, the WIPO GRATK Treaty creates a historic global standard:\n"
            "1. Mandatory Patent Disclosure: Patent applicants worldwide MUST disclose the country of origin of genetic resources and the "
            "indigenous/local community providing associated traditional knowledge.\n"
            "2. Information Systems: Establishes interoperable traditional knowledge databases linking foreign patent offices with resources "
            "like India's TKDL to stop international biopiracy.\n"
            "3. Global Filing: For international patent protection across 157 countries, applicants file via the Patent Cooperation Treaty (PCT)."
        ),
        "citation_id": "wipo_gratk_treaty_2024",
        "excerpt": "Where the claimed invention in a patent application is based on genetic resources and associated traditional knowledge, each Contracting Party shall require applicants to disclose the country of origin or source.",
    },
    {
        "doc_id": "doc_bioenhancers_piperine_synergy",
        "title": "Patentability of Bio-enhancers (Piperine) and Overcoming Section 3(d) and 3(e)",
        "category": "patent_pharma",
        "source_name": "Indian Patent Office Guidelines & Section 3(d)/3(e) Case Law",
        "source_type": "Patent Guidelines",
        "section": "Section 3(d) & 3(e)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "बायोएन्हांसर पिपरीन करक्यूमिन जैवउपलब्धता धारा 3(d) धारा 3(e) सिनर्जी पेटेंट",
        "content": (
            "Classical texts (e.g. Trikatu) describe using black pepper to increase digestive fire (Dipana/Pachana). Using crude black pepper powder "
            "in traditional ratios is barred as traditional knowledge under Section 3(p).\n"
            "Patentable Bio-enhancer Inventions: If an applicant uses a purified constituent (e.g. 98% pure Piperine) combined with a botanical active "
            "(e.g. Curcumin) at defined non-classical molar ratios, and produces comparative experimental data showing dramatic bioavailability increase "
            "(e.g. 2000% serum AUC increase) resulting in statistically superior therapeutic efficacy, this overcomes Section 3(e) (inventive synergy) "
            "and satisfies the Supreme Court Novartis standard under Section 3(d)."
        ),
        "citation_id": "patent_guidelines_pharma",
        "excerpt": "To establish synergism under Section 3(e), the applicant must produce comparative experimental data demonstrating that the combined action of the components exceeds the aggregate effect.",
    },
    {
        "doc_id": "doc_advertising_magic_remedies_act",
        "title": "Advertising Restrictions on Ayurvedic Medicines under DMR Act and Rule 170",
        "category": "advertising_law",
        "source_name": "The Drugs and Magic Remedies (Objectionable Advertisements) Act, 1954 & Rule 170",
        "source_type": "Statute & Regulation",
        "section": "Section 3 & Rule 170",
        "url": "https://ayush.gov.in",
        "keywords_hi": "विज्ञापन प्रतिबंध औषधि एवं चमत्कारिक उपचार अधिनियम नियम 170 कैंसर इलाज दावा भ्रामक विज्ञापन",
        "content": (
            "Under Section 3 of the Drugs and Magic Remedies (Objectionable Advertisements) Act, 1954, no person may publish any advertisement "
            "claiming the diagnosis, cure, mitigation, or prevention of 54 specified diseases listed in the Schedule (including cancer, diabetes, "
            "kidney disorders, epilepsy, blindness).\n"
            "Rule 170 of the Drugs and Cosmetics Rules mandates prior approval from the State Licensing Authority before publishing any advertisement "
            "for ASU medicines. Violations carry criminal penalties, fines, and cancelation of manufacturing licenses."
        ),
        "citation_id": "dmra_1954_sec3",
        "excerpt": "No person shall take part in the publication of any advertisement referring to any drug which suggests or is calculated to lead to the use of that drug for the diagnosis, cure, mitigation, treatment or prevention of any disease specified in the schedule.",
    },
    {
        "doc_id": "doc_rasa_panchaka_dravyaguna",
        "title": "Rasa Panchaka Epistemology and Therapeutic Efficacy under Section 3(d)",
        "category": "canonical_epistemology",
        "source_name": "Charaka Samhita Sutrasthana Ch. 26 & Indian Patents Act Section 3(d)",
        "source_type": "Classical & Patent Statute",
        "section": "Sutrasthana 26 & Section 3(d)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "रस पंचक द्रव्यगुण रस गुण वीर्य विपाक प्रभाव धारा 3(d) चिकित्सीय प्रभावकारिता",
        "content": (
            "Ayurvedic pharmacology is governed by Rasa Panchaka:\n"
            "1. Rasa (6 tastes initiating immediate autonomic feedback).\n"
            "2. Guna (20 somatic qualities like heavy/light, dry/unctuous).\n"
            "3. Virya (thermodynamic potency: Sheeta or Ushna).\n"
            "4. Vipaka (post-digestive transformation: Madhura, Amla, Katu).\n"
            "5. Prabhava (specific unexplained pharmacological action not deducible from Rasa, Virya, or Vipaka alone).\n"
            "Section 3(d) Bridge: Section 3(d) of the Patents Act, 1970 requires proof of enhanced therapeutic efficacy for new forms of known substances. "
            "Prabhava and pharmaceutical processing (Samskara / Bhavana) represent classical counterparts to demonstrating unexpected therapeutic bio-efficacy."
        ),
        "citation_id": "ayur_pramana_rasa_panchaka",
        "excerpt": "Prabhava represents the specific pharmacological action of a drug that transcends deducible Rasa and Virya, aligning with the modern requirement of enhanced therapeutic efficacy under Section 3(d).",
    },
    {
        "doc_id": "doc_schedule_t_gmp_standards",
        "title": "Schedule T Good Manufacturing Practices (GMP) for Ayurvedic Medicines",
        "category": "manufacturing_standards",
        "source_name": "Drugs and Cosmetics Rules, 1945 — Schedule T",
        "source_type": "Regulation",
        "section": "Schedule T",
        "url": "https://ayush.gov.in",
        "keywords_hi": "अनुसूची टी जीएमपी विनिर्माण मानक गुणवत्ता नियंत्रण आयुष औषधि निर्माण",
        "content": (
            "Schedule T of the Drugs and Cosmetics Rules, 1945 prescribes mandatory Good Manufacturing Practices (GMP) for all ASU manufacturing units. "
            "It establishes strict statutory standards for:\n"
            "1. Factory premises, hygiene, and environmental controls.\n"
            "2. Quality control laboratories and raw material batch verification.\n"
            "3. Heavy metal, pesticide residue, and microbial contamination limits.\n"
            "4. Standard Operating Procedures (SOP) for classical and proprietary dosage forms (Asava, Arishta, Churna, Bhasma, Taila).\n"
            "All commercial Ayurvedic manufacturers must hold a valid Schedule T GMP certification issued by the State Licensing Authority."
        ),
        "citation_id": "ayur_classical_dosage_forms_schedule_t",
        "excerpt": "Schedule T prescribes mandatory Good Manufacturing Practices including factory hygiene, quality control, raw material testing, and batch records for ASU drugs.",
    },
    {
        "doc_id": "doc_rasashastra_bhasma_safety",
        "title": "Regulation of Herbo-metallic Formulations (Bhasmas) and Schedule E(1)",
        "category": "safety_standards",
        "source_name": "Drugs and Cosmetics Rules, 1945 — Rule 161 & Schedule E(1)",
        "source_type": "Regulation",
        "section": "Rule 161 & Schedule E(1)",
        "url": "https://ayush.gov.in",
        "keywords_hi": "भस्म रसशास्त्र शोधन मारण भारी धातु परीक्षण अनुसूची ई(1) विषैले द्रव्य",
        "content": (
            "Herbo-metallic and mineral formulations (Bhasmas and Rasashastra medicines) undergo classical purification (Shodhana) and incineration (Marana) "
            "converting toxic metals into biocompatible nano-particles.\n"
            "Testing & Labeling Rules: Ayurvedic Pharmacopoeia of India (API) specifies organometallic Bhasma Parikshas (Varitaratva, Rekhapurnatva) and "
            "physicochemical limits. ASU formulations containing poisonous botanical or mineral substances specified in Schedule E(1) (e.g. Vatsanabha, Parada, "
            "Kupilu) must carry a mandatory cautionary label: 'Caution: To be taken under medical supervision'."
        ),
        "citation_id": "dc_rules_rule161_heavy_metals",
        "excerpt": "Mandatory testing for heavy metals and cautionary labeling for ASU medicines containing poisonous substances specified in Schedule E(1).",
    },
    {
        "doc_id": "doc_ctri_registration_clinical_trials",
        "title": "Mandatory CTRI Registration for Ayurvedic Clinical Trials",
        "category": "clinical_trials",
        "source_name": "Clinical Trials Registry - India (ICMR-CTRI) & AYUSH GCP Guidelines",
        "source_type": "Clinical Guidelines",
        "section": "CTRI Registration",
        "url": "https://ctri.nic.in",
        "keywords_hi": "सीटीआरआई नैदानिक परीक्षण रजिस्ट्री आईसीएमआर आयुष जीसीपी दिशानिर्देश",
        "content": (
            "While classical Ayurvedic medicines are exempt from clinical trials under Rule 158-B, any human clinical trial conducted for proprietary "
            "formulations, new indications, or academic R&D must strictly comply with the Good Clinical Practice (GCP) Guidelines for ASU Drugs.\n"
            "Prospective CTRI Mandate: Every clinical trial on human participants in India must be prospectively registered in the Clinical Trials "
            "Registry - India (CTRI) hosted by ICMR before enrolling the first participant. Retrospective registration is prohibited."
        ),
        "citation_id": "ctri_icmr_ayush",
        "excerpt": "Prospective registration in CTRI is mandatory for all clinical trials on ASU interventions before subject recruitment.",
    },
    # ===================================================================
    # NEW TRAINING DOCUMENTS — Expanded Dataset (34 additional entries)
    # ===================================================================
    {
        "doc_id": "doc_trademark_act_1999",
        "title": "Trademark Protection for Ayurvedic Brands under Trade Marks Act, 1999",
        "category": "trademark_law",
        "source_name": "The Trade Marks Act, 1999 — Section 2(1)(zb), Section 9, Section 18",
        "source_type": "Statute",
        "section": "Sections 2(1)(zb), 9, 18",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "ट्रेडमार्क व्यापार चिह्न आयुर्वेदिक ब्रांड पंजीकरण धारा 18 व्यापार चिह्न अधिनियम 1999",
        "content": (
            "The Trade Marks Act, 1999 provides statutory protection for distinctive brand names, logos, "
            "and packaging trade dress used by Ayurvedic product manufacturers. Under Section 2(1)(zb), a "
            "trade mark means a mark capable of being represented graphically and capable of distinguishing "
            "goods or services of one person from those of others. For Ayurvedic brands, this covers product "
            "names, logos, taglines, and distinctive packaging designs.\n"
            "Registration Process: Applications are filed under Section 18 with the Trade Marks Registry. "
            "Section 9 lists absolute grounds for refusal — marks that are not distinctive, descriptive of "
            "goods quality, or common names in trade cannot be registered. Generic Ayurvedic terms like "
            "'Triphala' or 'Chyawanprash' cannot be trademarked as they are common names, but coined brand "
            "names used for such products can be protected.\n"
            "Duration: Registration is valid for 10 years, renewable indefinitely. International protection "
            "is available through the Madrid Protocol (India joined in 2013)."
        ),
        "citation_id": "trademarks_act_1999_sec18",
        "excerpt": "Any person claiming to be the proprietor of a trade mark used or proposed to be used by him may apply for registration.",
    },
    {
        "doc_id": "doc_wellknown_trademarks",
        "title": "Well-Known Trade Marks and Ayurvedic Brand Protection",
        "category": "trademark_law",
        "source_name": "The Trade Marks Act, 1999 — Section 11(6)-(10)",
        "source_type": "Statute",
        "section": "Section 11(6)-(10)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "प्रसिद्ध ट्रेडमार्क आयुर्वेदिक ब्रांड सुरक्षा धारा 11 व्यापार चिह्न",
        "content": (
            "Under Section 11(6)-(10) of the Trade Marks Act, 1999, a well-known trade mark receives "
            "enhanced cross-class protection — it is protected even in unrelated goods categories. For "
            "established Ayurvedic brands with significant market reputation, this prevents third parties "
            "from registering identical or similar marks even for non-competing products.\n"
            "Determination Criteria: The Registrar considers factors including the knowledge of the mark "
            "among the relevant public, duration and extent of use, geographical area of use, duration and "
            "extent of advertising, and record of successful enforcement. The 2017 Trade Mark Rules introduced "
            "a dedicated procedure for listing well-known trade marks in the official journal."
        ),
        "citation_id": "trademarks_act_1999_sec11",
        "excerpt": "A trade mark which has become well known to a substantial segment of the public which uses such goods or receives such services shall be considered a well-known trade mark.",
    },
    {
        "doc_id": "doc_copyright_classical_texts",
        "title": "Copyright Protection for Classical Ayurvedic Texts and Compilations",
        "category": "copyright_law",
        "source_name": "The Copyright Act, 1957 — Section 13, Section 2(o)",
        "source_type": "Statute",
        "section": "Section 13 & Section 2(o)",
        "url": "https://copyright.gov.in",
        "keywords_hi": "कॉपीराइट प्रतिलिप्यधिकार शास्त्रीय ग्रंथ आयुर्वेद चरक संहिता सुश्रुत साहित्यिक कृति",
        "content": (
            "The Copyright Act, 1957 protects original literary, dramatic, musical, and artistic works. "
            "Classical Ayurvedic texts like Charaka Samhita and Sushruta Samhita are ancient works in the "
            "public domain — their original Sanskrit texts cannot be copyrighted. However, modern creative "
            "additions ARE copyrightable:\n"
            "1. Original translations with scholarly commentary or annotations.\n"
            "2. Compilations and databases of Ayurvedic formulations that involve creative selection and arrangement.\n"
            "3. Modern textbooks that contain original analysis and interpretation.\n"
            "4. Illustrations, diagrams, and photographs of medicinal plants.\n"
            "Section 2(o) defines 'literary work' to include tables, compilations, and computer databases. "
            "Copyright lasts for the author's lifetime plus 60 years. Registration is optional but recommended "
            "for evidentiary purposes."
        ),
        "citation_id": "copyright_act_1957_sec13",
        "excerpt": "Copyright shall subsist in original literary, dramatic, musical and artistic works, and compilations including computer databases.",
    },
    {
        "doc_id": "doc_designs_act_2000",
        "title": "Industrial Design Protection for Ayurvedic Product Packaging",
        "category": "design_law",
        "source_name": "The Designs Act, 2000 — Section 2(d), Section 4",
        "source_type": "Statute",
        "section": "Section 2(d) & Section 4",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "डिज़ाइन औद्योगिक डिजाइन पैकेजिंग बोतल आकृति आयुर्वेदिक उत्पाद डिजाइन अधिनियम 2000",
        "content": (
            "The Designs Act, 2000 protects novel and original visual designs applied to articles of "
            "manufacture. For Ayurvedic products, protectable designs include distinctive bottle shapes, "
            "container forms, packaging configurations, and ornamental patterns.\n"
            "Section 2(d) defines 'design' as features of shape, configuration, pattern, ornament or "
            "composition of lines or colours applied to any article by any industrial process. Section 4 "
            "requires the design to be new or original, not previously published, and not contrary to "
            "public order or morality.\n"
            "Registration grants exclusive rights for 10 years, extendable to 15 years. International "
            "protection is available via the Hague System (India acceded in 2019). Design rights complement "
            "trademark protection — a distinctive Ayurvedic product bottle can be both a registered design "
            "and a trade dress."
        ),
        "citation_id": "designs_act_2000_sec4",
        "excerpt": "A design which is new or original, not previously published in India, and is not contrary to public order or morality shall be registrable.",
    },
    {
        "doc_id": "doc_ppvfr_act_2001",
        "title": "Plant Variety Protection for Medicinal Plants under PPV&FR Act, 2001",
        "category": "plant_variety",
        "source_name": "Protection of Plant Varieties and Farmers' Rights Act, 2001",
        "source_type": "Statute",
        "section": "Section 14, Section 15, Section 39",
        "url": "https://plantauthority.gov.in",
        "keywords_hi": "पौध किस्म संरक्षण औषधीय पौधे कृषक अधिकार पीपीवीएफआर अधिनियम 2001",
        "content": (
            "The Protection of Plant Varieties and Farmers' Rights (PPV&FR) Act, 2001 provides sui generis "
            "protection for new plant varieties, extant varieties, and farmers' varieties of medicinal plants "
            "used in Ayurveda.\n"
            "Section 14 grants breeders' rights for new plant varieties that are novel, distinct, uniform, "
            "and stable (NDUS criteria). Section 15 extends registration to extant varieties (existing "
            "varieties not previously registered) and farmers' varieties.\n"
            "Section 39 protects Farmers' Rights — farmers who have conserved and improved traditional "
            "varieties of medicinal plants are entitled to recognition and reward. This is crucial for "
            "communities maintaining landraces of Ashwagandha, Brahmi, Shatavari, and other Ayurvedic "
            "botanicals.\n"
            "Protection duration: Trees and vines — 18 years; other crops — 15 years."
        ),
        "citation_id": "ppvfr_act_2001_sec14",
        "excerpt": "A breeder or his successor or his agent or his licensee may make application for registration of any variety under this Act.",
    },
    {
        "doc_id": "doc_trade_secrets_ayurveda",
        "title": "Trade Secret Protection for Proprietary Ayurvedic Formulations",
        "category": "trade_secret",
        "source_name": "Indian Contract Act, 1872 (Section 27) & Common Law",
        "source_type": "Statute & Common Law",
        "section": "Section 27 & Common Law Principles",
        "url": "https://indiacode.nic.in",
        "keywords_hi": "व्यापार रहस्य गोपनीय सूत्र स्वामित्व आयुर्वेदिक योग गोपनीयता अनुबंध",
        "content": (
            "India does not have a standalone trade secrets statute, but proprietary Ayurvedic formulations "
            "can be protected as trade secrets through contract law (confidentiality agreements under the "
            "Indian Contract Act, 1872) and common law principles of breach of confidence.\n"
            "Protectable Elements: The exact proportions and ratios of ingredients in a proprietary formula, "
            "specific processing methods (Bhavana, Mardana techniques), quality control parameters, and "
            "proprietary extraction processes can all qualify as trade secrets if they are:\n"
            "1. Not generally known or readily ascertainable.\n"
            "2. Subject to reasonable efforts to maintain secrecy (NDAs, restricted access, employee agreements).\n"
            "3. Commercially valuable because of their secrecy.\n"
            "Limitation: Classical formulations from First Schedule texts are public domain and cannot be "
            "claimed as trade secrets. Only genuinely novel proprietary modifications qualify."
        ),
        "citation_id": "contract_act_1872_sec27",
        "excerpt": "Every agreement by which any one is restrained from exercising a lawful profession, trade or business is void, subject to statutory exceptions for reasonable restraint of trade.",
    },
    {
        "doc_id": "doc_patents_section_3d_efficacy",
        "title": "Section 3(d) Enhanced Therapeutic Efficacy — Novartis Standard",
        "category": "patent_law",
        "source_name": "The Patents Act, 1970 — Section 3(d) & Novartis v. Union of India (2013)",
        "source_type": "Patent Statute & Case Law",
        "section": "Section 3(d)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "धारा 3(d) बढ़ी हुई चिकित्सीय प्रभावकारिता नोवार्टिस ज्ञात पदार्थ नया रूप",
        "content": (
            "Section 3(d) of the Patents Act, 1970 bars patents on new forms of known substances unless "
            "they demonstrate significantly enhanced therapeutic efficacy. The Supreme Court in Novartis AG "
            "v. Union of India (2013) interpreted 'enhanced efficacy' for pharmaceutical substances to mean "
            "enhanced therapeutic efficacy specifically.\n"
            "Impact on Ayurveda:\n"
            "1. New salt forms, polymorphs, or particle sizes of known Ayurvedic compounds (e.g. curcumin "
            "nanoparticles) must demonstrate statistically significant improvement in bioavailability or "
            "therapeutic outcomes.\n"
            "2. Mere physical changes (grinding, encapsulation) without enhanced therapeutic data are barred.\n"
            "3. The standard specifically requires comparative clinical or preclinical data showing the new "
            "form performs significantly better than the known substance.\n"
            "This provision prevents evergreening of Ayurvedic compound patents while still allowing "
            "genuinely innovative formulation improvements."
        ),
        "citation_id": "patents_act_1970_sec3d_novartis",
        "excerpt": "The mere discovery of a new form of a known substance which does not result in the enhancement of the known efficacy of that substance is not patentable.",
    },
    {
        "doc_id": "doc_patents_section_3e_admixture",
        "title": "Section 3(e) Mere Admixture vs Synergistic Composition",
        "category": "patent_law",
        "source_name": "The Patents Act, 1970 — Section 3(e)",
        "source_type": "Patent Statute",
        "section": "Section 3(e)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "धारा 3(e) मिश्रण सिनर्जी संयोजन पेटेंट योग्यता समुच्चयन गुण",
        "content": (
            "Section 3(e) of the Patents Act, 1970 excludes from patentability 'a substance obtained by a "
            "mere admixture resulting only in the aggregation of the properties of the components thereof or "
            "a process for producing such substance'.\n"
            "For polyherbal Ayurvedic compositions, this creates a critical threshold:\n"
            "1. A simple mixture of known herbs in standard proportions — NOT patentable (mere admixture).\n"
            "2. A composition where herbs interact to produce an unexpected, synergistic therapeutic effect "
            "BEYOND the sum of individual effects — POTENTIALLY patentable.\n"
            "Proving Synergy: The applicant must provide comparative experimental data:\n"
            "- Individual herb efficacy data.\n"
            "- Combined composition efficacy data.\n"
            "- Statistical proof that combined efficacy exceeds additive prediction.\n"
            "This corresponds to Yukti (rational experimental combination) in classical Ayurvedic epistemology."
        ),
        "citation_id": "patents_act_1970_sec3e_detail",
        "excerpt": "A substance obtained by a mere admixture resulting only in the aggregation of the properties of the components thereof is not an invention.",
    },
    {
        "doc_id": "doc_compulsory_licensing_sec84",
        "title": "Compulsory Licensing for Patents under Section 84",
        "category": "patent_law",
        "source_name": "The Patents Act, 1970 — Section 84",
        "source_type": "Patent Statute",
        "section": "Section 84",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "अनिवार्य लाइसेंस धारा 84 पेटेंट सार्वजनिक स्वास्थ्य सस्ती दवा",
        "content": (
            "Section 84 of the Patents Act, 1970 allows any interested person to apply for a compulsory "
            "license after three years from the date of grant of a patent on three grounds:\n"
            "1. The reasonable requirements of the public with respect to the patented invention have not "
            "been satisfied.\n"
            "2. The patented invention is not available to the public at a reasonably affordable price.\n"
            "3. The patented invention is not worked in the territory of India.\n"
            "For Ayurvedic pharmaceuticals, compulsory licensing can ensure that patented formulation "
            "innovations (standardized extracts, bio-enhanced compositions) remain accessible and affordable "
            "to public health systems. India's 2012 compulsory license on sorafenib (Natco v. Bayer) "
            "demonstrated the practical application of this provision."
        ),
        "citation_id": "patents_act_1970_sec84",
        "excerpt": "At any time after the expiration of three years from the date of the grant of a patent, any person interested may make an application for grant of compulsory licence on any of the specified grounds.",
    },
    {
        "doc_id": "doc_patent_opposition",
        "title": "Pre-Grant and Post-Grant Patent Opposition (Sections 25(1) & 25(2))",
        "category": "patent_law",
        "source_name": "The Patents Act, 1970 — Section 25",
        "source_type": "Patent Statute",
        "section": "Section 25(1) & 25(2)",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "पेटेंट विरोध पूर्व-अनुदान विरोध पश्चात-अनुदान विरोध धारा 25 आपत्ति",
        "content": (
            "The Patents Act, 1970 provides two opposition mechanisms to challenge wrongful patents:\n"
            "Section 25(1) — Pre-Grant Opposition: Any person may file a representation opposing a patent "
            "application after it is published but before grant. Grounds include prior publication, prior "
            "claim, wrongful obtaining, lack of inventive step, non-patentability under Section 3 (including "
            "traditional knowledge under 3(p)), and non-disclosure of biological material source.\n"
            "Section 25(2) — Post-Grant Opposition: Any person interested may file opposition within one year "
            "of patent publication in the official gazette. Same grounds apply.\n"
            "Relevance to Ayurveda: TKDL-based oppositions use Section 25(1)(k) (traditional knowledge under "
            "Section 3(p)) and Section 25(1)(j) (non-disclosure of biological material geographical origin "
            "under Section 10(4)(d)) to block biopiracy patents."
        ),
        "citation_id": "patents_act_1970_sec25",
        "excerpt": "Any person may, by way of representation, oppose the grant of patent on grounds including that the invention is anticipated by traditional knowledge.",
    },
    {
        "doc_id": "doc_prior_art_search",
        "title": "Prior Art Search Methodology for Ayurvedic Patent Inventions",
        "category": "patent_law",
        "source_name": "Indian Patent Office Guidelines & CGPDTM AYUSH Guidelines (2025)",
        "source_type": "Patent Guidelines",
        "section": "Prior Art Search Guidelines",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "पूर्व कला खोज पेटेंट परीक्षण टीकेडीएल शास्त्रीय ग्रंथ खोज पद्धति",
        "content": (
            "Prior art searching for Ayurvedic inventions requires a multi-database approach:\n"
            "1. TKDL Search: Mandatory for AYUSH-related patent applications per CGPDTM guidelines. "
            "Examines 2.5 lakh+ formulations from 54 classical texts in IPC-classified format.\n"
            "2. Patent Database Search: InPASS (Indian Patent Advanced Search System), Espacenet, "
            "Google Patents, USPTO PAIR for existing patent applications and grants.\n"
            "3. Scientific Literature: PubMed, Google Scholar, AYUSH Research Portal for published "
            "research on the claimed composition or method.\n"
            "4. Classical Text Search: Charaka Samhita, Sushruta Samhita, Ashtanga Hridaya, Bhavaprakash "
            "Nighantu, Sharangadhara Samhita for historical prior art.\n"
            "5. Pharmacopoeia: Ayurvedic Pharmacopoeia of India (API), Ayurvedic Formulary of India (AFI).\n"
            "The search must cover both English and Sanskrit/Hindi terms."
        ),
        "citation_id": "cgpdtm_prior_art_guidelines",
        "excerpt": "Patent examiners shall conduct a TKDL search for all AYUSH-related patent applications and apply Section 3 patentability exclusions rigorously.",
    },
    {
        "doc_id": "doc_patent_filing_india",
        "title": "Patent Filing Process in India — Forms, Examination and Timeline",
        "category": "patent_law",
        "source_name": "The Patents Act, 1970 & Patents (Amendment) Rules, 2024",
        "source_type": "Patent Statute & Rules",
        "section": "Sections 7-10, Form 1, Form 2, Form 18",
        "url": "https://ipindia.gov.in",
        "keywords_hi": "पेटेंट आवेदन प्रक्रिया फॉर्म 1 फॉर्म 18 जांच आवेदन भारतीय पेटेंट कार्यालय",
        "content": (
            "Patent filing in India follows a structured procedure:\n"
            "1. Application Filing (Form 1 & Form 2): File a provisional or complete specification with "
            "the Indian Patent Office. For Ayurvedic inventions using biological resources, include "
            "geographical origin disclosure (Section 10(4)(d)) and NBA approval status.\n"
            "2. Publication: Application is published in the Patent Journal 18 months after filing or "
            "earlier on request (Form 9).\n"
            "3. Request for Examination (Form 18): Must be filed within 48 months of filing date.\n"
            "4. Examination: Patent examiner conducts prior art search (including TKDL), issues First "
            "Examination Report (FER), applicant responds within 6 months.\n"
            "5. Grant or Refusal: Controller decides based on examination.\n"
            "6. Opposition Window: Pre-grant opposition possible after publication; post-grant opposition "
            "within 1 year of grant.\n"
            "Patent term: 20 years from filing date."
        ),
        "citation_id": "patents_rules_2024_filing",
        "excerpt": "A request for examination shall be made on Form 18 within forty-eight months from the date of filing of the application.",
    },
    {
        "doc_id": "doc_nagoya_protocol",
        "title": "Nagoya Protocol on Access and Benefit-Sharing (ABS)",
        "category": "biodiversity_law",
        "source_name": "Nagoya Protocol on Access to Genetic Resources and Benefit-Sharing (2010/2014)",
        "source_type": "International Treaty",
        "section": "Articles 5, 6, 15",
        "url": "https://www.cbd.int/abs/",
        "keywords_hi": "नागोया प्रोटोकॉल जैव विविधता लाभ बंटवारा आनुवंशिक संसाधन पहुंच",
        "content": (
            "The Nagoya Protocol (adopted 2010, entered into force 2014) implements the access and "
            "benefit-sharing (ABS) objectives of the Convention on Biological Diversity.\n"
            "Key Provisions:\n"
            "Article 5 — Fair and Equitable Benefit-Sharing: Benefits from utilization of genetic resources "
            "and associated traditional knowledge must be shared fairly with the providing country/community "
            "on mutually agreed terms.\n"
            "Article 6 — Access with Prior Informed Consent (PIC): Access to genetic resources requires prior "
            "informed consent of the providing party and issuance of a permit or equivalent.\n"
            "Article 15 — Compliance: User countries must ensure that genetic resources and traditional "
            "knowledge within their jurisdiction were accessed in accordance with the provider country's laws.\n"
            "India's Implementation: India ratified the Nagoya Protocol in 2012. The Biological Diversity Act, "
            "2002 (amended 2023) and its Rules are India's implementing legislation."
        ),
        "citation_id": "nagoya_protocol_abs",
        "excerpt": "Benefits arising from the utilization of genetic resources as well as subsequent applications and commercialization shall be shared in a fair and equitable way with the Party providing such resources.",
    },
    {
        "doc_id": "doc_cbd_convention",
        "title": "Convention on Biological Diversity (CBD) and Traditional Knowledge",
        "category": "biodiversity_law",
        "source_name": "Convention on Biological Diversity (1992) — Articles 1, 8(j), 15",
        "source_type": "International Treaty",
        "section": "Articles 1, 8(j), 15",
        "url": "https://www.cbd.int",
        "keywords_hi": "जैव विविधता सम्मेलन सीबीडी पारंपरिक ज्ञान अनुच्छेद 8(j) आनुवंशिक संसाधन",
        "content": (
            "The Convention on Biological Diversity (CBD, 1992) is the foundational international treaty "
            "governing conservation, sustainable use, and benefit-sharing of biological resources.\n"
            "Article 1 — Objectives: Conservation of biological diversity, sustainable use, and fair and "
            "equitable sharing of benefits from genetic resources.\n"
            "Article 8(j) — Traditional Knowledge: Each Contracting Party shall respect, preserve and "
            "maintain knowledge, innovations and practices of indigenous and local communities relevant to "
            "conservation and sustainable use, promote their wider application with prior approval, and "
            "encourage equitable sharing of benefits.\n"
            "Article 15 — Access to Genetic Resources: Recognizes sovereign rights of States over their "
            "natural resources. Access requires prior informed consent and mutually agreed terms.\n"
            "India ratified the CBD in 1994. The Biological Diversity Act, 2002 is India's CBD implementation."
        ),
        "citation_id": "cbd_1992_art8j",
        "excerpt": "Each Contracting Party shall respect, preserve and maintain knowledge, innovations and practices of indigenous and local communities embodying traditional lifestyles relevant for the conservation and sustainable use of biological diversity.",
    },
    {
        "doc_id": "doc_bda_benefit_sharing_sec21",
        "title": "Benefit-Sharing Mechanisms under BDA Section 21 (Amended 2023)",
        "category": "biodiversity_law",
        "source_name": "Biological Diversity Act, 2002 (as amended 2023) — Section 21",
        "source_type": "Statute",
        "section": "Section 21",
        "url": "https://nbaindia.org",
        "keywords_hi": "लाभ बंटवारा धारा 21 जैव विविधता अधिनियम राष्ट्रीय जैव विविधता प्राधिकरण",
        "content": (
            "Section 21 of the Biological Diversity Act empowers the National Biodiversity Authority to "
            "determine benefit-sharing terms when granting approval for access to biological resources.\n"
            "Forms of Benefit-Sharing:\n"
            "1. Monetary: Royalty payments, license fees, upfront payments, milestone payments.\n"
            "2. Non-Monetary: Technology transfer, capacity building, training of local communities, "
            "joint research, contribution to conservation activities.\n"
            "2023 Amendment Changes: The Biological Diversity (Amendment) Act, 2023 simplified benefit-sharing "
            "by exempting registered AYUSH practitioners and codified traditional knowledge users from "
            "benefit-sharing obligations. Indian companies accessing biological resources domestically have "
            "reduced compliance burdens, while foreign entities retain full ABS obligations.\n"
            "The benefit-sharing amount is credited to the National Biodiversity Fund or State Biodiversity Fund."
        ),
        "citation_id": "bda_2002_sec21_benefit_sharing",
        "excerpt": "The National Biodiversity Authority shall while granting approvals under this Act ensure that the terms and conditions secure equitable sharing of benefits arising out of the use of biological resources.",
    },
    {
        "doc_id": "doc_sbb_bmc",
        "title": "State Biodiversity Boards and Biodiversity Management Committees",
        "category": "biodiversity_law",
        "source_name": "Biological Diversity Act, 2002 — Sections 22, 41",
        "source_type": "Statute",
        "section": "Sections 22 & 41",
        "url": "https://nbaindia.org",
        "keywords_hi": "राज्य जैव विविधता बोर्ड जैव विविधता प्रबंधन समिति बीएमसी पंचायत स्थानीय निकाय",
        "content": (
            "The Biological Diversity Act establishes a three-tier governance structure:\n"
            "1. National Biodiversity Authority (NBA) — Central level: Regulates access by foreign entities "
            "and approves IP applications based on Indian biological resources.\n"
            "2. State Biodiversity Boards (SBB) — State level (Section 22): Regulate access by Indian "
            "entities for commercial purposes, advise the State Government on conservation.\n"
            "3. Biodiversity Management Committees (BMC) — Local level (Section 41): Constituted by every "
            "local body (panchayat/municipality) to promote conservation, sustainable use, and documentation "
            "of biological diversity. BMCs prepare People's Biodiversity Registers (PBR) documenting local "
            "traditional knowledge including Ayurvedic plant usage.\n"
            "For Ayurvedic companies sourcing raw materials, prior intimation to the concerned SBB is "
            "required under Section 7 for commercial utilization of biological resources."
        ),
        "citation_id": "bda_2002_sec41_bmc",
        "excerpt": "Every local body shall constitute a Biodiversity Management Committee within its area for the purpose of promoting conservation, sustainable use and documentation of biological diversity.",
    },
    {
        "doc_id": "doc_trips_27_3b",
        "title": "TRIPS Agreement Article 27.3(b) — Plant and Animal Patent Exclusions",
        "category": "international_ip",
        "source_name": "Agreement on Trade-Related Aspects of Intellectual Property Rights (TRIPS) — Article 27.3(b)",
        "source_type": "International Treaty",
        "section": "Article 27.3(b)",
        "url": "https://www.wto.org",
        "keywords_hi": "ट्रिप्स समझौता अनुच्छेद 27 पादप जीव पेटेंट बहिष्करण विश्व व्यापार संगठन",
        "content": (
            "Article 27.3(b) of the TRIPS Agreement allows WTO Members to exclude from patentability plants "
            "and animals other than micro-organisms, and essentially biological processes for the production "
            "of plants or animals. However, Members must provide protection for plant varieties either by "
            "patents or by an effective sui generis system or any combination.\n"
            "India uses this TRIPS flexibility through: (a) Section 3(j) of the Patents Act, 1970 excluding "
            "plants, animals, and essentially biological processes from patentability; (b) The PPV&FR Act, "
            "2001 as India's sui generis plant variety protection system that includes Farmers' Rights.\n"
            "Significance for Ayurveda: Whole medicinal plants cannot be patented in India, but isolated "
            "compounds, extraction processes, and novel formulations can be — subject to Sections 3(d), 3(e), "
            "and 3(p) thresholds."
        ),
        "citation_id": "trips_art27_3b",
        "excerpt": "Members may exclude from patentability plants and animals other than micro-organisms, and essentially biological processes.",
    },
    {
        "doc_id": "doc_pct_ayurvedic_filing",
        "title": "PCT Filing for International Ayurvedic Patent Applications",
        "category": "international_ip",
        "source_name": "Patent Cooperation Treaty (PCT) — WIPO",
        "source_type": "International Treaty System",
        "section": "PCT Chapters I & II",
        "url": "https://www.wipo.int/pct/en/",
        "keywords_hi": "पीसीटी अंतर्राष्ट्रीय पेटेंट आवेदन विपो आयुर्वेदिक आविष्कार विदेश फाइलिंग",
        "content": (
            "The Patent Cooperation Treaty (PCT) enables Ayurvedic innovators to file a single international "
            "patent application covering 150+ countries simultaneously.\n"
            "Filing Route from India:\n"
            "1. File PCT application at Indian Patent Office (RO/IN) or WIPO International Bureau using ePCT.\n"
            "2. International Search Report (ISR) and Written Opinion issued within ~16 months.\n"
            "3. International publication at 18 months from priority date.\n"
            "4. Optional Chapter II examination (International Preliminary Examining Authority).\n"
            "5. Enter national phase in chosen countries within 30/31 months from priority date.\n"
            "Key consideration for Ayurvedic applications: The WIPO GRATK Treaty (2024) will require "
            "disclosure of genetic resource origin and traditional knowledge source in PCT applications "
            "once it enters into force."
        ),
        "citation_id": "pct_wipo_filing",
        "excerpt": "A single international patent application under the PCT can seek patent protection across 150+ contracting states through a unified filing procedure.",
    },
    {
        "doc_id": "doc_madrid_trademarks",
        "title": "Madrid System for International Trademark Registration of Ayurvedic Brands",
        "category": "international_ip",
        "source_name": "Madrid Protocol — WIPO International Trademark System",
        "source_type": "International Treaty System",
        "section": "Madrid Protocol",
        "url": "https://www.wipo.int/madrid/en/",
        "keywords_hi": "मैड्रिड प्रणाली अंतर्राष्ट्रीय ट्रेडमार्क पंजीकरण आयुर्वेदिक ब्रांड विपो",
        "content": (
            "The Madrid System, administered by WIPO, enables Ayurvedic brand owners to obtain international "
            "trademark protection through a single application filed via the Indian Trade Marks Office.\n"
            "Process:\n"
            "1. Base Application/Registration: File or register the trademark in India first.\n"
            "2. International Application: File through the Indian Trade Marks Office as Office of Origin.\n"
            "3. Designate Countries: Select target markets for protection.\n"
            "4. WIPO Examination: WIPO conducts formalities check and transmits to designated offices.\n"
            "5. National Examination: Each designated country examines under its own law.\n"
            "Benefits: Single application, one set of fees, centralized management of the portfolio. "
            "Coverage: 130+ member countries. India joined the Madrid Protocol in 2013.\n"
            "Important: The Madrid System registers TRADE MARKS only — not patents or designs."
        ),
        "citation_id": "madrid_protocol_wipo",
        "excerpt": "The Madrid System offers a cost-effective and efficient solution for registering and managing trade marks worldwide through a single application in one language with one set of fees.",
    },
    {
        "doc_id": "doc_hague_designs",
        "title": "Hague System for International Industrial Design Registration",
        "category": "international_ip",
        "source_name": "Hague Agreement (Geneva Act) — WIPO International Design System",
        "source_type": "International Treaty System",
        "section": "Geneva Act of the Hague Agreement",
        "url": "https://www.wipo.int/hague/en/",
        "keywords_hi": "हेग प्रणाली अंतर्राष्ट्रीय औद्योगिक डिजाइन पंजीकरण पैकेजिंग आकृति",
        "content": (
            "The Hague System enables international registration of industrial designs (packaging shapes, "
            "bottle designs, label layouts, product forms) through a single application.\n"
            "For Ayurvedic Products: Distinctive packaging, container shapes, and ornamental label designs "
            "can be protected across multiple countries simultaneously.\n"
            "Process:\n"
            "1. File a single international application with WIPO (up to 100 designs per application).\n"
            "2. WIPO conducts formalities examination.\n"
            "3. International registration published in the International Designs Bulletin.\n"
            "4. Designated countries examine under their national law.\n"
            "India acceded to the Geneva Act of the Hague Agreement in 2019. Protection duration varies "
            "by country but is generally 15-25 years.\n"
            "The Hague System protects DESIGNS only — not patents, trademarks, or copyright."
        ),
        "citation_id": "hague_geneva_act_wipo",
        "excerpt": "The Hague System provides a practical business solution for registering up to 100 designs in over 90 countries by filing one single international application.",
    },
    {
        "doc_id": "doc_budapest_treaty",
        "title": "Budapest Treaty for Microorganism Deposits in Patent Applications",
        "category": "international_ip",
        "source_name": "Budapest Treaty on the International Recognition of the Deposit of Microorganisms (1977)",
        "source_type": "International Treaty",
        "section": "Articles 3 & 7",
        "url": "https://www.wipo.int/budapest/en/",
        "keywords_hi": "बुडापेस्ट संधि सूक्ष्मजीव जमा पेटेंट अंतर्राष्ट्रीय डिपॉजिटरी प्राधिकरण",
        "content": (
            "The Budapest Treaty (1977) provides that a single deposit of a microorganism with any "
            "International Depositary Authority (IDA) suffices for patent applications in all contracting "
            "states.\n"
            "Relevance to Ayurveda:\n"
            "1. Fermented Ayurvedic preparations (Asava, Arishta) using specific microbial strains may "
            "require deposit of the strain for patent sufficiency.\n"
            "2. Probiotics or microbial-based Ayurvedic formulations need Budapest Treaty deposits for "
            "international patent filings.\n"
            "3. Endophytic fungi or bacteria isolated from medicinal plants for novel compounds.\n"
            "India has two IDAs: Microbial Type Culture Collection (MTCC) at IMTECH, Chandigarh, and "
            "Microbial Culture Collection (MCC) at NCCS, Pune.\n"
            "Patent Rule 13(8) of the Indian Patents Rules requires deposit of biological material "
            "mentioned in the specification at a recognized depository."
        ),
        "citation_id": "budapest_treaty_1977",
        "excerpt": "A single deposit of a microorganism with any International Depositary Authority shall suffice for the purposes of patent procedure before the industrial property offices of all contracting states.",
    },
    {
        "doc_id": "doc_api_pharmacopoeia",
        "title": "Ayurvedic Pharmacopoeia of India (API) Monograph Standards",
        "category": "drug_regulation",
        "source_name": "Ayurvedic Pharmacopoeia of India (API) — Ministry of AYUSH",
        "source_type": "Pharmacopoeia",
        "section": "API Volumes I-IX",
        "url": "https://ayush.gov.in",
        "keywords_hi": "आयुर्वेदिक फार्माकोपिया भारत एपीआई मोनोग्राफ मानक गुणवत्ता नियंत्रण",
        "content": (
            "The Ayurvedic Pharmacopoeia of India (API), published by the Ministry of AYUSH, is the official "
            "compendium of quality standards for single Ayurvedic drugs (crude drugs and mineral drugs).\n"
            "Each API monograph specifies:\n"
            "1. Botanical Identity: Latin name, family, Sanskrit/Hindi synonyms.\n"
            "2. Macroscopic and Microscopic Characters: Physical identification parameters.\n"
            "3. Identity Tests: TLC fingerprints, specific chemical tests.\n"
            "4. Quantitative Standards: Total ash, acid-insoluble ash, extractive values, moisture content.\n"
            "5. Heavy Metal Limits: Lead, mercury, arsenic, cadmium within WHO-permissible limits.\n"
            "6. Microbial Limits: Bacterial, fungal, and pathogen contamination limits.\n"
            "7. Therapeutic Properties: Rasa, Guna, Virya, Vipaka, and indicated Doshas.\n"
            "API compliance is mandatory for all Ayurvedic drug manufacturers. The Ayurvedic Formulary of "
            "India (AFI) separately covers compound formulation standards."
        ),
        "citation_id": "api_ayush_standards",
        "excerpt": "The Ayurvedic Pharmacopoeia of India provides quality standards for single Ayurvedic drugs including identity, purity, and strength parameters.",
    },
    {
        "doc_id": "doc_who_traditional_medicine",
        "title": "WHO Guidelines for Safety Evaluation of Traditional Medicines",
        "category": "drug_regulation",
        "source_name": "WHO Traditional Medicine Strategy 2014-2023 & WHO Guidelines",
        "source_type": "International Guidelines",
        "section": "WHO Traditional Medicine Strategy",
        "url": "https://www.who.int",
        "keywords_hi": "विश्व स्वास्थ्य संगठन डब्ल्यूएचओ पारंपरिक चिकित्सा दिशानिर्देश सुरक्षा मूल्यांकन",
        "content": (
            "The World Health Organization (WHO) Traditional Medicine Strategy 2014-2023 provides global "
            "policy guidance for traditional medicine regulation, safety, and integration.\n"
            "Key Guidelines:\n"
            "1. WHO Guidelines on Safety Monitoring of Herbal Medicines: Recommends pharmacovigilance "
            "systems for adverse event reporting of traditional medicines.\n"
            "2. WHO Guidelines for Assessing Quality of Herbal Medicines: Specifies testing for identity, "
            "purity, contamination (heavy metals, pesticides, microbes), and marker compound quantification.\n"
            "3. WHO Guidelines on Good Agricultural and Collection Practices (GACP): Standards for "
            "sustainable sourcing of medicinal plant raw materials.\n"
            "4. WHO Benchmarks for Training in Traditional Medicine: Educational standards for practitioners.\n"
            "India's AYUSH regulatory framework (Schedule T GMP, API monographs) is aligned with WHO "
            "guidelines and is recognized by many importing countries."
        ),
        "citation_id": "who_traditional_medicine_strategy",
        "excerpt": "WHO Member States should develop policies and regulations for traditional medicine to promote safety, efficacy and quality of herbal medicines.",
    },
    {
        "doc_id": "doc_ayush_licensing",
        "title": "AYUSH Ministry Drug Licensing Framework — State vs Central",
        "category": "drug_regulation",
        "source_name": "Drugs and Cosmetics Act, 1940 & AYUSH Ministry Notifications",
        "source_type": "Regulation",
        "section": "Sections 33C-33N (AYUSH)",
        "url": "https://ayush.gov.in",
        "keywords_hi": "आयुष औषधि लाइसेंस राज्य लाइसेंसिंग प्राधिकरण केंद्रीय लाइसेंसिंग विनिर्माण अनुमति",
        "content": (
            "The AYUSH drug licensing framework operates at two levels:\n"
            "State Level: State Licensing Authorities (Drug Controllers) issue manufacturing and "
            "sale licenses for ASU (Ayurvedic, Siddha, Unani) drugs under Sections 33C-33N of the "
            "Drugs and Cosmetics Act, 1940.\n"
            "Central Level: The AYUSH Division of CDSCO handles:\n"
            "- Import licenses for ASU drugs.\n"
            "- Approval for new drug applications (Category C & D under Rule 158-B).\n"
            "- Clinical trial permissions for proprietary formulations.\n"
            "Manufacturing License Requirements:\n"
            "1. Schedule T GMP compliance (factory premises, equipment, QC lab).\n"
            "2. Qualified technical staff (pharmacist or Vaidya with prescribed qualifications).\n"
            "3. Drug testing laboratory with prescribed equipment.\n"
            "4. Batch-wise quality testing records.\n"
            "Each product requires separate product-wise approval."
        ),
        "citation_id": "dc_act_ayush_licensing",
        "excerpt": "The State Government may appoint Licensing Authorities for the purpose of granting licences for the manufacture and sale of Ayurvedic, Siddha and Unani drugs.",
    },
    {
        "doc_id": "doc_schedule_e1_poisons",
        "title": "Schedule E(1) Poisonous Substances in Ayurvedic Medicines",
        "category": "drug_regulation",
        "source_name": "Drugs and Cosmetics Rules, 1945 — Schedule E(1)",
        "source_type": "Regulation",
        "section": "Schedule E(1)",
        "url": "https://ayush.gov.in",
        "keywords_hi": "अनुसूची ई(1) विषैले द्रव्य आयुर्वेदिक औषधि वत्सनाभ कुपीलु पारद सावधानी लेबल",
        "content": (
            "Schedule E(1) of the Drugs and Cosmetics Rules, 1945 lists poisonous botanical and mineral "
            "substances used in Ayurvedic medicines that require special handling:\n"
            "Botanical Poisons: Vatsanabha (Aconitum), Kupilu (Strychnos nux-vomica), Ahiphena (opium "
            "poppy), Bhallataka (Semecarpus), Dhattura (Datura), Jayapala (Croton tiglium).\n"
            "Mineral Poisons: Parada (Mercury), Hartala (Arsenic trisulphide), Manahshila (Arsenic "
            "disulphide), Tuttha (Copper sulphate).\n"
            "Mandatory Requirements:\n"
            "1. Cautionary Label: 'Caution: To be taken under medical supervision'.\n"
            "2. Classical Shodhana (purification): Must be processed according to prescribed classical "
            "methods before incorporation into formulations.\n"
            "3. Heavy metal testing: Final product must meet API/WHO heavy metal limits.\n"
            "4. Dose restrictions as per classical texts."
        ),
        "citation_id": "dc_rules_schedule_e1",
        "excerpt": "Preparations containing poisonous substances specified in Schedule E(1) shall bear the cautionary label 'Caution: To be taken under medical supervision'.",
    },
    {
        "doc_id": "doc_export_ayurvedic",
        "title": "Export of Ayurvedic Products — Regulatory Requirements",
        "category": "export_regulation",
        "source_name": "AYUSH Ministry Export Guidelines & APEDA/DGFT Regulations",
        "source_type": "Regulation & Guidelines",
        "section": "Export Guidelines",
        "url": "https://ayush.gov.in",
        "keywords_hi": "निर्यात आयुर्वेदिक उत्पाद अंतर्राष्ट्रीय बाजार एपीईडीए डीजीएफटी प्रमाणपत्र",
        "content": (
            "Exporting Ayurvedic products requires compliance with both Indian export regulations and "
            "importing country requirements:\n"
            "Indian Requirements:\n"
            "1. Valid Manufacturing License under Schedule T GMP.\n"
            "2. Certificate of Pharmaceutical Product (CoPP) from Drug Controller.\n"
            "3. Free Sale Certificate from State Drug Controller.\n"
            "4. FSSAI license for food-category products.\n"
            "5. APEDA registration for plant-based products.\n"
            "6. DGFT Import-Export Code (IEC).\n"
            "Importing Country Requirements:\n"
            "- EU: Registration under Traditional Herbal Medicinal Products Directive (2004/24/EC) or "
            "food supplement regulations.\n"
            "- USA: DSHEA dietary supplement notification or FDA drug application.\n"
            "- ASEAN: ASEAN harmonized regulatory framework for traditional medicines.\n"
            "- GCC: GCC product registration requirements.\n"
            "Ayurvedic exporters must also comply with BDA/NBA if using Indian biological resources."
        ),
        "citation_id": "ayush_export_guidelines",
        "excerpt": "Ayurvedic products for export must comply with Good Manufacturing Practices under Schedule T and obtain Certificate of Pharmaceutical Product from the Drug Controller.",
    },
    {
        "doc_id": "doc_eu_thmpd",
        "title": "EU Traditional Herbal Medicinal Products Directive (THMPD 2004/24/EC)",
        "category": "export_regulation",
        "source_name": "Directive 2004/24/EC of the European Parliament and Council",
        "source_type": "EU Regulation",
        "section": "Directive 2004/24/EC",
        "url": "https://ec.europa.eu",
        "keywords_hi": "यूरोपीय संघ ईयू पारंपरिक हर्बल औषधि निर्देश टीएचएमपीडी सरलीकृत पंजीकरण",
        "content": (
            "The EU Traditional Herbal Medicinal Products Directive (THMPD, 2004/24/EC) established a "
            "simplified registration procedure for traditional herbal medicines in the European Union.\n"
            "Key Requirements:\n"
            "1. Traditional Use Evidence: At least 30 years of traditional use (including 15 years within "
            "the EU) must be documented. For Ayurvedic products, India's documented traditional usage "
            "typically satisfies the 30-year requirement.\n"
            "2. Safety Data: Bibliographic safety data and an expert safety report. No clinical efficacy "
            "trials required.\n"
            "3. EU GMP Compliance: Manufacturing must comply with EU GMP standards.\n"
            "4. HMPC Monographs: Products should align with Community herbal monographs issued by the "
            "Committee on Herbal Medicinal Products (HMPC).\n"
            "Challenge for Ayurveda: Many polyherbal Ayurvedic formulations lack individual HMPC monographs "
            "and documented EU usage history, making registration difficult."
        ),
        "citation_id": "eu_thmpd_2004_24",
        "excerpt": "Traditional herbal medicinal products may be registered under a simplified procedure demonstrating at least 30 years of traditional use including at least 15 years within the Community.",
    },
    {
        "doc_id": "doc_labeling_rule161",
        "title": "Labeling Requirements for ASU Medicines under Rule 161",
        "category": "labeling_law",
        "source_name": "Drugs and Cosmetics Rules, 1945 — Rule 161",
        "source_type": "Regulation",
        "section": "Rule 161",
        "url": "https://ayush.gov.in",
        "keywords_hi": "लेबलिंग आवश्यकताएं नियम 161 आयुर्वेदिक औषधि पैकेजिंग संरचना खुराक",
        "content": (
            "Rule 161 of the Drugs and Cosmetics Rules, 1945 prescribes mandatory labeling requirements "
            "for Ayurvedic, Siddha, and Unani (ASU) medicines:\n"
            "Required Label Information:\n"
            "1. Name of the drug and its Ayurvedic/Sanskrit name.\n"
            "2. Name and address of the manufacturer and manufacturing license number.\n"
            "3. Batch or lot number and date of manufacture.\n"
            "4. Date of expiry and storage conditions.\n"
            "5. Net content and dosage form.\n"
            "6. Composition: List of all ingredients with quantities.\n"
            "7. Therapeutic indications and recommended dosage.\n"
            "8. 'For external use only' where applicable.\n"
            "9. Schedule E(1) caution label for products containing poisonous substances.\n"
            "10. Ayurveda Aahara logo and 'Not for medicinal use' for food-category products.\n"
            "Non-compliance is a criminal offence under the Drugs and Cosmetics Act."
        ),
        "citation_id": "dc_rules_rule161_labeling",
        "excerpt": "The label on the innermost container of an Ayurvedic, Siddha or Unani drug shall bear the name of the drug, manufacturer details, batch number, date of manufacture, expiry date, composition and dosage.",
    },
    {
        "doc_id": "doc_dpdp_act_2023",
        "title": "Digital Personal Data Protection Act, 2023 — Health Data Compliance",
        "category": "data_protection",
        "source_name": "The Digital Personal Data Protection Act, 2023",
        "source_type": "Statute",
        "section": "Sections 4, 5, 6, 7",
        "url": "https://meity.gov.in",
        "keywords_hi": "डिजिटल व्यक्तिगत डेटा संरक्षण अधिनियम 2023 स्वास्थ्य डेटा गोपनीयता सहमति",
        "content": (
            "The Digital Personal Data Protection Act, 2023 (DPDP Act) establishes India's comprehensive "
            "data protection framework, with specific implications for Ayurvedic healthcare:\n"
            "Key Provisions:\n"
            "Section 4 — Consent: Processing personal data requires free, specific, informed, unconditional, "
            "and unambiguous consent.\n"
            "Section 5 — Purpose Limitation: Data collected for Ayurvedic consultation/treatment cannot be "
            "used for unrelated marketing without fresh consent.\n"
            "Section 6 — Legitimate Uses: Health data processing permitted for medical emergency, public "
            "health threats, and epidemic management without consent.\n"
            "Section 7 — Data Fiduciary Obligations: Ayurvedic clinics and telemedicine platforms must "
            "implement reasonable security safeguards for patient data.\n"
            "Impact on AI Systems: AI assistants processing health queries must comply with DPDP Act "
            "requirements for data minimization, storage limitation, and purpose limitation."
        ),
        "citation_id": "dpdp_act_2023",
        "excerpt": "Every Data Fiduciary shall process personal data in a manner that is fair, reasonable, and lawful, and shall ensure consent is free, specific, informed, unconditional and unambiguous.",
    },
    {
        "doc_id": "doc_sushruta_samhita",
        "title": "Sushruta Samhita — Surgical Epistemology and IP Relevance",
        "category": "canonical_epistemology",
        "source_name": "Sushruta Samhita — Sutrasthana & Chikitsasthana",
        "source_type": "Classical Treatise",
        "section": "Sutrasthana & Chikitsasthana",
        "url": "https://tkdl.res.in",
        "keywords_hi": "सुश्रुत संहिता शल्य तंत्र शल्य चिकित्सा प्रमाण ज्ञानमीमांसा नासा संधान",
        "content": (
            "The Sushruta Samhita, attributed to Acharya Sushruta (circa 600 BCE), is the foundational "
            "text of Indian surgical science (Shalya Tantra) and one of the 54 First Schedule authoritative "
            "texts under the Drugs and Cosmetics Act.\n"
            "Key Contributions with IP Significance:\n"
            "1. Rhinoplasty (Nasasandhana): The world's first documented reconstructive surgery — Indian "
            "flap rhinoplasty technique is prior art for modern plastic surgery patents.\n"
            "2. 120+ Surgical Instruments: Classification and design of Yantra (blunt) and Shastra (sharp) "
            "surgical instruments documented in Sutrasthana.\n"
            "3. Dravya-Guna-Karma Framework: Classification of medicines by their substance (Dravya), "
            "qualities (Guna), and therapeutic actions (Karma) — the classical precursor to modern "
            "pharmacological classification.\n"
            "4. Sushruta's Shodhana procedures for mineral drugs are documented prior art for any claimed "
            "novel purification methods."
        ),
        "citation_id": "sushruta_samhita_shalya",
        "excerpt": "Sushruta Samhita documents the earliest known systematic classification of surgical procedures, instruments, and wound management protocols.",
    },
    {
        "doc_id": "doc_ashtanga_hridaya",
        "title": "Ashtanga Hridaya (Vagbhata) — Pharmacological Contributions",
        "category": "canonical_epistemology",
        "source_name": "Ashtanga Hridaya of Vagbhata — Sutrasthana & Chikitsasthana",
        "source_type": "Classical Treatise",
        "section": "Sutrasthana Chapters 1-30",
        "url": "https://tkdl.res.in",
        "keywords_hi": "अष्टांग हृदय वाग्भट औषध विज्ञान रस शास्त्र आयुर्वेद प्रमाण ग्रंथ",
        "content": (
            "The Ashtanga Hridaya, composed by Acharya Vagbhata (circa 7th century CE), synthesizes and "
            "systematizes the teachings of Charaka and Sushruta into a unified Ayurvedic treatise. It is "
            "one of the Brihat Trayi (three great treatises) and a First Schedule authoritative text.\n"
            "IP-Relevant Contributions:\n"
            "1. Comprehensive Dravyaguna (pharmacology) classification covering 500+ single drugs with "
            "Rasa, Guna, Virya, Vipaka, Prabhava — constituting defensive prior art.\n"
            "2. Savirya Kala (drug potency duration) and Anupana (vehicle/adjuvant) concepts relevant to "
            "modern drug delivery and bioavailability enhancement patents.\n"
            "3. Compound formulations documented in Chikitsasthana — prior art under Section 3(p).\n"
            "4. Pathya-Apathya (dietary/lifestyle do's and don'ts) for each disease — prior art for "
            "personalized medicine and nutraceutical claims."
        ),
        "citation_id": "ashtanga_hridaya_vagbhata",
        "excerpt": "Ashtanga Hridaya systematically classifies the pharmacology, therapeutics and treatment protocols of the Charaka and Sushruta traditions into a unified reference.",
    },
    {
        "doc_id": "doc_nighantu_materia_medica",
        "title": "Nighantu Texts — Classical Materia Medica and Drug Identification",
        "category": "canonical_epistemology",
        "source_name": "Bhavaprakash Nighantu, Dhanvantari Nighantu, Raja Nighantu",
        "source_type": "Classical Treatise",
        "section": "Varga Classification System",
        "url": "https://tkdl.res.in",
        "keywords_hi": "निघंटु भावप्रकाश धन्वंतरि राज निघंटु द्रव्य वर्गीकरण औषधि पहचान मटेरिया मेडिका",
        "content": (
            "Nighantu texts are the materia medica lexicons of Ayurveda — systematic catalogues that "
            "classify, describe, and identify medicinal substances (Dravya) used in therapeutics.\n"
            "Major Nighantus with IP Relevance:\n"
            "1. Bhavaprakash Nighantu (16th century): Most widely used, classifies drugs into Vargas "
            "(groups) — Haritakyadi, Guduchyadi, Vatadi, etc. Documents synonyms (Paryaya), properties, "
            "actions, and indications for 470+ drugs.\n"
            "2. Dhanvantari Nighantu (10th century): One of the earliest surviving Nighantus; "
            "classifies drugs by therapeutic action groups.\n"
            "3. Raja Nighantu (17th century): Extensive with detailed descriptions of drug identity markers.\n"
            "IP Significance: Nighantu descriptions provide species-level botanical identification and "
            "therapeutic-use documentation constituting prior art. They are critical for TKDL entries and "
            "prior art searches during patent examination of herbal inventions."
        ),
        "citation_id": "nighantu_materia_medica",
        "excerpt": "Nighantu texts systematically catalogue medicinal substances with their synonyms, morphological identity, therapeutic properties, and classical indications.",
    },
    {
        "doc_id": "doc_shodhana_marana",
        "title": "Shodhana (Purification) and Marana (Calcination) Pharmaceutical Processes",
        "category": "canonical_epistemology",
        "source_name": "Rasa Tarangini & Rasaratna Samuchchaya — Classical Rasa Shastra",
        "source_type": "Classical Treatise",
        "section": "Shodhana & Marana Prakarana",
        "url": "https://tkdl.res.in",
        "keywords_hi": "शोधन मारण भस्म रस शास्त्र शुद्धिकरण कल्सिनेशन रसतरंगिणी रसरत्न समुच्चय",
        "content": (
            "Shodhana (purification) and Marana (calcination/incineration) are classical pharmaceutical "
            "processes in Rasa Shastra (Ayurvedic mineral pharmacology):\n"
            "Shodhana (Purification): Systematic detoxification of minerals and metals through repeated "
            "heating and quenching in specific media (milk, decoctions, juices). Example: Parada Shodhana "
            "(mercury purification) involves 18 sequential operations (Ashtadasha Samskara).\n"
            "Marana (Calcination): High-temperature incineration converting purified metals/minerals into "
            "biocompatible nano-scale particles (Bhasma). Quality tests include Varitaratva (floats on water), "
            "Rekhapurnatva (fills finger lines), and Nishchandratva (no metallic lustre).\n"
            "IP Relevance:\n"
            "1. Classical Shodhana/Marana processes are prior art under Section 3(p).\n"
            "2. Novel modifications (e.g. green synthesis of Bhasma) may qualify for patent protection if "
            "they demonstrate enhanced safety/efficacy beyond classical methods.\n"
            "3. API monographs specify physicochemical standards for Bhasmas."
        ),
        "citation_id": "rasa_shastra_shodhana",
        "excerpt": "Shodhana involves systematic purification of minerals and metals through classical processes to render them safe for internal administration.",
    },
    {
        "doc_id": "doc_classical_dosage_forms",
        "title": "Classical Ayurvedic Dosage Forms — Asava, Arishta, Churna, Bhasma, Taila",
        "category": "formulation_types",
        "source_name": "Sharangadhara Samhita — Madhyama Khanda & Ayurvedic Formulary of India",
        "source_type": "Classical Treatise & Formulary",
        "section": "Madhyama Khanda Chapters 1-12",
        "url": "https://ayush.gov.in",
        "keywords_hi": "शास्त्रीय खुराक रूप आसव अरिष्ट चूर्ण भस्म तैल क्वाथ गुटिका शारंगधर संहिता",
        "content": (
            "Sharangadhara Samhita classifies Ayurvedic dosage forms (Kalpana) into distinct categories, "
            "each with prescribed manufacturing processes:\n"
            "1. Churna (Powders): Dried herbs ground to fine powder. Shelf life: 2 months (classical).\n"
            "2. Kwatha/Kashaya (Decoctions): Boiled aqueous extracts. To be prepared fresh.\n"
            "3. Asava (Cold-infused fermented preparations): Sugar-based fermentation without boiling. "
            "Contains self-generated alcohol (5-12%). Shelf life improves with age.\n"
            "4. Arishta (Decoction-based fermented preparations): Decoction fermented with jaggery/sugar.\n"
            "5. Taila (Medicated oils): Herbs processed in sesame/coconut oil base.\n"
            "6. Ghrita (Medicated ghee): Herbs processed in clarified butter.\n"
            "7. Bhasma (Calcined metals/minerals): Processed through Shodhana and Marana.\n"
            "8. Gutika/Vati (Tablets/pills): Powders bound with liquid media.\n"
            "9. Avaleha/Lehya (Confections): Semi-solid preparations with sugar/honey base.\n"
            "These dosage forms documented in First Schedule texts are prior art under Section 3(p)."
        ),
        "citation_id": "sharangadhara_dosage_forms",
        "excerpt": "Sharangadhara Samhita systematically describes the preparation methods, proportions, and shelf life of classical Ayurvedic dosage forms.",
    },
    {
        "doc_id": "doc_intl_patent_pct",
        "title": "Patent Cooperation Treaty (PCT) — International Patent Filing for Inventions",
        "category": "international_patent",
        "source_name": "Patent Cooperation Treaty (PCT)",
        "source_type": "official_system_overview",
        "section": "Treaty overview & National Phase",
        "url": "https://www.wipo.int/en/web/treaties/registration/pct/index",
        "keywords_hi": "अंतरराष्ट्रीय पेटेंट पीसीटी पेटेंट सहयोग संधि वाइपो वैश्विक दाखिला राष्ट्रीय चरण",
        "content": (
            "The Patent Cooperation Treaty (PCT) makes it possible to seek patent protection for an invention simultaneously "
            "in each of a large number of countries by filing an 'international' patent application. The PCT procedure consists "
            "of an international phase and a national phase. In the international phase, an applicant files a single application "
            "with a receiving Office (or WIPO), receives an International Search Report (ISR) and Written Opinion on patentability "
            "(novelty, inventive step, industrial applicability). In the national phase, patents can only be granted by each of "
            "the national Offices (e.g. USPTO, EPO, JPO) according to their national patent laws. The PCT does not itself grant "
            "a worldwide patent. For Ayurvedic innovations with inventive modifications or standardized formulations, the PCT route "
            "secures a priority date and provides 30 or 31 months from the priority date to enter individual national phases worldwide."
        ),
        "citation_id": "pct-system-overview",
        "excerpt": "The Patent Cooperation Treaty (PCT) makes it possible to seek patent protection for an invention simultaneously in each of a large number of countries by filing an \"international\" patent application.",
        "jurisdiction": "International",
    },
    {
        "doc_id": "doc_intl_trademark_madrid",
        "title": "WIPO Madrid System for the International Registration of Marks (Trademarks & Brands)",
        "category": "international_trademark",
        "source_name": "Madrid System — Frequently Asked Questions",
        "source_type": "official_system_overview",
        "section": "General questions, Question 1",
        "url": "https://www.wipo.int/en/web/madrid-system/faq",
        "keywords_hi": "मैड्रिड सिस्टम अंतरराष्ट्रीय ट्रेडमार्क ब्रांड सुरक्षा वाइपो फॉर्म एमएम2 वैश्विक पंजीकरण",
        "content": (
            "The Madrid System (governed by the Madrid Protocol) is a one-stop solution for registering and managing trademarks "
            "worldwide. You file a single international trademark application (Form MM2) through your national IP office (e.g. "
            "Trade Marks Registry India) and pay one set of fees in one currency (Swiss Francs, CHF) to apply for protection in "
            "multiple countries or regions simultaneously (over 130 countries). It provides brand owners of Ayurvedic products, "
            "herbal formulations, wellness goods (Class 5 for pharmaceuticals/herbal supplements, Class 3 for cosmetics/toiletries, "
            "Class 30 for herbal teas/confections) a streamlined, cost-effective route to protect brand names, trademarks, and "
            "logos internationally. The Madrid System is strictly for trademarks and brand marks; it does not govern patents or industrial designs."
        ),
        "citation_id": "madrid-system-overview",
        "excerpt": "You file a single international trademark application and pay one set of fees, in one currency, to apply for protection in multiple countries or regions simultaneously",
        "jurisdiction": "International",
    },
    {
        "doc_id": "doc_intl_design_hague",
        "title": "WIPO Hague System for the International Registration of Industrial Designs (Packaging & Bottles)",
        "category": "international_industrial_design",
        "source_name": "Hague System — Questions and Answers",
        "source_type": "official_system_overview",
        "section": "Question 1: What is the Hague System?",
        "url": "https://www.wipo.int/en/web/hague-system/faqs",
        "keywords_hi": "हेग व्यवस्था अंतरराष्ट्रीय डिजाइन पैकेजिंग सुरक्षा वाइपो औद्योगिक डिजाइन",
        "content": (
            "The Hague System is a practical business solution to secure and manage up to 100 industrial designs in multiple "
            "countries by filing a single international design application directly with WIPO or through a national office. For "
            "Ayurvedic and herbal enterprises, the Hague System protects the novel and ornamental visual design of product packaging, "
            "unique dispensing containers, bottle shapes, aesthetic jars, and labels across member contracting parties. Protection "
            "covers ornamental or aesthetic aspects rather than technical or therapeutic functions. The Hague System is exclusively "
            "for industrial designs; it does not grant patents or register brand trademarks."
        ),
        "citation_id": "hague-system-overview",
        "excerpt": "The Hague System is a practical business solution to secure and manage up to 100 designs in multiple countries by filing a single international design application",
        "jurisdiction": "International",
    },
    {
        "doc_id": "doc_intl_gratk_treaty",
        "title": "WIPO GRATK Treaty — Mandatory Patent Disclosure for Genetic Resources & Traditional Knowledge",
        "category": "international_treaty_gratk",
        "source_name": "WIPO Treaty on Intellectual Property, Genetic Resources and Associated Traditional Knowledge",
        "source_type": "multilateral_treaty",
        "section": "Article 3.1 & 3.2",
        "url": "https://www.wipo.int/wipolex/en/text/593055",
        "keywords_hi": "वाइपो ग्रैटक संधि पारंपरिक ज्ञान प्रकटीकरण आनुवंशिक संसाधन स्रोत का प्रकटीकरण पेटेंट दायित्व",
        "content": (
            "The WIPO Treaty on Intellectual Property, Genetic Resources and Associated Traditional Knowledge (GRATK Treaty, "
            "adopted May 24, 2024) establishes a groundbreaking international legal standard: Contracting Parties must require patent "
            "applicants to disclose the country of origin or source when a claimed invention in a patent application is based on "
            "genetic resources (Article 3.1) or based on traditional knowledge associated with genetic resources (Article 3.2). "
            "This mandatory disclosure mechanism prevents misappropriation of indigenous and Ayurvedic traditional knowledge, "
            "facilitates patent examination by connecting patent offices with documented prior art, and ensures international "
            "traceability and benefit-sharing compliance across member states."
        ),
        "citation_id": "gratk-art-3-1",
        "excerpt": "Where the claimed invention in a patent application is based on genetic resources, each Contracting Party shall require applicants to disclose:",
        "jurisdiction": "International",
    },
    {
        "doc_id": "doc_intl_trips_agreement",
        "title": "WTO TRIPS Agreement Article 27.3(b) — Plant Patentability & Traditional Knowledge Flexibilities",
        "category": "international_treaty_trips",
        "source_name": "Agreement on Trade-Related Aspects of Intellectual Property Rights (TRIPS)",
        "source_type": "multilateral_treaty",
        "section": "Article 27.3(b)",
        "url": "https://www.wto.org/english/docs_e/legal_e/27-trips_04c_e.htm",
        "keywords_hi": "ट्रिप्स समझौता डब्ल्यूटीओ अनुच्छेद 27.3 पादप पेटेंट-योग्यता जैविक प्रक्रियाएं सुई जेनेरिस",
        "content": (
            "Article 27.3(b) of the WTO TRIPS Agreement permits WTO Member States to exclude from patentability plants and animals "
            "other than micro-organisms, and essentially biological processes for the production of plants or animals. However, "
            "Members must provide for the protection of plant varieties either by patents or by an effective sui generis system "
            "(such as plant breeders' rights) or by any combination thereof. This foundational flexibility allows sovereign nations "
            "to prevent broad biopiracy patents on raw medicinal botanical species while protecting improved varieties."
        ),
        "citation_id": "trips-art-27-3-b",
        "excerpt": "Plants and animals other than micro-organisms, and essentially biological processes for the production of plants or animals other than non-biological and microbiological processes.",
        "jurisdiction": "International",
    },
    {
        "doc_id": "doc_intl_cbd_nagoya_abs",
        "title": "Convention on Biological Diversity (CBD) & Nagoya Protocol — International ABS and PIC",
        "category": "international_treaty_abs",
        "source_name": "Nagoya Protocol on Access and Benefit-sharing",
        "source_type": "multilateral_treaty",
        "section": "Article 5.1 & CBD Article 15",
        "url": "https://www.cbd.int/abs/text/articles?sec=abs-05",
        "keywords_hi": "सीबीडी नागोया प्रोटोकॉल अंतरराष्ट्रीय लाभ साझाकरण पूर्व सूचित सहमति जैव विविधता",
        "content": (
            "The Convention on Biological Diversity (CBD, Article 15) and its Nagoya Protocol on Access to Genetic Resources "
            "and the Fair and Equitable Sharing of Benefits Arising from their Utilization (Article 5.1 & 6.1) establish that "
            "sovereign states have authority over their natural resources. Utilization and commercialization of genetic resources "
            "and associated traditional knowledge must be based on Prior Informed Consent (PIC) from the provider country/community "
            "and on Mutually Agreed Terms (MAT) providing fair and equitable benefit sharing. Any entity exporting or commercializing "
            "biological materials internationally must respect provider country national ABS legislation and international compliance obligations."
        ),
        "citation_id": "nagoya-art-5-1",
        "excerpt": "Benefits arising from the utilization of genetic resources as well as subsequent applications and commercialization shall be shared in a fair and equitable way",
        "jurisdiction": "International",
    },
    {
        "doc_id": "doc_intl_ayurveda_global_ip_export",
        "title": "Global Regulatory & IP Strategy for Ayurvedic Products — US FDA, EU EMA, and Target Markets",
        "category": "international_regulatory_strategy",
        "source_name": "Patent Cooperation Treaty (PCT)",
        "source_type": "official_system_overview",
        "section": "Treaty overview & International Regulations",
        "url": "https://www.wipo.int/en/web/treaties/registration/pct/index",
        "keywords_hi": "अंतरराष्ट्रीय आईपी आयुर्वेद निर्यात वैश्विक बाजार एफडीए डीएसएचईए यूरोपीय संघ टीएचएमपीडी",
        "content": (
            "International commercialization and IP protection of Ayurvedic formulations requires navigating both global IP systems "
            "and target jurisdiction regulatory frameworks:\n"
            "1. Patents & Inventions: Classical formulations cannot be patented as they are in the public domain (prior art documented "
            "in TKDL). Novel, proprietary extracts, synergistic formulations with proven non-obvious efficacy, or innovative delivery "
            "mechanisms can be protected internationally via the WIPO PCT route (entering national phase in US USPTO, European EPO, Japan JPO, etc.).\n"
            "2. Trademarks & Brands: Brand names, logos, and proprietary product identifiers should be registered internationally "
            "via the WIPO Madrid System (Classes 5 and 3) to prevent brand hijacking.\n"
            "3. Packaging Aesthetics: Bottle shapes and novel packaging can be protected via the WIPO Hague System.\n"
            "4. Target Market Regulatory Approvals:\n"
            "- United States (US FDA): Ayurvedic products are predominantly marketed as Dietary Supplements under DSHEA 1994 (21 CFR Part 111 cGMP "
            "compliance, structure/function claims, no disease treatment claims). Therapeutic claims require filing an Investigational New Drug (IND) under FDA Botanical Drug Guidance.\n"
            "- European Union (EU EMA): Regulated under the Traditional Herbal Medicinal Products Directive (Directive 2004/24/EC - THMPD) "
            "requiring evidence of 30 years traditional use (including 15 years within the EU), or as food/dietary supplements under national food regulations.\n"
            "- United Kingdom (MHRA): Traditional Herbal Registration (THR) scheme.\n"
            "- Australia (TGA): Listed Complementary Medicines on the Australian Register of Therapeutic Goods (ARTG)."
        ),
        "citation_id": "pct-system-overview",
        "excerpt": "The Patent Cooperation Treaty (PCT) makes it possible to seek patent protection for an invention simultaneously in each of a large number of countries by filing an \"international\" patent application.",
        "jurisdiction": "International",
    },
    {
        "doc_id": "doc_intl_overview_ip_systems",
        "title": "Comprehensive Guide to International Intellectual Property (IP) for Herbal & Ayurvedic Innovation",
        "category": "international_ip_guide",
        "source_name": "Madrid System — Frequently Asked Questions",
        "source_type": "official_system_overview",
        "section": "General questions, Question 1",
        "url": "https://www.wipo.int/en/web/madrid-system/faq",
        "keywords_hi": "अंतरराष्ट्रीय बौद्धिक संपदा क्या है कैसे काम करती है पेटेंट ट्रेडमार्क डिजाइन वैश्विक संधियां",
        "content": (
            "International Intellectual Property (IP) operates on the fundamental principle of territoriality: intellectual "
            "property rights are granted, governed, and enforced by the domestic laws of each individual sovereign nation or regional office. "
            "There is no single 'world patent' or automatic global trademark. Instead, multilateral treaties administered by WIPO "
            "(World Intellectual Property Organization) provide unified, cost-effective international filing and priority systems:\n"
            "1. Patent Cooperation Treaty (PCT): For patents. Single application providing an international filing date and 30/31-month "
            "window to enter national phases across 150+ countries.\n"
            "2. Madrid System (Madrid Protocol): For trademarks and brand names. Single application (Form MM2) designating over 130 countries.\n"
            "3. Hague System: For industrial designs and aesthetic product packaging across 90+ contracting parties.\n"
            "4. WIPO GRATK Treaty (2024): Mandates patent disclosure of origin for genetic resources and traditional knowledge.\n"
            "5. WTO TRIPS Agreement: Establishes global baseline minimum IP standards across WTO member nations.\n"
            "6. CBD & Nagoya Protocol: Governs sovereign biodiversity rights, Prior Informed Consent (PIC), and international Access and Benefit Sharing (ABS)."
        ),
        "citation_id": "madrid-system-overview",
        "excerpt": "You file a single international trademark application and pay one set of fees, in one currency, to apply for protection in multiple countries or regions simultaneously",
        "jurisdiction": "International",
    },
]
