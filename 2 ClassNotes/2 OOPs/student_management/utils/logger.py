from datetime import datetime

class Logger:
    log_count = 0
    logs = []

    @staticmethod
    def format_log(msg):
        return f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"

    @classmethod
    def log(cls, msg):
        formatted = cls.format_log(msg)
        cls.logs.append(formatted)
        cls.log_count += 1
        print(formatted)

    @classmethod
    def dump_logs(cls, filepath="system_logs.txt"):
        with open(filepath, "w") as f:
            for log in cls.logs:
                f.write(log + "\n")
