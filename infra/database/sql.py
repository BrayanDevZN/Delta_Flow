from infra.logs.log import Logs

"""
Executa querys sql
"""
from sqlalchemy import text, create_engine, CursorResult
from typing import Any

class QueryDb:

    def __init__(self, url:str, log:Logs)->None:

        self.con = create_engine(url)

        log.config()

        self.logger = log.logger()

    #Executa uma query
    def query(self, sql:str) -> Any:

        self.logger.info("Executando query...")

        try:

            with self.con.begin() as session:

                result = session.execute(
                    text(sql)
                )

                return result

        except Exception as e:
            raise Exception(e)

    #Pega o resultado da query e reotorna um dict
    def rows(self, sql:CursorResult) -> dict:

        return sql.mappings().fetchall()


        