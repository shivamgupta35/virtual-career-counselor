/* ---------------- LOADER ---------------- */
function showLoader() {
  document.getElementById("loader").classList.remove("hidden");
}

function hideLoader() {
  document.getElementById("loader").classList.add("hidden");
}

/* ---------------- API CALL ---------------- */
async function postData(url, payload) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  const data = await res.json();
  return data.result || "No data available";
}

/* ---------------- AI TEXT FORMATTER ---------------- */
function formatAIText(raw) {
  if (!raw) return "";

  // Remove markdown stars
  let text = raw.replace(/\*\*/g, "").replace(/\*/g, "");

  const lines = text
    .split("\n")
    .map(l => l.trim())
    .filter(Boolean);

  let html = "";
  let inList = false;

  lines.forEach(line => {
    // Headings
    if (
      line.endsWith(":") ||
      line.toLowerCase().includes("skills") ||
      line.toLowerCase().includes("salary") ||
      line.toLowerCase().includes("demand") ||
      line.toLowerCase().includes("career") ||
      line.toLowerCase().includes("outlook")
    ) {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
      html += `<h3>${line}</h3>`;
    }

    // Bullet points
    else if (line.startsWith("-") || /^\d+\./.test(line)) {
      if (!inList) {
        html += "<ul>";
        inList = true;
      }
      html += `<li>${line.replace(/^[-\d\.]+/, "").trim()}</li>`;
    }

    // Normal paragraph
    else {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
      html += `<p>${line}</p>`;
    }
  });

  if (inList) html += "</ul>";

  return html;
}

/* ---------------- MAIN EXPLORE FUNCTION ---------------- */
async function exploreAll() {
  const career = document.getElementById("career").value.trim();
  if (!career) {
    alert("Please enter a career");
    return;
  }

  const careerBox = document.getElementById("outputText");
  const coursesBox = document.getElementById("coursesText");
  const marketBox = document.getElementById("marketText");

  careerBox.classList.remove("hidden");
  coursesBox.classList.remove("hidden");
  marketBox.classList.remove("hidden");

  careerBox.innerHTML = "";
  coursesBox.innerHTML = "";
  marketBox.innerHTML = "";

  showLoader();

  try {
    const [careerRes, courseRes, marketRes] = await Promise.all([
      postData("/generate_career_path", { career }),
      postData("/generate_courses", { career }),
      postData("/job_market_insights", { career })
    ]);

    careerBox.innerHTML = formatAIText(careerRes);
    coursesBox.innerHTML = formatAIText(courseRes);
    marketBox.innerHTML = formatAIText(marketRes);

  } catch (err) {
    careerBox.innerHTML = "<p>Error loading career path</p>";
    coursesBox.innerHTML = "<p>Error loading courses</p>";
    marketBox.innerHTML = "<p>Error loading job market data</p>";
  }

  hideLoader();
}

/* ---------------- EXPOSE FUNCTION ---------------- */
window.exploreAll = exploreAll;
