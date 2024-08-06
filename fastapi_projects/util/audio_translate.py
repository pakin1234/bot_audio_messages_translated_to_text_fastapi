import speech_recognition as sr

r = sr.Recognizer()


def converting_to_text(audio_name_orig: str):
    # audio_name = input("Enter text name: ")

    audio_file = sr.AudioFile(audio_name_orig)

    with audio_file as source:
        audio_data = r.record(source)

    try:
        # print("Google Recognition: " + r.recognize_google(audio_data))
        text = r.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))




# print(text) audio_2024-07-27_12-35-17.wav

