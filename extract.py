import json

response_text = '{"emotionPredictions":[{"emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":27, "text":"I love this new technology."}, "emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'

formatted_response = json.loads(response_text)

emotions = formatted_response['emotionPredictions'][0]['emotion']

print(formatted_response)
print("#" * 50)
print(emotions)
print("#" * 50)

max_emotion = max(emotions, key=emotions.get)
print(f"The dominant emotion is: {max_emotion} with a score of {emotions[max_emotion]}")

emotions["dominant_emotion"] = max_emotion

print(emotions)