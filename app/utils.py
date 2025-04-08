import requests
import os

def download_audio(url, save_path):
    r = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(r.content)
