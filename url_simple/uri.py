
class URI:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'URI({self.value})'

    def __eq__(self, other):
        return str(self) == str(other)


