import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for command...")
        try:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=5)
            text = recognizer.recognize_google(audio).lower()
            print(f"Command: {text}")
            return text
        except:
            return None