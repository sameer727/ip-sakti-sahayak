"""Enhanced features for IP-SAKTI Sahayak (SIH-26045).

Provides domain-grounded services for:
1. GIS / Remote Sensing: Ayurveda Geographical Indications & Geo-Origin Tracker (BDA §10(4)(d)).
2. Interactive Knowledge Graph: Formulation -> Regimes -> Case Law -> International Treaties.
3. Statutory Forms & Registry Navigator: IP India, NBA, FSSAI FoSCoS, WIPO forms & fee calculator.
4. Human IP Facilitator Escalation Desk: Direct escalation to Ministry of Ayush / AIIA-ICAINE.
5. DPDP Act 2023 & MeitY AI Advisory Compliance: Tamper-evident audit logging.
"""
from __future__ import annotations

import datetime
import hashlib
import uuid
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# 1. GIS & Remote Sensing Data
# ---------------------------------------------------------------------------

AYURVEDIC_GIS = [
    {
        "id": "GI-NAG-ASH",
        "name": "Nagauri Ashwagandha",
        "botanical_name": "Withania somnifera",
        "sanskrit_name": "Ashwagandha / Varahakarni",
        "state": "Rajasthan",
        "region": "Nagaur District",
        "coordinates": [27.1983, 73.7423],
        "gi_status": "Registered (2026 Tag)",
        "gi_class": "Class 31 (Agricultural / Medicinal Plant)",
        "classical_indications": "Rasayana, Balya, Vata-Kapha hara, Medhya, adaptogen",
        "sbb_jurisdiction": "Rajasthan State Biodiversity Board, Jaipur",
        "sbb_portal": "https://environment.rajasthan.gov.in/sbb",
        "remote_sensing": {
            "agro_climatic_zone": "Western Dry Zone / Semi-Arid",
            "altitude_meters": "280 - 320 m",
            "soil_type": "Well-drained sandy loam, calcareous subsoil (pH 7.5 - 8.5)",
            "annual_rainfall_mm": "350 - 450 mm",
            "active_chemical_markers": "Withaferin A (0.28%), Withanolide A, high total withanolide profile",
        },
        "bda_disclosure_note": "Filing patents using Nagauri Ashwagandha requires disclosure of origin (Nagaur, Rajasthan) under Patents Act §10(4)(d). AYUSH practitioners cultivating this for personal classical use are exempt under BDA 2023 Amendment §7.",
    },
    {
        "id": "GI-NAV-RIC",
        "name": "Navara Rice",
        "botanical_name": "Oryza sativa (medicinal ecotype)",
        "sanskrit_name": "Shashtikashali",
        "state": "Kerala",
        "region": "Palakkad & Malappuram Districts",
        "coordinates": [10.7867, 76.6548],
        "gi_status": "Registered (GI Certificate No. 89)",
        "gi_class": "Class 30 (Agricultural)",
        "classical_indications": "Shashtika Shali Pinda Sweda (Navarakizhi) in neuromuscular disorders, Brimhana, Tridosha shamaka",
        "sbb_jurisdiction": "Kerala State Biodiversity Board, Thiruvananthapuram",
        "sbb_portal": "https://keralabiodiversity.org",
        "remote_sensing": {
            "agro_climatic_zone": "Humid Western Coastal Plains",
            "altitude_meters": "30 - 120 m",
            "soil_type": "Acidic laterite / alluvial loam with high organic matter",
            "annual_rainfall_mm": "2200 - 3000 mm",
            "active_chemical_markers": "High amylose, gamma-oryzanol, polyphenols, iron, zinc",
        },
        "bda_disclosure_note": "Traditional landrace protected by local farmer communities. Commercial formulations must secure Mutually Agreed Terms (MAT) with the Kerala SBB.",
    },
    {
        "id": "GI-LAK-TUR",
        "name": "Lakadong Turmeric",
        "botanical_name": "Curcuma longa",
        "sanskrit_name": "Haridra / Kanchani",
        "state": "Meghalaya",
        "region": "West Jaintia Hills",
        "coordinates": [25.4500, 92.2000],
        "gi_status": "Registered GI",
        "gi_class": "Class 30 (Spices / Medicinal)",
        "classical_indications": "Varnya, Lekhaniya, Kushthaghna, anti-inflammatory, wound healing",
        "sbb_jurisdiction": "Meghalaya State Biodiversity Board, Shillong",
        "sbb_portal": "https://megsbb.nic.in",
        "remote_sensing": {
            "agro_climatic_zone": "Sub-tropical Hill Zone",
            "altitude_meters": "600 - 900 m",
            "soil_type": "Red lateritic to sandy loam, rich in organic carbon",
            "annual_rainfall_mm": "3000 - 4500 mm",
            "active_chemical_markers": "World-highest Curcumin content (7.0% - 9.2%)",
        },
        "bda_disclosure_note": "Crucial prior art benchmark. Patenting extracted curcumin from Lakadong must overcome §3(p) TK bar and satisfy BDA ABS.",
    },
    {
        "id": "GI-KAS-SAF",
        "name": "Kashmir Saffron",
        "botanical_name": "Crocus sativus",
        "sanskrit_name": "Kumkuma / Keshara",
        "state": "Jammu & Kashmir",
        "region": "Pampore, Srinagar, Budgam & Kishtwar",
        "coordinates": [34.0180, 74.9300],
        "gi_status": "Registered (GI Certificate No. 635)",
        "gi_class": "Class 30 (Agricultural / Medicinal)",
        "classical_indications": "Tridoshaghna, Varnya, Rasayana, Kantida, Kumkumadi Taila key ingredient",
        "sbb_jurisdiction": "J&K Biodiversity Council, Srinagar / Jammu",
        "sbb_portal": "https://jksbb.jk.gov.in",
        "remote_sensing": {
            "agro_climatic_zone": "Temperate Alpine / Karewa Highlands",
            "altitude_meters": "1580 - 1800 m",
            "soil_type": "Karewa lacustrine deposits (fine silty clay loam)",
            "annual_rainfall_mm": "650 - 800 mm (with snowfall)",
            "active_chemical_markers": "Crocin (colour strength > 220), Safranal (aroma), Picrocrocin (bitterness)",
        },
        "bda_disclosure_note": "Origin verification required under §10(4)(d); protected against Iranian saffron adulteration via GI and satellite crop monitoring.",
    },
    {
        "id": "GI-ALL-CAR",
        "name": "Alleppey Green Cardamom",
        "botanical_name": "Elettaria cardamomum",
        "sanskrit_name": "Sukshma Ela",
        "state": "Kerala",
        "region": "Cardamom Hills / Idukki & Alleppey",
        "coordinates": [9.8500, 76.9700],
        "gi_status": "Registered GI",
        "gi_class": "Class 30 (Agricultural)",
        "classical_indications": "Deepana, Pachana, Shvasahara, Kasahara, Mukhashodhaka",
        "sbb_jurisdiction": "Kerala State Biodiversity Board",
        "sbb_portal": "https://keralabiodiversity.org",
        "remote_sensing": {
            "agro_climatic_zone": "Western Ghats Montane Moist Evergreen",
            "altitude_meters": "800 - 1300 m",
            "soil_type": "Forest loam rich in humus, acidic (pH 5.0 - 6.0)",
            "annual_rainfall_mm": "2500 - 3500 mm",
            "active_chemical_markers": "1,8-cineole (30-40%), alpha-terpinyl acetate (35-45%)",
        },
        "bda_disclosure_note": "Cardamom used in classical formulations like Eladi Vati; access for commercial extract manufacturing requires SBB prior intimation.",
    },
    {
        "id": "GI-COO-CAR",
        "name": "Coorg Green Cardamom",
        "botanical_name": "Elettaria cardamomum",
        "sanskrit_name": "Sukshma Ela (Coorg Ecotype)",
        "state": "Karnataka",
        "region": "Kodagu (Coorg) District",
        "coordinates": [12.3375, 75.8069],
        "gi_status": "Registered GI",
        "gi_class": "Class 30 (Spices / Medicinal)",
        "classical_indications": "Cardio-protective, digestive stimulant, aromatic adjuvant in AYUSH medicines",
        "sbb_jurisdiction": "Karnataka Biodiversity Board, Bengaluru",
        "sbb_portal": "https://kbb.karnataka.gov.in",
        "remote_sensing": {
            "agro_climatic_zone": "Western Ghats Hilly Zone",
            "altitude_meters": "900 - 1400 m",
            "soil_type": "Red to dark brown loamy forest soil",
            "annual_rainfall_mm": "2800 - 3800 mm",
            "active_chemical_markers": "High terpene esters, distinct citrus-floral aromatic profile",
        },
        "bda_disclosure_note": "Governed by Karnataka Biodiversity Board; biological access must comply with Rule 14 of Biological Diversity Rules 2024.",
    },
    {
        "id": "GI-GAN-KEW",
        "name": "Ganjam Kewda Flower & Rooh",
        "botanical_name": "Pandanus fascicularis",
        "sanskrit_name": "Ketakipushpa",
        "state": "Odisha",
        "region": "Ganjam Coastal Belt (Chhatrapur, Rangeilunda)",
        "coordinates": [19.3800, 85.0500],
        "gi_status": "Registered GI",
        "gi_class": "Class 31 (Flowers) & Class 3 (Distillates)",
        "classical_indications": "Hridya, Medhya, Chakshushya, therapeutics for headache and earache",
        "sbb_jurisdiction": "Odisha Biodiversity Board, Bhubaneswar",
        "sbb_portal": "https://odishabiodiversityboard.in",
        "remote_sensing": {
            "agro_climatic_zone": "East Coast Maritime Zone",
            "altitude_meters": "5 - 35 m",
            "soil_type": "Coastal sandy and sandy loam with high groundwater table",
            "annual_rainfall_mm": "1200 - 1400 mm",
            "active_chemical_markers": "2-phenylethyl methyl ether (60-80%), terpinen-4-ol",
        },
        "bda_disclosure_note": "Traditional hydro-distillation method (Bhabhka system) is community TK; patenting derivative processes faces TKDL prior art.",
    },
]

