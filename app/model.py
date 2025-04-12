import joblib

# Load the pre-trained model and vectorizer
model = joblib.load('models/email_classifier_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def classify_email(content):
    transformed_content = vectorizer.transform([content])
    return model.predict(transformed_content)[0]