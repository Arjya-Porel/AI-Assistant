import tkinter as tk
from tkinter import scrolledtext
import threading
import time

from voice import listen_for_wake_word, listen_command
from speak import speak
from intent import detect_intent
from commands import execute

listening = True

window = tk.Tk()
window.title("Pluto Assistant")
window.geometry("450x600")

output = scrolledtext.ScrolledText(window, height=20)
output.pack(pady=10)

listening = True

def log(text):
    window.after(0, lambda: update_log(text))

def update_log(text):
    output.insert(tk.END, text + "\n")
    output.see(tk.END)


def assistant_loop():
    global listening

    while listening:
        text = listen_for_wake_word()

        if not listening:
            break   # <-- safe exit

        if "pluto" in text:
            log("Wake word detected ✔")
            speak("Yes?")

            command = listen_command()

            if command:
                intent, target = detect_intent(command)

                log("You: " + command)
                log(f"Intent: {intent}, Target: {target}")

                execute(intent, target, speak, log)

        time.sleep(0.5)


def start():
    threading.Thread(target=assistant_loop).start()


btn = tk.Button(window, text="Start Assistant", command=start)
btn.pack(pady=10)

window.mainloop()

def on_close():
    global listening
    listening = False
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)