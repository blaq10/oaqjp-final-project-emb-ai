import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    json_obj = json.loads(response.text)

    nose = json_obj
    dom_emo = "anger"

    if response.status_code == 200:
        editted_json = json_obj["emotionPredictions"][0]["emotion"]
        dominant = {"dominant_emotion": editted_json["anger"]}

        for emotion in editted_json.keys():        
            if editted_json[emotion] > dominant["dominant_emotion"]:
                dominant["dominant_emotion"] = editted_json[emotion]
                dom_emo = emotion

        dominant["dominant_emotion"] = dom_emo
        editted_json.update(dominant)
        nose = editted_json

    elif response.status_code == 400:
        nose = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
    
    return nose