"use strict";
(() => {
  const diagram = document.querySelector(".model-diagram");
  const inspector = document.getElementById("model-inspector");
  const content = document.getElementById("model-inspector-content");
  const status = document.getElementById("model-selection-status");
  if (!diagram || !inspector || !content || !status) return;
  document.querySelector(".model-controls").hidden = false;
  const choose = name => {
    const original = document.getElementById(`class-${name}`);
    if (!original) return;
    diagram.dataset.filtered = "true";
    const targets = new Set([name]);
    diagram.querySelectorAll(".model-edge").forEach(edge => {
      const selected = edge.dataset.source === name;
      edge.dataset.selected = String(selected);
      if (selected) targets.add(edge.dataset.target);
    });
    diagram.querySelectorAll(".model-node").forEach(node => {
      node.dataset.selected = String(node.dataset.class === name);
      node.dataset.related = String(targets.has(node.dataset.class));
    });
    document.querySelectorAll("[data-select-class]").forEach(button => {
      button.setAttribute("aria-pressed", String(button.dataset.selectClass === name));
    });
    const copy = original.cloneNode(true);
    copy.removeAttribute("id");
    copy.removeAttribute("tabindex");
    copy.querySelectorAll("[id]").forEach(element => element.removeAttribute("id"));
    content.replaceChildren(copy);
    status.textContent = `${name}: required fields and references from one record. The complete class list remains below.`;
    inspector.hidden = false;
  };
  document.querySelectorAll("[data-select-class]").forEach(button => {
    button.addEventListener("click", () => choose(button.dataset.selectClass));
  });
  diagram.querySelectorAll(".model-node[data-class]").forEach(node => {
    node.addEventListener("click", event => {
      if (node.dataset.class === "IdentifiedRecord") return;
      event.preventDefault();
      choose(node.dataset.class);
    });
  });
  document.getElementById("model-show-all").addEventListener("click", () => {
    diagram.dataset.filtered = "false";
    diagram.querySelectorAll("[data-selected], [data-related]").forEach(element => {
      element.dataset.selected = "false";
      element.dataset.related = "false";
    });
    document.querySelectorAll("[data-select-class]").forEach(button => button.setAttribute("aria-pressed", "false"));
    status.textContent = "All reference relationships are visible. Exact cardinalities and constraints are listed below.";
    content.replaceChildren();
  });
})();
