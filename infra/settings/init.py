from infra.logs.log import Logs

"""
Cria todos os caminhos
"""

import os


class FolderControl:

    def __init__(self, level:str,logger:Logs, path:str = None) -> None:

        #Nivel dos arquivos
        levels = ["processed", "cleaned", "raw"]
        index = levels.index(level)
        self.level = levels[index:]

        #caminho onde vai salvar tudo, se ele for none, ai vai salvar na raiz do projeto
        self.path = path

        self._log()

        logger.config()

        self.log = logger.logger()


    #Cria o caminho inicial se o parametro path existir
    def create(self) -> None:
        try:
            

            if self.path is not None and not os.path.exists(self.path):

                self.log.info(f"Criando o caminho {self.path}...")
                os.makedirs(self.path, exist_ok=True)

        except Exception as e:
            raise Exception(e)

   

    #Cria o caminho onde os logs vão ser guardados
    def _log(self) -> None:

        os.makedirs(f"{self.path}/logs" if self.path is not None else "logs", exist_ok=True)

    #Cria as camadas
    def _layer(self) -> None:

         #Cria storage se não existir
         path = f"{self.path}/storage" if self.path is not  None else "storage"
         os.makedirs(f"{path}", exist_ok=True)

         for layer in self.level:

             path = f"storage/{layer}" if self.path is None else f"{self.path}/storage"

             if not os.path.exists(path):

                 self.log.info(f"Criando camada {layer} no caminho {"~/" + path if path is None else path}...")
                 os.makedirs(path, exist_ok=True)

    #Executa os metodos
    def run(self) -> None:
        self.create()
        self._layer()




      


        
                
                
            




            



           






        

