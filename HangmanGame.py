from tkinter import *
import random

##canvas.create_line(25, 5, 25, 200, tags = "line")
##canvas.create_line(25, 5, 95, 5, tags = "line")
##canvas.create_line(95, 5, 95, 30, tags = "line")

def displayHead(x):
    canvas.create_oval(160, 60 + x, 220, 120 + x,
                       width = 2, tags = "body")
    return

def displayBody(x):
    canvas.create_line(190, 120 + x, 190, 240 + x,
                       width = 2, tags = "body")
    canvas.create_line(186, 122 + x, 194, 122 + x,
                       width = 3, tags = "noose", fill = "saddlebrown")
    return

def displayLeftArm(x):
    canvas.create_line(190, 130 + x, 150, 240 + x,
                       width = 2, tags = "body")
    return

def displayRightArm(x):
    canvas.create_line(190, 130 + x, 230, 240 + x,
                       width = 2, tags = "body")
    return

def displayLeftLeg(x):
    canvas.create_line(190, 240 + x, 150, 360 + x,
                       width = 2, tags = "body")
    return

def displayRightLeg(x):
    canvas.create_line(190, 240 + x, 230, 360 + x,
                       width = 2, tags = "body")
    return

def displayNoose(x):
    canvas.create_line(190, 20, 190, 60 + x, width = 6,
                       tags = "noose", fill = "saddlebrown")

def dropMan():
    canvas.delete("plat", "body", "noose")
    canvas.create_rectangle(250, 370, 260, 490, tags = "plat",
                            fill = "saddlebrown")
    #canvas.create_rectangle(250, 370, 254, 420, tags = "plat", fill = "red")
    displayNoose(40)
    for i in range(6):
        bodyList[i](40)
    quitFrame.grid_remove()

#Word Replacer
def replaceWord():
    global hiddenWord
    hiddenWord.grid_remove()
    wordBuildPrint = ""
    for i in range(len(word)):
        wordBuildPrint += wordBuild[i] + " "
    hiddenWord = Label(wordFrame, text = str(wordBuildPrint), font = 4)
    hiddenWord.grid(row = 1, column = 1)

#Determine which button/letter was chosen and determine win/lose
def getletter(t,index):
    x = letbuttonlist[index]["text"]
    print(x)
    global strike
    found = False
    for i in range(len(word)):
        if t == letterList[i]:
            wordBuild[i] = t
            found = True
    if found:
        replaceWord()
    else:
        bodyList[strike](0)
        strike += 1
        canvas.delete("strikes")
        canvas.create_text(400, 20, text = "Strikes: " + str(strike),
                           tags = "strikes")
        canvas.create_text(400, 40, text = "Strikes Left: " + str(6 - strike),
                           tags = "strikes")
    if strike == 6:
        dropMan()
        letterframe.grid_remove()
        quitFrame.grid_remove()
        loseframe.grid()
        doneframe.grid()
    if "__" not in wordBuild:
        letterframe.grid_remove()
        quitFrame.grid_remove()
        winframe.grid()
        doneframe.grid()
    letbuttonlist[index]["state"] = "disable"
    
    return

def playagain():
    playAgain = "y"
    window.destroy()

def endgame():
    global playAgain
    playAgain = "n"
    window.destroy()
    startwindow()

def startwindow():
    global opening
    opening = Tk()
    opening.title("Hangman")
    photoFrame = Frame(opening)
    photoFrame.grid()
    openCanvas = Canvas(photoFrame, width = 600, height = 350)
    openCanvas.grid()
    gallows = PhotoImage(file = "Hangman_Title.gif")
    openCanvas.create_image(0, 0, image = gallows, anchor=NW)
    playFrame = Frame(opening)
    playButton = Button(playFrame, text = "Play", command = play)
    exitButton = Button(playFrame, text = "Exit", command = exitgame)
    playButton.grid(row = 1, column = 1)
    exitButton.grid(row = 1, column = 2)
    playFrame.grid()
    opening.mainloop()

def play():
    global playAgain
    playAgain = "y"
    opening.destroy()

def exitgame():
    global playAgain
    playAgain = "n"
    opening.destroy()
    

#Set up opening screen
startwindow()
        
