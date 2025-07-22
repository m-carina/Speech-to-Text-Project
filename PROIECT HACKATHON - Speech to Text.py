import speech_recognition as sr

language_reg = input("Choose language recognition: Type RO for Romanian or press Enter for English: ")
duration = int(input("Set duration of speech recording (in seconds) = "))

# initializing the recognizer
r = sr.Recognizer()
print("Please talk")

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=duration)
    print("Recognizing...")
    # convert speech to text
    try:

        if language_reg=="RO":
            text = r.recognize_google(audio_data, language = "ro-RO")
            print(text)
        else:
            text = r.recognize_google(audio_data)
            print(text)

    except sr.UnknownValueError:

        print("Sorry, I could not understand the audio.")

    except sr.RequestError as e:

        print(f"Could not request results; {e}")
