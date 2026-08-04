"""
regra de negocio da camada infra
"""
import infra.module as ifr
from typing import Literal

class RoleEngine:

    def __init__(self, type:ifr.request| ifr.QueryDb| ifr.SparkDb| ifr.PandasDb)->None:

        self.type = type
        
    #Valida os parametros do metodo read de acordo com o tipo
    
    def read(self, name:str=None, query:str=None)->dict:

        if isinstance(self.type, ifr.request):

            if name is not None or query is not None:
                raise TypeError("Type engine is request, not expected argument")

        elif isinstance(self.type, ifr.PandasDb):

            if name is None or query is None:
                raise TypeError("Type engine is pandas, expeted two arguments")

        elif isinstance(self.type, ifr.QueryDb):
            if name is not None:
                raise TypeError("Type engine is query, not expeted name")

            if name is not None or query is not None:
                        raise TypeError("Type engine is query, expeted just argument query")


        elif isinstance(self.type, ifr.SparkDb):
             if name is None:
                  raise TypeError("Type engine is spark, expeted name")

             if query is not None:
                  raise TypeError("Type engine is spark, not expeted query")

        return {"name":name, "query": query}

    #Valida os parametros do metodo save
    def save(self, name:str = None, df:ifr.PandasDb|ifr.SparkDb = None, query:str=None) -> None:

         if isinstance(self.type, ifr.QueryDb):

              if name or df is not None:
                   raise TypeError("Type connection is a query, expeted just param query")

         else:

              if query is not None:
                   raise TypeError("not expeted param query")

              if name is not None or df is not None:
                   raise TypeError("Expeted params name and df")


         return {"name":name, "df": df, "query":query}
                  

            


