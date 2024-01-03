class SecretAgent:
    _codeword = "fide"

    def __init__(self, codename):  ## initializer
        self.codename = codename
        self._secrets = []

    def __repr__(self) -> str:
        return f"{self.codename} is the codename with secrets {self._secrets}"

    def add_secrets(self, secret: str):
        self._secrets.append(secret)

    def __del__(self):
        print(f"Agent {self.codename} has been fired")

    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword

    @staticmethod
    def inquire(question):
        print("I know nothing")
