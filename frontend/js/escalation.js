/* escalation.js — Human IP Facilitator Escalation Modal.
   Complies with SIH-26045 requirement: "a path to escalate to a human IP facilitator".
   Connects AYUSH practitioners and startups to the Ministry of Ayush / AIIA-ICAINE IP Facilitation Desk.
*/
"use strict";

const EscalationModal = (() => {
  const el = (id) => document.getElementById(id);

  function open(context = {}) {
    const modal = el("escalationModal");
    if (!modal) return;

    el("escQuery").value = context.query || "";
    el("escJurisdiction").value = context.jurisdiction || "India";
    el("escClass").value = context.formulationClass || "Proprietary";

    el("escFormContainer").classList.remove("hidden");
    el("escSuccessContainer").classList.add("hidden");

    modal.classList.remove("hidden");
  }

  function close() {
    const modal = el("escalationModal");
    if (modal) modal.classList.add("hidden");
  }

  function init() {
    const modal = el("escalationModal");
    if (!modal) return;

    el("escCloseBtn").addEventListener("click", close);
    el("escCancelBtn").addEventListener("click", close);

    el("escForm").addEventListener("submit", async (e) => {
      e.preventDefault();
      const submitBtn = el("escSubmitBtn");
      submitBtn.disabled = true;
      submitBtn.textContent = "Submitting…";

      const payload = {
        query: el("escQuery").value,
        jurisdiction: el("escJurisdiction").value,
        formulation_class: el("escClass").value,
        user_name: el("escName").value,
        user_email: el("escEmail").value,
        user_phone: el("escPhone").value,
        user_organization: el("escOrg").value,
        details: el("escDetails").value,
      };

      try {
        const resp = await fetch("/api/escalate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
        if (!resp.ok) throw new Error("Escalation request failed");
        const ticket = await resp.json();

        el("escFormContainer").classList.add("hidden");
        const successBox = el("escSuccessContainer");
        successBox.classList.remove("hidden");
        successBox.innerHTML = `
          <div class="ticket-card animate-fade">
            <div class="ticket-header">
              <svg class="icon icon-lg text-success"><use href="#i-check"/></svg>
              <h3>Escalation Request Lodged</h3>
              <span class="ticket-id">${ticket.ticket_id}</span>
            </div>
            <p>Your case has been forwarded to the <strong>${ticket.assigned_desk}</strong>.</p>
            <p>An empanelled AYUSH IP facilitator will contact you at <strong>${ticket.user_email}</strong> within <strong>${ticket.expected_response_hours} hours</strong>.</p>
            <div class="ticket-foot">
              <button type="button" class="btn-primary" onclick="EscalationModal.close()">Done</button>
            </div>
          </div>
        `;
      } catch (err) {
        alert("Failed to submit escalation request. Please verify network and try again.");
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = "Submit Escalation";
      }
    });
  }

  return { init, open, close };
})();
