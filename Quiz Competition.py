from tkinter import *
import tkinter as tk
# importing message box from the tkinter
from tkinter import messagebox
# importing a library converting text in to audio
import pyttsx3

# parent window initialization
root = tk.Tk()
root.geometry("1000x700")
root.configure(bg="white")
Label(root, text=" QUIZ COMPETITION", fg="black", font=("Aerial", 27), bg="white").\
    place(x=320,y=80)
button3=Button(root, text="PLAY QUIZ", fg="white", bg="green", width=40, height=2, bd=5,command=lambda:StartApp())
button3.place(x=360,y=550)
img = PhotoImage(file="C:\\Users\\NIHARIKA SONI\\Downloads\\quiz competion1.png")
Label(root, image=img).place(x=250,y=150)

root.configure()
def StartApp():
    frameImp = Frame(root, bg="green")
    frameImp.pack(side=tk.LEFT)

    frameImp.pack()

    def speak1():
        engine = pyttsx3.init()
        engine.say(" score is 1")
        engine.runAndWait()

    # a function for converting text in to audio 2
    def speak2():
        engine = pyttsx3.init()
        engine.say(" score is 0")
        engine.runAndWait()

    # function to create  fifth frame
    # function to create sixth frame
    def output6():
        output6_frame = tk.Frame(frame2)
        Checkbutton1 = IntVar()
        Checkbutton2 = IntVar()
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        frame4 = LabelFrame(output6_frame)
        Label(frame2, text=" PYTHON QUIZ", fg="black", font=("Aerial", 27)).grid(row=0,
                                                                                             column=1,
                                                                                             padx=200,
                                                                                             pady=50)

        Label(frame2, text="  WHAT IS THE FULL FORM OF HTTP ?", fg="black", font=("Aerial", 17)). \
            grid(row=1, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="HyperText Transport Protocol", variable=Checkbutton1, onvalue=1, offvalue=0, fg="red",

                    width=23, height=1, bd=5, command=lambda: speak1()). \
            grid(row=2, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="HyperText Tranfer Protocol", fg="red", variable=Checkbutton2, onvalue=1,
                    offvalue=0,
                    width=23, height=1, bd=5, command=lambda: speak2()). \
            grid(row=3, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="HyperText Transport Promotion", fg="red", width=23, variable=Checkbutton3,
                    onvalue=1,
                    offvalue=0, height=1, bd=5, command=lambda: speak2()). \
            grid(row=4, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="HyperText Tranmission Protocol", fg="red",  width=23, variable=Checkbutton4,
                    onvalue=1,
                    offvalue=0, height=1, bd=5, command=lambda: speak2()). \
            grid(row=5, column=1, padx=150, pady=30)
        frame4.pack(side=LEFT)
        frame4.pack_propagate(False)
        frame4.configure(width=450, height=650)
        output6_frame.pack(pady=20)
    def output5():
        output5_frame = tk.Frame(frame2)
        Checkbutton1 = IntVar()
        Checkbutton2 = IntVar()
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        frame4 = LabelFrame(output5_frame)
        Label(frame2, text=" PYTHON QUIZ", fg="black", font=("Aerial", 27)).grid(row=0,
                                                                                             column=1,
                                                                                             padx=200,
                                                                                             pady=50)

        Label(frame2, text="  WHAT IS THE FULL FORM OF SQL ?", fg="black", font=("Aerial", 17)). \
            grid(row=1, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Structure Query Language", variable=Checkbutton1, onvalue=1, offvalue=0, fg="red",

                    width=23, height=1, bd=5, command=lambda: speak1()). \
            grid(row=2, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Simple Query Language", fg="red", variable=Checkbutton2, onvalue=1,
                    offvalue=0,
                    width=23, height=1, bd=5, command=lambda: speak2()). \
            grid(row=3, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Standard Query Language", fg="red", width=23, variable=Checkbutton3,
                    onvalue=1,
                    offvalue=0, height=1, bd=5, command=lambda: speak2()). \
            grid(row=4, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Standard Questioning Language", fg="red",  width=23, variable=Checkbutton4,
                    onvalue=1,
                    offvalue=0, height=1, bd=5, command=lambda: speak2()). \
            grid(row=5, column=1, padx=150, pady=30)
        frame4.pack(side=LEFT)
        frame4.pack_propagate(False)
        frame4.configure(width=450, height=650)
        output5_frame.pack(pady=20)


        output5_frame.pack(pady=20)

    # function to create  fourth frame
    def output4():
        output4_frame = tk.Frame(frame2)

        Checkbutton1 = IntVar()
        Checkbutton2 = IntVar()
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        frame4 = LabelFrame(output4_frame)
        Label(frame2, text=" PYTHON QUIZ", fg="black", font=("Aerial", 27)).grid(row=0,
                                                                                             column=1,
                                                                                             padx=200,
                                                                                             pady=50)

        Label(frame2, text="  WHAT IS THE FULL FORM OF INTERNET?", fg="black", font=("Aerial", 17)).grid(
            row=1, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Inertial Network", fg="red", variable=Checkbutton1, onvalue=1, offvalue=0,
                    width=18, height=1, bd=5, command=lambda: speak2()). \
            grid(row=2, column=1, padx=50, pady=30)
        Checkbutton(frame2, text="International Network", fg="red", variable=Checkbutton2, onvalue=1,
                    offvalue=0,
                    width=18, height=1, bd=5, command=lambda: speak1()). \
            grid(row=3, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Interpersonal Network", fg="red", variable=Checkbutton3, onvalue=1,
                    offvalue=0,
                    width=18, height=1, bd=5, command=lambda: speak2()). \
            grid(row=4, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Infrastructural Network", fg="red",  variable=Checkbutton4, onvalue=1,
                    offvalue=0,
                    width=18, height=1, bd=5, command=lambda: speak2()). \
            grid(row=5, column=1, padx=150, pady=30)
        frame4.pack(side=LEFT)
        frame4.pack_propagate(False)
        frame4.configure(width=550, height=600)
        output4_frame.pack(pady=20)

        output4_frame.pack(pady=20)

    # function to create third frame
    def output3():
        output3_frame = tk.Frame(frame2)
        Checkbutton1 = IntVar()
        Checkbutton2 = IntVar()
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        frame4 = LabelFrame(output3_frame)
        Label(frame2, text=" PYTHON QUIZ", fg="black", font=("Aerial", 27)).grid(row=0,
                                                                                             column=1,
                                                                                             padx=200,
                                                                                             pady=50)

        Label(frame2, text=" WHAT IS THE FULL FORM  OF  WWW?", fg="black", font=("Aerial", 17)).grid(
            row=1,
            column=1,
            padx=150,
            pady=30)
        Checkbutton(frame2, text=" World Wide Website", fg="red", variable=Checkbutton1, onvalue=1,
                    offvalue=0,
                    width=15, height=1, bd=5, command=lambda: speak2()). \
            grid(row=2, column=1, padx=150, pady=30)
        Checkbutton(frame2, text=" World Whole Web", fg="red", width=15, variable=Checkbutton2, onvalue=1,
                    offvalue=0,
                    height=1, bd=5, command=lambda: speak2()). \
            grid(row=3, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Wide World  Web", fg="red", width=15, variable=Checkbutton3, onvalue=1,
                    offvalue=0,
                    height=1, bd=5, command=lambda: speak2()). \
            grid(row=4, column=1, padx=150, pady=30)
        Checkbutton(frame2, text=" World Wide Web", fg="red", width=15, variable=Checkbutton4, onvalue=1,
                    offvalue=0,
                    height=1, bd=5, command=lambda: speak1()). \
            grid(row=5, column=1, padx=150, pady=30)
        frame4.pack(side=LEFT)
        frame4.pack_propagate(False)
        frame4.configure(width=500, height=600)
        output3_frame.pack(pady=20)

        output3_frame.pack(pady=20)

    # function to create  second frame
    def output2():
        output2_frame = tk.Frame(frame2)

        Checkbutton1 = IntVar()
        Checkbutton2 = IntVar()
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        frame4 = LabelFrame(output2_frame)
        Label(frame2, text=" PYTHON QUIZ", fg="black", font=("Aerial", 27)).grid(row=0,
                                                                                             column=1,
                                                                                             padx=200,
                                                                                             pady=50)
        Label(frame2, text=" WHAT IS THE FULL FORM OF MU ?", fg="black", font=("Aerial", 17)).grid(
            row=1,
            column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Masked Unit", fg="red", width=15, variable=Checkbutton1, onvalue=1,
                    offvalue=0,
                    height=1, bd=5, command=lambda: speak2()). \
            grid(row=2, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Management Unit", fg="red", width=15, variable=Checkbutton2, onvalue=1,
                    offvalue=0,
                    height=1, bd=5, command=lambda: speak2()). \
            grid(row=3, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Memory Unit", fg="red", width=15, variable=Checkbutton3, onvalue=1,
                    offvalue=0,
                    height=1, bd=5, command=lambda: speak1()). \
            grid(row=4, column=1, padx=150, pady=30)
        Checkbutton(frame2, text="Main Unit", fg="red", width=15, variable=Checkbutton4, onvalue=1,
                    offvalue=0,
                    height=1, bd=5, command=lambda: speak2()). \
            grid(row=5, column=1, padx=150, pady=30)
        frame4.pack(side=LEFT)
        frame4.pack_propagate(False)
        frame4.configure(width=500, height=600)
        output2_frame.pack(pady=20)

        output2_frame.pack(pady=20)

    # function to create  first frame
    def output1():
        output1_frame = tk.Frame(frame2)

        Checkbutton1 = IntVar()
        Checkbutton2 = IntVar()
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        frame4 = LabelFrame(output1_frame)
        Label(frame2, text=" PYTHON QUIZ", fg="black", font=("Aerial", 27)).grid(row=0,
                                                                                             column=1,
                                                                                             padx=200,
                                                                                             pady=50)

        Label(frame2, text=" WHAT IS THE FULL FORM OF IP ?",fg="black", font=("Aerial", 17)).grid(
            row=1, column=1,
            padx=150, pady=30)
        Checkbutton(frame2, text="Intranet Process", fg="red",  width=15, variable=Checkbutton1, onvalue=1,
                    offvalue=0, height=1, bd=5, command=lambda: speak2()). \
            grid(row=2, column=1, padx=50, pady=30)
        Checkbutton(frame2, text="Internet Protocol", fg="red",  width=15, variable=Checkbutton2,
                    onvalue=1,
                    offvalue=0, height=1, bd=5, command=lambda: speak1()). \
            grid(row=3, column=1, padx=50, pady=30)
        Checkbutton(frame2, text="Internet Process", fg="red", width=15, variable=Checkbutton3, onvalue=1,
                    offvalue=0, height=1, bd=5, command=lambda: speak2()). \
            grid(row=4, column=1, padx=50, pady=30)
        Checkbutton(frame2, text="Intranet Protocol", fg="red", width=15, variable=Checkbutton4,
                    onvalue=1,
                    offvalue=0, height=1, bd=5, command=lambda: speak2()). \
            grid(row=5, column=1, padx=50, pady=30)
        frame4.pack(side=LEFT)
        frame4.pack_propagate(False)
        frame4.configure(width=450, height=600)
        output1_frame.pack(pady=20)
        output1_frame.pack(pady=20)

    # function to hide indicator
    def hide_indicator():

        Next1.config(bg="light grey")
        Next2.config(bg="light grey")
        Next3.config(bg="light grey")
        Next4.config(bg="light grey")
        Next5.config(bg="light grey")
        Next6.config(bg="light grey")

    # function to clear page
    def clear_page():
        for frame in frame2.winfo_children():
            frame.destroy()

    # function for indicator
    def indicate(l, page):
        hide_indicator()
        l.config(bg='green')
        clear_page()
        page()

    # creating frame1
    frame1 = tk.Frame(frameImp, bg="light grey")

    button1 = tk.Button(frame1, text="NEXT1", fg="white", bg="green", width=10, height=2, bd=5,
                        command=lambda: indicate(Next1, output1))
    button1.place(x=50, y=50)
    Next1 = tk.Label(frame1, text='', font=('Bold', 32), fg='white',bg="light grey", bd=0)
    Next1.place(x=40, y=52, width=10, height=50)
    button2 = tk.Button(frame1, text="NEXT2", fg="white", bg="green", width=10, height=2, bd=5,
                        command=lambda: indicate(Next2, output2))
    button2.place(x=50, y=150)
    Next2 = tk.Label(frame1, text='', font=('Bold', 32), fg='white', bd=0, bg='light grey')
    Next2.place(x=40, y=152, width=10, height=50)
    button3 = tk.Button(frame1, text="NEXT3", fg="white", bg="green", width=10, height=2, bd=5,
                        command=lambda: indicate(Next3, output3))
    button3.place(x=50, y=250)
    Next3 = tk.Label(frame1, text='', font=('Bold', 32), fg='white', bd=0, bg='light grey')
    Next3.place(x=40, y=252, width=10, height=50)
    button4 = tk.Button(frame1, text="NEXT4", fg="white", bg="green", width=10, height=2, bd=5,
                        command=lambda: indicate(Next4, output4))
    button4.place(x=50, y=350)
    Next4 = tk.Label(frame1, text='', font=('Bold', 32), fg='white', bd=0,bg='light grey')
    Next4.place(x=40, y=352, width=10, height=50)
    button5 = tk.Button(frame1, text="NEXT5", fg="white", bg="green", width=10, height=2, bd=5,
                        command=lambda: indicate(Next5, output5))
    button5.place(x=50, y=450)
    Next5 = tk.Label(frame1, text='', font=('Bold', 32), fg='white', bd=0, bg='light grey')
    Next5.place(x=40, y=452, width=10, height=50)
    button6 = tk.Button(frame1, text="NEXT6", fg="white", bg="green", width=10, height=2, bd=5,
                        command=lambda: indicate(Next6, output6))
    button6.place(x=50, y=550)
    Next6 = tk.Label(frame1, text='', font=('Bold', 32), fg='white', bd=0, bg='light grey')
    Next6.place(x=40, y=552, width=10, height=50)

    frame1.pack(side=tk.LEFT)
    frame1.pack_propagate(False)
    frame1.configure(width=200, height=700)

    # creating frame2
    frame2 = tk.Frame(frameImp,bg="light green", highlightbackground="white", highlightthickness=2)
    frame2.pack(side=tk.LEFT)
    frame2.pack_propagate(False)
    frame2.configure(width=590, height=600)
    Label(frame2, text="WELCOME", fg="WHITE",bg="light green", font=("Aerial", 40)).\
        place(x=150,y=100)
    Label(frame2, text="TO ",fg="WHITE",bg="light green",font=("Aerial", 30)). \
        place(x=230, y=200)
    Label(frame2, text=" QUIZ", fg="WHITE",bg="light green",font=("Aerial", 36)). \
        place(x=200, y=300)
    Label(frame2, text="COMPETITION !!",  fg="WHITE",bg="light green",font=("Aerial", 36)). \
        place(x=120, y=400)
root.mainloop()
