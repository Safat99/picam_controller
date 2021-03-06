import tkinter as tk
from tkinter import Y, Label, messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
import actions
from datetime import datetime
import threading


# messagebox.showinfo("hello","welcome to picam controller")
gui = tk.Tk()
gui.configure(background="light grey")
gui.title("picam controller")
gui.geometry("800x600")
panel = None

frame = tk.Frame(gui, background='white')
frame.place(relheight=0.4, relwidth=0.7, relx=0.15, rely=0)
# frame.pack()
#####################################################33
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open camera')
    exit()

########################################################################
IR_isON = False
def ir_toggle():
    global IR_isON 
    if IR_isON == True: ## button is pressed
        button1.config(text='IR OFF')
        IR_isON = False
        actions.ir_off()
    else:
        button1.config(text="IR ON")
        IR_isON = True
        actions.ir_on()
button1 = tk.Button(frame, text='IR OFF', fg='white', bg='black', command=ir_toggle)
button1.place(relx=0.1,rely=0.2, relwidth=0.125)


#################################<< brightness slider  >> ####################################
current_value = tk.DoubleVar()
def get_current_value():
    return '{:.1f}'.format(current_value.get())

value_label = ttk.Label(frame, text=get_current_value(), background='white')
value_label.place(relx=0.5, rely=0.15)

def slider_changed(event):
    value_label.configure(text=get_current_value())
    # print(brightness_slider.get()) ##for getting the value
    brightness = int(brightness_slider.get()*15//100) ## set_gain limitaions
    if brightness == 0:
        actions.led_off(actions.led_ir)
    else:
        actions.led_on(brightness=brightness,leds=actions.led_ir)
slider_label = ttk.Label(frame, text='Brightness:', background='white')
slider_label.place(relx = 0.3, rely=0.15)

brightness_slider = ttk.Scale(frame, from_=0, to=100, orient='horizontal', variable=current_value, command=slider_changed)
brightness_slider.set(0)
brightness_slider.place(relx=0.3, rely=0.25, relwidth=0.5)


######################################<< snap >>##########################################
def take_snapshot():
    actions.led_on(15,leds=actions.led_white)
    ts = datetime.now()
    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
    #saving
    _,frame = cap.read()
    cv2.imwrite(filename=filename, img=frame)
    actions.led_off(leds=actions.led_white)

button_snap = tk.Button(frame, text='SNAP', bg='black', fg='white', command=take_snapshot)
button_snap.place(relx=0.1,rely=0.5)

###################################
current_value_focus = tk.DoubleVar()

def get_current_value_focusing():
    return '{:.1f}'.format(current_value_focus.get())
value_label_focusing = ttk.Label(frame, text=get_current_value_focusing(), background='white')
value_label_focusing.place(relx=0.5, rely=0.45)

def slider_changed_focusing(event):
    value_label_focusing.configure(text=get_current_value_focusing())
    # print(brightness_slider.get()) ##for getting the value

slider_label_foc = ttk.Label(frame, text='Focus:', background='white')
slider_label_foc.place(relx = 0.3, rely=0.45)


focus_slider = ttk.Scale(frame, from_=-100, to=100, orient='horizontal', variable=current_value_focus, command=slider_changed_focusing)
focus_slider.set(0)
focus_slider.place(relx=0.3,rely=0.55,relwidth=0.5)

################################################## canvas #################################
camera_view_label = ttk.Label(gui, text='CAM VIEW', background='light grey', font='bold')
camera_view_label.place(relx=0.425,rely=0.45)

def video_stream():
    global panel
    try:
        while not stopEvent.is_set():
            _,frame = cap.read()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            ###updates the image panel by the config
            if panel is None:
                panel = tk.Label(canvas)
                panel.imgtk = imgtk
                panel.pack()
            else:
                panel.configure(image=imgtk)
                panel.imgtk = imgtk
                panel.pack()
    except RuntimeError:
        print("caught a runtime error")

##########################################3

stopEvent = threading.Event()
thread = threading.Thread(target=video_stream,args=())
thread.start()

canvas = tk.Canvas(gui, background='red')
canvas.place(relheight=0.5, relwidth=0.7, relx=0.15, rely=0.5,)

# frame2 = tk.Frame(gui, background='white')
# frame2.place(relheight=0.5, relwidth=0.7, relx=0.15, rely=0.5,)

# video_stream()

#############
def onClose():
    print("closing...")
    stopEvent.set()
    gui.quit()

gui.protocol("WM_DELETE_WINDOW", onClose)
gui.mainloop()
