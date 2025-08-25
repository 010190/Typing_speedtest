import time
from tkinter import *
from tkinter.ttk import *
import keyboard

app = Tk()
app.geometry("500x500")
welcome_label = Label(app, text="Welcome to Typing Speed Test", font=("Arial", 25))
welcome_label.place(x=25,y=20)

text = ("A fitness studio was struggling to attract new members. "
        "The owner, Maria, decided to launch a 30-day fitness challenge with a $500 cash prize for the most improved participant. "
        "The challenge went viral on social media, generating 500 new leads within the first week. "
        "By the end of the month, the studio had gained 150 new members, "
        "a 20% increase in revenue, and a revitalized community of fitness enthusiasts.").replace(".","").replace(",","").lower().strip().split()
frame = Frame(app,width=450, height=350, borderwidth=2, relief="solid")
frame.place(x=100, y=75)

count = 0
row  = 0
label_list = []
time_value = 30
correct_words = []
correct_count = 0
wrong_count = 0
character_count = 0

for text_item in text:
    count +=1
    label = Label(frame, text=text_item, font=("Arial", 8))

    if count != 5:
        label.grid(column=count, row=row)
    else:
        row += 1
        count = 0
        label.grid(column=count, row=row)
    label_list.append(label)

user_var = StringVar()

entry = Entry(app, width=45, textvariable=user_var, font=("Arial", 8))
entry.place(x=100, y=350)


text_label_list = [label["text"] for label in label_list]


def speed_test(event):
    global correct_count, wrong_count, character_count
    user_input = user_var.get().strip()
    if user_input in text:
        for item in label_list:
            if item["background"] == "" and user_input == item["text"]:
                item.configure(background="green")
                break
            # elif user_input != item["text"]:
        # id = text_label_list.index(user_input)
        # label_list[id].configure(background="green")
        #
        correct_words.append(user_input)
        correct_count += 1
        character_count += len(label["text"])
    else:
        for item in label_list[::-1]:
            if item["background"] != "":
                id = label_list.index(item)
                label_list[id + 1].configure(background="red")
                break
        if label_list[0]["background"] == "":
            label_list[0].configure(background="red")
        wrong_count += 1
    try:
        entry.delete(0, END)
    except TclError:
        print(correct_words, wrong_count)

def check():
    global time_value
    # multiplier = 60 / time_value
    wpm_value = correct_count * 2
    cpm_value = character_count * 2
    wpm_label.configure(text=f"WPM:{wpm_value}")
    cpm_label.configure(text=f"CPM:{cpm_value}")

time_label = Label(app, text="00:00", font=("Arial", 15))
time_label.place(x=400,y=100)

def counter():
    global time_value

    time_value -= 1
    if time_value >= 0:
        time_label.configure(text=f"00:{time_value}")

        app.after(1000,counter)
    if time_value < 10 and time_value != 0:
        time_label.configure(text=f"00:0{time_value}")
    if time_value == 0:
        time_label.configure(text=f"00:00")

        entry.destroy()
        check()

def reset():
    for label in label_list:
        label.configure(background="")
    wpm_label.configure(text="WPM:", font=("Arial", 15))
    time_label.configure(text="00:00")
    cpm_label.configure(text="CPM:", font=("Arial", 15))

start_button = Button(app, text="Start", command=counter)
start_button.place(x=220,y=380)

reset_button = Button(app, text="reset", command=reset)
reset_button.place(x=220,y=400)

wpm_label = Label(app, text="WPM:", font=("Arial", 12))
cpm_label = Label(app, text="CPM:", font=("Arial", 12))


wpm_label.place(x=400,y=125)
cpm_label.place(x=400,y=150)
app.bind('<space>', speed_test)
app.mainloop()