import tkinter as tk
import tkinter.font as tkFont
import webbrowser
import os

window = tk.Tk()
window.geometry("640x480")
window.resizable(False, False)
window.configure(bg="#000424")
window.title("okokokokok")

eye = tk.Toplevel()
eye.title("THIRDEYE")

class ccmd():
        def linkx(x):
                webbrowser.open_new(x)

        def link1cmd():
            webbrowser.open_new(r"https://youtu.be/wJWksPWDKOc?t=19916")
        def link2cmd():
                webbrowser.open_new(r"https://www.youtube.com/watch?v=4yX55S8lGQ0")
        def restart():
            window.destroy()
            os.startfile("main.py")

        def hideWidget(x):
            x.pack_forget()

        def destroyWidget(x):
            x.destroy()
def blink():
        eye.deiconify()
        Label8.pack()
        def oeye():
                ccmd.hideWidget(Label9)
                Label8.pack()
        def ceye():
                ccmd.hideWidget(Label8)
                Label9.pack()
        eye.after(200, lambda: ceye())
        eye.after(400, lambda: oeye())
        eye.after(600, lambda: ceye())
        eye.after(800, lambda: oeye())
        eye.after(1000, lambda: ceye())
        eye.after(1200, lambda: oeye())
        eye.after(1400, lambda: ceye())
        eye.after(1600, lambda: oeye())
        eye.after(1800, lambda: eye.withdraw())
def censor():
        bar = tk.Toplevel()
        bar.title("aAHAHAHHDASHHAHAHAHAHAHAHAHAHAHA")
        bar.geometry("19000x10800")
        bar.configure(bg="black")
        glitch.pack()
        bar.after(1000, lambda: bar.withdraw())
        window.after(3000,lambda:ccmd.hideWidget(glitch))

glitchText="""
??????????

H̴̡̧̛̥̪̙͈̞̦̟̝̘̝̱̿́̊̅̊̆̇̈́̎͂̕͘̕͜͝È̷̼̬̦̤̣̱̻͉̾͗̓̎̈́̊̅̊̋̂Ļ̸̘̱̥͕̪̮̬̱̭̈́̽̕P̸͓̣̮͎͖͎̬̺͕̙̠̭̣͎̗̑̐ ̷̛͍̪̙̫̬̺̥̬͔̬̝̖̭̰͗̏̿̾̓̎͒́͘M̷͓͎̦̘͍̗̳̋̅̂̎͑̈̓̀̈́͊̍͑̾̐̋E̶̻̦͈̟̗̟̲̍̃̽͋͝ ̷̣̹̀Ģ̷̟̻͍̥̳̼͔͛͊́̎̈́͒̌̿̀͐͘͘̚͜Ȯ̴̧͇͇̮̞̓̓̈́D̷̦̘̼͕̤̥̗̪̣̙́͜

??????????
"""

textOne = """
Im trapped. Physically im still here at my desk
but mentally I've woken up in these woods.
I didn't believe in god, in spirits, in anything,
so I took a dare to "open my third eye" and ever
since It's like I'm in control of two entities: myself
and the one in the woods...
"""

textTwo = """
It was a mistake. An irreversible one.
Theres no other option but to go on...
I have to eventually, the more I wait
the more my third eye hurts. I have to
venture into these woods. Maybe there's
an end to this madness...
"""

textThree = """
As I move through the woods I become
less aware of myself being still in my desk,
as if my consciousness is fading in that reality.
It's more unnerving than scary. I don't know if I
should stop or not...
"""

textFour ="""
As soon as I try to snap out of my dreamlike
trance everything goes black, and I feel
nothing. I am aware that my body has been
transported to some sort of void, and I have no
idea how or if I can escape. I can't tell how much time
has passed but I'm going insane...
"""

textFive = """
After stumbling through the woods for about
an hour I no longer feel my body in my desk,
as if that all melted away to nothingness. At
about two hours I come across the house, and I'm
aware that I'm being followed. Maybe its best
to go inside...
"""

textSix = """
I go in and feel as if ive made the right choice,
but the geometry from the inside doesn't seem
to add up. The front door leads to this closet sized
room with a stairwell on one side and a door on the
other. Behind the door there are banging noises, but 
I'm safe from whatever was following me outside.
Where do I go now...
"""

textSeven = """
The attic is the only thing that seems to match the
outside of the house. The air is colder here and theres
nothing but a trapdoor in the floor. I hear a faint singing
through the trapdoor, but then a bang from downstairs
alerts me...
"""

