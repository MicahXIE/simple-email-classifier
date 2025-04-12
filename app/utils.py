import re

def preprocess_email(content):
    # Example preprocessing: remove special characters, convert to lowercase
    content = re.sub(r'\W+', ' ', content)
    return content.lower()