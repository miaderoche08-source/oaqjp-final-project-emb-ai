import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # POST request
    response = requests.post(url, json=myobj, headers=headers)
    
    return response.text