from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('models/spam_classifier.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('classify.html')

@app.route('/classify', methods=['POST'])
def classify():
    email = request.form['email']
    print(f"Email received: {email}")  # Debugging
    email_transformed = vectorizer.transform([email])
    prediction = model.predict(email_transformed)[0]
    print(f"Prediction: {prediction}")  # Debugging
    prediction_text = "Spam" if prediction == 1 else "Not Spam"
    return render_template('result.html', prediction=prediction_text, email=email)

if __name__ == "__main__":
    app.run(debug=True)
