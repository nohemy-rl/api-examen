from fastapi import FastAPI
import requests
import json

app = FastAPI()

def generate_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

@app.get("/")
def consumir_api_chucknorris():
    elementos=[]

    for num in range(0,25):
        response = generate_request('https://api.chucknorris.io/jokes/random')
        
        if response and response.get('id') not in elementos:
            elementos.append(response.get('id'))

    return json.dumps(elementos)