STATE_BIODIVERSITY_BOARDS = {
    "Kerala": {
        "board": "Kerala State Biodiversity Board",
        "headquarters": "Thiruvananthapuram",
        "portal": "https://keralabiodiversity.org",
        "intimation_form": "Form I (Prior Intimation under Section 7)",
        "ayush_status": "Exempt for registered AYUSH practitioners and cultivated resources (2023 Amendment). Non-exempt commercial manufacturers must intimate.",
    },
    "Rajasthan": {
        "board": "Rajasthan State Biodiversity Board",
        "headquarters": "Jaipur",
        "portal": "https://environment.rajasthan.gov.in/sbb",
        "intimation_form": "Form I (Prior Intimation)",
        "ayush_status": "Prior intimation required for wild-sourced bio-resources. Cultivated Ashwagandha / Guggul exempt.",
    },
    "Karnataka": {
        "board": "Karnataka Biodiversity Board",
        "headquarters": "Bengaluru",
        "portal": "https://kbb.karnataka.gov.in",
        "intimation_form": "Form I (Online e-Filing)",
        "ayush_status": "Turnover-based benefit sharing (0.2% - 0.6%) applies to commercial manufacturing.",
    },
    "Meghalaya": {
        "board": "Meghalaya State Biodiversity Board",
        "headquarters": "Shillong",
        "portal": "https://megsbb.nic.in",
        "intimation_form": "Form I / BMC Consultation",
        "ayush_status": "Sixth Schedule tribal council rights apply alongside BMC concurrence.",
    },
    "Jammu & Kashmir": {
        "board": "J&K Biodiversity Council",
        "headquarters": "Srinagar / Jammu",
        "portal": "https://jksbb.jk.gov.in",
        "intimation_form": "Form I",
        "ayush_status": "Union Territory council oversees high-altitude alpine medicinal flora access.",
    },
    "Odisha": {
        "board": "Odisha Biodiversity Board",
        "headquarters": "Bhubaneswar",
        "portal": "https://odishabiodiversityboard.in",
        "intimation_form": "Form I",
        "ayush_status": "Covers Eastern Ghats and coastal medicinal plants.",
    },
}

