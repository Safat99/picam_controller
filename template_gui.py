import tkinter as tk
from tkinter import Label, messagebox
from tkinter import ttk

# messagebox.showinfo("hello","welcome to picam controller")
gui = tk.Tk()
gui.configure(background="light grey")
gui.title("picam controller")
gui.geometry("640x480")

frame = tk.Frame(gui, background='white')
frame.place(relheight=0.4, relwidth=0.7, relx=0.15, rely=0)
# frame.pack()
########################################################################
IR_isON = False
def ir_toggle():
    global IR_isON 

    if IR_isON == True: ## button is pressed
        button1.config(text='IR OFF')
        IR_isON = False
    else:
        button1.config(text="IR ON")
        IR_isON = True

button1 = tk.Button(frame, text='IR OFF', fg='white', bg='black', command=ir_toggle)
button1.place(relx=0.1,rely=0.2, relwidth=0.125)
#####################################################################
current_value = tk.DoubleVar()

def get_current_value():
    return '{:.1f}'.format(current_value.get())
    # return '{:.1f}'.format(current_value.get()*15//100) ## if want to display from 0 to 15

value_label = ttk.Label(frame, text=get_current_value(), background='white')
value_label.place(relx=0.5, rely=0.15)

def slider_changed(event):
    value_label.configure(text=get_current_value())
    # print(brightness_slider.get()) ##for getting the value
    # print(brightness_slider.get()*15//100) ## for mapping

    
slider_label = ttk.Label(frame, text='Brightness:', background='white')
slider_label.place(relx = 0.3, rely=0.15)

brightness_slider = ttk.Scale(frame, from_=0, to=100, orient='horizontal', variable=current_value, command=slider_changed)
brightness_slider.set(0)
brightness_slider.place(relx=0.3, rely=0.25, relwidth=0.5)

#####################################################################
button_snap = tk.Button(frame, text='SNAP', bg='black', fg='white')
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

canvas = tk.Canvas(gui, background='red')
canvas.place(relheight=0.5, relwidth=0.7, relx=0.15, rely=0.5,)

# frame2 = tk.Frame(gui, background='white')
# frame2.place(relheight=0.5, relwidth=0.7, relx=0.15, rely=0.5,)

gui.mainloop() 