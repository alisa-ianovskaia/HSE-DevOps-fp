import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from proper_solution import calc_rain_water

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get("/index")
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post("/result")
async def show_plot(request: Request, heights: str = Form(...)):

    params = [int(x) for x in heights.split(',')]
    result = calc_rain_water(params)

    return templates.TemplateResponse('result.html', {'request': request,
                                                      'result': result})


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host="0.0.0.0", reload=True)