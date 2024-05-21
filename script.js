async function generateImage() {
    const prompt = document.getElementById('prompt').value;
    const response = await fetch('/api/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: prompt })
    });
    const data = await response.json();
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = `<img src="${data.image_url}" alt="Generated Image">`;
}
