
from browser import document,html,ajax,bind
import json
from typing import Dict



print("Brython activated!!!!!")
print("Javascript = NO THANKS")


class Picture():
    def __init__(self):
        print("Initializing Picture")
        self.request1 = ajax.ajax()


    def load(self):
        print("function load -- request Picture")
        request1 = self.request1
        request1.bind('complete',self.on_complete)
        request1.open('POST',"/load_picture/",True)
        text = document["formFileLg"].value
        print("TEXT VALUE = ",text)
        filename = json.dumps({"text":text})
        request1.send(filename)
        print("Picture loaded")
    
    def on_complete(request1):
        print("On complete loading picture")
        if request1.status == 200 or request1.status == 0:
            print("LOADING IS COMPLETE")
        elif request1.status == 422:
            pass

class Switch_boutton():
    def __init__(self):
        print("Initializing switch_boutton") 
        print("start ajax switch")
        self.request3 = ajax.Ajax()
        self.state = False


    def change(self,state:bool):
        self.state = state
        if self.state == True:
            print("SWITCH IS ON")
        else:
            print("SWITCH IS OFF")

        url3 = "/switch/"
        self.request3.bind("complete",self.on_complete)
        self.request3.open("POST",url3,True)
        self.request3.set_header("content-type","application/json")
        self.request3.send(json.dumps({"state":state}))
        print("End ajax switch")
        print("!!SEND!!")


    def on_complete(request3):
        print("On complete switch button")
        if request3.status == 200 or request3.status == 0:
            print("SWITCH IS COMPLETE")         
        elif request3.status == 422:
            pass


class Stream_state():
    def __init__(self):
        print("Initializing switch_boutton") 
        print("start ajax stream")
        self.request4 = ajax.Ajax()


    def load(self,path):
        print("start function stream")
        print("stream the path:",path)
        url4 = path
        self.request4 = ajax.Ajax()
        self.request4.bind('complete', self.on_complete)
        self.request4.open('GET', url4, True)
        self.request4.send()
        print("Getting stream")

    def on_complete(request4):
        print("On complete stream")
        print("Request status = ",request4.status)
        if request4.status == 200 or request4.status == 0:
            print("stream of the path:",request4.responseText," of this path complete")
        else:
            print("Request status = ",request4.status)
            print("Request text = ",request4.text)
            print("STREAM ERROR")   

class Reboot():
    def __init__(self):
        print("Reboot activated")
        self.request5 = ajax.Ajax()


    def start(self):
        print("start function start")
        url = "/reboot/"
        self.request5.bind('complete', self.on_complete)
        self.request5.open('POST', url, True)
        self.request5.set_header('content-type', 'application/json')
        response = json.dumps({"state":"true"})
        self.request5.send(response)
        print("response = ",response)
        print("!!!!!!!SEND!!!!!!!")
        print("Starting reboot")
    
    def on_complete(request5):
        print("On complete start")
        if request5.status == 200 or request5.status == 0:
            print("START COMPLETE")
        elif request5.status == 422:
            pass


class Camera():
    def __init__(self):
        print("Camera initialized")
        print("start ajax camera")
        self.request = ajax.Ajax()

    def shoot(self):
        print("start function shoot")
        url2 = "/take_picture/"
        self.request.bind('complete', self.on_complete)
        self.request.open('POST', url2, True)
        self.request.set_header('content-type', 'application/json')
        #text = json.dumps({"text":"que la force soit avec toi!"})
        self.request.send()
        print("!!!!!!!SEND!!!!!!!")
            
    def on_complete(request):
        print("On complete shoot")
        if request.status == 200 or request.status == 0:
            document["text_to_show"].html = request.text
            document["my_button_picture"].text = "Restart"
            print("Change the text 'Take a picture' to 'Restart'")
        elif request.status == 422:
            document["text_to_show"].html = request.text
        else:
            document["text_to_show"].html = "error " + request.text



if "my_button_picture" in document:
    print("my_button_picture found")
    @bind('#my_button_picture',"click")             
    def clicked(ev):
        print("clicked on #my_button_picture !")
        print(ev.currentTarget.text)
        if ev.currentTarget.text == "Take a picture":
            cam = Camera()
            switch = Switch_boutton()
            switch.change(False)
            cam.shoot()
            document["my_button_picture"].text = "Restart"
            print("Change the text 'Take a picture' to 'Restart'")
            
        elif ev.currentTarget.text == "Restart":
            reboot = Reboot()
            switch = Switch_boutton()
            switch.change(True)
            reboot.start()
            # state_stream = Stream_state()
            # state_stream.load("/video_original/")
            # state_stream.load("/video_gray/")
            # state_stream.load("/video_blurr/")
            # state_stream.load("/video_thresold/")
            # state_stream.load("/video_frame/")
            
            document["my_button_picture"].text = "Take a picture"
            print("Change the text 'Restart' to 'Take a picture'")
            
            

if "my-loaded-image" in document:
    print("my_loaded_image found")
    @bind('#button-load-image',"click")             
    def image_loaded(ev):
        print("loaded on #my-loaded-image !")
        print(ev.currentTarget.src)
        if ev.currentTarget.src == "picture.jpg":
            print("empty")
        else:
            print("not empty")
else:
    print("!!!!!!!!!!my_loaded_image not found")
            

