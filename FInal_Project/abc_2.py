import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import tkinter as tk
from itertools import count
import string
import threading

class ImageLabel(tk.Label):
    """A label that displays images and plays them if they are GIFs."""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(len(self.frames))  # Move to the next frame
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100  # Default delay if duration is not available

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def display_gif(text):
    root = tk.Toplevel()  # Use Toplevel to avoid conflicting with the main Tkinter loop
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load(r'ISL_Gifs/{0}.gif'.format(text.lower()))
    root.mainloop()

def func(text):
    isl_gif = [
        'any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
        'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
        'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
        'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
        'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing',
        'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
        'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
        'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
        'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
        'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
        'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
        'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
        'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'agra', 'ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
        'bihar', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile', 'dasara',
        'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
        'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
        'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
        'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
        'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'tuesday', 'usa', 'village',
        'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number', 'what are you doing', 'are you busy'
    ]

    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    try:
        a = text
        a = a.lower()
        print('You Said: ' + a.lower())

        for c in string.punctuation:
            a = a.replace(c, "")

        if a.lower() in isl_gif:
            threading.Thread(target=display_gif, args=(a,)).start()
        else:
            for i in range(len(a)):
                if a[i] in arr:
                    ImageAddress = 'letters/' + a[i] + '.jpg'
                    ImageItself = Image.open(ImageAddress)
                    ImageNumpyFormat = np.asarray(ImageItself)
                    plt.imshow(ImageNumpyFormat)
                    plt.draw()
                    plt.pause(0.8)
                else:
                    continue
    except Exception as e:
        print("Error:", e)
    plt.close()

def text_to_sign_language(p, sign_type="ISL"):
    """Handles Text-to-Sign Language Conversion."""
    text = p[1:]
    if text:
        func(text)