from logger import logger


logger.info("========== INICIO PIPELINE ETL ==========")
logger.info("Ejecutando extracción")
import extract

logger.info("Ejecutando transformación")
import transform

logger.info("Ejecutando carga")
import load

logger.info("Pipeline finalizado correctamente")


logger.info("========== PIPELINE FINALIZADO ==========")