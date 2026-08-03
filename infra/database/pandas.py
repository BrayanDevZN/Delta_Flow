from infra.logs.log import Logs

"""
Conversa com o banco usando pandas
"""

from sqlalchemy import create_engine, inspect

import pandas as pd
class PandasDb:

    def __init__(self, url:str, log:Logs)->None:

        self.con = create_engine(url)

        log.config()

        self.logger = log.logger()


    #Le
    def read(self, name:str, query:str) -> pd.DataFrame:

        try:

            self.logger.info(f"Lendo a tabela {name}...")

            if not inspect(self.con).has_table(name):

                self.logger.warning(f"Não existe {name}")

            df = pd.read_sql(query, self.con)

            return df

        except Exception as e:
            raise Exception(e)

    #Salva
    def save(self, name:str, df:pd.DataFrame) -> None:
        try:

            self.logger.info(f"Salvando {name}...")

            df.to_sql(
                if_exists="replace", 
                name=name,
                con=self.con,
                index=False
            )

        except Exception as e:
            raise Exception(e)







    
        