# IP-SAKTI Sahayak (Intellectual Property & Traditional Knowledge AI Assistant)

**IP-SAKTI Sahayak** is a multi-agent, regulatory-grounded Artificial Intelligence decision support platform designed to assist inventors, MSMEs, researchers, and patent professionals in navigating Indian and International Intellectual Property regimes, Ayurvedic & formulation classification, Access & Benefit Sharing (ABS), and Traditional Knowledge Digital Library (TKDL) compliance.

---

## 🏛 Architecture Overview

The platform uses a modular, multi-domain architecture located under `src/ipsakti/`:

- **`src/ipsakti/core/` (Core Orchestrator & API)**:
  Central FastAPI gateway, query intent classifier, jurisdiction routing, TF-IDF corpus indexing, and answer generation orchestrator.
- **`src/ipsakti/classifier/` (Formulation Classification Engine)**:
  Rule-based multi-step decision engine determining regulatory classification across AYUSH, Classical ASU, Patentable herbal products, and FSSAI nutraceutical regimes.
- **`src/ipsakti/india_ip/` (India IP & Regulatory Specialist)**:
  Statutory guidance for Patents Act 1970 (including Section 3(p), 3(d), 3(e)), Biological Diversity Act 2002, Form 1–3 requirements, and IP India workflows.
- **`src/ipsakti/abs_tk/` (ABS & Traditional Knowledge Specialist)**:
  Guidance on National Biodiversity Authority (NBA) approvals, State Biodiversity Boards (SBB), Prior Informed Consent (PIC), Mutually Agreed Terms (MAT), and TKDL prior art defense.
- **`src/ipsakti/international_ip/` (International IP Specialist)**:
  Guidance on PCT national phase timelines (30/31 months), Paris Convention priority, WIPO Hague, Madrid system, and Nagoya Protocol compliance.
- **`src/ipsakti/integration/` (Multi-Agent Assembler & Semantic Engine)**:
  Synthesis layer coordinating specialist adapters, unified multi-domain response formatting, citation validation, scikit-learn TF-IDF semantic embeddings, and LLM orchestration with offline deterministic fallbacks.

---

## 🚀 Quick Start

### 1. Prerequisites & Installation

Python 3.10+ is recommended.

```bash
git clone https://github.com/your-org/IP-SAKTI-Sahayak.git
cd IP-SAKTI-Sahayak

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

### 2. Running the System

Start the integrated web API server:
```bash
python -m uvicorn ipsakti.integration.app:app --host 127.0.0.1 --port 8000 --reload
```
The interactive API documentation is available at `http://127.0.0.1:8000/docs`.  
The web frontend is available at `http://127.0.0.1:8000/`.

Optional: Start the built-in free offline LLM server:
```bash
python scripts/free_api_server.py
```

---

## 🧪 Testing & Verification

Run the entire unified test suite (all 815 tests across all domains):
```bash
python -m pytest tests
```

Run domain-specific test suites:
```bash
python -m pytest tests/core             # Core routing, models & API (131 tests)
python -m pytest tests/classifier       # Formulation classifier (93 tests)
python -m pytest tests/india_ip         # India IP & regulatory (118 tests)
python -m pytest tests/abs_tk           # ABS, BDA & Traditional Knowledge (149 tests)
python -m pytest tests/international_ip # International IP, PCT, Madrid (63 tests)
python -m pytest tests/integration      # Full multi-agent integration & QA (261 tests)
```

---

## 📚 Documentation

Detailed documentation and research specifications are available in the `docs/` directory:
- `docs/specs/`: Problem statements, architectural specifications, and implementation plans.
- `docs/members/`: Individual workstream specifications and member roles.
- `docs/research/`: Regulatory research whitepapers and presentation decks.
