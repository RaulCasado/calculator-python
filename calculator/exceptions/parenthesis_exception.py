class ParenthesisError(Exception):
    def __init__(self):
        self.message = f"Los paréntesis no son válidos"