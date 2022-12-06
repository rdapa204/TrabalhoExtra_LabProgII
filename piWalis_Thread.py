from threading import Thread
from time import perf_counter
import math


def Termos_pares(precision):
    prod = 1
    for i in range(1,math.ceil(1/precision)):
        prod = prod*(2*i/(2*i-1))
    global thread1
    thread1 = prod

def Termos_impares(precision):
    prod = 1
    for i in range(1,math.ceil(1/precision)):
        prod = prod*(2*i/(2*i+1))
    global thread2
    thread2 = prod

def pi_Wallis(precision):
    pi = 2
    i=1
    while(abs(pi-math.pi)>precision):
        pi *= (4*i**2)/(4*i**2-1)
        i=i+1
    return pi

thread1 = None
thread2 = None
precision = float(input('Entre com a precisão desejada:\n'))

inicio = perf_counter()
x = Thread(target = Termos_pares(precision))
y = Thread(target = Termos_impares(precision))
    
x.start()
y.start()

x.join()
y.join()
fim = perf_counter()
pi = 2*thread1*thread2

print(f"Com utilização de duas Threads o cálculo de pi demorou {(fim-inicio)*1000:0.5f} millisegundos, apresentando valor de {pi}\n")
print(f"\t Tempo Execução Threads : {(fim-inicio)*1000:0.5f} millisegundos\n \t valor de pi Threads : \t{pi}\n")

inicio = perf_counter()
pi = pi_Wallis(precision)
fim = perf_counter()

print(f"Com utilização da abordagem sequencial o cálculo de pi demorou {(fim-inicio)*1000:0.5f} millisegundos, apresentando valor de {pi}\n")
print(f"\t Tempo Execução Sequencial : {(fim-inicio)*1000:0.5f} millisegundos\n \t valor de pi Sequencial : {pi}\n")
