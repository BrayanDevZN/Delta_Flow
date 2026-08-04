
"""
controla e adapta toda camada infra
"""


import infra.module as ifr
from domain.module import Valid_Engine, RoleEngine
class Engine:

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
    def read(self, name:str=None, query:str=None):

        #Valida os parametros
        args = self.role.read(name=name, query=query)

        #Executa
        data = self.instance.read(**args)

        return data


