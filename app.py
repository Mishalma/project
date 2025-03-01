from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask app
application = Flask(__name__)
app = application


# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')


# Route for prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Create CustomData object from form data
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),  # Match with form field name
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),  # Fixed mapping
                writing_score=float(request.form.get('writing_score'))  # Fixed mapping
            )

            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            print("Input DataFrame:\n", pred_df)  # Debugging

            # Initialize prediction pipeline
            predict_pipeline = PredictPipeline()
            print("Before Prediction")

            # Make prediction
            results = predict_pipeline.predict(pred_df)
            print("Prediction Result:", results)

            # Render the home page with the result
            return render_template('home.html', results=float(results[0]))  # Convert to float for template

        except Exception as e:
            # Handle errors gracefully
            error_message = f"An error occurred: {str(e)}"
            print(error_message)  # Log to console
            return render_template('home.html', error=error_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)  # Added debug=True for development