from infra.logs.log import config_logs

"""
Cria todos os caminhos
"""

import os


class FolderControl:

    def __init__(self,name:str, level:str, path:str = None) -> None:

        #Nivel dos arquivos
        levels = ["processed", "cleaned", "raw"]
        index = levels.index(level)
        self.level = levels[index:]

        #caminho onde vai salvar tudo, se ele for none, ai vai salvar na raiz do projeto
        self.path = path

        #Nome do projeto
        self.name = name


    #Cria o caminho inicial
    def create(self) -> None:
        try:

            if not os.path.exists(self.path):

                print(f"Criando o caminho {self.path}...")
                os.makedirs(self.path, exist_ok=True)

        except Exception as e:
            raise Exception(e)

    #Define o caminho
    def _path(self) -> None:
            
            self.path = self.name if self.path is None else f"{self.path}/{self.name}"
            

    

    #Cria o caminho onde os logs vão ser guardados
    def _log(self) -> None:
        try:

            if os.path.exists("app.log"):
                import shutil
                shutil.move("app.log", f"{self.path}/logs/app.log")
            




            



           






        

