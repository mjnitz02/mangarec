import logging
import os


class AppEnv:
    if os.getenv("CONFIG_PATH") is not None:
        CONFIG_PATH = os.getenv("CONFIG_PATH")
    else:
        CONFIG_PATH = "\\config"

    if os.getenv("PROXY_URL") is None:
        PROXY_URL = None
    else:
        PROXY_URL = os.getenv("PROXY_URL")

    if os.getenv("LOG_LEVEL") is None:
        LOG_LEVEL = logging.INFO
    else:
        level = os.getenv("LOG_LEVEL")
        if level == "DEBUG":
            LOG_LEVEL = logging.DEBUG
        elif level == "INFO":
            LOG_LEVEL = logging.INFO
        elif level == "WARNING":
            LOG_LEVEL = logging.WARNING
        elif level == "ERROR":
            LOG_LEVEL = logging.ERROR
        else:
            LOG_LEVEL = logging.INFO
