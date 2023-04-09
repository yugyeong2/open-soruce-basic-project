from tkinter import *

btnList = [None] * 9
fnameList = ["Bedtime_Bear.gif", "Cheer_Bear.gif", "Friend_Bear.gif", "Funshine_Bear.gif", "Good_Luck_Bear.gif", "Grumpy_Bear.gif", "Share_Bear.gif", "Tenderheart_Bear.gif", "Wish_Bear.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("210x210")

for i in range(0, 9) :
    photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()