import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy import text as liketext

engine_dbsica=create_engine('postgresql://userboot:G4#m$2024+@192.168.11.3:5432/DBSICA')

def Agente_aereo(num_agente ):
    query_open = open('querys\query_agenteaereo.txt')
     
     
    query_agente = query_open.read()
    query_agente=query_agente.replace("numero_agente",num_agente)
    df_agente = pd.read_sql(query_agente, engine_dbsica)
    # print(df_agente)
    # df_res=df_agente.to_json(orient='records')
    json_result = df_agente.to_json(orient='records')

    # print(json_result)
    return json_result

