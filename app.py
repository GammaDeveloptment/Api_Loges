from flask import Flask, request,jsonify
from sqlalchemy import create_engine 
import prop 
import pandas as pd
from flask_cors import CORS, cross_origin
engine_dbsica=create_engine('postgresql://userboot:G4#m$2024+@192.168.11.3:5432/DBSICA')
engine_factura=create_engine('postgresql://userboot:G4#m$2024+@192.168.11.3:5432/BOTDB')
engine_loges_sli=create_engine('postgresql://user_xml_tx_sunat:Sistem4s2024@192.168.11.3:5432/loges_sli')


# from markupsafe import escape
app = Flask(__name__)
CORS(app)


@cross_origin
@app.route("/ws1/<negocio>/<servicio>", methods=['GET', 'POST'])
def agente_aereo(negocio,servicio): 
    token = request.args.get('token') 
    query_servicio=f"SELECT * FROM api_loges.servicios where nombreservicio='{servicio}' "
    query_negocio=f"SELECT * FROM api_loges.negocio where carpeta='{negocio}'"
    query_token=f"SELECT * FROM  api_loges.entidades_api where tokenentidad='{token}'"
     
    if not token :
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    df_response_ngc = pd.read_sql(query_negocio, engine_loges_sli)
    df_response_svc = pd.read_sql(query_servicio, engine_loges_sli)
    df_response_token = pd.read_sql(query_token, engine_loges_sli)
    if  df_response_token.empty:
        return  jsonify({"error": "Token no valido"}), 400
     
    if df_response_ngc.empty or  df_response_svc.empty or df_response_token.empty:
        return jsonify({"error": "Consulta no valida"}), 400
    
        
    funcion=f"{negocio}_{servicio}"
    if hasattr(prop, funcion): 
        funcion_a_llamar = getattr(prop, funcion,request.args)
        data_json = funcion_a_llamar(request) 
    else :
        data_json="Error, no aplica"
    return  data_json


@cross_origin
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Manejar datos enviados por POST
        nombre = request.form.get('nombre')
        return f'Datos recibidos: {nombre}'
    else:
        # Mostrar formulario para GET
        return  ""
    
@cross_origin
@app.route("/errorbl" )
def reporte( ): 
    print("entro")
    query_facturaproc= "select * from reporte_factura where estado='Error, bhm no encontrado' "
    df_response_facterrbl = pd.read_sql(query_facturaproc, engine_factura)
    if 'fecha_proceso' in df_response_facterrbl.columns:   
        # print(df_response_facterrbl['fecha_proceso'])
        df_response_facterrbl['fecha_proceso'] = pd.to_datetime(df_response_facterrbl['fecha_proceso'])
        df_response_facterrbl['fecha_proceso'] = df_response_facterrbl['fecha_proceso'].dt.strftime('%d de %B  %Y')
    
    json_result = df_response_facterrbl.to_json(orient='records')
    
    return  json_result 

# @app.route("/<username>")
# def hello_world(username): 
    
#     return f"hola mundo{username}  "

 