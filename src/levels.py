
class Calculator:
    def __init__(self):
        pass
    def sum(self,a: float|int|str,b: float|int|str) -> str:
        return f"Sum is {float(a) + float(b)}"
    def difference(self,a: float|int|str,b: float|int|str) -> str:
        return f"Sum is {float(a) - float(b)}"
    def devide(self,a: float|int|str,b: float|int|str) -> str:
        return f"Sum is {float(a) / float(b)}"
    def multiply(self,a: float|int|str,b: float|int|str) -> str:
        return f"Sum is {float(a) * float(b)}"