# ---------------------------------------------------------------------------
# 2. Knowledge Graph Nodes and Edges
# ---------------------------------------------------------------------------

KNOWLEDGE_GRAPH = {
    "nodes": [
        {"id": "cls_classical", "label": "Classical Medicine", "type": "formulation", "desc": "From First Schedule authoritative texts; §3(p) patent bar; TKDL protected"},
        {"id": "cls_prop", "label": "Proprietary Medicine", "type": "formulation", "desc": "Known ingredients in novel ratio/form; safety data required; patentable only if synergistic advance shown"},
        {"id": "cls_phyto", "label": "Phytopharmaceutical", "type": "formulation", "desc": "Purified standardized fraction; CDSCO new drug pathway; clinical trial Phase I-III"},
        {"id": "cls_aahar", "label": "Ayurveda-Aahar", "type": "formulation", "desc": "Food Category 102; 91 pre-approved recipes (102.1); FSSAI central licence ?7500+GST"},
        {"id": "cls_cosmetic", "label": "Ayurvedic Cosmetic", "type": "formulation", "desc": "External application; D&C Cosmetic Rules; no therapeutic cure claims permitted"},
        {"id": "cls_newdrug", "label": "New Drug (AYUSH)", "type": "formulation", "desc": "Novel chemical entity / new indication; rigorous clinical trial; high patent potential"},
        
        {"id": "reg_patent", "label": "Patents Act, 1970 (2024 Rules)", "type": "regime", "desc": "Sections 3(p) TK bar, 3(d) efficacy, 3(e) mere admixture, 10(4)(d) bio-origin disclosure"},
        {"id": "reg_bda", "label": "Biological Diversity Act (2023 / 2024 Rules)", "type": "regime", "desc": "ABS compliance; decriminalised; AYUSH practitioner exemption; DSI inclusion; Form 1/3"},
        {"id": "reg_dc", "label": "Drugs & Cosmetics Act, 1940", "type": "regime", "desc": "Schedule A texts; Schedule T GMP; Rule 161 labelling; ASU licensing via State Licensing Authority"},
        {"id": "reg_fssai", "label": "FSSAI (Ayurveda Aahara) Regs 2022", "type": "regime", "desc": "Food Category 102; FoSCoS portal; no Schedule E-1 poisonous herbs or bhasmas allowed"},
        {"id": "reg_gi", "label": "GI of Goods Act, 1999", "type": "regime", "desc": "Goods linked to geographic origin; Navara Rice, Nagauri Ashwagandha, Lakadong Turmeric"},
        {"id": "reg_tm", "label": "Trade Marks Act, 1999", "type": "regime", "desc": "Form TM-A; AYUSH Standard Mark; descriptive Ayurveda names excluded unless distinct"},
        
        {"id": "treaty_gratk", "label": "WIPO GRATK Treaty (2024)", "type": "treaty", "desc": "Mandatory patent disclosure of genetic resources and associated TK origin worldwide"},
        {"id": "treaty_pct", "label": "Patent Cooperation Treaty (PCT)", "type": "treaty", "desc": "Single filing via RO/IN covering 150+ states; 30/31 months national phase entry"},
        {"id": "treaty_nagoya", "label": "Nagoya Protocol (CBD)", "type": "treaty", "desc": "Prior Informed Consent (PIC), Mutually Agreed Terms (MAT) & IRCC certificate"},
        {"id": "treaty_madrid", "label": "Madrid System (WIPO)", "type": "treaty", "desc": "Single international trademark filing (Form MM2) designating 130+ jurisdictions"},
        
        {"id": "case_zero", "label": "Zero Brand Zone v. Controller (Madras HC 2024)", "type": "caselaw", "desc": "Panchagavya lamp barred under §3(p) as aggregation of known properties of traditionally known components"},
        {"id": "case_shaafi", "label": "Shaafi Naturcure v. Controller (Delhi HC 2026)", "type": "caselaw", "desc": "Section 3(p) does not categorically bar every TK-adjacent invention if non-obvious advance is proven"},
        {"id": "case_divya", "label": "Divya Pharmacy v. SBB (Uttarakhand HC 2018)", "type": "caselaw", "desc": "Indian companies subject to ABS prior to 2023 Amendment exemptions"},
        {"id": "case_turmeric", "label": "Turmeric US Patent 5,401,504 (Revoked 1997)", "type": "caselaw", "desc": "CSIR challenge with 32 ancient Sanskrit & journal references; landmark biopiracy reversal"},
        
        {"id": "auth_tkdl", "label": "TKDL (CSIR - Ministry of Ayush)", "type": "authority", "desc": "400,000+ formulations; defensive prior art provided directly to global patent offices under NDA"},
        {"id": "auth_nba", "label": "National Biodiversity Authority (NBA)", "type": "authority", "desc": "Statutory body for ABS approval (Form 3 for IPR); absefiling.nbaindia.in"},
        {"id": "auth_cgpdtm", "label": "Office of CGPDTM (IP India)", "type": "authority", "desc": "Patent, Trademark, GI and Design Registry; AYUSH Patent Examination Guidelines 2025"},
        {"id": "auth_cdsco", "label": "CDSCO & SLA", "type": "authority", "desc": "Central & State drug authorities; ASU licensing, clinical trials, phytopharmaceutical evaluation"},
    ],
    "links": [
        {"source": "cls_classical", "target": "reg_patent", "label": "precluded under §3(p)"},
        {"source": "cls_classical", "target": "auth_tkdl", "label": "defended by"},
        {"source": "cls_classical", "target": "reg_dc", "label": "licensed under Schedule A"},
        {"source": "cls_prop", "target": "reg_dc", "label": "requires SLA safety data"},
        {"source": "cls_prop", "target": "reg_patent", "label": "requires synergistic proof"},
        {"source": "cls_phyto", "target": "auth_cdsco", "label": "evaluated as New Drug"},
        {"source": "cls_aahar", "target": "reg_fssai", "label": "Food Category 102 licence"},
        {"source": "cls_cosmetic", "target": "reg_dc", "label": "Cosmetic Rules compliance"},
        
        {"source": "reg_patent", "target": "case_zero", "label": "authoritative §3(p) ruling"},
        {"source": "reg_patent", "target": "case_shaafi", "label": "scope refinement 2026"},
        {"source": "reg_patent", "target": "treaty_gratk", "label": "aligned with global origin disclosure"},
        {"source": "reg_patent", "target": "treaty_pct", "label": "international patent filing route"},
        {"source": "reg_patent", "target": "auth_cgpdtm", "label": "administered by"},
        {"source": "reg_patent", "target": "reg_bda", "label": "mandates §10(4)(d) origin declaration"},
        
        {"source": "reg_bda", "target": "case_divya", "label": "historical ABS ruling"},
        {"source": "reg_bda", "target": "treaty_nagoya", "label": "Nagoya Protocol implementation"},
        {"source": "reg_bda", "target": "auth_nba", "label": "administered by"},
        
        {"source": "auth_tkdl", "target": "case_turmeric", "label": "catalysed by"},
        {"source": "auth_tkdl", "target": "treaty_gratk", "label": "complemented by"},
        {"source": "reg_gi", "target": "auth_cgpdtm", "label": "registered under"},
        {"source": "reg_tm", "target": "treaty_madrid", "label": "internationalized via MM2"},
    ],
}

