#

import webbrowser
import time

url = "www.youtube.com"
while True:
    print("Waiting...")
    time.sleep(600)
    print("Starting...")
    if webbrowser.open(url):
        print("Opening....")
    else:
        print("Can't open web browser.")
