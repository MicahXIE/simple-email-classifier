from flask import Blueprint, request, jsonify, render_template
from .model import classify_email
from .utils import preprocess_email

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    if not data or 'email_content' not in data:
        return jsonify({"error": "Invalid input, 'email_content' is required"}), 400

    email_content = data['email_content']
    preprocessed_content = preprocess_email(email_content)
    classification = classify_email(preprocessed_content)
    classificationStr = "SPAM" if classification == 1 else "NOT SPAM"
    return jsonify({"classification": classificationStr})