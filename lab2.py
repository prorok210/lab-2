from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Calc(BaseModel):
    x: float
    y: str
    z: float
@app.post('/')
def calc(data: Calc):
   x = float(data.x)
   y = data.y
   z = float(data.z)
   if y == '+':
       return x + z
   elif y == '-':
       return x - z
   elif y == '*':
       return x * z
   elif y == '/' and z != 0:
       return x / z
   else: return 'деление на 0'
