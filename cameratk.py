import cv2
import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image

gui = tk.Tk()
gui.configure(background="light yellow")
gui.title("cameraTK")
gui.geometry("680x480")


#####################################################33
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open camera')
    exit()


frame = tk.Frame(gui, background='white')
frame.place(relheight=0.75,relwidth=0.75, relx=0.125,rely=0.125)

##################################################
def video_stream():
    _,frames = cap.read()
    # frames = cv2.resize(frames,(640,480))
    cv2image = cv2.cvtColor(frames, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1,video_stream)

lmain = tk.Label(frame)
lmain.grid()

################################################
def take_snapshot():
    ts = datetime.now()
    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
    #saving
    _,frames = cap.read()
    cv2.imwrite(filename=filename, img=frames)

snapbutton = tk.Button(gui,text='CAPTURE', command=take_snapshot)
snapbutton.place(relx=0.0625+0.375,rely=0.125+0.75)


video_stream()
gui.mainloop()