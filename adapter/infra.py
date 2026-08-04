
"""
controla e adapta toda camada infra
"""


import infra.module as ifr
from domain.module import Valid_Engine, RoleEngine
from sqlalchemy import Engine
import pandas as pd
from pyspark.sql import DataFrame
class EngineDb:

    def __init__(self, eng:str, data:dict, log:ifr.Logs)->None:

        #pega o model e valida
        valid = Valid_Engine(eng=eng, data=data)

        self.data = valid.data

        self.data["log"] = log
        
        self.type = valid.eng

        self.instance = self.connection()

        self.role = RoleEngine(type=self.instance)

    #Cria a conexão 
    def connection(self) -> ifr.PandasDb| ifr.QueryDb | ifr.SparkDb | ifr.request:

        engs = {
            "pandas": ifr.PandasDb,
            "request": ifr.request,
            "spark": ifr.SparkDb,
            "query": ifr.QueryDb
        }

        eng = engs[self.type]

        return eng(**self.data)


    #Pega os dados
    def read(self, name:str=None, query:str=None)-> pd.DataFrame|DataFrame|Engine|dict:

        #Valida os parametros
        args = self.role.read(name=name, query=query)

        #Executa
        data = self.instance.read(**args) if not isinstance(self.instance, ifr.QueryDb) else self.instance.query(**args)

        return data

    #Salva os dados
    def save(self, name:str=None, query:str=None, df:ifr.SparkDb|ifr.PandasDb=None):

        #argumentos
        args = self.role.save(name=name, query=query, df=df)

         #Executa
        data = self.instance.save(**args) if not isinstance(self.instance, ifr.QueryDb) else self.instance.query(**args)

        return data
        



    
    

    