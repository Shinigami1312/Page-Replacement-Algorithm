from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


def fifo(capacity, inputstr):
    f, fault, top = [], 0, 0
    for i in inputstr:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
            else:
                f[top] = i
                top = (top + 1) % capacity
            fault += 1

    return fault


def lru(capacity, inputstr):
    fault = 0
    frameList = [-1] * capacity
    countOlder = [0] * capacity

    for i in range(capacity):
        frameList[i] = inputstr[i]
        countOlder = UpdateOlder(countOlder, frameList)
        fault += 1
    for j in range(capacity, len(inputstr)):
        if(frameList.count(inputstr[j]) == 0):
            fault += 1
            frameList[countOlder.index(max(countOlder))] = inputstr[j]
            countOlder[countOlder.index(max(countOlder))] = 0
        else:
            countOlder[frameList.index(inputstr[j])] = 0
        countOlder = UpdateOlder(countOlder, frameList)

    return fault

def UpdateOlder(countOlder, frameList):
    for i in range(len(countOlder)):
        if frameList[i] != -1:
            countOlder[i] += 1
    return countOlder


def opt(capacity, inputstr):
    fault = 0
    frameList = [-1] * capacity
    point = 0
    for i in range(len(inputstr)):
        if point < capacity:
            frameList[i] = inputstr[i]
            fault += 1
            point += 1
        elif frameList.count(inputstr[i]) == 0:
            fault += 1
            checkFar = [1] * capacity
            for j in range(i+1, len(inputstr)):
                if checkFar.count(1) <= 1:
                    break
                if frameList.count(inputstr[j]) != 0:
                    checkFar[frameList.index(inputstr[j])] = 0
            frameList[checkFar.index(1)] = inputstr[i]

    return fault



def getvals():
    frames = framevalue.get()
    pagestring = stringvalue.get()
    algorithm = algovalue.get()

    if frames == "" or pagestring == '' or algorithm == "":
        messagebox.showerror("Error", "Fill all the information!!")
    else:
        list(pagestring)
        if algorithm == "fifo":
            pagefault = fifo(int(frames), pagestring)
        if algorithm == "lru":
            pagefault = lru(int(frames), pagestring)
        if algorithm == "opt":
            pagefault = opt(int(frames),pagestring)

        pagehit = len(pagestring) - pagefault
        pagefaultratio = (pagefault/len(pagestring))*100
        pagefaultratio = '{:.2f}'.format(pagefaultratio)
        pagehitratio = (pagehit/len(pagestring))*100
        pagehitratio = '{:.2f}'.format(pagehitratio)

        pagefaultans_label.configure(text=pagefault)
        pagehitans_label.configure(text=pagehit)
        pagefaultratioans_label.configure(text=pagefaultratio)
        pagehitratioans_label.configure(text=pagehitratio)


# GUI starts here
root = Tk()

# width x height
root.geometry("1000x750")
root.resizable(0, 0)
# root.configure(bg="white")
root.title("OS PROJECT")

# labeling

title_label = Label(root, text="Page Replacement Algorithm", bg="CYAN", font="comicsansms 30 bold", width=100)
title_label.pack(fill=X)

frame_label = Label(root, text="Frame Size : ", bg="YELLOW", font="comicsansms 20 bold", width=10)
frame_label.place(x=250, y=100)

string_label = Label(root, text="Enter String: ", bg="YELLOW", font="comicsansms 20 bold", width=10)
string_label.place(x=250, y=140)

algo_label = Label(root, text="Algorithm   : ", bg="YELLOW", font="comicsansms 20 bold", width=10)
algo_label.place(x=250, y=182)

pagehit_label = Label(root, text="Page Hits: ", bg="YELLOW", font="comicsansms 20 bold", width=14)
pagehit_label.place(x=100, y=500)

pagehitans_label = Label(root, text="0", bg="RED", font="comicsansms 20 bold", width=5)
pagehitans_label.place(x=360, y=500)

pagefault_label = Label(root, text="Page Faults: ", bg="YELLOW", font="comicsansms 20 bold", width=14)
pagefault_label.place(x=500, y=500)

pagefaultans_label = Label(root, text="0", bg="RED", font="comicsansms 20 bold", width=5)
pagefaultans_label.place(x=760, y=500)

pagehitratio_label = Label(root, text="Page Hit Ratio: ", bg="YELLOW", font="comicsansms 20 bold", width=14)
pagehitratio_label.place(x=100, y=570)

pagehitratioans_label = Label(root, text="0", bg="RED", font="comicsansms 20 bold", width=5)
pagehitratioans_label.place(x=360, y=570)

pagefaultratio_label = Label(root, text="Page Fault Ratio: ", bg="YELLOW", font="comicsansms 20 bold", width=14)
pagefaultratio_label.place(x=500, y=570)

pagefaultratioans_label = Label(root, text="0", bg="RED", font="comicsansms 20 bold", width=5)
pagefaultratioans_label.place(x=760, y=570)


# Variables
dropdown = [1,2,3,4,5,6,7,8,9,10]
framevalue = IntVar()
framevalue.set(dropdown[0])
stringvalue = StringVar()
algovalue = StringVar()
algovalue.set("fifo")  # This is done so that all the buttons aren't checked

frameentry = Combobox(root, textvariable=framevalue, width=20, value=dropdown, font="comicsansms 19 bold", state="readonly")
stringentry = Entry(root, textvariable=stringvalue, width=20, font="comicsansms 20 bold")
fifoentry = Radiobutton(root, text="First In First Out", variable=algovalue, value="fifo", font="comicsansms 20 bold")
optentry = Radiobutton(root, text="Optimal Page Replacement ", variable=algovalue, value="opt", font="comicsansms 20 bold")
lruentry = Radiobutton(root, text="Least Recently Used", variable=algovalue, value="lru", font="comicsansms 20 bold")

frameentry.place(x=440, y=100)
stringentry.place(x=440, y=140)
fifoentry.place(x=440, y=180)
optentry.place(x=440, y=220)
lruentry.place(x=440, y=260)

# Button
cal = Button(root, text="Submit", bg="ORANGE", width=20, height=2, command=getvals, font="comicsansms")
cal.place(x=380, y=370)

root.mainloop()