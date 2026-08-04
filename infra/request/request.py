from infra.logs.log import Logs

"""
Serve para fazer requisições para outras apis
"""

import requests

class request:
    def __init__(self, url:str, log:Logs):
        self.url = url

        log.config()

        self.log = log.logger()

#Faz a requisição
        
def read(self) ->dict:

    try:

      

        self.logger.info(f"Fazendo requisição para {self.url}...")

        response = requests.get(url=self.url)

        if response.status_code != 200:

            self.logger.error(f"Houve um erro em {self.url} | status: {response.status_code}")

        {"status": response.status_code, "data": response.json()}

    except Exception as e:
        raise Exception(e)


        

        