import math

class Integracion:
    def __init__(self, dof, x, error_aceptable=0.00001):
        self.error_aceptable = error_aceptable
        self.dof = dof
        self.x = x

    def gamma(self, n):  
        if n == 1: return 1
        if n == 0.5: return math.sqrt(math.pi)
        if n % 1 == 0: return math.factorial(int(n) - 1)
        resol, act = 1, n - 1
        while act > 1: 
            resol *= act
            act -= 1
        gamma = resol * math.sqrt(math.pi)
        return gamma

    def f_X(self, x, dof):   
        numerador = self.gamma((dof + 1) / 2)
        denominador = math.sqrt(dof * math.pi) * self.gamma(dof / 2) 
        return (numerador / denominador) * (1 + (x**2 / dof)) ** (-(dof + 1) / 2)

    def calcular_area(self, num_seg): 
        w = self.x / num_seg
        suma = self.f_X(0, self.dof) + self.f_X(self.x, self.dof)
        for i in range(1, num_seg):
            mult = 4 if i % 2 != 0 else 2
            suma += mult * self.f_X(i * w, self.dof)
        return (w / 3) * suma

    def integrar(self):
        num_seg = 10
        area_ant = self.calcular_area(num_seg) 
        while True:
            num_seg *= 2
            area_nueva = self.calcular_area(num_seg) 
            if abs(area_ant - area_nueva) < self.error_aceptable:
                return round(area_nueva, 5)
            area_ant = area_nueva