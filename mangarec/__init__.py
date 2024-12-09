import logging

from mangarec.common.env import AppEnv

env = AppEnv()
logger = logging.getLogger()
logging.basicConfig(level=env.LOG_LEVEL)