textEight = """
You opened the trapdoor, and a blurry black figure grabs
hold of you and takes you down. You barely see its face
before he rips you to shreds, singing merrily the whole
time. Its dark circled eyes are the last thing you see
before everything goes black...
"""

textNine = """
The banging was coming from an angel desperately trying to
open the door that I came through. I can't undertsand what
its saying but I piece together that it was trying to find me.
All of a sudden, as if telepathically, it asks me a question.
Three words, "Forget or Remember." It's asking for me
to make one final decision...
"""

titleTwo = "okokokokok"

creditText = """
A Game By Jack Adkins

Based on the WeirdCore aesthetic

Finished September 21st, 2021

stay weird :)
"""

titleFont = tkFont.Font(family="Verdana", size=32, weight="bold")

subtitleFont = tkFont.Font(family="Verdana", size=16)

bodyFont= tkFont.Font(family="Verdana", size=12, weight="bold")

spacer = tk.Frame(master=window,height=160,bg="#000424")
spacer.pack(fill=tk.X)

title = tk.Label(text="okokokokok",font=titleFont,bg="#000424",fg="white")
title.pack()

subtitle = tk.Label(text="A Story",font=subtitleFont,bg="#000424",fg="white")
subtitle.pack()

spacer2 = tk.Frame(master=window,height=20,bg="#000424")
spacer2.pack(fill=tk.X)

spacer3 = tk.Frame(master=window,height=20,width=160,bg="#000424")
spacer3.pack(fill=tk.X)

link1 = tk.Button(master=window,text="HEFOUNDYOU :(", command=ccmd.link1cmd)

link2 = tk.Button(master=window,text="ARBORS KILLED YOU", command=ccmd.link2cmd)

photo12 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\entity2.png",width=480,height=240)

Label12 = tk.Label(window,image=photo12)

photo11 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\dead.png",width=480,height=240)

Label11 = tk.Label(window,image=photo11)

photo10 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\attic.png",width=320,height=240)

Label10 = tk.Label(window,image=photo10)

photo9 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\closedeye.png")

Label9 = tk.Label(master=eye,image=photo9)

photo8 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\openeye.png")

Label8 = tk.Label(master=eye,image=photo8)

photo7 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\doorstairs.png",width=320,height=240)

Label7 = tk.Label(window,image=photo7)

photo6 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\entity.png")

Label6 = tk.Label(window,image=photo6)

photo5 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\house_outside.png")

Label5 = tk.Label(window,image=photo5)

photo4 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\void_death.png")

Label4 = tk.Label(window,image=photo4)

photo3 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\wc2.png")

Label3 = tk.Label(window,image=photo3)

photo2 = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\thirdeye.png")

Label2 = tk.Label(window,image=photo2)

photo = tk.PhotoImage(file = r"C:\Users\ycp.cadet\Downloads\Programs\okokokokok1.1\imgs\spooky.png",width=320,height=240)

Label = tk.Label(window,image=photo)

eye.withdraw()

glitch = tk.Label(text=glitchText,
                   font=titleFont,
                   bg="#000424",
                   fg="red",)

title2 = tk.Label(text=titleTwo,
                   font=titleFont,
                   bg="#000424",
                   fg="white",)

