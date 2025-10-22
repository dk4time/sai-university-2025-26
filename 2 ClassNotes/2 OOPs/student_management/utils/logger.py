# utils/logger.py
import datetime

class Logger:
    log_count = 0
    logs = []

    @staticmethod
    def format_log(msg):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {msg}"

    @classmethod
    def log(cls, msg):
        cls.log_count += 1
        formatted = cls.format_log(msg)
        cls.logs.append(formatted)
        print(formatted)
