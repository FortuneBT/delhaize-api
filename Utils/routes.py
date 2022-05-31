from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Utils.routes_stream import Routes as Routes_stream
from Utils.routes_page import Routes as Routes_page
from Utils.routes_request import Routes as Routes_request
from Utils.validation import Switch
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse,StreamingResponse
from PIL import Image as IMG
from Utils.ocr import detect2
from Utils.validation import Message
from Utils.camera import Webcam
from Utils.camera import Stream
from Utils.validation import Switch


class Routes():

    def __init__(self):
        self.app = FastAPI()
        self.app.mount("/static", StaticFiles(directory="./static"), name="static")
        self.templates = Jinja2Templates(directory="templates")
        self.webcam = Webcam()
        self.webcam2 = Webcam()
        self.webcam3 = Webcam()
        self.webcam4 = Webcam()
        self.webcam5 = Webcam()
        self.image = None
        self.requests = None
        self.stream = None
        self.pages = None
        self.switch = True
        self.text = ""
        
    def create(self):
        print("Create main routes")
        self.start()
        return self.app
        
    def stop_stream(self):
        print("Stop Web Application Delhaize")
        self.stream.stop()
        self.stream = None

    def restart_stream(self):
        print("Restart Web Application Delhaize")
        self.stop_stream()
        self.start()


    def get_stream(self):
        return self.stream

    def get_switch(self):
        return self.switch

    def set_switch(self,switch):
        self.switch = switch

    def start_stream(self):
        print("function start_stream")
        self.stream = Stream()
        self.set_switch(True)
        self.text = ""

    def start(self):
        print("Start Web Application Delhaize")
        app = self.app
        templates = self.templates
        self.start_stream()


        @app.post("/reboot/")
        def reboot(switch:Switch):
            print("REBOOT WebApplication")
            #my_dict = switch.dict()
            #response = my_dict["state"]
            self.restart_stream()
            print("restart stream")
            print("start cameras")

        
        print("Web Application Delhaize started")
            

        @app.get("/",response_class=HTMLResponse)
        async def index(request:Request):
            print("loading index")
            context = {"request":request}
            return templates.TemplateResponse("index.html",context)


        @app.get("/camera/",response_class=HTMLResponse)
        async def my_camera(request:Request):
            print("loading camera web page")
            context = {"request":request}
            return templates.TemplateResponse("camera.html",context)


        @app.get("/picture/",response_class=HTMLResponse)
        async def picture(request:Request):
            print("loading picture")
            context = {"request":request}
            return templates.TemplateResponse("picture.html",context)


        @app.get("/options/",response_class=HTMLResponse)
        async def options(request:Request):
            print("loading options")
            context = {"request":request}
            return templates.TemplateResponse("options.html",context)

        
        print("Pages loaded")

        
        @app.post("/take_picture/")
        async def take_picture():         
            self.stream.save_picture()
            picture = "./picture.jpg"
            self.image,jpg = self.stream.load_picture(picture)
            text = detect2(self.image)
            print("Request take a picture done")
            return text

        @app.post("/load_picture/")
        async def load_picture(message:Message):
            file_name = message
            self.image = self.stream.load_picture(file_name)
            print("Request loaded image")


        @app.get("/video_original/",response_class=HTMLResponse)
        def video_original(request:Request):
            print("webcam : ",self.webcam.get_switch_webcam())
            return StreamingResponse(self.webcam.generate(self.stream,"original"),
            media_type="multipart/x-mixed-replace;boundary=frame"
            )


        @app.get("/video_gray/",response_class=HTMLResponse)
        def video_gray(request:Request):
                print("webcam2 : ",self.webcam2.get_switch_webcam())
                return StreamingResponse(self.webcam2.generate(self.stream,"gray"),
                media_type="multipart/x-mixed-replace;boundary=frame"
                )


        @app.get("/video_blurr/",response_class=HTMLResponse)
        def video_blurr(request:Request):
            print("webcam3 : ",self.webcam3.get_switch_webcam())
            return StreamingResponse(self.webcam3.generate(self.stream,"blurr"),
            media_type="multipart/x-mixed-replace;boundary=frame"
            )


        @app.get("/video_thresold/",response_class=HTMLResponse)
        def video_thresold(request:Request):
            print("webcam4 : ",self.webcam4.get_switch_webcam())
            return StreamingResponse(self.webcam4.generate(self.stream,"thresold"),
            media_type="multipart/x-mixed-replace;boundary=frame"
            )


        @app.get("/video_frame/",response_class=HTMLResponse)
        def video_frame(request:Request):
            print("webcam5 : ",self.webcam5.get_switch_webcam())
            self.text = self.stream.get_text()
            return StreamingResponse(self.webcam5.generate(self.stream,"video_frame"),
            media_type="multipart/x-mixed-replace;boundary=frame"
            )

        @app.post("/switch/")
        def switch(switch:Switch):
            
            print("get switch : ",self.get_switch())
            switch = switch.dict()
            print("Changing switch state")
            self.set_switch(switch["state"])
            print("switch state changed to : ",self.get_switch())
            self.webcam.set_switch_webcam(switch["state"])
            self.webcam2.set_switch_webcam(switch["state"])
            self.webcam3.set_switch_webcam(switch["state"])
            self.webcam4.set_switch_webcam(switch["state"])
            self.webcam5.set_switch_webcam(switch["state"])
            print("self.webcam5 : ",self.webcam.get_switch_webcam())
            print("self.webcam5 : ",self.webcam2.get_switch_webcam())
            print("self.webcam5 : ",self.webcam3.get_switch_webcam())
            print("self.webcam5 : ",self.webcam4.get_switch_webcam())
            print("self.webcam5 : ",self.webcam5.get_switch_webcam())
            if switch["state"] == True:
                self.start_stream()
                print("start streaming")
            else:
                self.stop_stream()
                print("stop streaming")

            #return {"Switch State":switch["state"]}

        print("Stream loaded")