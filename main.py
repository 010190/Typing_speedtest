import time
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import keyboard
from PIL import Image, ImageTk
from PIL.ImageOps import expand

app = Tk()
app.geometry("500x500")
app.title("Typing Speedtest")

style = ttk.Style()
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = '#FE653C')
normal_text = ("A fitness studio was struggling to attract new members. "
        "The owner, Maria, decided to launch a 30-day fitness challenge with a $500 cash prize for the most improved participant. "
        "The challenge went viral on social media, generating 500 new leads within the first week. "
        "By the end of the month, the studio had gained 150 new members, "
        "a 20% increase in revenue, and a revitalized community of fitness enthusiasts.")
easy_text = ("The world of typing and office technology is constantly evolving. "
             "Invest in continuing education to stay up-to-date with the latest trends and technologies. "
             "Consider pursuing certifications in specialized areas to enhance your skillset and marketability.")


hard_text = ("Teamwork is not only about achieving goals; it's also about the joy of collaboration, "
             "the satisfaction of working together towards a common purpose, "
             "and the sense of camaraderie that comes from being part of something bigger than oneself. "
             "When team members feel connected to each other and to their shared mission, "
             "they are more engaged, motivated, and productive. "
             "They are also more likely to experience a sense of fulfillment and satisfaction in their work. "
             "The joy of teamwork is a powerful force that can transform workplaces, communities, and even the world.")

count = 0
row  = 0
label_list = []
time_value = 90
correct_words = []
correct_count = 0
wrong_count = 0
character_count = 0
counter_id = 0

image = Image.open("C:/Users/olcza/Desktop/typing_speedtest/tp logo.png").resize((500,500))
canvas = Canvas(app, width=500, height=500)
canvas.place(x=0, y=0)
image = ImageTk.PhotoImage(image)

canvas.create_image( 0, 0, image = image, anchor="nw")
welcome_label = Label(app, text="Welcome to Typing Speed Test", font=("Arial", 25, 'bold'),background="#FE8D6F", foreground="white")
welcome_label.place(x=8,y=20)

choose_label = Label(app, text="Choose a level:", font=("Arial", 20, "bold"),background="#FE8D6F", foreground="white")
choose_label.place(x=160,y=75)

easy_button = Button(app, text="Easy", command=lambda:new_dialog(easy_text, "easy"),style = 'W.TButton')
easy_button.place(x=225,y=120)

normal_button = Button(app, text="Normal", command=lambda:new_dialog(normal_text, "normal"),style = 'W.TButton')
normal_button.place(x=225,y=150)


hard_button = Button(app, text="Hard", command=lambda:new_dialog(hard_text, "hard"),style = 'W.TButton')
hard_button.place(x=225,y=180)

def new_dialog(content,level):

        global row, count
        window = Toplevel(app)
        window.geometry("500x500")
        vscrollbar = ttk.Scrollbar(window, orient=VERTICAL)
        vscrollbar.place(x=60, y=120)
        window.configure(background="#FE8D6F")
        inside_canvas = Canvas(window, width=305, height=200,bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)

        inside_canvas.place(x=100, y=75)
        # inside_canvas.config(scrollregion=inside_canvas.bbox("all"))
        vscrollbar.config(command=inside_canvas.yview)

        text = content.replace(".","").replace(",","").lower().strip().split()
        level_label = Label(window, text=f"Typing speed test: level {level}", font=("Arial", 25, 'bold'),
                              background="#FE8D6F", foreground="white")
        level_label.place(x=9, y=20)
        frame = Frame(inside_canvas,width=200, height=200)
        frame.place(x=100, y=75, relx=0, rely=0)
        inside_canvas.create_window(0, 0, window=frame, anchor="nw")

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

        entry = Entry(window, width=48, textvariable=user_var, font=("Arial", 8))
        entry.place(x=100, y=350)


        text_label_list = [label["text"] for label in label_list]


        def speed_test(event):
            global correct_count, wrong_count, character_count
            user_input = user_var.get().strip()
            if user_input in text:
                for item in label_list:
                    if item["background"] == "" and user_input == item["text"]:
                        item.configure(background="green")
                        print(item.place_info())

                        break
                            # if item.place_info()["Y"] >= 5:
                            #     inside_canvas.yview_moveto(0.2)
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
            wpm_value = correct_count * 2
            cpm_value = character_count * 2
            wpm_label.configure(text=f"WPM:{wpm_value}")
            cpm_label.configure(text=f"CPM:{cpm_value}")

        time_label = Label(window, text="00:00", font=("Arial", 15))
        time_label.place(x=425,y=100)

        def counter():
            global  time_value,counter_id
            entry = Entry(window, width=45, textvariable=user_var, font=("Arial", 8))
            entry.place(x=100, y=350)
            if time_value > 0:
                time_label.configure(text=f"00:{time_value}")
                time_value -= 1
                counter_id = window.after(1000, counter)

            if time_value < 10 and time_value != 0:
                time_value -= 1
                time_label.configure(text=f"00:0{time_value}")
            if time_value == 0:
                time_label.configure(text=f"00:00")

                entry.destroy()
                check()
            window.bind('<space>', speed_test)


        def reset():
            global time_value
            time_value = 30
            window.after_cancel(counter_id)
            for label in label_list:
                label.configure(background="")
            wpm_label.configure(text="WPM:", font=("Arial", 15))
            time_label.configure(text="00:00")
            cpm_label.configure(text="CPM:", font=("Arial", 15))

        start_button = Button(window, text="Start", command=counter,style = 'W.TButton')
        start_button.place(x=220,y=380)

        reset_button = Button(window, text="Reset", command=reset,style = 'W.TButton')
        reset_button.place(x=220,y=400)

        wpm_label = Label(window, text="WPM:", font=("Arial", 12))
        cpm_label = Label(window, text="CPM:", font=("Arial", 12))


        wpm_label.place(x=425,y=130)
        cpm_label.place(x=425,y=160)

app.mainloop()