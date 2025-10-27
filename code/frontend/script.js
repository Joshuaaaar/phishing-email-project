// script.js
const btn = document.getElementById("check_btn");
const textarea = document.getElementById("email_input");
const result = document.getElementById("result");

btn.addEventListener("click", async () => {
  const text = textarea.value.trim();
  if (!text) {
    result.textContent = "Please paste an email first.";
    return;
  }

  result.textContent = "Checking...";

  try {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await res.json();

    if (!res.ok) {
      result.textContent = "Error: " + (data.error || "Request failed");
      return;
    }

    const confidence = typeof data.confidence === "number"
      ? ` (Confidence: ${(data.confidence * 100).toFixed(2)}%)`
      : "";

    result.textContent = `Prediction: ${data.label}${confidence}`;
  } catch (e) {
    result.textContent = "Could not reach the server.";
    console.error(e);
  }
});