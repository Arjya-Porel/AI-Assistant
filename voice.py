import speech_recognition as sr

# Create ONE recognizer instance (important for performance)
r = sr.Recognizer()

# Reduce unnecessary delay from ambient noise calibration
AMBIENT_DURATION = 0.3


def listen_for_wake_word():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=AMBIENT_DURATION)

            audio = r.listen(
                source,
                timeout=3,
                phrase_time_limit=3
            )

        text = r.recognize_google(audio, language="en-IN")
        return text.lower()

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""

    except Exception:
        return ""


def listen_command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=AMBIENT_DURATION)

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        text = r.recognize_google(audio, language="en-IN")
        return text.lower()

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""

    except Exception:
        return ""