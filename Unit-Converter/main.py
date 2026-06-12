from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )

@app.get("/length")
def lenght(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="length.html"
    )

@app.post("/length")
def length_convert(
    request: Request,
    value: float = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...)
):

    units = {
        "Millimeter": 0.001,
        "Centimeter": 0.01,
        "Meter": 1,
        "Kilometer": 1000,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34
    }
    meter_value = value * units[from_unit]
    result = meter_value / units[to_unit]
    return templates.TemplateResponse(
        request=request,
        name="length.html",
        context={
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": result
        }
    )

@app.get("/weight")
def weight(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="weight.html",
    )

@app.post("/weight")
def weight(
    request:Request,
    value : float=Form(...),
     from_unit: str = Form(...),
    to_unit: str = Form(...)
):
    units = {
    "Milligram": 0.000001,
    "Gram": 0.001,
    "Kilogram": 1,
    "Ounce": 0.0283495,
    "Pound": 0.453592
    }

    kg_value = value * units[from_unit]

    result = kg_value / units[to_unit]

    return templates.TemplateResponse(
        request=request,
        name="weight.html",
        context={
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": result
        }
    )

@app.get("/temp")
def temp(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="temp.html"
    )


@app.post("/temp")
def temp(
    request: Request,
    value: float = Form(...),
    from_unit: str = Form(...),
    to_unit: str = Form(...)
):
    if from_unit == to_unit:
        result = value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result = (value - 273.15) * 9/5 + 32
    return templates.TemplateResponse(
        request=request,
        name="temp.html",
        context={
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": result
        }
    )