from Utils.validation import Message
from pydantic import Json
import cv2
from PIL import Image as IMG
from Utils.ocr import detect2



class Routes():
    # def __init__(self,app,stream):
    #     self.app = app
    #     self.routes_stream = stream
    #     self.stream = stream.get_stream()
    #     self.switch = True
    #     self.text = ""


    # def load(self):
    #     print("function load -- Loading Request")
    #     app = self.app
    #     stream = self.stream
    #     text = self.text

    #     @app.post("/update_text/")
    #     async def update_text(message:Message):         
    #         stream.save_picture()
    #         image = IMG.open("./picture.jpg")
    #         text = detect2(image)
    #         return text

    #     @app.post("/load_picture/")
    #     async def load_picture(message:Message):
    #         image = IMG.open("./picture.jpg")
    #         print("MANAGING THE PICTURE!!!!!!!!!!!!!")
    #         #text = detect2(image)
    #         #return text

    #     print("Request loaded")
    pass