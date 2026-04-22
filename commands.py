import os
import webbrowser


def announce(action, speak, log):
    speak(f"Opening {action}")
    log(f"Opening {action}")


def execute(intent, target, speak, log):

    if intent == "open":

        if target == "youtube":
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif target == "google":
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif target == "chrome":
            os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
            speak("Opening Chrome")

        elif target == "notepad":
            os.system("notepad")
            speak("Opening Notepad")

        elif target == "calculator":
            os.system("calc")
            speak("Opening Calculator")

        elif target == "cmd":
            os.system("start cmd")
            speak("Opening Command Prompt")

        else:
            speak("I cannot open that application")
            log("Unknown app: " + str(target))

    elif intent == "shutdown":
        speak("Shutting down system")
        os.system("shutdown /s /t 5")

    else:
        speak("Command not understood")