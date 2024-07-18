import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy import text as liketext
from flask import Flask,jsonify
engine_dbsica=create_engine('postgresql://userboot:G4#m$2024+@192.168.11.3:5432/DBSICA')
engine_loges_sli=create_engine('postgresql://user_xml_tx_sunat:Sistem4s2024@192.168.11.3:5432/loges_sli')
def operativocarga_consultaprealerta(request ):
    num_agente = request.args.get('num_agente')
    token=  request.args.get('token') 
    query_tokenagente=f"SELECT * FROM  api_loges.entidades_api where tokenentidad='{token}' and codigoentidad='{num_agente}'"
    df_response_tokenagente = pd.read_sql(query_tokenagente, engine_loges_sli)
    if  df_response_tokenagente.empty:
        return  jsonify({"error": "Token no valido con agente"}), 400 
    
    if(request.method=='POST'):
        if request.is_json:
            data = request.get_json()
            master = data.get('master')
            query_openpost = open('querys\query_agenteaereoxmaster.sql') 
            query_agentemaster = query_openpost.read() 
            query_agentemaster = f"{query_agentemaster.replace('numero_agente', num_agente).replace('numero_master', master)}"
 
            df_agentemaster = pd.read_sql(query_agentemaster, engine_dbsica)
            json_result = df_agentemaster.to_json(orient='records')
        else:
            return  jsonify({"error": "Faltan campos obligatorios"}), 400      
    else:
        
        query_open = open('querys\query_agenteaereo.sql')
        
        query_agente = query_open.read()
        query_agente=query_agente.replace("numero_agente",num_agente)
        df_agente = pd.read_sql(query_agente, engine_dbsica)
        
        json_result = df_agente.to_json(orient='records')

     
    return json_result

