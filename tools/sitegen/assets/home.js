/* Progressive enhancement: proposal, evidence and comparisons are static HTML. */
(() => {
  "use strict";
  const workspace = document.getElementById("comparison-workspace");
  const cases = Array.from(document.querySelectorAll("[data-case]"));
  const chooser = document.getElementById("case-select");
  const main = document.getElementById("main");
  const narrow = window.matchMedia("(max-width: 1050px)");
  let returnFocus = null;
  let returnY = 0;
  let returnHash = "";
  let opened = false;

  function selectTab(example, name, focus) {
    const tabs = Array.from(example.querySelectorAll("[data-case-tab]"));
    tabs.forEach(tab => {
      const selected = tab.dataset.caseTab === name;
      tab.setAttribute("aria-selected", String(selected));
      tab.tabIndex = selected ? 0 : -1;
      if (selected && focus) tab.focus();
    });
    example.querySelectorAll("[data-case-panel]").forEach(panel => {
      panel.hidden = panel.dataset.casePanel !== name;
    });
  }

  function selectRepresentation(example, attribute, value) {
    example.querySelectorAll("[" + attribute + "]").forEach(panel => {
      panel.hidden = panel.getAttribute(attribute) !== value;
    });
  }

  function inspectObject(example, object) {
    example.querySelectorAll("[data-object-node]").forEach(node => {
      node.setAttribute("aria-pressed", String(node.dataset.objectNode === object));
    });
    example.querySelectorAll("[data-object]").forEach(token => {
      token.classList.toggle("object-selected", token.dataset.object === object);
    });
    example.querySelectorAll("[data-edge-source]").forEach(edge => {
      edge.classList.toggle("edge-selected", edge.dataset.edgeSource === object || edge.dataset.edgeTarget === object);
    });
    const feedback = example.querySelector(".selection-feedback");
    if (feedback) feedback.textContent = "Object " + object + " is marked in every candidate serialization on the Comparison tab.";
  }

  function modality() {
    const modal = opened && narrow.matches;
    main.inert = modal;
    document.querySelector(".wb-header").inert = modal;
    document.querySelector(".wb-footer").inert = modal;
    document.querySelector(".home-source-license").inert = modal;
    workspace.setAttribute("role", modal ? "dialog" : "complementary");
    if (modal) workspace.setAttribute("aria-modal", "true");
    else workspace.removeAttribute("aria-modal");
  }

  function openCase(id, fromLink = false) {
    const example = cases.find(candidate => candidate.dataset.case === id);
    if (!example) return false;
    if (!opened) {
      returnFocus = document.activeElement;
      returnY = window.scrollY;
      returnHash = location.hash.startsWith("#example=") ? "" : location.hash;
    }
    opened = true;
    cases.forEach(candidate => { candidate.hidden = candidate !== example; });
    chooser.value = id;
    workspace.classList.add("workspace-visible");
    document.body.classList.add("workspace-open");
    modality();
    workspace.scrollTop = 0;
    if (fromLink && location.hash !== "#example=" + id) {
      history.pushState({ example: id }, "", "#example=" + id);
    }
    example.querySelector('[role="tab"][aria-selected="true"]').focus({ preventScroll: true });
    return true;
  }

  function closeCase(updateLocation = true) {
    if (!opened) return;
    opened = false;
    workspace.classList.remove("workspace-visible");
    document.body.classList.remove("workspace-open");
    modality();
    if (updateLocation) history.replaceState(null, "", location.pathname + location.search + returnHash);
    window.scrollTo(0, returnY);
    if (returnFocus && returnFocus.isConnected && returnFocus !== document.body) {
      returnFocus.focus({ preventScroll: true });
    } else {
      main.tabIndex = -1;
      main.focus({ preventScroll: true });
    }
  }

  function syncHash() {
    if (location.hash.startsWith("#example=")) {
      const id = decodeURIComponent(location.hash.slice(9));
      if (!openCase(id)) closeCase(false);
    } else {
      closeCase(false);
    }
  }

  cases.forEach(example => {
    const tabs = Array.from(example.querySelectorAll("[data-case-tab]"));
    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => selectTab(example, tab.dataset.caseTab, false));
      tab.addEventListener("keydown", event => {
        let next = index;
        if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
        else if (event.key === "ArrowLeft") next = (index + tabs.length - 1) % tabs.length;
        else if (event.key === "Home") next = 0;
        else if (event.key === "End") next = tabs.length - 1;
        else return;
        event.preventDefault();
        selectTab(example, tabs[next].dataset.caseTab, true);
      });
    });
    selectTab(example, "comparison", false);
    const p5 = example.querySelector("[data-p5-select]");
    const binding = example.querySelector("[data-binding-select]");
    p5.addEventListener("change", () => selectRepresentation(example, "data-p5-variant", p5.value));
    binding.addEventListener("change", () => selectRepresentation(example, "data-binding", binding.value));
    selectRepresentation(example, "data-p5-variant", p5.value);
    selectRepresentation(example, "data-binding", binding.value);
    p5.closest("label").hidden = !p5.options.length;
    binding.closest("label").hidden = !binding.options.length;
    example.querySelectorAll("[data-object-node]").forEach(node => {
      node.addEventListener("click", () => inspectObject(example, node.dataset.objectNode));
      node.addEventListener("keydown", event => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          inspectObject(example, node.dataset.objectNode);
        }
      });
    });
  });

  document.addEventListener("click", event => {
    const link = event.target.closest('a[href^="#example="]');
    if (!link) return;
    event.preventDefault();
    openCase(decodeURIComponent(link.getAttribute("href").slice(9)), true);
  });
  chooser.addEventListener("change", () => openCase(chooser.value, true));
  document.getElementById("close-comparison").addEventListener("click", () => closeCase());
  document.addEventListener("keydown", event => {
    if (!opened) return;
    if (event.key === "Escape") {
      event.preventDefault();
      closeCase();
      return;
    }
    if (event.key === "Tab" && narrow.matches) {
      const focusable = Array.from(workspace.querySelectorAll("a[href], button, select, summary, [tabindex]"))
        .filter(element => element.tabIndex >= 0 && !element.closest("[hidden]") && element.getClientRects().length);
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault(); last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault(); first.focus();
      }
    }
  });
  window.addEventListener("hashchange", syncHash);
  window.addEventListener("popstate", syncHash);
  narrow.addEventListener("change", modality);

  const coverage = Array.from(document.querySelectorAll("[data-coverage-row]"));
  document.getElementById("coverage-search").addEventListener("input", event => {
    const query = event.target.value.trim().toLocaleLowerCase();
    let count = 0;
    coverage.forEach(row => {
      row.hidden = !row.dataset.search.includes(query);
      if (!row.hidden) count += 1;
    });
    document.getElementById("coverage-count").textContent = count + " of " + coverage.length + " modules";
    document.getElementById("coverage-empty").hidden = count !== 0;
  });

  const toc = Array.from(document.querySelectorAll(".proposal-toc nav:first-child a"));
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
      if (opened) return;
      const visible = entries.filter(entry => entry.isIntersecting);
      if (!visible.length) return;
      const current = visible[0].target.id;
      toc.forEach(link => {
        if (link.hash === "#" + current) link.setAttribute("aria-current", "true");
        else link.removeAttribute("aria-current");
      });
    }, { rootMargin: "-5% 0px -70% 0px" });
    toc.forEach(link => {
      const target = document.getElementById(link.hash.slice(1));
      if (target) observer.observe(target);
    });
  }
  document.documentElement.classList.add("js");
  syncHash();
})();
