# Email-spam-classification
The spam classification model uses Machine Learning to analyze email content and predict whether it is spam or not. The model is trained on a dataset containing labeled examples of spam and non-spam emails.



# About Dataset
The original dataset can be found here : https://www.kaggle.com/datasets/abdallahwagih/spam-emails

## Project Structure
- **app.py**: The main Flask application file that handles routes and logic for classification.
- **templates/**: Contains HTML templates for the web interface.
  - **classify.html**: The form where users can input email content for classification.
  - **result.html**: Displays the classification result.
- **models/**: Contains the trained machine learning model and vectorizer.
  - **spam_classifier.pkl**: The trained Random Forest model for spam classification.
  - **tfidf_vectorizer.pkl**: The TF-IDF vectorizer for transforming email content.
- **spam_classification_project.ipynb**: Jupyter Notebook used for training the model and performing data analysis.
- **spam.csv**: Dataset used for training the spam classifier.

