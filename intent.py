def detect_intent(command):
    command = command.lower()

    open_keywords = ["open", "launch", "start", "run", "please open", "can you open"]

    apps = {
        "youtube": ["youtube"],
        "google": ["google"],
        "chrome": ["chrome"],
        "notepad": ["notepad"],
        "calculator": ["calc", "calculator", "calcu"],
        "cmd": ["cmd", "command prompt", "cmd prompt"]
    }

    for word in open_keywords:
        if word in command:
            for app, aliases in apps.items():
                for alias in aliases:
                    if alias in command:
                        return ("open", app)

    if "shutdown" in command:
        return ("shutdown", None)

    return (None, None)