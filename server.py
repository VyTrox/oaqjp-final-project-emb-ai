"""
Emotion Detector Server Module
This module contains the Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector_detail

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def run_emotion_detector():
    """
    Run the emotion detector and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector_detail(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!."

    return (
        "For the given statement, the system response is:\n"
        f"'anger': {response.get('anger')},\n"
        f"'disgust': {response.get('disgust')},\n"
        f"'fear': {response.get('fear')},\n"
        f"'joy': {response.get('joy')},\n"
        f"'sadness': {response.get('sadness')}.\n"
        f"The dominant emotion is {response.get('dominant_emotion')}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