#Set up game loop
newwindow = "y"
#playAgain = "y" #unmute this if you take out opening window

while playAgain == "y":
    window = Tk()
    window.title("Hangman")

    #Choose game word
    wordlist = ['DISCOMBOBULATED', 'KITTENS', 'BANDWAGON', 'ABRUPTLY', 'HAPHAZARD',
                'NIGHTCLUB', 'WRISTWATCH', 'ROGUE', 'KEYHOLE', 'FRIZZLED', 'PARTY',
                'SINGER', 'HAPPY', 'ASTRONOMY', 'ENTHUSIASTIC', 'DEVOTED', 'CAT', 'DOG',
                'HEAD', 'WATER', 'PERSON']
    word = wordlist[random.randint(0, len(wordlist)-1)]
    letterList = list(word)



    #Create canvas with text
    canvas = Canvas(window, width = 500, height = 520)

    canvas.grid()

    canvas.create_rectangle(-10, -10, 550, 550, tags = "back", fill = "red")
    canvas.create_rectangle(40, 10, 50, 360, tags = "rect", fill = "saddlebrown")
    canvas.create_rectangle(50, 10, 200, 20, tags = "rect", fill = "saddlebrown")
    displayNoose(0)
    canvas.create_rectangle(0, 360, 130, 370, tags = "rect", fill = "saddlebrown")
    canvas.create_rectangle(130, 360, 250, 370, tags = "plat", fill = "saddlebrown")
    canvas.create_rectangle(250, 360, 400, 370, tags = "rect", fill = "saddlebrown")
    canvas.create_rectangle(0, 370, 40, 500, tags = "rect", fill = "saddlebrown")
    canvas.create_rectangle(360, 370, 400, 500, tags = "rect", fill = "saddlebrown")

    #detail

    ##canvas.create_rectangle(23, 90, 25, 95, tags = "line", fill = "red")
    ##canvas.create_rectangle(40, 180, 60, 182, tags = "line", fill = "red")
    ##canvas.create_rectangle(100, 180, 125, 182, tags = "plat", fill = "red")

    bodyList = [displayHead, displayBody, displayLeftArm, displayRightArm,
                displayLeftLeg, displayRightLeg]

    #Create frame for word
    wordFrame = Frame(window)
    wordFrame.grid()
    wordBuild = []
    for i in range(len(word)):
        wordBuild.append("__")
    wordBuildPrint = ""
    for i in range(len(word)):
        wordBuildPrint += wordBuild[i] + " "
    hiddenWord = Label(wordFrame, text = str(wordBuildPrint), font = 4)
    hiddenWord.grid(row = 1, column = 1)
    strike = 0
    canvas.create_text(400, 20, text = "Strikes: " + str(strike),
                               tags = "strikes")

    quitFrame = Frame(window)
    quitFrame.grid()
    quitButton = Button(quitFrame, text = "Quit Game", command = endgame)
    quitButton.grid()

    #Create frame for letter buttons
    letterframe = Frame(window)
    letterframe.grid()



    letbuttonlist = [] #Letter button list
    #Generate Letter buttons and place in Letter button list
    for i in range(26):
        letter = chr(65+i)
        b = Button(letterframe, text = letter, command = lambda ltr=letter,
                   ltrnum=i: getletter(ltr,ltrnum))
        
        letbuttonlist.append(b)
        b.config(height = 2, width = 4)
        b.grid(row=i//13, column=i%13)

    #Create ending frames
    loseframe = Frame(window)
    loseLabel = Label(loseframe, text = "You lost, and have been hung.")
    winframe = Frame(window)
    winLabel = Label(winframe, text = "You won, and avoided getting hung.")
    doneframe = Frame(window)
    wordLabel = Label(doneframe, text = "The word was:\n" + word)
    playAgainButton = Button(doneframe, text = "Play Again", command = playagain)
    endButton = Button(doneframe, text = "End Game", command = endgame)
        
    loseLabel.grid()
    winLabel.grid()
    wordLabel.grid(columnspan = 3)
    playAgainButton.config(height = 2, width = 8)
    endButton.config(height = 2, width = 8)
    playAgainButton.grid(row = 2, column = 1)
    endButton.grid(row = 2, column = 2)

    if playAgain == "y":
        window.mainloop()


