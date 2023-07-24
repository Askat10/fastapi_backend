from fastapi import FastAPI

from fastapi.routing import APIRouter


from settings import DB_URL

app = FastAPI(
    title='Coursesanywhere'
)

@app.get('/')
def home_page():
    return {'message': 'hello'}