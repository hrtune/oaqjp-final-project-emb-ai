"""
This module is to deploy emotion detector application to web.
"""

from flask import Flask, request
from EmotionDetection import emotion_detection

app = Flask(__name__)
emotion_detector = emotion_detection.emotion_detector

def emotion_score_string(data):
    """
        Output string of emotion score
    """
    result = ""
    for emotion in data:
        if emotion == "dominant_emotion":
            continue

        result += f"'{emotion}': {data[emotion]}, "

    result = result.strip()
    result = result[:-1]

    return result


@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_route():
    """
        Route for emotion detector
    """
    data = request.json
    text = data.get('text')
    emotion_score = emotion_detector(text)
    dominant_emotion = emotion_score['dominant_emotion']

    if dominant_emotion is None:
        return "<strong>Invalid text! Please try again!</strong>", 400

    result = (
        "<p>For the given statement, the system response is "
        f"{emotion_score_string(emotion_score)}. The dominant emotion is "
        f"<strong>{dominant_emotion}</strong>.</p>"
    )

    return result
    