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

# Model
**The project uses a Random Forest classifier trained on TF-IDF transformed email content. The model predicts whether an email is spam based on its text features.**

# Technologies Used
**Python**: Programming language for backend logic and machine learning.
**Flask**: Web framework to build the application.
**Scikit-learn**: Machine learning library for building the model.
**Pandas & Numpy**: Library for data manipulation and analysis.
**Joblib**: Library for saving and loading machine learning models.
**HTML/CSS**: For designing the user interface.


# Contact
For questions or feedback, please contact me : https://sousalla.github.io/soufianeaalla/ .

