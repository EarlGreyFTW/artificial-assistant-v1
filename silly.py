import datetime, colorama, pyttsx3
foreground = colorama.Fore
tts = pyttsx3.init()


def fourtwo():
    print(foreground.LIGHTMAGENTA_EX + "42")
    tts.say("42")
    tts.runAndWait()
