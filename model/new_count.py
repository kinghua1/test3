#/user/bin/python
#conding=utf-8

from count import A

class B(A):
    def __sub__(self, a, b):
        return a - b

resule =B().add(2, 5)
print(resule)