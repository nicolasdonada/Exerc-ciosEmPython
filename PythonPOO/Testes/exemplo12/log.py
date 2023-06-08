class LogMixin:

    @staticmethod
    def write(msg):
        with open("log.log", "a+") as file:
            file.write(msg)
            file.write("\n")
            file.write("\n")

    def info(self, msg):
        self.write(f"INFO: {msg}")

    def error(self, msg):
        self.write(f"ERROR: {msg}")