# Author: Sakthi Santhosh
# Created on: 11/05/2023
from .telemetry import Telemetry
from .inferrer import Inferrer
from .constants import MODEL_FILE, LOG_FILE
from .log import Logger

log_handle = Logger(LOG_FILE).get_log_handle()


inferrer_handle = Inferrer(MODEL_FILE)
telemetry_handle = Telemetry()
