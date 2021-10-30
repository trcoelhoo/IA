#Exercicio 1.1
def comprimento(lista):
	if lista== []:
		return 0
	return 1 + comprimento(lista[1:])
#Exercicio 1.2
def soma(lista):
	if lista== []:
		return 0
	return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if lista==[]:
		return False
	if lista[0] == elem:
		return True
	return existe(lista[1:],elem) 

#Exercicio 1.4
def concat(l1, l2):
	if l1 == []:
		return l2
	if l2 == []:
		return l1
	l1.append(l2[0])
	return concat(l1,l2[1:])

#Exercicio 1.5
def inverte(lista):
	if lista==[]:
		return []
	inv = inverte(lista[1:])
	inv[len(inv):] = [lista[0]]
	return inv

#Exercicio 1.6
def capicua(lista):
	if lista == []:
		return True
	return lista[0]==lista[-1] and capicua(lista[1:-1])

#Exercicio 1.7
def explode(lista):
	if lista==[]:
		return lista
	conc=explode(lista[1:])
	conc[:0]=lista[0]
	return conc

#Exercicio 1.8
def substitui(lista, original, novo):

	if lista==[]:
		return []
	if lista[0] == original:
		return [novo] + substitui(lista[1:], original, novo)
	return [lista[0]] + substitui(lista[1:], original, novo)
	


#Exercicio 1.9
def junta_ordenado(lista1, lista2):
	aux=[]
	if lista1==[]:
		return lista2
	if lista2==[]:
		return lista1
	if lista1[0] <=	lista2[0]:
		aux.append(lista1[0])
		aux=aux+junta_ordenado(lista1[1:],lista2)
	if lista1[0] > lista2[0]:
		aux.append(lista2[0])
		aux=aux+junta_ordenado(lista1,lista2[1:])

	return aux


#Exercicio 2.1
def separar(lista):
	if lista==[]:
		return ([],[])
	c1,c2=lista[0]
	cauda1, cauda2=separar(lista[1:])
	return ([c1]+cauda1,[c2]+cauda2)

#Exercicio 2.2
def remove_e_conta(lista, elem):
	if lista==[]:
		return lista,0
	li,el = remove_e_conta(lista[1:],elem)
	if lista[0]== elem:
		return li,el+1
	return [lista[0]]+li,el
#Exercicio 3.1
def cabeca(lista):
	if lista==[]:
		return None
	return lista[0]

#Exercicio 3.2
def cauda(lista):
	pass

#Exercicio 3.3
def juntar(l1, l2):
	if len(l1)!=len(l2):
		return None
	if l1==[]:
		return []
	return [(l1[0],l2[0])]+juntar(l1[1:],l2[1:])


#Exercicio 3.4
def menor(lista):
	if lista==[]:
		return None
	me=menor(lista[1:])
	if me is None or lista[0]<me:
		return lista[0]

	return me

#Exercicio 3.6
def max_min(lista):
	if lista ==[]:
		return None
	max,min=max_min(lista[1:])
	if max is None or min is None:
		return lista[0],lista[0]
	if lista[0]>max:
		return lista[0],min
	if lista[0]<min:
		return max,lista[0]
	return max,min