import os

# TTS API
TTS_API_URL = os.getenv('TTS_API_URL')
TTS_API_KEY = os.getenv('TTS_API_KEY')

# STT API
STT_API_URL = "https://api.openai.com/v1/audio/transcriptions"
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Recordings folder
RECORDINGS_FOLDER = "recordings/"
