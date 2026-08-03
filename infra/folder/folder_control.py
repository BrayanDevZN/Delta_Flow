from infra.logs.log import logger

"""
Cria todos os caminhos
"""

import os


class FolderControl:

    def __init__(self,level:str, path:str = None) -> None:

        #Nivel dos arquivos
        levels = ["processed", "cleaned", "raw"]
        index = levels.index(level)
        self.level = levels[index:]

        #caminho onde vai salvar tudo, se ele for none, ai vai salvar na raiz do projeto
        self.path = path


    #Cria o caminho inicial
    def create(self) -> None:
        try:

            if self.path is not None and not os.path.exists(self.path):

                logger.info(f"Criando o caminho {self.path}...")
                os.makedirs(self.path, exist_ok=True)

        except Exception as e:
            raise Exception(e)

    #Cria o caminho onde os logs vão ser guardados
    def _log(self) -> None:
        try:



            



           






        

