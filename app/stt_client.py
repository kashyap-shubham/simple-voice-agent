import requests
from config import STT_API_URL, OPENAI_API_KEY

def transcribe_audio(audio_path):
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    files = {"file": open(audio_path, "rb")}
    data = {"model": "whisper-1"}
    response = requests.post(STT_API_URL, headers=headers, files=files, data=data)
    if response.status_code == 200:
        return response.json()['text']
    else:
        raise Exception(f"STT Error: {response.text}")
