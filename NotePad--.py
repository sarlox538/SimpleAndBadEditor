import os

print("1 For Create A File\n2 To Edit a File\n3 To Delete A File\n4 To Read the File\n5 To Rename a File")
c = input("What do you want to do ? :")
c = int(c)


def CreateFile():
    f = open(input("Name of The File "), "w+")
    f.write("#This File was Created using BudgetNotepad#")
    f.close()


def EditFile():
    print("Warning! If You decide to Edit the File Pls Know that it will delete everything in it and Overwrite it!")
    f = open(input("Enter the File you Want To Edit 'With Path'"), "w+")
    print("This is in the Text Document")
    print(f.read())
    f.write(input("Now Write something"))
    f.close()


def DeleteFile():
    os.remove(input("Pls enter The Filename with Path"))


def ReadFile():
    f = open(input("Enter The File You Want to Read 'With Path'"), "r")
    print(f.read())


def RenameFile():
    os.rename(input("Enter The File you Want to Rename 'With Path'"), input("Enter The New Name"))


if c == 1:
    CreateFile()
elif c == 2:
    EditFile()
elif c == 3:
    DeleteFile()
elif c == 4:
    ReadFile()
elif c == 5:
    RenameFile()
