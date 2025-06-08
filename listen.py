import speech_recognition as sr
from playsound import playsound

def listen_and_scream():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening... Say something!")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # adjust for background noise

    while True:
        with mic as source:
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")

            if "job" in text:
                print("Keyword detected! SCREAMING!")
                playsound('static/no.mp3')

        except sr.UnknownValueError:
            print("Couldn't understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    listen_and_scream()
