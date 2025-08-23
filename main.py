from tkinter import *
from tkinter.ttk import *
import keyboard

app = Tk()
app.geometry("500x500")

text = ("A fitness studio was struggling to attract new members. "
        "The owner, Maria, decided to launch a 30-day fitness challenge "
        "with a $500 cash prize for the most improved participant. "
        "The challenge went viral on social media, generating 500 new leads within the first week. "
        "By the end of the month, the studio had gained 150 new members, a 20% increase in revenue, "
        "and a revitalized community of fitness enthusiasts.")

text_list = [word for word in text.split()][:3]
y_pos = [0,50,100,150,200,250,300,350,400,450]
x_pos = [0,50,100,150,200,250,300,350,400,450]
starting_x = 0
starting_y = 0
label_list = []

user_entry = StringVar()
for word in text_list:

    x = starting_x + (text_list.index(word) *50)
    y = y_pos[0]
    # y = starting_y + (text_list.index(word) * 20)
    if x >= 450:
        x = 0
        y = y_pos[+1]
    label = Label(app, text=word, borderwidth=2, relief="solid")
    label.place(x=x,y=y )
    label_list.append(label)



label = Label(app, text="Start speed test",font=('calibre',25,'normal'))
label.place(x=100,y=200)

entry = Entry(app, textvariable=user_entry)
entry.place(x=200,y=200)

def get_text(event):
    entry = user_entry.get().split()
    print(entry)
    # for label in label_list:
    #     print(label["text"], entry[label_list.index(label)])
    #     try:
    #         if label["text"] == entry[label_list.index(label)]:
    #             label.configure(background="green")
    #         else:
    #             label.configure(background="green")
    #
    #     except IndexError:
    #         pass
def speed_test():

    if keyboard.is_pressed("space"):
        get_text()
    # for label in label_list:



start_button = Button(app, text="Start", command=speed_test)
start_button.place(x=220,y=300)

submit_button = Button(app, text="Submit", command=get_text)
submit_button.place(x=220,y=400)

# user_input_label = Label(app, text=user_entry.get(), font=('calibre', 25, 'normal'))
# user_input_label.place(x=220, y=500)

app.bind('<BackSpace>', get_text)
app.mainloop()