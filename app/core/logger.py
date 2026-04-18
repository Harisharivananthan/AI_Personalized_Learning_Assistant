import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(leveltime)s - %(message)s"
)
logger = logging.getLogger(__name__)