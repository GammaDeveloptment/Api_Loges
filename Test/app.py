from flask import Flask, request

import prop 
import pandas as pd
# from markupsafe import escape
app = Flask(__name__)

@app.route("/ws-loges-client/<num_agente>"  )
def agente_aereo(num_agente): 
     
    # num_agente = req['num_agente']
    data_json=prop.Agente_aereo(num_agente)
    # print(data_json)
    return  data_json
@app.route("/<username>"  )
def hello_world(username): 
    
    return f"hola mundo{username}  "

 