from infra.logs.log import Logs

"""
Faz a conexão com banco de dados usando spark
"""

from pyspark.sql import SparkSession, DataFrame

class SparkDb:

    def __init__(self, url:str, session:SparkSession, log:Logs,user:str, password:str, driver:str = None)->None:

        #Dados para a conexão
        self.url = url

        #objeto spark
        self.session = session

        self.session.sparkContext.setLogLevel("ERROR")

        log.config()

        self.logger = log.logger()

        #Driver do banco
        self.driver = driver

        self.user = user
        self.password = password



    #Le banco de dados 
    def read(self, name:str) -> DataFrame:

        try:

            self.logger.info(f"Lendo a tabela {name}...")

            df = self.session.read.format("jdbc").option("url", self.url).option("dbtable", name).load()

            return df

        except Exception as e:
            raise Exception(e)


    #Salva no banco
    def save(self, name:str, df:DataFrame) -> None:
        try:
            self.logger.info(f"Salvando {name}...")

            if self.driver is None:
                df.write \
                .format("jdbc") \
                .option(
                    "url",
                    self.url
                ) \
                .option(
                    "dbtable",
                    name
                ) \
                .option(
                    "user",
                    self.user
                ) \
                .option(
                    "password",
                    self.password
                ) \
                .mode("append") \
                .save()

            else:
                df.write \
                .format("jdbc") \
                .option(
                    "url",
                    self.url
                ) \
                .option(
                    "dbtable",
                    name
                ) \
                .option(
                    "user",
                    self.user
                ) \
                .option(
                    "password",
                    self.password
                ) \
                .option(
                    "driver",
                    self.password
                ) \
                .mode("append") \
                .save()

        except Exception as e:
            raise Exception(e)



    



        
        