# Smart Urban Hotline — AI Agent for Real-Time City Risk Alerts

## Overview
Smart Urban Hotline is an AI-powered incident detection and alerting system built with:
- Google ADK (Agent Developer Kit)
- Gemini / Gemma models (LLM reasoning)
- Cloud Run (GPU-ready) for inference
- FastAPI for the API layer

This repo contains a phone-friendly prototype you can deploy using Google Cloud Shell.

## Repo structure
See the repository root for `Dockerfile`, `requirements.txt`, `main.py`, and `agent.yaml`.
The `agents/` folder contains modular agent code. `sample_dataset/` contains small sample files.

## Quick start (phone-friendly)
1. Open Google Cloud Console → Cloud Shell (or use any terminal with gcloud).
2. Upload/extract this repo into Cloud Shell workspace.
3. Build and push container:
   ```
   gcloud builds submit --tag gcr.io/$PROJECT_ID/urban-hotline
   ```
4. Deploy to Cloud Run (GPU optional):
   ```
   gcloud run deploy urban-hotline \
     --image gcr.io/$PROJECT_ID/urban-hotline \
     --region=us-central1 --platform=managed --allow-unauthenticated
   ```
5. Test:
   ```
   curl "https://YOUR_SERVICE_URL/urban_hotline?location=Velachery"
   ```
