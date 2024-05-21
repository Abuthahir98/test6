from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']
    
    # Call the DALL-E Mini API or your custom model here
    # Example using a hypothetical API endpoint:
    response = requests.post("http://dalle-mini-api/generate", json={"prompt": prompt})
    image_url = response.json().get('image_url')
    
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
