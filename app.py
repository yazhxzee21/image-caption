from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from transformers import BlipProcessor, BlipForConditionalGeneration

app = Flask(__name__)

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    try:
        img = Image.open(BytesIO(file.read())).convert('RGB')
    except Exception:
        return jsonify({'error': 'Invalid image'}), 400

    inputs = processor(img, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return jsonify({'caption': caption})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
