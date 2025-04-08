#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.call_handler import process_call

def main():
    transcriptions = process_call()
    print("Call completed. Collected responses:")
    for t in transcriptions:
        print(f"Q: {t['question']}")
        print(f"A: {t['answer']}")

if __name__ == "__main__":
    main()