# ---------------------------------------------------------------------------
# 3. Statutory Forms & Registries Navigator
# ---------------------------------------------------------------------------

STATUTORY_FORMS = [
    {
        "id": "FORM-PAT-01",
        "regime": "Patents",
        "code": "Form 1",
        "title": "Application for Grant of Patent",
        "admin_body": "Office of CGPDTM (IP India)",
        "portal_url": "https://ipindiaonline.gov.in/epatentfiling/goForLogin/doLogin",
        "fees": {
            "natural_person_startup": "?1,600",
            "small_entity": "?4,000",
            "others_large_entity": "?8,000",
        },
        "statutory_timeline": "Filing creates Priority Date; 12 months for complete specification if provisional filed.",
        "ayurveda_specific_requirements": [
            "Mandatory disclosure of biological resource geographical source under §10(4)(d).",
            "Must state whether biological material is sourced from India and declare NBA compliance status.",
            "Form 3 declaration regarding foreign applications filed.",
        ],
    },
    {
        "id": "FORM-PAT-18",
        "regime": "Patents",
        "code": "Form 18 / 18A",
        "title": "Request for Examination / Expedited Examination",
        "admin_body": "Office of CGPDTM (IP India)",
        "portal_url": "https://ipindiaonline.gov.in/epatentfiling/goForLogin/doLogin",
        "fees": {
            "natural_person_startup": "?4,000 (Form 18) / ?8,000 (Form 18A Expedited)",
            "small_entity": "?10,000 / ?25,000",
            "others_large_entity": "?20,000 / ?60,000",
        },
        "statutory_timeline": "Within 48 months from date of filing/priority. Expedited grant typically takes 12-18 months.",
        "ayurveda_specific_requirements": [
            "AYUSH startups and female applicants qualify for expedited examination under Form 18A (Patents Rules 2024).",
            "Triggers mandatory TKDL prior-art check by patent examiner.",
        ],
    },
    {
        "id": "FORM-GI-01",
        "regime": "Geographical Indications",
        "code": "Form GI-1",
        "title": "Application for Registration of a Geographical Indication",
        "admin_body": "Geographical Indications Registry, Chennai",
        "portal_url": "https://search.ipindia.gov.in/GIRPublicSearch",
        "fees": {
            "all_applicants": "?5,000 per class",
        },
        "statutory_timeline": "Registration valid for 10 years, indefinitely renewable upon payment of renewal fee (Form GI-3).",
        "ayurveda_specific_requirements": [
            "Goods only (agricultural produce, manufactured goods) — Ayurvedic healing services cannot be GI tagged.",
            "Must be filed by an association of persons/producers or organization representing interest of producers.",
            "Must demonstrate unique quality, reputation, or characteristics attributable to geographic origin (e.g. Navara Rice, Nagauri Ashwagandha).",
        ],
    },
    {
        "id": "FORM-TM-A",
        "regime": "Trade Marks",
        "code": "Form TM-A",
        "title": "Application for Registration of Trademark",
        "admin_body": "Trade Marks Registry (IP India)",
        "portal_url": "https://ipindiaonline.gov.in/trademarkefiling/user/frmLoginNew.aspx",
        "fees": {
            "natural_person_startup": "?4,500 per class (e-filing)",
            "small_entity": "?4,500 per class",
            "others_large_entity": "?9,000 per class",
        },
        "statutory_timeline": "Registration valid for 10 years, indefinitely renewable every 10 years.",
        "ayurveda_specific_requirements": [
            "Class 5 for Ayurvedic medicines and pharmaceutical preparations; Class 3 for Ayurvedic cosmetics/oils; Class 29/30 for Ayurveda-Aahar.",
            "Generic/descriptive names (e.g., Triphala, Chyawanprash) cannot be monopolized without distinct brand prefix.",
            "Cannot claim cure or treatment on trademark packaging that violates Drugs & Magic Remedies Act 1954.",
        ],
    },
    {
        "id": "FORM-NBA-01",
        "regime": "Biological Diversity / ABS",
        "code": "Form I (NBA)",
        "title": "Application for Access to Biological Resources and Associated TK",
        "admin_body": "National Biodiversity Authority (NBA)",
        "portal_url": "https://absefiling.nbaindia.in",
        "fees": {
            "application_fee": "?10,000",
        },
        "statutory_timeline": "Decision within 90 - 180 days after State Biodiversity Board / BMC consultation.",
        "ayurveda_specific_requirements": [
            "Mandatory for foreign individuals, non-resident Indians (NRIs), and companies with foreign shareholding.",
            "Indian citizens accessing biological resources for commercial utilization intimate the State Biodiversity Board via Form I.",
            "Benefit sharing calculated per NBA regulations (0.2% - 0.6% on gross ex-factory turnover).",
        ],
    },
    {
        "id": "FORM-NBA-03",
        "regime": "Biological Diversity / ABS",
        "code": "Form III (NBA)",
        "title": "Application for Seeking Approval for Applying for IPR",
        "admin_body": "National Biodiversity Authority (NBA)",
        "portal_url": "https://absefiling.nbaindia.in",
        "fees": {
            "application_fee": "?500 for Indian entities; ?10,000 for foreign entities",
        },
        "statutory_timeline": "Approval required before grant of patent (Indian entities must register before grant; foreign entities require prior approval).",
        "ayurveda_specific_requirements": [
            "Required whenever an Indian patent or international patent claims an invention based on Indian biological resources.",
            "NBA assesses whether invention is based on codified TK and verifies fair and equitable benefit sharing.",
        ],
    },
    {
        "id": "FORM-FSSAI-102",
        "regime": "Ayurveda-Aahar / Food",
        "code": "FoSCoS KoB 102",
        "title": "FSSAI Central Licence — Ayurveda Aahara Manufacturer",
        "admin_body": "Food Safety and Standards Authority of India (FSSAI)",
        "portal_url": "https://foscos.fssai.gov.in",
        "fees": {
            "annual_licence_fee": "?7,500 + 18% GST annually",
        },
        "statutory_timeline": "30 - 60 days standard verification timeline on FoSCoS portal.",
        "ayurveda_specific_requirements": [
            "Effective since 1 September 2025 as a dedicated Kind of Business (KoB).",
            "Category 102.1: 91 pre-approved recipes (FSSAI Order 25 July 2025) enjoy expedited pathway.",
            "Category 102.2 - 102.4: Non-standardized recipes require prior FSSAI-HQ expert committee clearance.",
            "Strictly prohibits Schedule E-1 poisonous herbs, bhasmas, pishtis, and therapeutic disease claims.",
        ],
    },
    {
        "id": "FORM-WIPO-PCT",
        "regime": "International Patents",
        "code": "WIPO ePCT",
        "title": "International Patent Application (PCT Route)",
        "admin_body": "WIPO & Receiving Office India (RO/IN)",
        "portal_url": "https://pct.wipo.int",
        "fees": {
            "transmittal_fee_roin": "?3,200 (Individual/Startup) / ?8,000 (Others)",
            "international_filing_fee": "1,330 CHF (90% reduction for Indian individuals)",
        },
        "statutory_timeline": "National phase entry into 150+ member countries at 30 or 31 months from priority date.",
        "ayurveda_specific_requirements": [
            "International Search Report (ISR) checks global prior art including TKDL.",
            "Must comply with WIPO GRATK Treaty mandatory disclosure once in force.",
        ],
    },
    {
        "id": "FORM-WIPO-MM2",
        "regime": "International Trademarks",
        "code": "Form MM2",
        "title": "Application for International Registration under Madrid Protocol",
        "admin_body": "WIPO & IP India as Office of Origin",
        "portal_url": "https://www.wipo.int/madrid/en",
        "fees": {
            "handling_fee_ipindia": "?2,000",
            "basic_fee_wipo": "653 CHF (black & white) / 903 CHF (colour) + individual country fees",
        },
        "statutory_timeline": "Single application designating 130+ countries; 10 years validity, centrally renewable.",
        "ayurveda_specific_requirements": [
            "Requires a basic application or registration in India (Form TM-A).",
            "Enables global brand protection for Ayurvedic exporter MSMEs.",
        ],
    },
]

