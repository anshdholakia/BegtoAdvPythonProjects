import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils


a=input("Enter football or cricket: ")


if a=="cricket":
    stream=cv2.VideoCapture("C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\DRS\\clip.mp4")
    flag=True
    def play(speed):
        global flag
        # print(f"you clicked on play with speed {speed}")

        # play the video in reverse
        frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
        stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
        grabbed, frame=stream.read()
        if not grabbed:
            exit()

        frame=imutils.resize(frame,width=1280,height=720)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0, -40, image=frame, anchor=tkinter.NW)
        if flag:
            canvas.create_text(129,25, fill="brown", font="Times 25 bold",text="Decision Pending")

        flag=not flag

    # Width and Height of our main screen


    def out():
        thread=threading.Thread(target=pending,args=("out",))
        thread.daemon=1
        thread.start()
        # print("Player is out")

    def notout():
        thread = threading.Thread(target=pending, args=("notout",))
        thread.daemon = 1
        thread.start()
        # print("Player is not out")

    def pending(decision):
        # 1 Display decision pending image
        frame=cv2.cvtColor(cv2.imread("C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\DRS\\pending.png"), cv2.COLOR_BGR2RGB)
        frame=imutils.resize(frame,width=1280,height=720)  # for resizing frame
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0,-40,image=frame,anchor=tkinter.NW)
        # 2 wait for a second
        time.sleep(1)
        # 3 display sponsor image
        frame = cv2.cvtColor(
            cv2.imread("C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\DRS\\sponsor.png"),
            cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=1280, height=720)  # for resizing frame
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, -40, image=frame, anchor=tkinter.NW)
        # 4 wait 1.5 second
        time.sleep(1.5)
        # 5 display out/notout image
        if decision=="out":
            decisionImg="C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\DRS\\out.png"
        else:
            decisionImg = "C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\DRS\\notout.png"

        frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=1280, height=720)  # for resizing frame
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, -40, image=frame, anchor=tkinter.NW)


    SET_WIDTH=1920
    SET_HEIGHT=500

    #tkinter gui starts here
    window=tkinter.Tk()
    window.title("Digital Review System by Ansh Dholakia")

    cv_img= cv2.cvtColor(cv2.imread("C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\DRS\\stadium.png"),cv2.COLOR_BGR2RGB)

    canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)

    photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

    image_on_canvas=canvas.create_image(0,-40, anchor=tkinter.NW,image=photo)
    canvas.pack()


    # buttons to control playback
    btn=tkinter.Button(window,text="<< Previous (Fast)", width=150, command=partial(play,-25))
    btn.pack()

    btn=tkinter.Button(window,text="<< Previous (Slow)", width=150, command=partial(play,-2))
    btn.pack()

    btn=tkinter.Button(window,text="Next (Fast) >>", width=150, command=partial(play,25))
    btn.pack()

    btn=tkinter.Button(window,text="Next (Slow) >>", width=150, command=partial(play,2))
    btn.pack()

    btn=tkinter.Button(window,text="Out", width=150, command=out)
    btn.pack()

    btn=tkinter.Button(window,text="Not Out", width=150, command=notout)
    btn.pack()

    window.mainloop()

elif a=="football":

    stream = cv2.VideoCapture("C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\VAR\\clip.mp4")
    flag = True

    def play(speed):
        global flag
        # print(f"you clicked on play with speed {speed}")

        # play the video in reverse
        frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
        stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
        grabbed, frame = stream.read()
        if not grabbed:
            exit()

        frame = imutils.resize(frame, width=1280, height=720)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, -40, image=frame, anchor=tkinter.NW)
        if flag:
            canvas.create_text(129, 25, fill="brown", font="Times 25 bold", text="Decision Pending")
        flag = not flag


    # Width and Height of our main screen

    def goal():
        thread = threading.Thread(target=pending, args=("goal",))
        thread.daemon = 1
        thread.start()
        # print("Goal given")


    def nogoal():
        thread = threading.Thread(target=pending, args=("nogoal",))
        thread.daemon = 1
        thread.start()
        # print("Goal not given")

    def foul():
        thread = threading.Thread(target=pending, args=("foul",))
        thread.daemon = 1
        thread.start()
        # print("Fouled")


    def pending(decision):

        # 1 Display decision pending image
        frame = cv2.cvtColor(cv2.imread("C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\VAR\\pending.png"),cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=1280, height=720)  # for resizing frame
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, -40, image=frame, anchor=tkinter.NW)

        # 2 wait for a second
        time.sleep(1)
        # 3 display sponsor image
        frame = cv2.cvtColor(cv2.imread("C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\VAR\\sponsor.png"),cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=1280, height=720)  # for resizing frame
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, -40, image=frame, anchor=tkinter.NW)

        # 4 wait 1.5 second
        time.sleep(1.5)
        # 5 display goal/nogoal image

        if decision == "goal":
            decisionImg = "C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\VAR\\goal.png"
        elif decision=="nogoal":
            decisionImg = "C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\VAR\\nogoal.png"
        else:
            decisionImg = "C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\VAR\\foul.png"


        frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=1280, height=720)  # for resizing frame
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, -40, image=frame, anchor=tkinter.NW)


    SET_WIDTH = 1920
    SET_HEIGHT = 470

    # tkinter gui starts here
    window = tkinter.Tk()
    window.title("Virtual Assistant Referee by Ansh Dholakia")

    cv_img = cv2.cvtColor(
        cv2.imread("C:\\Users\\Ansh\\PycharmProjects\\First Project File\\VAR_Sytem_Project\\VAR\\stadium.png"),
        cv2.COLOR_BGR2RGB)

    canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)

    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

    image_on_canvas = canvas.create_image(0, -100, anchor=tkinter.NW, image=photo)
    canvas.pack()

    # buttons to control playback
    btn = tkinter.Button(window, text="<< Previous (Fast)", width=150, command=partial(play, -25))
    btn.pack()

    btn = tkinter.Button(window, text="<< Previous (Slow)", width=150, command=partial(play, -2))
    btn.pack()

    btn = tkinter.Button(window, text="Next (Fast) >>", width=150, command=partial(play, 25))
    btn.pack()

    btn = tkinter.Button(window, text="Next (Slow) >>", width=150, command=partial(play, 2))
    btn.pack()

    btn = tkinter.Button(window, text="Goal", width=150, command=goal)
    btn.pack()

    btn = tkinter.Button(window, text="Not a goal", width=150, command=nogoal)
    btn.pack()

    btn = tkinter.Button(window, text="Foul", width=150, command=foul)
    btn.pack()

    window.mainloop()

else:
    print("Enter a valid sport!")
