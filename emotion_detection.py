from flask import Flask
import requests


def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT = {"raw_document": {"text": text_to_analyze}}

    res = requests.post(url=URL, headers=HEADERS, data=INPUT)

    print(res.status_code)

    return res.json()["text"]
