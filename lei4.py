#coding=utf-8

class A():

    def add(self, a, b):
        return a + b

class B(A):
    def sub(self, a, b):
        return a - b

print(B().add(5, 5))
