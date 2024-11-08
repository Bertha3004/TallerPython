from ctypes import c_ulong

import self
import math


class FormGral:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def op(self)->int:
        return self.b**2-4*self.a*self.c
    def sol(self):
        d = self.op()
        x1= (- self.b + math.sqrt(d))
        x2 = (- self.b - math.sqrt(d))
        return x1, x2

        print("la solucion 1 es: ",x1)
        print("la solucion 2 es: ",x2)