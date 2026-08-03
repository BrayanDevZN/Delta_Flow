from infra.logs.log import Logs

"""
Serve para fazer requisições para outras apis
"""

import requests


def request(url:str, log:Logs) ->dict:

    try:

        log.config()

        logger = log.logger()

        logger.info(f"Fazendo requisição para {url}...")

        response = requests.get(url=url)

        if response.status_code != 200:

            logger.error(f"Houve um erro em {url} | status: {response.status_code}")

        {"status": response.status_code, "data": response.json()}

    except Exception as e:
        raise Exception(e)


        

        