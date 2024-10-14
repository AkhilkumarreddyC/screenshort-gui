import unicodedata as name
import pyautogui
import time
import tkinter as tk

def screenshot():
    time.sleep(0.00000000001)
    name=time.time()
    name="C:/Users/akhil/Desktop/udemy courses/python projects/screenshot application/generated png photos/{}.png".format(name)
    img=pyautogui.screenshot()
    imgname=img.save(name)
    #img.show()

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame,text="Take screenshot",command=screenshot)
button.pack(side=tk.LEFT)

close=tk.Button(frame,text="quit",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()