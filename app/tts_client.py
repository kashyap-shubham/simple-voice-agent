import requests
from config import TTS_API_URL, TTS_API_KEY

def get_tts_audio(text):
    headers = {"Authorization": f"Bearer {TTS_API_KEY}"}
    payload = {"text": text}
    response = requests.post(TTS_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['audio_url']
    else:
        raise Exception(f"TTS Error: {response.text}")
