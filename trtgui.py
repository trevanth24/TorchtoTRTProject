from re import S
import tkinter as tk
import requests
from tkinter import filedialog
import json 

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    filename_text.set(filename)
    print('Selected:', filename)

#Root
root = tk.Tk()
root.title("Torch to TensorRT (TRT)")

info_text = tk.StringVar()
info_text.set("Input Model Location and Information")
info = tk.Label(root, textvariable = info_text, font="Helvetica 10 bold italic").pack()

alert_text = tk.StringVar()
alert_text.set("No Alerts")
alert = tk.Label(root, textvariable = alert_text, font="red").pack()


filename_text = tk.StringVar()
filename_text.set("No File Selected")
filename_label = tk.Label(root, textvariable = filename_text).pack()

button = tk.Button(root, text='Open', command=UploadAction)
button.pack()


#Gender Radio Btns
gender_label = tk.Label(
    text="Precision Setting",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
).pack(pady=(10,10))
gender = tk.IntVar()
gender.set(1)
radiobutton_1 = tk.Radiobutton(root, text='fp16', variable=gender, value=1)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(root, text='int8', variable=gender, value=2)
radiobutton_2.pack()

#Age Spinbox 
batch_label = tk.Label(root, text="Batch Size (1, 4, 8 , 16)").pack()
batch = tk.IntVar()
batch.set(1)
batch_spin  = tk.Spinbox(root, from_ = 1, to= 16, textvariable=batch).pack()

#Input Size
input_label = tk.Label(root, text="Input Image Size (1, 3, 224, 224)").pack()
input_text = tk.StringVar()
input_entry = tk.Entry(root, fg="white", bg="grey", width=30, textvariable=input_text).pack()

#Load Test Size Spinbox 
load_label = tk.Label(root, text="Load Size for Testing (1 - 200)").pack()
load = tk.IntVar()
load.set(1)
load_spin  = tk.Spinbox(root, from_ = 1, to= 200, textvariable=load).pack()


#File information is sent over to Google Drive/ Local Host/ Cloud Provider

def send_results():
    if filename_text.get() == "No File Selected":
        alert_text.set("Select File!")
    elif len(input_text.get()) == 0:
        alert_text.set("Add an Input!")
    else:
        alert_text.set("Completed! Please Wait")
        
        prec = ""
        if gender.get() == 1:
            prec = "fp16"
        else:
            prec = "fp16"



        # Data to be written 
        dictionary_settings = { 
            "model": filename_text.get(), 
            "batch_size": batch.get(), 
            "dtype": prec,
            "input_size": input_text.get(),
            "load": load.get()
        } 

        with open('settings/data.json', 'w') as f:
            json.dump(dictionary_settings, f)
        # Serializing json  
        # json_object = json.dumps(dictionary_settings, indent = 4) 
            # print(json_object)

#submit button
submit_button = tk.Button(
    text="Submit!",
    width=25,
    height=2,
    bg="green",
    fg="black",
    command=send_results,
)

#Layout

submit_button.pack(pady=(10,10))

#runs the GUI
root.mainloop()