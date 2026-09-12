/* graph.js — Interactive Ayurveda IP & Regulatory Knowledge Graph.
   Complies with SIH-26045 requirement: "A relational knowledge graph and agentic,
   multi-source orchestration deepen multi-step reasoning".
*/
"use strict";

const KnowledgeGraph = (() => {
  let graphData = null;
  let activeFilter = "all";
  let selectedNode = null;

  const el = (id) => document.getElementById(id);

  const TYPE_COLORS = {
    formulation: "#2d7a4f",
    regime: "#1d4ed8",
    caselaw: "#b45309",
    authority: "#6b21a8",
    treaty: "#047857",
  };

  async function loadData() {
    if (graphData) return graphData;
    try {
      const resp = await fetch("/api/knowledge-graph");
      if (!resp.ok) throw new Error("Failed to load Knowledge Graph");
      graphData = await resp.json();
      return graphData;
    } catch (err) {
      console.error("Knowledge Graph error:", err);
      return null;
    }
  }

  function renderGraph() {
    if (!graphData) return;
    const canvas = el("kgCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const width = canvas.width = canvas.parentElement.clientWidth || 700;
    const height = canvas.height = 550;

    let nodes = graphData.nodes || [];
    let links = graphData.links || [];

    if (activeFilter !== "all") {
      nodes = nodes.filter((n) => n.type === activeFilter);
      const nodeIds = new Set(nodes.map((n) => n.id));
      links = links.filter((l) => nodeIds.has(l.source) && nodeIds.has(l.target));
    }

    // Position nodes using concentric/force layout
    const nodeMap = new Map();
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) * 0.38;

    nodes.forEach((n, idx) => {
      const angle = (idx / nodes.length) * 2 * Math.PI;
      const x = centerX + radius * Math.cos(angle);
      const y = centerY + radius * Math.sin(angle);
      nodeMap.set(n.id, { ...n, x, y });
    });

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    // Draw Links
    links.forEach((link) => {
      const src = nodeMap.get(link.source);
      const tgt = nodeMap.get(link.target);
      if (!src || !tgt) return;

      ctx.beginPath();
      ctx.moveTo(src.x, src.y);
      ctx.lineTo(tgt.x, tgt.y);
      ctx.strokeStyle = "#cbd5e1";
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Draw relationship label midpoint
      const midX = (src.x + tgt.x) / 2;
      const midY = (src.y + tgt.y) / 2;
      ctx.fillStyle = "#64748b";
      ctx.font = "10px sans-serif";
      ctx.fillText(link.label, midX - 20, midY);
    });

    // Draw Nodes
    nodeMap.forEach((node) => {
      const isSelected = selectedNode && selectedNode.id === node.id;
      const color = TYPE_COLORS[node.type] || "#475569";

      // Outer glow if selected
      if (isSelected) {
        ctx.beginPath();
        ctx.arc(node.x, node.y, 22, 0, 2 * Math.PI);
        ctx.fillStyle = "rgba(45, 122, 79, 0.25)";
        ctx.fill();
      }

      ctx.beginPath();
      ctx.arc(node.x, node.y, 14, 0, 2 * Math.PI);
      ctx.fillStyle = color;
      ctx.fill();
      ctx.strokeStyle = isSelected ? "#0f172a" : "#ffffff";
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // Label
      ctx.fillStyle = isSelected ? "#0f172a" : "#334155";
      ctx.font = isSelected ? "bold 11px sans-serif" : "11px sans-serif";
      ctx.fillText(node.label, node.x + 18, node.y + 4);
    });

    // Click handler on canvas
    canvas.onclick = (e) => {
      const rect = canvas.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const clickY = e.clientY - rect.top;

      let found = null;
      nodeMap.forEach((node) => {
        const dist = Math.hypot(node.x - clickX, node.y - clickY);
        if (dist <= 18) found = node;
      });

      if (found) {
        selectNode(found);
      }
    };
  }

  function selectNode(node) {
    selectedNode = node;
    renderGraph();

    const inspector = el("kgInspector");
    if (!inspector) return;

    // Find relationships
    const outgoing = (graphData.links || []).filter((l) => l.source === node.id);
    const incoming = (graphData.links || []).filter((l) => l.target === node.id);

    const relsHtml = `
      <div class="kg-rels">
        ${outgoing.map((l) => {
          const targetNode = (graphData.nodes || []).find((n) => n.id === l.target);
          return `<div class="kg-rel-item"><strong>${node.label}</strong> <span class="rel-tag">${l.label}</span> <strong>${targetNode ? targetNode.label : l.target}</strong></div>`;
        }).join("")}
        ${incoming.map((l) => {
          const srcNode = (graphData.nodes || []).find((n) => n.id === l.source);
          return `<div class="kg-rel-item"><strong>${srcNode ? srcNode.label : l.source}</strong> <span class="rel-tag">${l.label}</span> <strong>${node.label}</strong></div>`;
        }).join("")}
      </div>
    `;

    inspector.innerHTML = `
      <div class="card detail-content animate-fade">
        <div class="detail-top">
          <div>
            <span class="badge" style="background:${TYPE_COLORS[node.type] || '#475569'}; color:#fff">${node.type.toUpperCase()}</span>
            <h3>${node.label}</h3>
          </div>
        </div>
        <p class="kg-node-desc">${node.desc}</p>
        <h4>Connected Relationships</h4>
        ${outgoing.length + incoming.length > 0 ? relsHtml : '<p class="muted">No direct links in current view.</p>'}
      </div>
    `;
  }

  function initFilters() {
    document.querySelectorAll(".kg-filter-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".kg-filter-btn").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        activeFilter = btn.dataset.filter;
        renderGraph();
      });
    });

    const searchInput = el("kgSearchInput");
    if (searchInput) {
      searchInput.addEventListener("input", () => {
        const query = searchInput.value.toLowerCase().trim();
        if (!query) return;
        const match = (graphData.nodes || []).find((n) => n.label.toLowerCase().includes(query));
        if (match) selectNode(match);
      });
    }
  }

  async function show() {
    await loadData();
    initFilters();
    renderGraph();
    if (graphData && graphData.nodes && graphData.nodes.length > 0 && !selectedNode) {
      selectNode(graphData.nodes[0]);
    }
  }

  return { show };
})();
