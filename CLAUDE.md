# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the application:**
```bash
python3 server.py
```
Flask starts on `http://0.0.0.0:5000`

**Run tests:**
```bash
python3 test_emotion_detection.py
```

**Install dependencies (no requirements.txt — install manually):**
```bash
pip install flask requests
```

## Architecture

This is a Flask web app that detects emotions in text by calling an external IBM Watson NLP API.

**Request flow:**
1. Browser submits text via `static/mywebscript.js` (`RunSentimentAnalysis()`) to `GET /emotionDetector?textToAnalyze=...`
2. `server.py` calls `emotion_detector()` from the `EmotionDetection` package
3. `EmotionDetection/emotion_detection.py` POSTs to the Watson API at `https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict` with header `grpc-metadata-mm-model-id: emotion_aggregated-workflow_lang_en_stock`
4. Returns a dict with scores for `anger`, `disgust`, `fear`, `joy`, `sadness`, and a computed `dominant_emotion` key

**Key files:**
- `server.py` — Flask routes (`/` and `/emotionDetector`)
- `EmotionDetection/emotion_detection.py` — core `emotion_detector(text)` function
- `test_emotion_detection.py` — unittest tests covering all 5 emotion types
