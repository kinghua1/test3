def funx(x):
    def funy(y):
        return x*y
    return funy
print(funx(5)(6))
