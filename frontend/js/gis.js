/* gis.js — Ayurveda Geographical Indications & Geo-Origin Explorer (GIS / Remote Sensing).
   Complies with SIH-26045 technology requirement: Artificial Intelligence + GIS / Remote Sensing.
   Features:
   - Interactive SVG map of India with GI clusters
   - Remote sensing agro-climatic habitat analysis (altitude, soil, rainfall, spectral active markers)
   - Biological Diversity Act §10(4)(d) Geo-Origin & State Biodiversity Board (SBB) lookup
*/
"use strict";

const GIS = (() => {
  let gisData = null;
  let selectedGI = null;

  const el = (id) => document.getElementById(id);

  async function loadData() {
    if (gisData) return gisData;
    try {
      const resp = await fetch("/api/gis/data");
      if (!resp.ok) throw new Error("Failed to fetch GIS data");
      gisData = await resp.json();
      return gisData;
    } catch (err) {
      console.error("GIS load error:", err);
      return null;
    }
  }

  function renderMap() {
    if (!gisData) return;
    const records = gisData.gis_records || [];
    const container = el("gisMapPins");
    if (!container) return;

    // Map SVG projection: India bounding box approx lat 8-37, lon 68-97
    // Container width 600, height 650
    const minLat = 7.0, maxLat = 37.5;
    const minLon = 68.0, maxLon = 97.5;
    const w = 560, h = 620;

    let pinsHtml = "";
    records.forEach((rec) => {
      const lat = rec.coordinates[0];
      const lon = rec.coordinates[1];
      // Equirectangular projection mapping
      const x = ((lon - minLon) / (maxLon - minLon)) * w + 20;
      const y = h - ((lat - minLat) / (maxLat - minLat)) * h + 20;

      pinsHtml += `
        <g class="gis-pin ${selectedGI && selectedGI.id === rec.id ? 'active' : ''}" 
           data-id="${rec.id}" transform="translate(${x.toFixed(1)}, ${y.toFixed(1)})">
          <circle r="12" class="gis-pulse"></circle>
          <circle r="6" class="gis-dot"></circle>
          <text x="10" y="4" class="gis-label">${rec.name}</text>
        </g>
      `;
    });
    container.innerHTML = pinsHtml;

    // Attach click listeners to pins
    container.querySelectorAll(".gis-pin").forEach((g) => {
      g.addEventListener("click", () => {
        const id = g.dataset.id;
        const found = records.find((r) => r.id === id);
        if (found) selectGI(found);
      });
    });
  }

  function renderList() {
    if (!gisData) return;
    const container = el("gisRecordsList");
    if (!container) return;

    const records = gisData.gis_records || [];
    container.innerHTML = records.map((r) => `
      <div class="gis-card ${selectedGI && selectedGI.id === r.id ? 'active' : ''}" data-id="${r.id}">
        <div class="gis-card-header">
          <span class="gis-tag">${r.state}</span>
          <span class="gis-badge">${r.gi_status}</span>
        </div>
        <h4 class="gis-name">${r.name}</h4>
        <p class="gis-botanical"><em>${r.botanical_name}</em> (${r.sanskrit_name})</p>
        <p class="gis-desc">${r.classical_indications}</p>
      </div>
    `).join("");

    container.querySelectorAll(".gis-card").forEach((card) => {
      card.addEventListener("click", () => {
        const id = card.dataset.id;
        const found = records.find((r) => r.id === id);
        if (found) selectGI(found);
      });
    });
  }

  function selectGI(rec) {
    selectedGI = rec;
    renderMap();
    renderList();

    const detailBox = el("gisDetailPanel");
    if (!detailBox) return;

    const rs = rec.remote_sensing || {};
    detailBox.innerHTML = `
      <div class="card detail-content animate-fade">
        <div class="detail-top">
          <div>
            <span class="badge badge-success">${rec.gi_status}</span>
            <span class="badge badge-info">${rec.gi_class}</span>
            <h3>${rec.name}</h3>
            <p class="text-muted"><strong>Botanical:</strong> <em>${rec.botanical_name}</em> | <strong>Sanskrit:</strong> ${rec.sanskrit_name}</p>
          </div>
          <div class="coords-box">
            <span class="coords-latlon">${rec.coordinates[0]}° N, ${rec.coordinates[1]}° E</span>
            <span class="coords-region">${rec.region}, ${rec.state}</span>
          </div>
        </div>

        <div class="detail-section">
          <h4><svg class="icon icon-sm"><use href="#i-leaf"/></svg> Classical Ayurvedic Indications</h4>
          <p>${rec.classical_indications}</p>
        </div>

        <div class="detail-section">
          <h4><svg class="icon icon-sm"><use href="#i-globe"/></svg> Remote Sensing & Agro-Climatic Habitat Profile</h4>
          <div class="rs-grid">
            <div class="rs-item"><span class="rs-label">Agro-Climatic Zone:</span> <span>${rs.agro_climatic_zone || 'N/A'}</span></div>
            <div class="rs-item"><span class="rs-label">Elevation / Altitude:</span> <span>${rs.altitude_meters || 'N/A'}</span></div>
            <div class="rs-item"><span class="rs-label">Soil Signature:</span> <span>${rs.soil_type || 'N/A'}</span></div>
            <div class="rs-item"><span class="rs-label">Annual Rainfall:</span> <span>${rs.annual_rainfall_mm || 'N/A'}</span></div>
            <div class="rs-item full"><span class="rs-label">Active Chemical Fingerprint:</span> <span class="highlight">${rs.active_chemical_markers || 'N/A'}</span></div>
          </div>
        </div>

        <div class="detail-section highlight-box">
          <h4><svg class="icon icon-sm"><use href="#i-scale"/></svg> BDA §10(4)(d) Geo-Origin & ABS Compliance</h4>
          <p>${rec.bda_disclosure_note}</p>
          <p><strong>State Jurisdiction:</strong> ${rec.sbb_jurisdiction}</p>
          <a href="${rec.sbb_portal}" target="_blank" rel="noopener noreferrer" class="btn-link">
            Visit SBB Portal <svg class="icon icon-sm"><use href="#i-ext"/></svg>
          </a>
        </div>
      </div>
    `;
  }

  function initOriginChecker() {
    const checkBtn = el("gisCheckOriginBtn");
    if (!checkBtn) return;

    checkBtn.addEventListener("click", () => {
      const state = el("gisStateSelect").value;
      const sbb = (gisData && gisData.sbb_directory && gisData.sbb_directory[state]) || null;
      const resBox = el("gisOriginResult");
      if (!resBox) return;

      if (!sbb) {
        resBox.innerHTML = `<p class="muted">Select a state to view State Biodiversity Board requirements.</p>`;
        return;
      }

      resBox.innerHTML = `
        <div class="origin-result-card animate-fade">
          <h4>${sbb.board}</h4>
          <p><strong>Headquarters:</strong> ${sbb.headquarters}</p>
          <p><strong>Applicable Form:</strong> ${sbb.intimation_form}</p>
          <p><strong>AYUSH Practitioner Exemption Status:</strong> ${sbb.ayush_status}</p>
          <p><strong>Patents Act Compliance:</strong> Mandatory declaration of geographic origin under Section 10(4)(d).</p>
          <a href="${sbb.portal}" target="_blank" rel="noopener noreferrer" class="btn-link">
            Official State Portal <svg class="icon icon-sm"><use href="#i-ext"/></svg>
          </a>
        </div>
      `;
    });
  }

  async function show() {
    await loadData();
    renderMap();
    renderList();
    initOriginChecker();
    if (gisData && gisData.gis_records && gisData.gis_records.length > 0 && !selectedGI) {
      selectGI(gisData.gis_records[0]);
    }
  }

  return { show };
})();
