from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
#from pygame import mixer

root = Tk()
root.geometry("600x700+400+80")
root.resizable(False, False)
root.title("Voice recorder")
root.config(bg="#4a4a4a")

#mixer.init()

def Record():
    freq = 44100  # Sampling frequency
    try:
        dur = int(duration.get())  # Get duration from the input field
        if dur <= 0:
            raise ValueError("Duration should be a positive number.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid duration.")
        return
    
    recording = sound.rec(dur * freq, samplerate=freq, channels=2)  # Fix the typo here (channels instead of channel)

    # Timer
    temp = dur
    while temp > 0:
        root.update()
        time.sleep(1)
        temp -= 1

        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's Up")
        Label(text=f"{str(temp)}",font="arial 20",width=4,bg="#4a4a4a").place(x=240,y=530)

    sound.wait()
    write("recording.wav", freq, recording)
    messagebox.showinfo("Recording", "Recording saved successfully as 'recording.wav'.")

# Icon
icon_image = PhotoImage(file="logo3.png")
root.iconphoto(False, icon_image)

# Logo
photo = PhotoImage(file="logo3.png")
myimage = Label(image=photo, bg="#4a4a4a", bd=0).pack(padx=5, pady=5)

Label(text="Voice Recorder", font="arial 20 bold", bg="#4a4a4a", fg="white").pack()

# Entry
duration = StringVar()
entry = Entry(root, textvariable=duration, font="arial 20", width=15).pack(pady=10)
Label(text="Enter time in seconds", font="arial 12", bg="#4a4a4a", fg="white").pack()

# Record Button
record = Button(root, font="arial 15", text="Start Recording", fg="white", bg="#111111", border=0, command=Record).pack(pady=30)
#Button(root,font="arial 15", text="Pause", fg="white", bg="#111111", border=0,command=mixer.music.pause).pack(pady=30)

root.mainloop()
