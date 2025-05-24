import requests
import json


def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT = {"raw_document": {"text": text_to_analyze}}

    res = requests.post(url=URL, headers=HEADERS, json=INPUT)

    if res.status_code == 400:
        return {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion":None
                }
    
    emotion_score = json.loads(res.text)

    emotion_score = emotion_score["emotionPredictions"][0]["emotion"]

    emotion_score = {key: float(value) for key, value in emotion_score.items()}

    dominant_emotion = max(emotion_score, key=emotion_score.get)

    emotion_score["dominant_emotion"] = dominant_emotion

    return emotion_score
  
        
