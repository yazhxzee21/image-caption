AI-Based Image Captioning System

An AI-powered web application that generates descriptive captions for uploaded images using the BLIP image captioning model from Hugging Face Transformers.

🚀 Features
Upload images through a REST API
Automatic AI-generated image captions
Built using Flask and PyTorch
Uses BLIP pretrained model for image understanding
Docker support for containerized deployment
JSON-based API responses
🛠️ Tech Stack
Python
Flask
Hugging Face Transformers
PyTorch
Pillow
Docker
📂 Project Structure
project-folder/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2. Create Virtual Environment (Optional)
python -m venv venv

Activate the environment:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
▶️ Running the Application
python app.py

Server will start on:

http://localhost:5000
📤 API Endpoint
Upload Image

Endpoint

POST /upload

Request

Send an image file using form-data:

Key	Type
image	File
📥 Example Using cURL
curl -X POST -F "image=@sample.jpg" http://localhost:5000/upload
📄 Sample Response
{
  "caption": "a dog running through a field"
}
🐳 Docker Setup
Build Docker Image
docker build -t image-captioning-app .
Run Docker Container
docker run -p 5000:5000 image-captioning-app
🧠 Model Used

This project uses the pretrained:

BLIP Image Captioning Model
(Salesforce/blip-image-captioning-base)

from Hugging Face Transformers
