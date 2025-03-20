import webbrowser
import time
import os


chrome_path = webbrowser.get()

# List of URLs to open
urls = [
    "https://github.com",
    "https://mail.google.com",
    "https://stackoverflow.com",
    "https://visualgo.net/en"
    "https://www.youtube.com",
]


for url in urls:
    webbrowser.open_new_tab(url)
    time.sleep(1)  
