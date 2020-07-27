import os

def Get_Value():
    print("1 For Create A File\n2 To Edit a File\n3 To Delete A File\n4 To Read the File\n5 To Rename a File")
    while True:
        c = input("What do you want to do ? :")
        try:
            c = int(c)
            return c
        except ValueError:
            break
def createfile():
    c = Get_Value()
    if c == 1:
        f = open(input("Name of The File "), "w+")
        f.write("#This File was Created using BudgetNotepad#")
        f.close()
def editfile():
    c = Get_Value()
    if c == 2:
        print("Warning! If You decide to Edit the File Pls Know that it will delete everything in it and Overwrite it!")
        f = open(input("Enter the File you Want To Edit 'With Path'"), "w+")
        print("This is in the Text Document")
        print(f.read())
        f.write(input("Now Write something"))
        f.close()
def deletefile():
    c = Get_Value()
    if c == 3:
        os.remove(input("Pls enter The Filename with Path"))
def ReadFile():
    c = Get_Value()
    if c == 4:
        f = open(input("Enter The File You Want to Read 'With Path'"), "r")
        print(f.read())
def RenameFile():
    c = Get_Value()
    if c == 5:
        os.rename(input("Enter The File you Want to Rename 'With Path'"), input("Enter The New Name"))

Get_Value()
RenameFile()
ReadFile()
deletefile()
editfile()
createfile()
