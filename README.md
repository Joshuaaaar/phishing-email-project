# Phishing Email Detector

A machine learning powered web application that detects phishing emails using Natural Language Processing and Logistic Regression. The system exposes a Flask API for real time predictions and includes a simple JavaScript frontend for user interaction.

## Overview

This project classifies emails as Phishing Email or Safe Email using TF IDF text features and a supervised Logistic Regression model. It is implemented as an end to end machine learning pipeline including data preprocessing model training model persistence API deployment and frontend integration.

## Key Highlights

- Trained on a dataset of 15K+ labeled emails
- TF IDF vectorization with English stop word removal
- Logistic Regression optimized using GridSearchCV
- Flask REST API with JSON based inference
- JavaScript frontend using the Fetch API
- Confidence scores returned using predict_proba

## Tech Stack

### Backend and Machine Learning
- Python
- Flask
- scikit learn
- pandas
- joblib

### Frontend
- HTML
- CSS
- JavaScript Fetch API

## Project Structure

.
├── frontend/
│   └── script.js
├── app.py
├── dataSet.py
├── model.py
├── phishing_model.joblib
├── vectorized.joblib
├── placeholder.txt
└── README.md

## Machine Learning Pipeline

### Data Loading
- Emails loaded from a CSV dataset
- Missing values handled using empty string replacement

### Feature Engineering
- TF IDF vectorization
- English stop words removed

### Model Training
- Logistic Regression classifier
- Hyperparameter tuning using GridSearchCV
- Stratified 5 fold cross validation
- Optimization metric F1 score for the phishing class

### Evaluation
- Accuracy score
- Confusion matrix
- Classification report

### Model Persistence
- Best performing model saved using joblib
- TF IDF vectorizer saved for consistent inference

## API Usage

### Start the Flask Server

```bash
python app.py
```

The server runs on

http://127.0.0.1:8000

### Prediction Endpoint

POST /predict

#### Request body

```json
{
  "text": "Your email content here"
}
```

#### Response body

```json
{
  "label": "Phishing Email",
  "confidence": 0.92
}
```

### Error Handling

- Returns 400 if no email text is provided
- Returns 500 for unexpected server errors

## Frontend Usage

1. Open the frontend HTML file in your browser
2. Paste an email into the text box
3. Click Check
4. The prediction and confidence score are displayed in real time

The frontend communicates with the Flask backend using the Fetch API.

## Example Output

Prediction Phishing Email Confidence 91.87 percent

## How to Retrain the Model

1. Update or replace the dataset CSV
2. Run

```bash
python model.py
```

This generates
- phishing_model.joblib
- vectorized.joblib

Restart the Flask server to use the new model

## Future Improvements

- Deploy backend using Docker or a cloud service
- Add authentication and rate limiting
- Improve model performance using n grams or transformer based embeddings
- Add UI confidence visualization
- Support batch email classification

## Demo

A demo link is included in the repository under

link to project demo.txt

## Author

Joshua Ramnauth  
Machine Learning and Software Engineering  
University of Toronto
