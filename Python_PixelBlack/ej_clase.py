class A:

    def a(self):
        print('desde a')
    
class B:
    def b(self):
        print('desde b')
        
class c(A,B):
    def c(self):
        print('desde c')

letras = c()
letras.a()
letras.b()
letras.c()