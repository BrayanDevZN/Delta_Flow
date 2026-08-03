"""
configuração global dos logs
"""

import logging

#Configuração basica
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

#Variavel que pega a conexão
logger = logging.getLogger(__name__)


