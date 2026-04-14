import numpy as np

class CasoPrueba3():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.xk = 0
        self.xavg = 0
        self.yavg = 0
        self.n = 0
        self.B1 = 0
        self.B0 = 0
        self.r2 = 0
        self.Yk = 0
        self.rxy = 0
        self.sumx = 0
        self.sumy = 0
        self.B1_num = 0
        self.B1_denom = 0
        self.r_num = 0
        self.r_denom = 0

    def leerDatos(self):
        self.x = [163,765,141,166,137,355,136,1206,433,1130]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]
        self.xk = 386
        self.xavg = np.average(self.x)
        self.yavg = np.average(self.y)
        self.n = len(self.x)
        self.sumx = sum(self.x)
        self.sumy = sum(self.y)
        self.B1_num = sum(self.x*self.y)-(self.n*self.xavg*self.yavg)
        self.B1_denom = sum(np.pow(self.x,2))-self.n*(self.xavg**2)
        self.r_num = self.n*(sum(self.x*self.y))-(self.sumx*self.sumy)
        self.r_denom = (self.n*sum(np.pow(self.x,2))-(self.sumx**2))*((self.n*sum(np.pow(self.y,2)))-(self.sumy**2))

    def RealizarCalculo(self):

        self.B1 = self.B1_num/self.B1_denom
        self.B0 = self.yavg - self.B1
        self.rxy = self.r_num/np.sqrt(self.r_denom)
        self.r2 = self.rxy*self.rxy
        self.Yk = self.B0+self.B1*self.xk