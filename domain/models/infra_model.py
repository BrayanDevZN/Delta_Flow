"""
Valida os dados da camada infra
"""

from pydantic import BaseModel, field_validator, ValidationInfo
from typing import Literal
from pyspark.sql import SparkSession, DataFrame
import pandas as pd
from sqlalchemy import Engine
import infra.module as ifr

class Valid_Engine(BaseModel):

    eng: Literal["spark", "pandas", "request", "query"] 

    data:dict 

   

    @field_validator("data")
    def valid(cls, v, info:ValidationInfo):

        types = {"spark":{
            "url": str,
            "session": SparkSession,
            "user": str, 
            "password":str,
            "driver": str
        }, "pandas":{
            "url":str
        }, "request":{"url":str}, "query":{"url":str}}

        key = types[info.data["eng"]]

        if len(v) != len(key):
            raise KeyError(f"expeted {len(key)} argument in data")

        for Key, value in v.items():

            if not Key in key.keys():

                raise KeyError(f"Expeted key {Key} in data")

            if not isinstance(value, key[Key]):
                raise TypeError(f"{key}: expeted type {key[Key]}")

        return v






        








