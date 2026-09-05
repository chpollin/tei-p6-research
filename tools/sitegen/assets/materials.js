const search = document.querySelector("#search");
const statusFilter = document.querySelector("#status-filter");
const materialFilter = document.querySelector("#material-filter");
const rows = [...document.querySelectorAll("[data-source-row]")];
const tableBody = document.querySelector("#source-body");
const resultCount = document.querySelector("#result-count");
const empty = document.querySelector("#empty");
const repositoryBase = document.querySelector('meta[name="repository-base"]')?.content;
let sortKey = "title";
let sortDirection = "asc";

if (repositoryBase) {
  document.querySelectorAll("[data-repo-path]").forEach((link) => {
    link.href = new URL(link.dataset.repoPath, repositoryBase).href;
  });
  document.querySelectorAll("[data-project-link]").forEach((link) => {
    link.href = "project.html";
  });
}

function closeDetails(row) {
  const detail = document.querySelector(`#${row.dataset.detailId}`);
  const button = row.querySelector(".expand");
  if (detail) detail.hidden = true;
  if (button) button.setAttribute("aria-expanded", "false");
}

function compareRows(left, right) {
  let comparison = 0;
  if (sortKey === "status") {
    comparison = Number(left.dataset.statusRank) - Number(right.dataset.statusRank);
  } else if (sortKey === "date") {
    comparison = left.dataset.date.localeCompare(right.dataset.date);
  } else if (sortKey === "materials") {
    comparison = left.dataset.materials.localeCompare(right.dataset.materials, "en");
  } else {
    comparison = left.dataset.title.localeCompare(right.dataset.title, "en");
  }
  return sortDirection === "asc" ? comparison : -comparison;
}

function updateSortHeaders() {
  document.querySelectorAll("[data-sort-header]").forEach((header) => {
    const active = header.dataset.sortHeader === sortKey;
    header.setAttribute("aria-sort", active ? (sortDirection === "asc" ? "ascending" : "descending") : "none");
    const mark = header.querySelector(".sort-mark");
    if (mark) mark.textContent = active ? (sortDirection === "asc" ? "↑" : "↓") : "";
  });
}

function applyView() {
  const query = search.value.trim().toLowerCase();
  const selectedStatus = statusFilter.value;
  const selectedMaterial = materialFilter.value;
  let visible = 0;
  rows.forEach((row) => {
    const statusMatches = selectedStatus === "all" || row.dataset.status === selectedStatus;
    const materialMatches = selectedMaterial === "all" || row.dataset.materials.split("|").includes(selectedMaterial);
    const searchMatches = !query || row.dataset.search.includes(query);
    const show = statusMatches && materialMatches && searchMatches;
    row.hidden = !show;
    const detail = document.querySelector(`#${row.dataset.detailId}`);
    if (!show) closeDetails(row);
    if (detail && row.hidden) detail.hidden = true;
    if (show) visible += 1;
  });
  [...rows].sort(compareRows).forEach((row) => {
    const detail = document.querySelector(`#${row.dataset.detailId}`);
    tableBody.append(row);
    if (detail) tableBody.append(detail);
  });
  resultCount.textContent = visible;
  empty.style.display = visible ? "none" : "block";
  updateSortHeaders();
}

document.querySelectorAll(".sort-button").forEach((button) => {
  button.addEventListener("click", () => {
    const nextKey = button.dataset.sort;
    if (sortKey === nextKey) {
      sortDirection = sortDirection === "asc" ? "desc" : "asc";
    } else {
      sortKey = nextKey;
      sortDirection = nextKey === "date" ? "desc" : "asc";
    }
    applyView();
  });
});

document.querySelectorAll(".expand").forEach((button) => {
  button.addEventListener("click", () => {
    const row = button.closest("[data-source-row]");
    const detail = document.querySelector(`#${row.dataset.detailId}`);
    const willOpen = button.getAttribute("aria-expanded") !== "true";
    button.setAttribute("aria-expanded", String(willOpen));
    detail.hidden = !willOpen;
  });
});

search.addEventListener("input", applyView);
statusFilter.addEventListener("change", applyView);
materialFilter.addEventListener("change", applyView);
applyView();
