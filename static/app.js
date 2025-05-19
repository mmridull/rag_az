
document.getElementById('qaForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData();
    const file = document.getElementById('fileInput').files[0];
    const question = document.getElementById('questionInput').value;
    formData.append("file", file);
    formData.append("question", question);

    const res = await fetch("/ask", {
        method: "POST",
        body: formData
    });
    const data = await res.json();
    document.getElementById('answer').textContent = data.answer;
});
