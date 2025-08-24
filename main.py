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
        "a 20% increase in revenue, and a revitalized community of fitness enthusiasts.").replace(".","").strip().split()
frame = Frame(app,width=450, height=350, borderwidth=2, relief="solid")
frame.place(x=100, y=75)

count = 0
row  = 0
label_list = []
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

print(text_label_list)

def speed_test(event):
    user_input = user_var.get().strip()
    print(user_input)
    try:
        id = text_label_list.index(user_input)
        print(id)
        label_list[id].configure(background="green")

    except ValueError:
        for item in label_list[::-1]:
            print(item["background"])
            if item["background"] != "":
                id = label_list.index(item)
                print(id+1)
                label_list[id + 1].configure(background="red")
                break
            else:
                label_list[0].configure(background="red")


    entry.delete(0, END)


start_button = Button(app, text="Start")
start_button.place(x=220,y=380)

submit_button = Button(app, text="Submit")
submit_button.place(x=220,y=400)

# user_input_label = Label(app, text=user_entry.get(), font=('calibre', 25, 'normal'))
# user_input_label.place(x=220, y=500)

app.bind('<space>', speed_test)
app.mainloop()