"""
configuração global dos logs
"""

import logging

#Controla os logs
class Logs:
    def __init__(self, path:str = None)->None:

                
                #Caminho pra salvar os logs
                self.path = path

    #Configuração basica
    def config(self):
            
            logging.basicConfig(
                            level=logging.INFO,
                            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                            handlers=[
                                logging.FileHandler(f"{self.path}/logs/app.log" if self.path is not None else "logs/app.log"),
                                logging.StreamHandler()
                            ]
                        )

            

        

        
    #Retorna a variavel que pega a configuração  
    def logger(self) -> logging:
            return logging.getLogger("DeltaFlow")
            

