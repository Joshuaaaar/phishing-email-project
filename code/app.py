from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib



app = Flask(__name__)
CORS(app)


model = joblib.load("phishing_model.joblib")
vectorizer = joblib.load("vectorized.joblib")


@app.route("/predict",methods=["POST"])
def predict():
    
    try:
        data = request.get_json()
        email_text = data.get("text","")
        
        # Edge case
        if not email_text:
            return jsonify({"error": "No email text provided"}) , 400
        
        # Vectorize input
        email_vec = vectorizer.transform([email_text])
        
        #predict
        
        prediction = model.predict(email_vec)[0]
        
        confidence = (
            float(model.predict_proba(email_vec)[0].max())
            
            if hasattr(model,"predict_proba")
            else None
        )
        
        return jsonify({
            "label":prediction,
            "confidence":confidence
        })
    except Exception as e:
        return jsonify({"error":str(e)}),500

if __name__ == "__main__":
    app.run(port=8000,debug=True)
        
        