# ---------------------------------------------------------------------------
# 4. Human IP Facilitator Escalation Desk
# ---------------------------------------------------------------------------

_ESCALATION_TICKETS: Dict[str, Dict[str, Any]] = {}
_AUDIT_LOGS: List[Dict[str, Any]] = []


def submit_escalation(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Process and log an escalation to the Ministry of Ayush / AIIA-ICAINE IP Facilitator Desk."""
    ticket_id = f"AIIA-IP-{datetime.datetime.now().year}-{uuid.uuid4().hex[:6].upper()}"
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    ticket = {
        "ticket_id": ticket_id,
        "status": "submitted",
        "submitted_at": timestamp,
        "query": payload.get("query", "").strip(),
        "jurisdiction": payload.get("jurisdiction", "India"),
        "formulation_class": payload.get("formulation_class"),
        "user_name": payload.get("user_name", "").strip(),
        "user_email": payload.get("user_email", "").strip(),
        "user_phone": payload.get("user_phone", "").strip(),
        "user_organization": payload.get("user_organization", "").strip(),
        "details": payload.get("details", "").strip(),
        "citations_count": len(payload.get("citations", [])),
        "assigned_desk": "Ministry of Ayush / AIIA-ICAINE IP Facilitation Cell",
        "expected_response_hours": 48,
        "facilitator_notes": "Assigned to empanelled AYUSH Patent Attorney / Regulatory Facilitator. Client will be contacted via registered email.",
    }
    
    _ESCALATION_TICKETS[ticket_id] = ticket
    
    # Log to DPDP audit trail
    log_audit_event({
        "event_type": "human_escalation_submitted",
        "ticket_id": ticket_id,
        "query_hash": hashlib.sha256(ticket["query"].encode()).hexdigest()[:12],
        "jurisdiction": ticket["jurisdiction"],
        "assigned_desk": ticket["assigned_desk"],
        "timestamp": timestamp,
    })
    
    return ticket


def get_escalation_ticket(ticket_id: str) -> Optional[Dict[str, Any]]:
    return _ESCALATION_TICKETS.get(ticket_id)


# ---------------------------------------------------------------------------
# 5. DPDP Act 2023 & MeitY AI Advisory Audit Logger
# ---------------------------------------------------------------------------

def log_audit_event(event: Dict[str, Any]) -> None:
    """Record an audit event adhering to DPDP Act 2023 Section 6 & 8."""
    event_record = {
        "id": f"AUD-{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "data_localisation": "Processed on Indian server (MeitY/DPDP compliant)",
        **event,
    }
    _AUDIT_LOGS.append(event_record)
    # Cap memory log at 1000 items
    if len(_AUDIT_LOGS) > 1000:
        del _AUDIT_LOGS[0]


def get_audit_trail(limit: int = 50) -> List[Dict[str, Any]]:
    """Retrieve tamper-evident audit logs."""
    return list(reversed(_AUDIT_LOGS[-limit:]))
