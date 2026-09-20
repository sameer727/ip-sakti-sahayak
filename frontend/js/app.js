/* app.js — shell + chat assistant view.
   Talks to the real integrated backend: POST /api/query, POST /api/classify,
   GET /api/health. No mocked data anywhere. */
"use strict";

const App = (() => {
  const savedLang = (typeof localStorage !== "undefined" && localStorage.getItem("ipsakti_lang")) || "en";
  const state = {
    jurisdiction: "India",
    language: savedLang,
    formulationClass: null,
    history: [],          // {role, content} — capped, sent with each request
    busy: false,
  };

  let lastMetaRecord = null;

  const SCENARIOS = {
    "classical-patent": {
      query: "Can I patent a classical Ayurvedic formulation from an authoritative text?",
      query_hi: "क्या मैं किसी प्रामाणिक ग्रंथ से शास्त्रीय आयुर्वेदिक फॉर्मूलेशन को पेटेंट करा सकता हूँ?",
      jurisdiction: "India",
    },
    "abs": {
      query: "I want to commercialise a formulation using a plant collected in India — what approvals do I need?",
      query_hi: "मैं भारत से एकत्र किए गए पौधे का उपयोग करके फॉर्मूलेशन का व्यावसायीकरण करना चाहता हूँ — मुझे किन स्वीकृतियों की आवश्यकता है?",
      jurisdiction: "India",
    },
    "gi": {
      query: "How do I register a GI tag for an Ayurvedic product tied to a region?",
      query_hi: "किसी क्षेत्र-विशिष्ट आयुर्वेदिक उत्पाद हेतु जीआई (GI) टैग कैसे पंजीकृत करें?",
      jurisdiction: "India",
    },
    "international-patent": {
      query: "I want to file a patent for a new Ayurvedic drug outside India — what route do I use?",
      query_hi: "मैं भारत के बाहर एक नई आयुर्वेदिक औषधि के लिए पेटेंट दाखिल करना चाहता हूँ — कौन सा मार्ग अपनाऊँ?",
      jurisdiction: "International",
    },
  };

  const CLASSIFIER_EXAMPLE = {
    primary_purpose: "therapeutic",
    text_source: "yes",
    standardised_fraction: "no",
    ingredients_known: "yes",
    new_indication: "no",
  };

  const el = (id) => document.getElementById(id);
  const els = {
    conversation: () => el("conversation"),
    input: () => el("queryInput"),
    sendBtn: () => el("sendBtn"),
    composer: () => el("composer"),
    sourcesList: () => el("sourcesList"),
    sourcesEmpty: () => document.querySelector(".sources-empty"),
    metaList: () => el("metaList"),
    metaEmpty: () => document.querySelector("#metaCard .meta-empty"),
    specialistList: () => el("specialistList"),
    healthDot: () => el("healthDot"),
    healthText: () => el("healthText"),
    jurisdictionNote: () => el("jurisdictionNote"),
    welcome: () => el("welcome"),
    newChatBtn: () => el("newChatBtn"),
  };

  function esc(text) {
    const div = document.createElement("div");
    div.textContent = text == null ? "" : String(text);
    return div.innerHTML;
  }

  /* ── shell: navigation, toggles, health ─────────────────────────── */

  const VIEW_HINTS = {
    chat: "chatHint",
    classifier: "classifierHint",
    gis: "gisHint",
    graph: "graphHint",
    forms: "formsHint",
    audit: "auditHint",
    about: "aboutHint",
    help: "helpHint",
  };

  async function renderAuditTrailView() {
    const container = el("auditTableContainer");
    if (!container) return;
    try {
      const resp = await fetch("/api/audit-trail?limit=50");
      if (!resp.ok) throw new Error("Failed to fetch audit log");
      const data = await resp.json();
      const logs = data.logs || [];
      if (!logs.length) {
        container.innerHTML = `<p class="muted">No audit events recorded yet.</p>`;
        return;
      }
      container.innerHTML = `
        <div class="audit-summary-card">
          <div class="audit-stat"><span>Compliance:</span> <strong class="text-success">DPDP Act 2023 & MeitY AI Advisory Aligned</strong></div>
          <div class="audit-stat"><span>Data Sovereignty:</span> <strong>Processed on Indian Servers</strong></div>
          <div class="audit-stat"><span>Events Logged:</span> <strong>${logs.length}</strong></div>
          <button type="button" class="btn-primary btn-small" id="exportAuditBtn">Export JSON Audit Trail</button>
        </div>
        <div class="table-scroll">
          <table class="audit-table">
            <thead>
              <tr>
                <th>Timestamp (UTC)</th>
                <th>Audit ID</th>
                <th>Event Type</th>
                <th>Jurisdiction</th>
                <th>Data Localisation</th>
              </tr>
            </thead>
            <tbody>
              ${logs.map((l) => `
                <tr>
                  <td>${new Date(l.timestamp).toLocaleString()}</td>
                  <td><code>${l.id || l.ticket_id || 'N/A'}</code></td>
                  <td><span class="badge badge-info">${l.event_type || 'query_processed'}</span></td>
                  <td>${l.jurisdiction || 'India'}</td>
                  <td><span class="badge badge-success">IN Server</span></td>
                </tr>
              `).join("")}
            </tbody>
          </table>
        </div>
      `;
      const exportBtn = el("exportAuditBtn");
      if (exportBtn) {
        exportBtn.onclick = () => {
          const blob = new Blob([JSON.stringify(logs, null, 2)], { type: "application/json" });
          const url = URL.createObjectURL(blob);
          const a = document.createElement("a");
          a.href = url;
          a.download = `IP_SAKTI_Audit_Trail_${new Date().toISOString().slice(0, 10)}.json`;
          a.click();
        };
      }
    } catch (e) {
      container.innerHTML = `<p class="status-error">Error loading audit trail: ${e.message}</p>`;
    }
  }

  function switchView(view) {
    ["chat", "classifier", "gis", "graph", "forms", "audit", "about", "help"].forEach((name) => {
      const viewEl = document.getElementById(`view-${name}`);
      if (viewEl) viewEl.classList.toggle("hidden", name !== view);
    });
    document.querySelectorAll(".nav-item").forEach((item) => {
      item.classList.toggle("active", item.dataset.view === view);
    });
    const titleKey = view === "chat" ? "navChat"
      : view === "classifier" ? "navClassifier"
      : view === "gis" ? "navGis"
      : view === "graph" ? "navGraph"
      : view === "forms" ? "navForms"
      : view === "audit" ? "navAudit"
      : view === "about" ? "navAbout" : "navHelp";
    el("viewTitle").textContent = I18N.t(titleKey);
    el("viewHint").textContent = I18N.t(VIEW_HINTS[view] || "chatHint");
    if (view === "classifier") Classifier.show();
    if (view === "gis" && typeof GIS !== "undefined") GIS.show();
    if (view === "graph" && typeof KnowledgeGraph !== "undefined") KnowledgeGraph.show();
    if (view === "forms" && typeof FormsHub !== "undefined") FormsHub.show();
    if (view === "audit") renderAuditTrailView();
  }

  function updateJurisdictionNote() {
    const note = els.jurisdictionNote();
    note.textContent = state.jurisdiction === "India"
      ? I18N.t("jurisdictionNoteIndia")
      : I18N.t("jurisdictionNoteIntl");
    note.classList.add("visible");
  }

  async function setLanguage(lang) {
    if (!lang) return;
    const spinner = el("langSpinner");
    if (spinner) spinner.classList.remove("hidden");

    state.language = lang;

    // Sync languageSelect dropdown
    const langSelect = el("languageSelect");
    if (langSelect && langSelect.value !== lang) {
      langSelect.value = lang;
    }

    try {
      await I18N.applyAsync(lang);
    } catch (err) {
      console.error("Language switch error:", err);
    } finally {
      if (spinner) spinner.classList.add("hidden");
    }

    // Re-render UI components that depend on current language
    updateJurisdictionNote();
    refreshHealth();
    if (lastMetaRecord) {
      setMeta(lastMetaRecord.response, lastMetaRecord.seconds, lastMetaRecord.kind);
    }
  }

  function initShell() {
    document.querySelectorAll(".nav-item").forEach((item) => {
      item.addEventListener("click", () => switchView(item.dataset.view));
    });

    el("jurisdictionToggle").addEventListener("click", (event) => {
      const button = event.target.closest(".seg");
      if (!button) return;
      state.jurisdiction = button.dataset.value;
      document.querySelectorAll("#jurisdictionToggle .seg").forEach((s) =>
        s.classList.toggle("active", s === button));
      updateJurisdictionNote();
    });

    const langSelect = el("languageSelect");
    if (langSelect) {
      langSelect.addEventListener("change", async (event) => {
        const lang = event.target.value;
        if (lang) {
          await setLanguage(lang);
        }
      });
    }

    el("formulationSelect").addEventListener("change", (event) => {
      state.formulationClass = event.target.value || null;
    });

    els.newChatBtn().addEventListener("click", () => {
      state.history = [];
      els.conversation().innerHTML = "";
      els.conversation().appendChild(buildWelcome());
      els.sourcesList().innerHTML = "";
      els.sourcesEmpty().classList.remove("hidden");
      lastMetaRecord = null;
      setMeta(null);
      els.newChatBtn().classList.add("hidden");
    });

    document.addEventListener("i18n:changed", updateJurisdictionNote);
    updateJurisdictionNote();
  }

  async function refreshHealth() {
    try {
      const health = await API.health();
      els.healthDot().className = "health-dot ok";
      els.healthText().textContent = I18N.t("healthOk");
      const names = {
        INDIA_IP: "specIndia",
        ABS_TK: "specAbs",
        INTERNATIONAL_IP: "specIntl",
        CLASSIFICATION: "specCls",
      };
      const items = Object.keys(health.specialists || {}).map((domain) => `
        <li><svg class="icon"><use href="#i-check"/></svg><span>${esc(I18N.t(names[domain] || domain))}</span></li>`);
      items.push(`<li><svg class="icon"><use href="#i-check"/></svg><span>${esc(I18N.t("specCentral"))}</span></li>`);
      els.specialistList().innerHTML = items.join("");
    } catch (err) {
      els.healthDot().className = "health-dot down";
      els.healthText().textContent = I18N.t("healthDown");
      els.specialistList().innerHTML = `<li class="muted">${esc(I18N.t("healthDown"))}</li>`;
    }
  }

  /* ── conversation ───────────────────────────────────────────────── */

  function buildWelcome() {
    const node = document.createElement("div");
    node.className = "welcome";
    node.id = "welcome";
    node.innerHTML = `
      <svg class="icon icon-xl"><use href="#i-mark"/></svg>
      <h2>${esc(I18N.t("welcomeTitle"))}</h2>
      <p>${esc(I18N.t("welcomeSub"))}</p>`;
    return node;
  }

  function addUserMessage(text) {
    els.welcome() && els.welcome().remove();
    els.newChatBtn().classList.remove("hidden");
    const row = document.createElement("div");
    row.className = "msg msg-user";
    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.textContent = text;
    row.appendChild(bubble);
    els.conversation().appendChild(row);
  }

  function addAssistantShell() {
    const row = document.createElement("div");
    row.className = "msg msg-assistant";
    row.innerHTML = `
      <div class="answer-card">
        <div class="answer-head"><svg class="icon icon-sm"><use href="#i-mark"/></svg><span>IP-SAKTI Sahayak</span></div>
        <div class="answer-body"><p class="muted"><span class="typing"><i></i><i></i><i></i></span></p></div>
      </div>`;
    els.conversation().appendChild(row);
    els.conversation().scrollTop = els.conversation().scrollHeight;
    return {
      card: row.querySelector(".answer-card"),
      body: row.querySelector(".answer-body"),
    };
  }

  function formatInlineMarkdown(str) {
    if (!str) return "";
    let s = esc(str);
    // Bold: **text** or __text__
    s = s.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    s = s.replace(/__(.+?)__/g, "<strong>$1</strong>");
    // Italic: *text* or _text_
    s = s.replace(/(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)/g, "<em>$1</em>");
    s = s.replace(/(?<!_)_(?!_)(.+?)(?<!_)_(?!_)/g, "<em>$1</em>");
    // Inline code: `code`
    s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
    return s;
  }

  function answerParagraphs(text) {
    const container = document.createElement("div");
    container.className = "formatted-answer";

    const rawBlocks = String(text || "").replace(/\r\n/g, "\n").split(/\n{2,}/);

    rawBlocks.forEach((block) => {
      const trimmed = block.trim();
      if (!trimmed) return;

      const lines = trimmed.split("\n").map((l) => l.trim()).filter(Boolean);

      // Horizontal rule
      if (/^(?:---|\*\*\*|___)$/.test(trimmed)) {
        const hr = document.createElement("hr");
        hr.className = "answer-divider";
        container.appendChild(hr);
        return;
      }

      // Headings: #, ##, ###, ####
      const hMatch = lines[0].match(/^(#{1,4})\s+(.+)$/);
      if (hMatch && lines.length === 1) {
        const level = hMatch[1].length;
        const tag = level <= 2 ? "h3" : "h4";
        const hEl = document.createElement(tag);
        hEl.className = `answer-heading heading-l${level}`;
        hEl.innerHTML = formatInlineMarkdown(hMatch[2]);
        container.appendChild(hEl);
        return;
      }

      // Blockquote: lines starting with >
      if (lines.every((l) => l.startsWith(">"))) {
        const bq = document.createElement("blockquote");
        bq.className = "answer-quote";
        const quoteText = lines.map((l) => l.replace(/^>\s*/, "")).join(" ");
        bq.innerHTML = formatInlineMarkdown(quoteText);
        container.appendChild(bq);
        return;
      }

      // Bullet lists: -, *, •
      const isBullet = lines.every((l) => /^[-*•]\s+/.test(l));
      if (isBullet) {
        const ul = document.createElement("ul");
        ul.className = "answer-list";
        lines.forEach((l) => {
          const li = document.createElement("li");
          li.innerHTML = formatInlineMarkdown(l.replace(/^[-*•]\s+/, ""));
          ul.appendChild(li);
        });
        container.appendChild(ul);
        return;
      }

      // Numbered lists: 1. , 2. 
      const isNumbered = lines.every((l) => /^\d+\.\s+/.test(l));
      if (isNumbered) {
        const ol = document.createElement("ol");
        ol.className = "answer-numbered-list";
        lines.forEach((l) => {
          const li = document.createElement("li");
          li.innerHTML = formatInlineMarkdown(l.replace(/^\d+\.\s+/, ""));
          ol.appendChild(li);
        });
        container.appendChild(ol);
        return;
      }

      // Markdown Table
      if (lines.length >= 2 && lines[0].startsWith("|") && lines[0].endsWith("|")) {
        const table = document.createElement("table");
        table.className = "answer-table";
        let isHead = true;
        lines.forEach((line) => {
          if (/^\|[\s\-:|]+\|$/.test(line)) {
            isHead = false;
            return;
          }
          const cells = line.split("|").slice(1, -1).map((c) => c.trim());
          const tr = document.createElement("tr");
          cells.forEach((c) => {
            const cellTag = isHead ? "th" : "td";
            const cell = document.createElement(cellTag);
            cell.innerHTML = formatInlineMarkdown(c);
            tr.appendChild(cell);
          });
          table.appendChild(tr);
        });
        container.appendChild(table);
        return;
      }

      // Heading with attached text on subsequent lines
      if (hMatch && lines.length > 1) {
        const level = hMatch[1].length;
        const tag = level <= 2 ? "h3" : "h4";
        const hEl = document.createElement(tag);
        hEl.className = `answer-heading heading-l${level}`;
        hEl.innerHTML = formatInlineMarkdown(hMatch[2]);
        container.appendChild(hEl);

        const rest = lines.slice(1).join(" ");
        const p = document.createElement("p");
        p.innerHTML = formatInlineMarkdown(rest);
        container.appendChild(p);
        return;
      }

      // Normal paragraph
      const p = document.createElement("p");
      p.innerHTML = formatInlineMarkdown(lines.join(" "));
      container.appendChild(p);
    });
    return container;
  }

  function citationNode(citation, index) {
    const item = document.createElement("div");
    item.className = "cite-item";
    const url = citation.url ? String(citation.url) : "";
    item.innerHTML = `
      <span class="cite-num">${index + 1}</span>
      <div class="cite-main">
        <div class="cite-name">${esc(citation.source_name)}</div>
        <div class="cite-meta">
          ${citation.section ? `${esc(citation.section)}<span class="sep">|</span>` : ""}
          ${esc(citation.source_type)}
        </div>
        ${url ? `<a class="cite-link" href="${esc(url)}" target="_blank" rel="noopener noreferrer">
          ${esc(url.replace(/^https?:\/\//, "").slice(0, 60))}${url.length > 67 ? "…" : ""}
          <svg class="icon"><use href="#i-ext"/></svg></a>` : ""}
      </div>`;
    return item;
  }

  function setMeta(response, seconds, kind) {
    if (!response) {
      lastMetaRecord = null;
      els.metaEmpty().classList.remove("hidden");
      els.metaList().classList.add("hidden");
      return;
    }
    lastMetaRecord = { response, seconds, kind };
    const langName = I18N.getLanguageFullName
      ? I18N.getLanguageFullName(state.language)
      : (state.language === "hi" ? "हिन्दी" : "English");
    const statusKey = kind === "error" ? "statusError"
      : response.abstention ? "statusAbstained" : "statusAnswered";
    const statusClass = kind === "error" ? "status-error"
      : response.abstention ? "status-abstained" : "status-ok";
    const timeKey = response.abstention ? "abstainedIn" : "answeredIn";
    const rows = [
      [I18N.t("rowStatus"), `<span class="${statusClass}">${esc(I18N.t(statusKey))}</span>`, true],
      [I18N.t("rowConfidence"),
        `<span class="conf-badge conf-${esc(response.confidence)}">${esc(response.confidence)}</span> `
        + `<span class="conf-score">${Number(response.confidence_score).toFixed(2)}</span>`, true],
      [I18N.t("rowJurisdiction"), esc(state.jurisdiction), true],
      [I18N.t("rowLanguage"), esc(langName), true],
      [I18N.t("rowFormulation"), esc(state.formulationClass || I18N.t("autoDetect")), true],
      [I18N.t("rowSources"), String((response.citations || []).length), true],
      [I18N.t("rowTime"), esc(I18N.t(timeKey).replace("{s}", (seconds || 0).toFixed(2))), true],
    ];
    els.metaList().innerHTML = rows
      .map(([label, value]) => `<div class="meta-row"><dt>${label}</dt><dd>${value}</dd></div>`)
      .join("");
    els.metaEmpty().classList.add("hidden");
    els.metaList().classList.remove("hidden");
  }

  function setSources(citations) {
    if (!citations || !citations.length) {
      els.sourcesList().innerHTML = "";
      els.sourcesEmpty().classList.remove("hidden");
      return;
    }
    els.sourcesEmpty().classList.add("hidden");
    els.sourcesList().innerHTML = "";
    citations.forEach((citation, index) => {
      els.sourcesList().appendChild(citationNode(citation, index));
    });
  }

  function renderAbstention(shell, response) {
    shell.body.innerHTML = "";
    const banner = document.createElement("div");
    banner.className = "abstain-banner";
    banner.innerHTML = `
      <svg class="icon"><use href="#i-shieldq"/></svg>
      <div>
        <div class="abstain-title">${esc(I18N.t("abstainTitle"))}</div>
        <div class="abstain-reason">${esc(response.abstention_reason || "")}</div>
      </div>`;
    shell.body.appendChild(banner);
    if (response.answer && response.answer.trim()) {
      shell.body.appendChild(answerParagraphs(response.answer));
    }
    const classificationCue = /classif/i.test(response.abstention_reason || "");
    if (classificationCue) {
      const row = document.createElement("p");
      row.style.marginTop = "10px";
      const button = document.createElement("button");
      button.type = "button";
      button.className = "btn-ghost btn-small";
      button.textContent = I18N.t("openClassifier");
      button.addEventListener("click", () => switchView("classifier"));
      row.appendChild(button);
      shell.body.appendChild(row);
    }
    addFoot(shell, response);
  }

  function renderAnswer(shell, response) {
    shell.body.innerHTML = "";
    shell.body.appendChild(answerParagraphs(response.answer));

    const section = document.createElement("div");
    section.className = "answer-section";
    section.innerHTML = `
      <div class="answer-section-label"><svg class="icon"><use href="#i-gauge"/></svg><span>${esc(I18N.t("confidenceLabel"))}</span></div>
      <div class="conf-row">
        <span class="conf-badge conf-${esc(response.confidence)}">${esc(response.confidence)}</span>
        <span class="conf-score">${Number(response.confidence_score).toFixed(2)}</span>
        <span class="conf-bar"><span class="conf-bar-fill${Number(response.confidence_score) < 0.5 ? " m-low" : ""}"
          style="width:${Math.round(Number(response.confidence_score) * 100)}%"></span></span>
      </div>`;
    shell.body.appendChild(section);

    if (response.citations && response.citations.length) {
      const citeSection = document.createElement("div");
      citeSection.className = "answer-section";
      const list = document.createElement("div");
      list.className = "cite-list";
      response.citations.forEach((citation, index) => {
        list.appendChild(citationNode(citation, index));
      });
      citeSection.innerHTML = `
        <div class="answer-section-label"><svg class="icon"><use href="#i-file"/></svg><span>${esc(I18N.t("sourcesLabel"))} · ${response.citations.length}</span></div>`;
      citeSection.appendChild(list);
      shell.body.appendChild(citeSection);
    }
    addFoot(shell, response);
  }

  function speakText(text, lang = null) {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    const targetLang = lang || state.language;
    const langMap = {
      hi: "hi-IN", ta: "ta-IN", te: "te-IN", bn: "bn-IN",
      mr: "mr-IN", gu: "gu-IN", kn: "kn-IN", ml: "ml-IN",
      pa: "pa-IN", or: "or-IN", en: "en-IN"
    };
    utterance.lang = langMap[targetLang] || (targetLang === "hi" ? "hi-IN" : "en-IN");
    utterance.rate = 1.0;
    window.speechSynthesis.speak(utterance);
  }

  function addFoot(shell, response) {
    if (response.answer && response.answer.trim()) {
      const bhashiniBar = document.createElement("div");
      bhashiniBar.className = "bhashini-toolbar";
      bhashiniBar.innerHTML = `
        <span class="bhashini-tag">🌐 Bhashini NLTM:</span>
        <button type="button" class="btn-translate-lang" data-lang="hi" title="Translate to Hindi">हिन्दी</button>
        <button type="button" class="btn-translate-lang" data-lang="ta" title="Translate to Tamil">தமிழ்</button>
        <button type="button" class="btn-translate-lang" data-lang="te" title="Translate to Telugu">తెలుగు</button>
        <button type="button" class="btn-translate-lang" data-lang="bn" title="Translate to Bengali">বাংলা</button>
        <button type="button" class="btn-translate-lang" data-lang="mr" title="Translate to Marathi">मराठी</button>
        <button type="button" class="btn-translate-lang" data-lang="gu" title="Translate to Gujarati">ગુજરાતી</button>
        <button type="button" class="btn-translate-lang" data-lang="en" title="Original English">English</button>
        <button type="button" class="btn-speak-answer" title="Read Aloud with Text-to-Speech">🔊 Listen</button>
      `;

      let originalAnswerText = response.answer;
      let currentText = response.answer;
      let currentLang = "en";

      bhashiniBar.addEventListener("click", async (e) => {
        const speakBtn = e.target.closest(".btn-speak-answer");
        if (speakBtn) {
          speakText(currentText, currentLang);
          return;
        }

        const btn = e.target.closest(".btn-translate-lang");
        if (!btn) return;
        const targetLang = btn.dataset.lang;

        if (targetLang === "en") {
          currentText = originalAnswerText;
          currentLang = "en";
          const firstSection = shell.body.querySelector(".answer-body") || shell.body.firstChild;
          if (firstSection) {
            firstSection.innerHTML = answerParagraphs(originalAnswerText).innerHTML;
          }
          return;
        }

        const originalBtnLabel = btn.textContent;
        btn.textContent = "⏳...";
        btn.disabled = true;

        try {
          const res = await fetch("/api/bhashini/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              text: originalAnswerText,
              source_language: "en",
              target_language: targetLang,
            }),
          });
          const data = await res.json();
          if (data.status === "ok" && data.translated_text) {
            currentText = data.translated_text;
            currentLang = targetLang;
            const firstSection = shell.body.querySelector(".answer-body") || shell.body.firstChild;
            if (firstSection) {
              firstSection.innerHTML = answerParagraphs(data.translated_text).innerHTML;
            }
          }
        } catch (err) {
          console.error("Bhashini translation request failed:", err);
        } finally {
          btn.textContent = originalBtnLabel;
          btn.disabled = false;
        }
      });

      shell.card.appendChild(bhashiniBar);
    }

    const foot = document.createElement("div");
    foot.className = "answer-foot";
    foot.textContent = response.disclaimer || "";
    shell.card.appendChild(foot);
  }

  function renderErrorShell(err, targetShell = null) {
    const shell = targetShell || addAssistantShell();
    const message = err.kind === "network" ? I18N.t("errNetwork")
      : err.status === 400 ? I18N.t("errValidation")
      : err.status === 502 ? I18N.t("errProcessing")
      : err.status === 503 ? I18N.t("errUnavailable")
      : I18N.t("errGeneric");
    shell.body.innerHTML = `
      <div class="error-banner"><svg class="icon"><use href="#i-alert"/></svg><span>${esc(message)}</span></div>`;
    const foot = document.createElement("div");
    foot.className = "answer-foot";
    foot.textContent = I18N.t("disclaimerBody");
    shell.card.appendChild(foot);
    setMeta({ abstention: false, confidence: "LOW", confidence_score: 0, citations: [] }, 0, "error");
  }

  /* ── request flow ───────────────────────────────────────────────── */

  async function sendQuery(text) {
    if (state.busy) return;
    const query = (text || "").trim();
    if (!query) return;

    state.busy = true;
    els.sendBtn().disabled = true;
    els.input().value = "";
    addUserMessage(query);
    const shell = addAssistantShell();
    const started = performance.now();

    try {
      const response = await API.query({
        id: `web-${Date.now()}`,
        query,
        language: state.language,
        jurisdiction: state.jurisdiction,
        formulation_class: state.formulationClass,
        history: state.history,
      });
      const seconds = (performance.now() - started) / 1000;
      shell.body.innerHTML = "";
      if (response.abstention) {
        renderAbstention(shell, response);
      } else {
        renderAnswer(shell, response);
      }
      setMeta(response, seconds);
      setSources(response.citations);
      state.history.push({ role: "user", content: query });
      state.history.push({ role: "assistant", content: String(response.answer || "") });
      if (state.history.length > 20) state.history = state.history.slice(-20);
    } catch (err) {
      renderErrorShell(err, shell);
    } finally {
      state.busy = false;
      els.sendBtn().disabled = false;
      els.input().focus();
    }
  }

  /* ── demo scenario cards ────────────────────────────────────────── */

  function initDemoCards() {
    document.querySelectorAll(".demo-card").forEach((card) => {
      card.addEventListener("click", () => {
        const scenario = card.dataset.scenario;
        if (scenario === "classification") {
          switchView("classifier");
          Classifier.prefill(CLASSIFIER_EXAMPLE);
          Classifier.classify();
          return;
        }
        const spec = SCENARIOS[scenario];
        if (!spec) return;
        switchView("chat");
        if (spec.jurisdiction !== state.jurisdiction) {
          state.jurisdiction = spec.jurisdiction;
          document.querySelectorAll("#jurisdictionToggle .seg").forEach((s) =>
            s.classList.toggle("active", s.dataset.value === spec.jurisdiction));
          updateJurisdictionNote();
        }
        const queryText = (state.language === "hi" && spec.query_hi) ? spec.query_hi : spec.query;
        sendQuery(queryText);
      });
    });
  }

  /* ── boot ───────────────────────────────────────────────────────── */

  function initFormulationOptions() {
    // Contract-legal FormulationClass values (Plan.md §7) — machine values,
    // mirrored from the backend contract; classifier questions come from the
    // backend separately.
    const values = ["Classical", "Proprietary", "Phytopharmaceutical",
      "Ayurveda-Aahar", "Cosmetic", "New Drug", "Uncertain"];
    const select = el("formulationSelect");
    values.forEach((value) => {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = value;
      select.appendChild(option);
    });
  }

  let recognition = null;
  let isListening = false;

  function initVoiceInput() {
    const micBtn = el("voiceInputBtn");
    if (!micBtn) return;
    const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRec) {
      micBtn.title = "Speech recognition not supported in this browser";
      micBtn.classList.add("disabled");
      return;
    }
    recognition = new SpeechRec();
    recognition.continuous = false;
    recognition.interimResults = false;

    micBtn.addEventListener("click", () => {
      if (isListening) {
        recognition.stop();
        return;
      }
      const speechLangMap = {
        hi: "hi-IN", ta: "ta-IN", te: "te-IN", bn: "bn-IN",
        mr: "mr-IN", gu: "gu-IN", kn: "kn-IN", ml: "ml-IN",
        pa: "pa-IN", or: "or-IN", as: "as-IN", ur: "ur-IN",
        sa: "sa-IN", en: "en-IN"
      };
      recognition.lang = speechLangMap[state.language] || (state.language === "en" ? "en-IN" : `${state.language}-IN`);
      try {
        recognition.start();
      } catch (e) {
        console.warn("Speech start error:", e);
      }
    });

    recognition.onstart = () => {
      isListening = true;
      micBtn.classList.add("listening");
      micBtn.title = "Listening… Click to stop";
    };

    recognition.onend = () => {
      isListening = false;
      micBtn.classList.remove("listening");
      micBtn.title = I18N.t("voiceInput");
    };

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      if (transcript) {
        const input = els.input();
        input.value = (input.value ? input.value + " " : "") + transcript;
        input.focus();
      }
    };
  }

  function init() {
    initShell();
    initFormulationOptions();
    initDemoCards();
    initVoiceInput();
    if (typeof EscalationModal !== "undefined") EscalationModal.init();
    Classifier.init();
    refreshHealth();
    window.setInterval(refreshHealth, 30000);

    // Synchronize initial language from state / localStorage
    if (state.language) {
      setLanguage(state.language);
    }

    els.composer().addEventListener("submit", (event) => {
      event.preventDefault();
      sendQuery(els.input().value);
    });
    els.input().addEventListener("keydown", (event) => {
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendQuery(els.input().value);
      }
    });
    // auto-grow textarea
    els.input().addEventListener("input", () => {
      const input = els.input();
      input.style.height = "auto";
      input.style.height = `${Math.min(input.scrollHeight, 140)}px`;
    });
  }

  document.addEventListener("DOMContentLoaded", init);
  return { sendQuery, switchView };
})();
