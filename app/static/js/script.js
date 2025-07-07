function sendSelectedSkill() {
  const dropdown = document.getElementById("skill-dropdown");
  const selectedSkill = dropdown.value.trim();
  if (!selectedSkill) return;

  addMessage("You", selectedSkill);

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: selectedSkill })
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        addMessage("Bot", "Oops! Something went wrong.");
      } else {
        const reply = `
          <strong>Recommended Career:</strong> ${data.career}<br>
          <strong>Description:</strong> ${data.description}<br>
          <strong>Skills:</strong> ${data.skills.join(", ")}<br>
          <strong>Resources:</strong><br>
          <ul>${data.resources.map(link => `<li><a href="${link}" target="_blank">${link}</a></li>`).join("")}</ul>
        `;
        addMessage("Bot", reply);
      }
    })
    .catch(error => {
      console.error("Error:", error);
      addMessage("Bot", "Oops! Something went wrong.");
    });
}

function addMessage(sender, text) {
  const chatBox = document.getElementById("chat-box");
  const messageDiv = document.createElement("div");
  messageDiv.className = "chat-message";

  const senderSpan = document.createElement("span");
  senderSpan.className = "sender";
  senderSpan.innerText = `${sender}: `;

  const textSpan = document.createElement("span");
  textSpan.className = "text";
  textSpan.innerHTML = text;

  messageDiv.appendChild(senderSpan);
  messageDiv.appendChild(textSpan);
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