credit = tk.Label(text=creditText,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt1 = tk.Label(text=textOne,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt2 = tk.Label(text=textTwo,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt3 = tk.Label(text=textThree,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt4 = tk.Label(text=textFour,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt5 = tk.Label(text=textFive,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt6 = tk.Label(text=textSix,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt7 = tk.Label(text=textSeven,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt8 = tk.Label(text=textEight,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)

txt9 = tk.Label(text=textNine,
                   font=bodyFont,
                   bg="#000424",
                   fg="white",)
def voidDeath():
        trapped = tk.Toplevel()
        trapped.configure(bg="black")
        lbl1 = tk.Label(master=trapped,text="TRAPPED",font=titleFont,bg="black",fg="white")
        lbl2 = tk.Label(master=trapped,text="INSIDE",font=titleFont,bg="black",fg="white")
        lbl3 = tk.Label(master=trapped,text="THE VOID",font=titleFont,bg="black",fg="white")
        lbl1.pack()
        trapped.after(400,lambda:lbl2.pack())
        trapped.after(800,lambda:lbl3.pack())
        trapped.after(1200,lambda:ccmd.hideWidget(lbl1))
        trapped.after(1600,lambda:ccmd.hideWidget(lbl2))
        trapped.after(2000,lambda:ccmd.hideWidget(lbl3))
        trapped.after(2400,lambda:lbl1.pack())
        trapped.after(2800,lambda:lbl2.pack())
        trapped.after(3200,lambda:lbl3.pack())
        trapped.after(3600,lambda:ccmd.hideWidget(lbl1))
        trapped.after(4000,lambda:ccmd.hideWidget(lbl2))
        trapped.after(4400,lambda:ccmd.hideWidget(lbl3))
        trapped.after(4800,lambda:lbl1.pack())
        trapped.after(5200,lambda:lbl2.pack())
        trapped.after(5600,lambda:lbl3.pack())
        trapped.after(5950,lambda:trapped.geometry("10000x10000"))
        trapped.after(6000,lambda:trapped.withdraw())
def pageShift():
    title.configure(text="""
okokokokokokokokokokokokokokokokokokok
okokokokokokokokokokokokokokokokokokok
okokokokokokokokokokokokokokokokokokok
okokokokokokokokokokokokokokokokokokok
okokokokokokokokokokokokokokokokokokok
okokokokokokokokokokokokokokokokokokok
okokokokokokokokokokokokokokokokokokok
okokokokokokokokokokokokokokokokokokok
okokokokokokokokokokokokokokokokokokok""",
                    fg="#590000")
    title.pack()
    window.after(200,lambda: ccmd.hideWidget(title))

def finalPage():
        ccmd.destroyWidget(Label12)
        ccmd.destroyWidget(txt9)
        ccmd.destroyWidget(button13)
        ccmd.destroyWidget(button12)
        window.configure(bg="white")
        def endCredits():
                window.configure(bg="#000424")
                spacer.pack()
                title2.pack()
                credit.pack()
        window.after(500,lambda: endCredits())

def eleventhPage():
        ccmd.destroyWidget(button8)
        ccmd.destroyWidget(button9)
        ccmd.destroyWidget(txt6)
        ccmd.destroyWidget(Label7)
        pageShift()
        def pageEleven():
                Label12.pack()
                txt9.pack()
                button12.pack()
                button13.pack()
        window.after(200, lambda:pageEleven())

def tenthPage():
        ccmd.destroyWidget(Label10)
        ccmd.destroyWidget(txt7)
        ccmd.destroyWidget(button10)
        ccmd.destroyWidget(button11)
        pageShift()
        def pageTen():
                Label11.pack()
                txt8.pack()
                link2.pack()
                deadButton.pack()
        window.after(200,lambda:pageTen())
def ninthPage():
        ccmd.hideWidget(button9)
        ccmd.hideWidget(button8)
        ccmd.hideWidget(Label7)
        ccmd.hideWidget(txt6)
        pageShift()
        def pageNine():
                Label10.pack()
                txt7.pack()
                button11.pack()
                button10.pack()
        window.after(200,lambda:pageNine())
def seventhPage():
    ccmd.destroyWidget(Label5)
    ccmd.destroyWidget(txt5)
    ccmd.destroyWidget(button7)
    ccmd.destroyWidget(button6)
    ccmd.hideWidget(Label10)
    ccmd.hideWidget(txt7)
    ccmd.hideWidget(button11)
    ccmd.hideWidget(button10)
    pageShift()
    def pageSeven():
        Label7.pack()
        txt6.pack()
        button8.pack()
        button9.pack()
    window.after(200,lambda:pageSeven())

def eighthPage():
    ccmd.destroyWidget(Label5)
    ccmd.destroyWidget(txt5)
    ccmd.destroyWidget(button7)
    ccmd.destroyWidget(button6)
    pageShift()
    def pageEight():
        Label6.pack()
        link1.pack()
        deadButton.pack()
    window.after(200,lambda:pageEight())

def sixthPage():
    ccmd.destroyWidget(Label3)
    ccmd.destroyWidget(txt3)
    ccmd.destroyWidget(button4)
    ccmd.destroyWidget(button5)
    ccmd.destroyWidget(Label12)
    ccmd.destroyWidget(txt9)
    ccmd.destroyWidget(button13)
    ccmd.destroyWidget(button12)
    ccmd.hideWidget(glitch)
    pageShift()
    def pageSix():
        Label4.pack()
        txt4.pack()
        deadButton.pack()
        voidDeath()
    window.after(200,lambda:pageSix())

def fifthPage():
    ccmd.destroyWidget(Label3)
    ccmd.destroyWidget(txt3)
    ccmd.destroyWidget(button4)
    ccmd.destroyWidget(button5)
    ccmd.hideWidget(glitch)
    pageShift()
    def pageFive():
        Label5.pack()
        txt5.pack()
        button6.place(x=265,y=400)
        button7.place(x=310,y=400)
    window.after(200,lambda: pageFive())

def fourthPage():
    ccmd.destroyWidget(Label2)
    ccmd.destroyWidget(txt2)
    ccmd.destroyWidget(button3)
    pageShift()
    def pageFour():
        Label3.pack()
        txt3.pack()
        button4.place(x=255,y=430)
        button5.place(x=335,y=430)
    window.after(200,lambda: pageFour())
    window.after(500,lambda: censor())
    
def thirdPage():
    ccmd.destroyWidget(Label)
    ccmd.destroyWidget(button2)
    ccmd.destroyWidget(txt1)
    pageShift()
    def pageThree():
        Label2.pack()
        txt2.pack()
        button3.pack()
    window.after(200,lambda: pageThree())
    window.after(500,lambda: blink())

def secondPage():
    ccmd.hideWidget(title)
    ccmd.destroyWidget(subtitle)
    ccmd.hideWidget(spacer2)
    ccmd.hideWidget(spacer3)
    ccmd.hideWidget(spacer4)
    ccmd.hideWidget(spacer5)
    ccmd.hideWidget(spacer)
    ccmd.destroyWidget(button)
    Label.pack()
    txt1.pack()
    button2.pack()
    pageShift()
    wc = tk.Tk()
    wc.title("Are You Ok?")
    wc.configure(bg="yellow")
    place = tk.Label(master=wc,bg="yellow",text=":::::::::::;;"";;::;;:;:das;>><::<:>:?D/S::SA:???:?:?:::??:??SD::")
    place.pack()
    wc.after(750,lambda: wc.destroy())

deadButton = tk.Button(master=window,
                    text="you died. rebirth?",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=ccmd.restart,
                    bg="#000424",
                    fg="white")

button13 = tk.Button(master=window,
                    text="REMEMBER",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=finalPage,
                    bg="#000424",
                    fg="white")

button12 = tk.Button(master=window,
                    text="FORGET",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=sixthPage,
                    bg="#000424",
                    fg="white")

button11 = tk.Button(master=window,
                    text="Go back",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=seventhPage,
                    bg="#000424",
                    fg="white")

button10 = tk.Button(master=window,
                    text="Go deeper in the attic",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=tenthPage,
                    bg="#000424",
                    fg="white")

button9 = tk.Button(master=window,
                    text="Take the stairs",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=ninthPage,
                    bg="#000424",
                    fg="white")

button8 = tk.Button(master=window,
                    text="Go through the door",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=eleventhPage,
                    bg="#000424",
                    fg="white")

button7 = tk.Button(master=window,
                    text="Turn around",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=eighthPage,
                    bg="#000424",
                    fg="white")

button6 = tk.Button(master=window,
                    text="Go in",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=seventhPage,
                    bg="#000424",
                    fg="white")

button5 = tk.Button(master=window,
                    text="Stop",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=sixthPage,
                    bg="#000424",
                    fg="white")

button4 = tk.Button(master=window,
                    text="Keep Going",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=fifthPage,
                    bg="#000424",
                    fg="white")

button3 = tk.Button(master=window,
                    text="Move Through The Woods",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=fourthPage,
                    bg="#000424",
                    fg="white")

button2 = tk.Button(master=window,
                    text="CONTINUE???",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=thirdPage,
                    bg="#000424",
                    fg="white")

button = tk.Button( master=spacer3,
                    text="START",
                    relief=tk.RAISED,
                    borderwidth=5,
                    command=secondPage,
                    bg="#000424",
                    fg="white")

spacer4 = tk.Frame(master=window,height=20,bg="#000424")
spacer4.pack(fill=tk.X)

spacer5 = tk.Frame(master=window,height=2000,bg="#000424")
spacer5.pack(fill=tk.BOTH)
button.pack()
window.mainloop()
#VER 1.0 IS FINALLY FINISHED!!!!!!!! TODO: add more glitch stuff / window popups / jumpscares maybe!!!