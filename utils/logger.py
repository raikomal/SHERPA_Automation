import logging
import os

# ✅ Fix folder issue
if not os.path.exists("reports"):
    os.mkdir("reports")

if not os.path.exists("reports/logs"):
    os.mkdir("reports/logs")

def get_logger():
    logger = logging.getLogger("automation_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("reports/logs/automation.log", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger