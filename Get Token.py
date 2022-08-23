import requests
import json


def obtener_token(usuario, clave):
    url = "https://127.0.0.1:58000/api/v1/ticket"
    body = {
            "attributes": {
                "username" : "admin",
                "password" : "admin123!"
            }
        }
    cabecera = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()['imdata'][0]['attributes']

return token

token = obtener_token("admin", "admin123!")
print(token)