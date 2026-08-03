"""
configuração global dos logs
"""

import logging

#Controla os logs
class Logs:
    def __init__(self, path:str)->None:

                #Configuração baisca
                logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                handlers=[
                    logging.FileHandler(f"{path}/logs/app.logs"),
                    logging.StreamHandler()
                ]
            )

                #Variavel que carrega a configração
                self.log = logging.getLogger(__name__)

    #Retorna a variavel que pega a configuração  
    def logger(self) -> logging:
            return self.log
            

