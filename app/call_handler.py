import json
import os
from app.tts_client import get_tts_audio
from app.stt_client import transcribe_audio
from app.utils import download_audio
from config import RECORDINGS_FOLDER
from app.tts_client import text_to_speech
from app.stt_client import speech_to_text
import datetime



def process_call(mobile_number):
    with open('questions/questions.json') as f:
        questions = json.load(f)

    transcriptions = []

    for idx, question in enumerate(questions):
        print(f"Asking Question {idx+1}: {question}")

        # Generate TTS
        audio_url = get_tts_audio(question)
        tts_audio_file = os.path.join(RECORDINGS_FOLDER, f"question_{idx+1}.wav")
        download_audio(audio_url, tts_audio_file)

        # Here you would STREAM audio in Asterisk - for now just placeholder
        print(f"[Simulating playing] {tts_audio_file}")

        # Placeholder: simulate recording candidate answer
        print(f"[Simulating recording answer_{idx+1}.wav]")
        answer_file = os.path.join(RECORDINGS_FOLDER, f"answer_{idx+1}.wav")
        # Asterisk would create this recording

        # Transcribe recorded audio
        transcription = transcribe_audio(answer_file)
        transcriptions.append({
            "question": question,
            "answer": transcription
        })
    
    return transcriptions
