import datetime

class powermonkeyLogger:
    def __init__(self, name):
        self.name = name

    def log(self, message):
        print(f'[LOG] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {message}')

    def error(self, message):
        print(f'[ERR] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {message}')

    def warning(self, message):
        print(f'[WRN] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {message}')