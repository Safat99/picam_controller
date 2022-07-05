import cv2
import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image
import threading
import time

gui = tk.Tk()
gui.configure(background="light yellow")
gui.title("cameraTK")
gui.geometry("680x480")
panel = None

#####################################################33
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open camera')
    exit()


frame = tk.Frame(gui, background='white')
frame.place(relheight=0.75,relwidth=0.75, relx=0.125,rely=0.125)
##################################################
def video_stream():
    global panel
    try:
        while not stopEvent.is_set():
            _,frames = cap.read()
            # frames = cv2.resize(frames,(640,480))
            cv2image = cv2.cvtColor(frames, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)##converts PIL image from cv2 image(numpy array)
            imgtk = ImageTk.PhotoImage(image=img)
            ###updates the image panel by the config
            if panel is None:
                panel = tk.Label(frame)
                panel.imgtk = imgtk
                panel.pack()
            else:
                panel.configure(image=imgtk)
                panel.imgtk = imgtk
                panel.pack()
            # time.sleep(0.001)
    # lmain.after(1,video_stream)# built in after function( 1 miliseceond pore abar vide_stream func call hobe)
    except RuntimeError:
        print("caught a runtime error")

# lmain = tk.Label(image)
# lmain.pack()
##########################################3

stopEvent = threading.Event()
thread = threading.Thread(target=video_stream,args=())
thread.start()

################################################
def take_snapshot():
    ts = datetime.now()
    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
    #saving
    _,frames = cap.read()
    cv2.imwrite(filename=filename, img=frames)
    print("[INFO] saved {}".format(filename))

snapbutton = tk.Button(gui,text='CAPTURE', command=take_snapshot)
snapbutton.place(relx=0.0625+0.375,rely=0.125+0.75)

#############
def onClose():
    print("closing...")
    stopEvent.set()
    gui.quit()


# video_stream()
gui.protocol("WM_DELETE_WINDOW", onClose)
gui.mainloop()