/* forms.js — Statutory Forms & Registry Hub.
   Facilitates moving from a question to the right registry, record, or form.
   Complies with SIH-26045 requirement: "facilitates access to authoritative sources
   ... so that a user can move from a question to the right registry, record or form".
*/
"use strict";

const FormsHub = (() => {
  let formsData = null;
  let activeFilter = "all";
  let applicantType = "natural_person_startup";

  const el = (id) => document.getElementById(id);

  async function loadData() {
    if (formsData) return formsData;
    try {
      const resp = await fetch("/api/forms");
      if (!resp.ok) throw new Error("Failed to load forms");
      formsData = await resp.json();
      return formsData;
    } catch (err) {
      console.error("Forms load error:", err);
      return null;
    }
  }

  function renderForms() {
    if (!formsData) return;
    const container = el("formsGrid");
    if (!container) return;

    let forms = formsData.forms || [];
    const searchVal = (el("formsSearch") ? el("formsSearch").value : "").toLowerCase().trim();

    if (activeFilter !== "all") {
      forms = forms.filter((f) => f.regime.toLowerCase().includes(activeFilter.toLowerCase()));
    }

    if (searchVal) {
      forms = forms.filter((f) => 
        f.code.toLowerCase().includes(searchVal) ||
        f.title.toLowerCase().includes(searchVal) ||
        f.regime.toLowerCase().includes(searchVal)
      );
    }

    if (forms.length === 0) {
      container.innerHTML = `<p class="muted">No matching statutory forms found for the selected filter.</p>`;
      return;
    }

    container.innerHTML = forms.map((f) => {
      let feeDisplay = "";
      if (f.fees) {
        if (typeof f.fees === "object") {
          feeDisplay = f.fees[applicantType] || Object.values(f.fees)[0];
        } else {
          feeDisplay = String(f.fees);
        }
      }

      const reqList = (f.ayurveda_specific_requirements || [])
        .map((r) => `<li>${r}</li>`)
        .join("");

      return `
        <div class="card form-card animate-fade">
          <div class="form-card-top">
            <span class="badge badge-primary">${f.regime}</span>
            <span class="form-code">${f.code}</span>
          </div>
          <h3 class="form-title">${f.title}</h3>
          <p class="form-admin"><strong>Authority:</strong> ${f.admin_body}</p>
          
          <div class="form-fee-box">
            <span class="fee-label">Applicable Fee (${applicantType.includes("startup") ? "Startup / MSME" : "Large Entity"}):</span>
            <span class="fee-val">${feeDisplay}</span>
          </div>

          <div class="form-timeline">
            <strong>Statutory Timeline:</strong> ${f.statutory_timeline}
          </div>

          <div class="form-reqs">
            <strong>Ayurveda-Specific Compliance:</strong>
            <ul>${reqList}</ul>
          </div>

          <div class="form-actions">
            <a href="${f.portal_url}" target="_blank" rel="noopener noreferrer" class="btn-primary btn-small">
              Open Official Filing Portal <svg class="icon icon-sm"><use href="#i-ext"/></svg>
            </a>
          </div>
        </div>
      `;
    }).join("");
  }

  function initControls() {
    document.querySelectorAll(".forms-filter-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".forms-filter-btn").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        activeFilter = btn.dataset.filter;
        renderForms();
      });
    });

    const searchInput = el("formsSearch");
    if (searchInput) {
      searchInput.addEventListener("input", renderForms);
    }

    const typeSelect = el("formsApplicantType");
    if (typeSelect) {
      typeSelect.addEventListener("change", (e) => {
        applicantType = e.target.value;
        renderForms();
      });
    }
  }

  async function show() {
    await loadData();
    initControls();
    renderForms();
  }

  return { show };
})();
