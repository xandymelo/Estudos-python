import collections
from collections import Counter

#nesse estudo irei mostrar uma biblioteca muito útil chamada collections, e irei começar pelo comando
#Counter
#Counter como o nome já diz, ele conta as coisas, literalmente, e ela tem algumas vantagens
#ele retorna um objeto que funciona como um dicionário, porém com algumas vantagens
#serve para contar as frequências dos caracteres de uma string
#---Definição do objeto Counter
print("---DEFINIÇÕES")
c = Counter('teste')
print(c)
#também em uma lista
c = Counter(['a', 'a', 'b', 'teste', 'c'])
print(c)
#no objeto Counter você pode chamar
#um index que não existe, e não vai dar erro, diferente do dicionário
print(c['teste2']) #rerturn 0
#também pode converter um dicionário em um Counter
d = Counter({'a': 2, 'b':3, 'c': 2})
print(d)

#---MÉTODOS
#também podemos usar o .most_common para ver o que mais se repetiu, e escolher a quantidade de dados para
#retornar, o retorno é uma lista com tuplas, o primeiro é o dado, e o segundo é a frequência
print("---MÉTODOS")
print('--MOST_COMMON')
e = c.most_common()
print(e)

e = c.most_common(2)
print(e)

#também tem o .subtract, que subtrai as frequências
print('--SUBTRACT')
counter = Counter(a=4, b=3)
print(counter)
lista = ['a', 'a', 'b']
counter.subtract(lista)
print(counter)
#o .update é similar ao .subtract, só que soma as frequências
print('--UPDATE')
counter.update(lista)
print(counter)
#tanto no .update quanto no .subtract, estamos usando lista, mas poderíamos usar um dicionário, set,
#outro objeto Counter, ou uma tupla
#por fim desse estudo, o Counter é compatível com operações de +,-, e & e |
print('--OPERAÇÕES')
counter2 = Counter(lista)
print(counter + counter2)
print(counter - counter2)
print(counter & counter2)
print(counter | counter2)

