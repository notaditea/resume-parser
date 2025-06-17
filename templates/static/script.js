function uploadResume() {
  const fileInput = document.getElementById("resume");
  const formData = new FormData();
  formData.append("resume", fileInput.files[0]);

  fetch("/upload", {
    method: "POST",
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("name").value = data.name || "";
    document.getElementById("email").value = data.email || "";
    document.getElementById("phone").value = data.phone || "";
  })
  .catch(error => console.error("Error:", error));
}
