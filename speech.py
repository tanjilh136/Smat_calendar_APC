import speech_recognition as sr

def recognize():
    """
    Function for Speech Recognition
    :return:
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand"
    except sr.RequestError as e:
        return "Service Interrupted"

