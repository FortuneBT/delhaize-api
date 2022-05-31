from fastapi import Request
from fastapi.responses import HTMLResponse,StreamingResponse
from Utils.camera import Webcam
from Utils.camera import Stream
from Utils.validation import Switch

class Routes():
    # def __init__(self,app):
    #     self.app = app
    #     self.start_stream()

    # def get_stream(self):
    #     return self.stream

    # def get_switch(self):
    #     return self.switch

    # def set_switch(self,switch):
    #     self.switch = switch

    # def start_stream(self):
    #     print("function start_stream")
    #     self.stream = Stream()
    #     self.switch = True
    #     self.text = ""


    # def load(self):
    #     print("function load -- Loading Cameras")
    #     app = self.app
    #     #self.stream.start()
    #     stream = self.stream
    #     webcam = Webcam()
    #     webcam2 = Webcam()
    #     webcam3 = Webcam()
    #     webcam4 = Webcam()
    #     webcam5 = Webcam()


    #     @app.get("/video_original/",response_class=HTMLResponse)
    #     async def video_original(request:Request):
    #         print("webcam : ",webcam.get_switch())
    #         return StreamingResponse(webcam.generate(stream,"original"),
    #         media_type="multipart/x-mixed-replace;boundary=frame"
    #         )


    #     @app.get("/video_gray/",response_class=HTMLResponse)
    #     async def video_gray(request:Request):
    #             print("webcam2 : ",webcam2.get_switch())
    #             return StreamingResponse(webcam2.generate(stream,"gray"),
    #             media_type="multipart/x-mixed-replace;boundary=frame"
    #             )


    #     @app.get("/video_blurr/",response_class=HTMLResponse)
    #     async def video_blurr(request:Request):
    #         print("webcam3 : ",webcam3.get_switch())
    #         return StreamingResponse(webcam3.generate(stream,"blurr"),
    #         media_type="multipart/x-mixed-replace;boundary=frame"
    #         )


    #     @app.get("/video_thresold/",response_class=HTMLResponse)
    #     async def video_thresold(request:Request):
    #         print("webcam4 : ",webcam4.get_switch())
    #         return StreamingResponse(webcam4.generate(stream,"thresold"),
    #         media_type="multipart/x-mixed-replace;boundary=frame"
    #         )


    #     @app.get("/video_frame/",response_class=HTMLResponse)
    #     async def video_frame(request:Request):
    #         print("webcam5 : ",webcam5.get_switch())
    #         self.text = stream.get_text()
    #         return StreamingResponse(webcam5.generate(stream,"video_frame"),
    #         media_type="multipart/x-mixed-replace;boundary=frame"
    #         )

    #     @app.post("/switch/")
    #     async def switch(switch:Switch):
            
    #         print("get switch : ",self.get_switch())
    #         switch = switch.dict()
    #         print("Changing switch state")
    #         self.set_switch(switch["state"])
    #         print("switch state changed to : ",self.get_switch())
    #         webcam.set_switch(switch["state"])
    #         webcam2.set_switch(switch["state"])
    #         webcam3.set_switch(switch["state"])
    #         webcam4.set_switch(switch["state"])
    #         webcam5.set_switch(switch["state"])
    #         print("webcam5 : ",webcam.get_switch())
    #         print("webcam5 : ",webcam2.get_switch())
    #         print("webcam5 : ",webcam3.get_switch())
    #         print("webcam5 : ",webcam4.get_switch())
    #         print("webcam5 : ",webcam5.get_switch())
    #         if switch["state"] == True:
    #             self.start_stream()
    #             print("start streaming")
    #             self.load()
    #             print("routes loaded")
    #         return {"Switch State":switch["state"]}

    #     print("Stream loaded")

    pass