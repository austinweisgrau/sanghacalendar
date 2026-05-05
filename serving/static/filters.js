// Shared filter logic for calendar and map views.
// Each page must define: function onFilterChange() { ... }

const TRADITIONS = {
  "theravada": { label: "Theravada / Insight", color: "#3d7a56" },
  "zen":       { label: "Zen",                 color: "#4a5f82" },
  "tibetan":   { label: "Tibetan / Shambhala", color: "#7a6e28" },
  "secular":   { label: "Secular",             color: "#3a7070" },
  "pluralist": { label: "Non-sectarian",        color: "#5a6a5a" },
  "other":     { label: "Other",               color: "#888" },
  "unknown":   { label: "Other",               color: "#888" },
};

function localDateStr(offset) {
  const d = new Date();
  d.setDate(d.getDate() + offset);
  return d.toLocaleDateString("en-CA"); // "YYYY-MM-DD" in local time
}

// Close city dropdown on outside click
document.addEventListener("click", () => {
  const dd = document.getElementById("city-dropdown");
  if (dd) dd.classList.remove("open");
});

function toggleCityDropdown(e) {
  e.stopPropagation();
  document.getElementById("city-dropdown").classList.toggle("open");
}

function onCityChange() {
  const checked = Array.from(document.querySelectorAll("#city-dropdown input:checked")).map(el => el.value);
  const trigger = document.getElementById("city-trigger");
  if (checked.length === 0) {
    trigger.textContent = "All cities";
    trigger.classList.remove("active");
  } else {
    trigger.textContent = checked.join(", ");
    trigger.classList.add("active");
  }
  onFilterChange();
}

function onStateChange() {
  const state = document.getElementById("filter-state").value;
  document.querySelectorAll("#city-dropdown .multi-select-option").forEach(label => {
    const match = !state || label.dataset.state === state;
    label.style.display = match ? "" : "none";
    if (!match) label.querySelector("input").checked = false;
  });
  const trigger = document.getElementById("city-trigger");
  trigger.textContent = "All cities";
  trigger.classList.remove("active");
  onFilterChange();
}

function onDateWindowChange() {
  const window_val = document.getElementById("filter-date-window").value;
  const rangeRow   = document.getElementById("date-range-row");
  if (rangeRow) {
    if (window_val === "custom") {
      rangeRow.classList.add("visible");
    } else {
      rangeRow.classList.remove("visible");
      onFilterChange();
    }
  } else {
    onFilterChange();
  }
}

function buildFeedParams() {
  const cities        = Array.from(document.querySelectorAll("#city-dropdown input:checked")).map(el => el.value);
  const stateEl       = document.getElementById("filter-state");
  const state         = stateEl ? stateEl.value : "";
  const tradition     = document.getElementById("filter-tradition").value;
  const location_type = document.getElementById("filter-location").value;
  const window_val    = document.getElementById("filter-date-window").value;
  const startEl       = document.getElementById("filter-start-date");
  const endEl         = document.getElementById("filter-end-date");
  const start_date    = startEl ? startEl.value : "";
  const end_date      = endEl   ? endEl.value   : "";
  const params = new URLSearchParams();
  cities.forEach(c => params.append("city", c));
  if (state)         params.set("state", state);
  if (tradition)     params.set("tradition", tradition);
  if (location_type) params.set("location_type", location_type);
  if (window_val === "today") {
    const today = localDateStr(0);
    params.set("start_date", today + "T00:00:00");
    params.set("end_date",   today + "T23:59:59");
  } else if (window_val === "tomorrow") {
    const tmrw = localDateStr(1);
    params.set("start_date", tmrw + "T00:00:00");
    params.set("end_date",   tmrw + "T23:59:59");
  } else if (window_val === "custom") {
    if (start_date) params.set("start_date", start_date + "T00:00:00");
    if (end_date)   params.set("end_date",   end_date   + "T23:59:59");
  } else {
    params.set("days", window_val);
  }
  return params;
}

function initFiltersFromUrl() {
  const p = new URLSearchParams(window.location.search);
  const locEl = document.getElementById("filter-location");
  if (locEl && p.get("location_type")) locEl.value = p.get("location_type");
  const tradEl = document.getElementById("filter-tradition");
  if (tradEl && p.get("tradition")) tradEl.value = p.get("tradition");
  const stateEl = document.getElementById("filter-state");
  if (stateEl && p.get("state")) {
    stateEl.value = p.get("state");
    // Filter city options without triggering a reload
    const state = stateEl.value;
    document.querySelectorAll("#city-dropdown .multi-select-option").forEach(label => {
      label.style.display = (!state || label.dataset.state === state) ? "" : "none";
    });
  }
  const cities = p.getAll("city");
  if (cities.length) {
    cities.forEach(city => {
      const cb = document.querySelector(`#city-dropdown input[value="${CSS.escape(city)}"]`);
      if (cb) cb.checked = true;
    });
    const trigger = document.getElementById("city-trigger");
    if (trigger) {
      trigger.textContent = cities.join(", ");
      trigger.classList.add("active");
    }
  }
  const windowVal = p.get("window") || p.get("days");
  const windowEl = document.getElementById("filter-date-window");
  if (windowEl && windowVal) {
    windowEl.value = windowVal;
    if (windowVal === "custom") {
      const row = document.getElementById("date-range-row");
      if (row) row.classList.add("visible");
      const startEl = document.getElementById("filter-start-date");
      const endEl   = document.getElementById("filter-end-date");
      if (startEl && p.get("start_date")) startEl.value = p.get("start_date").slice(0, 10);
      if (endEl   && p.get("end_date"))   endEl.value   = p.get("end_date").slice(0, 10);
    }
  }
}
