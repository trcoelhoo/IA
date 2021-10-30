import math
#Exercicio 4.1
impar = lambda n: n % 2 == 1

#Exercicio 4.2
positivo = lambda n: n>0

#Exercicio 4.3
comparar_modulo = lambda x,y:abs(x)<abs(y)
#Exercicio 4.4
cart2pol = lambda x,y:(math.sqrt(x*x+y*y),math.atan2(y,x))

#Exercicio 4.5
ex5 = lambda f,g,h:lambda x,y,z:h(f(x,y),g(y,z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    return not False in [f(e) for e in lista]
    return len([e for e in lista if f(e)]) == len(lista)
    return [e for e in lista if not f(e)] == []

#Exercicio 4.9
def ordem(lista, f):
    if lista==[]:
        return None
    if(len(lista)==1):
        return lista[0]
    o=ordem(lista[1:],f)

    return lista[0] if f(lista[0],o) else o
#Exercicio 4.10
def filtrar_ordem(lista, f):
    if lista==[]:
        return [],[]
    if len(lista)==1:
        return lista[0],[]
    o,l=filtrar_ordem(lista[1:],f)
    return (lista[0],lista[1:]) if f(lista[0],o) else (o,[lista[0]]+l)

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    if lista==[]:
        return []

    o,l=filtrar_ordem(lista,ordem)
    return [o] +ordenar_seleccao(l,ordem)
