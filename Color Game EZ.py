import tkinter
import random

#we add the list of possible colors
colours = ['Red','Blue','Yellow','Green','Black','Pink','Orange','White','Purple','Brown']

#set original score to 0
score = 0

#set the orginial amount of time
timeLeft = 60

#now we have to start the game
def startGame(event):
    if timeLeft == 60:
        #start countdown timer(not defined yet)
        countdown()
    # We have choose the next color to show (not defined yet)
    nextColour()
    
# define nextColour
def nextColour():
    #global lets us modify the variable from anywhere
    global score
    global timeLeft
    #if the game is in play
    if timeLeft > 0:
        #to make the text box in tkinter active
        e.focus_set()
        #if the user gets the colour right...
        #also makes text lower to avoid confusion
        if e.get().lower()==colours[1].lower():
            
            score+=1
        #now we have to clear the text box for the next question
        e.delete(0, tkinter.END)
        
        random.shuffle(colours)
        
        #now we have to change the color type, by changing the text and color to a random colour value
        #We usse the shuffle() function to reorder items in the list and display the color label with the text 
        #as the first color in the list and the font color as the second color in the list. Use the config() 
        # function on scoreLabel (that asks to press Enter) to display the score as the game is in session.
        label.config(fg=str(colours[1]), text=str(colours[0]))
        #update the score
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeLeft
    #if game is in play
    if timeLeft>0:
        timeLeft -= 1
        timeLabel.config(text = "Time left: "+ str(timeLeft))
        #now we have to run the same function again a second later to make a functioning countdown
        timeLabel.after(1000, countdown)
               
root = tkinter.Tk()
root.title("Color Game With a Twist")
root.geometry("800x300")
root.configure(background='Grey')
 
# add an instructions label
instructions = tkinter.Label(root, text = "Type in the colour of the words, and not the word text!", font = ('Comic Sans MS', 20), bg= "grey")
instructions.pack()

 
# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Comic Sans MS', 15), bg= "grey")
scoreLabel.pack()
 
# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeLeft), font = ('Comic Sans MS', 15), bg= "grey")
               
timeLabel.pack()

 
# add a label for displaying the colours
label = tkinter.Label(root, font = ('Comic Sans MS', 60), bg= "grey")
label.pack()
 
# add a text entry box for
# typing in colours
e = tkinter.Entry(root)
 
# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
 
# set focus on the entry box
e.focus_set()
 
# start the GUI
root.mainloop()