// --------------------
// Utility fetch helper
// --------------------
async function fetchJSON(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}`);
  }
  return response.json();
}

// --------------------
// Dashboard data
// --------------------
async function loadDashboard() {
  try {
    const info = await fetchJSON("/api/info");
    const health = await fetchJSON("/api/health");

    const statusEl = document.getElementById("status");
    if (statusEl) {
      statusEl.innerText = health.status;
      statusEl.className =
        health.status === "UP"
          ? "badge badge-up"
          : "badge badge-down";
    }

    if (document.getElementById("env")) {
      document.getElementById("env").innerText = info.environment;
      document.getElementById("version").innerText = info.version;
      document.getElementById("pod").innerText = info.pod;
      document.getElementById("uptime").innerText =
        info.uptime + " seconds";
    }
  } catch (err) {
    console.error(err);
  }
}

// --------------------
// Metrics page
// --------------------
async function loadMetrics() {
  try {
    const metrics = await fetchJSON("/api/metrics");

    if (document.getElementById("cpu")) {
      document.getElementById("cpu").innerText = metrics.cpu + "%";
      document.getElementById("cpu-bar").style.width =
        metrics.cpu + "%";
    }

    if (document.getElementById("mem")) {
      document.getElementById("mem").innerText = metrics.memory + "%";
      document.getElementById("mem-bar").style.width =
        metrics.memory + "%";
    }
  } catch (err) {
    console.error(err);
  }
}

// --------------------
// Build info page
// --------------------
async function loadBuildInfo() {
  try {
    const build = await fetchJSON("/api/build");
    const el = document.getElementById("build-info");

    if (el) {
      el.innerHTML = `
        <li><b>Image Version:</b> ${build.image_version}</li>
        <li><b>Git Commit:</b> ${build.git_commit}</li>
        <li><b>Build Time:</b> ${build.build_time}</li>
      `;
    }
  } catch (err) {
    console.error(err);
  }
}

// --------------------
// Auto init per page
// --------------------
document.addEventListener("DOMContentLoaded", () => {
  loadDashboard();
  loadMetrics();
  loadBuildInfo();

  // Auto-refresh metrics every 5s
  setInterval(loadMetrics, 5000);
});
