from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from pydantic import EmailStr
from starlette.requests import Request
import requests, time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host="redis-12837.c14.us-east-1-3.ec2.cloud.redislabs.com",
    port=12837,
    password="qPhmlPlCZCfWHUu6tX6LV7OzRv7s6hIz",
    decode_responses=True
)


class User(HashModel):
    username: str
    password: str
    email: EmailStr
    total_amount: float

    class Meta:
        database = redis


@app.get('/users')
def all():
    return [format(pk) for pk in User.all_pks()]


def format(pk: str):
    user = User.get(pk)

    return {
        'id': user.pk,
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'total_amount': user.total_amount
    }

@app.post('/users')
def create(user: User):
    return user.save()


@app.post('/login')
async def create(request: Request):
    body = await request.json()
    # res = User.find((User.username == body['username']) & (User.password == body['password'])).all()
    return body


@app.get('/users/{pk}')
def get(pk: str):
    return User.get(pk)


@app.delete('/users/{pk}')
def delete(pk: str):
    return User.delete(pk)
