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

    def break_line(self):
        print('\n')

    def scoring(self, score, category):
        print(f'---> SCORE: {score}')
        print(f'Compare your system with others at: https://github.com/zlElo/Powermonkey#{category}')

    def result(self):
        print(r"""
        /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$   /$$ /$$    /$$$$$$$$ 
        | $$__  $$| $$_____/ /$$__  $$| $$  | $$| $$   |__  $$__/
        | $$  \ $$| $$      | $$  \__/| $$  | $$| $$      | $$  
        | $$$$$$$/| $$$$$   |  $$$$$$ | $$  | $$| $$      | $$ 
        | $$__  $$| $$__/    \____  $$| $$  | $$| $$      | $$  
        | $$  \ $$| $$       /$$  \ $$| $$  | $$| $$      | $$  
        | $$  | $$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  
        |__/  |__/|________/ \______/  \______/ |________/|__/  
        """)