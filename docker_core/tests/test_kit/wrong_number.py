class IncorrectQueryAmountError(Exception):
    def __init__(self, expected, found):
        self.expected = expected
        self.found = found
        super().__init__(f"Incorrect number of queries in file. Expected:{expected}, Found:{found}")