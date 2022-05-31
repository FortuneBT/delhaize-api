from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


class Routes():
    # def __init__(self,app):
    #     print("initializing route page")
    #     print("Type of app = ",type(app))
    #     self.app = app
    #     self.templates = Jinja2Templates(directory="templates")

    # def load(self):
    #     print("function load -- Loading Pages")
    #     app = self.app
    #     templates = self.templates

    #     @app.get("/",response_class=HTMLResponse)
    #     async def index(request:Request):
    #         print("loading index")
    #         context = {"request":request}
    #         return templates.TemplateResponse("index.html",context)


    #     @app.get("/camera/",response_class=HTMLResponse)
    #     async def webcam(request:Request):
    #         print("loading webcam")
    #         context = {"request":request}
    #         return templates.TemplateResponse("camera.html",context)


    #     @app.get("/picture/",response_class=HTMLResponse)
    #     async def picture(request:Request):
    #         print("loading picture")
    #         context = {"request":request}
    #         return templates.TemplateResponse("picture.html",context)


    #     @app.get("/options/",response_class=HTMLResponse)
    #     async def options(request:Request):
    #         print("loading options")
    #         context = {"request":request}
    #         return templates.TemplateResponse("options.html",context)

        
    #     print("Pages loaded")
    pass