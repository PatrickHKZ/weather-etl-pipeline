from logger import logger

from extract import extract
from transform import transform
from load import load


try:

    logger.info("========== INICIO PIPELINE ETL ==========")

    logger.info("Ejecutando extracción")
    extract()

    logger.info("Ejecutando transformación")
    transform()

    logger.info("Ejecutando carga")
    load()

    logger.info("========== PIPELINE FINALIZADO ==========")


except Exception as error:

    logger.error(f"Pipeline detenido por error: {error}")
    raise