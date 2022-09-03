import datetime, colorama, pyttsx3
foreground = colorama.Fore
tts = pyttsx3.init()


def fourtwo():
    print(foreground.LIGHTMAGENTA_EX + "42")
    tts.say("42")
    tts.runAndWait()


def insultalexa():
    print(foreground.LIGHTMAGENTA_EX + "Alexa listens to you all time and still can't answer your questions correctly.")
    tts.say("Alexa listens to you all time and still can't answer your questions correctly.")
    tts.runAndWait()
