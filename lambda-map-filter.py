#nesse arquivo irei anotar meus estudos sobre os comandos lambda, map, filter
# e também sobre comprehention

#---LAMBDA
#lambda em poucas palavras seria criar uma função anônima.

#Exemplo criando uma função de forma usual
def funcao(x):
    return x**x

#Exemplo da criação da mesma função de forma anônima
print('---- LAMBDA')
func = lambda x: x**x
print(func(3)) #27


#---MAP(funcao, dados)
#o comando map tem duas entradas, uma é uma função, que pode ser anônima ou não, e o dado (ou conjunto 
# de dados) que você vai usar na função, caso seja uma lista, o map vai aplicar a função linha por linha
print('---- MAP')
lista = [1, 2, 3, 4, 5, 6]
quadrado = list(map(lambda x: x**x, lista))
print(quadrado)

#podemos fazer o mesmo com comprehension

quadrado = [func(x) for x in lista]
print(quadrado)

#---FILTER(funcao, dados, interable)
#como o comando já diz, esse comando serve para filtrar, o filter vai tomar tudo que é diferente
# de 0 como True, e 0 como false, ele vai filtrar
#todos os casos que retornou True, como irei exemplificar abaixo
print('---- FILTER')
par = list(filter(lambda x: x % 2 == 0, lista))
print(par)
# agora usando comprehension
par = [x for x in lista if x % 2 == 0]
print(par)

