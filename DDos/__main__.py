from DDos import DDos, checkUrl
from re import compile, match
from tkinter import Tk
from tkinter.messagebox import showerror
from tkinter.simpledialog import askstring
def main():
    int_re, root = compile(r'^\d+$'), Tk()
    root.withdraw()
    while True:
        url = askstring("URL", "        Enter the url for the attack        ")
        if checkUrl(url): break
        elif url is not None:
            root.bell()
            showerror("Error", "Not a valid url, try again")
        else: exit()
    while True:
        sockets = askstring("SOCKETS", "Enter the number of sockets for the attack", initialvalue = "500")
        if match(int_re, sockets): break
        elif sockets is not None:
            root.bell()
            showerror("Error", "Not a valid number, try again")
        else: exit()
    while True:
        threads = askstring("THREADS", "Enter the number of threads for the attack", initialvalue = "10")
        if match(int_re, threads): break
        elif threads is not None:
            root.bell()
            showerror("Error", "Not a valid number, try again")
        else: exit()
    DDos(url, int(sockets), int(threads))
if __name__ == "__main__": main()