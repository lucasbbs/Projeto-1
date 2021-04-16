from collections import Counter

def printCSV(nome_arquivo,atributo_objeto,x1, y1, x2, y2):
  print(f'{nome_arquivo},{atributo_objeto},{x1},{y1},{x2},{y2}')

def printPercentages(objects, appeared_elements):
    counter = Counter(objects)
    soma = {}
    for e in appeared_elements:
        soma[e] = f'{(counter.get(e) or 0)/len(objects) * 100:.1f}'
    for i in soma:
      print(f'{i}: {soma[i]}') 

def calculaMedias(lista):
  print(f'{sum([(n[0] + n[2])/2 for n in lista])/len(lista):.0f}', end =" ")
  print(f'{sum([(n[1] + n[3])/2 for n in lista])/len(lista):.0f}', end =" ")
  print(f'{sum([(n[2] - n[0]) for n in lista])/len(lista):.0f}', end =" ")
  print(f'{sum([(n[3] - n[1]) for n in lista])/len(lista):.0f}')

def prinPositions(array):
  def printMoreCentral(array):
    array = sorted([dict(fileName= n["fileName"], objectAttribute= n["objectAttribute"], coord=(((n["coord"][0]+ n["coord"][2])/2 -128)**2 + ((n["coord"][1]+ n["coord"][3])/2 -128)**2)**(1/2)) for n in array], key = lambda x: x["coord"])[0]
    print(f'mais central: {array["objectAttribute"]},{array["fileName"]}')
  def printMoreLeft(array):
    array = sorted([dict(fileName= n["fileName"], objectAttribute= n["objectAttribute"], coord=(((n["coord"][0]+ n["coord"][2])/2 - 0)**2)**(1/2)) for n in array], key = lambda x: x["coord"])[0]
    print(f'mais a esquerda: {array["objectAttribute"]},{array["fileName"]}')
  def printMoreRight(array):
    array = sorted([dict(fileName= n["fileName"], objectAttribute= n["objectAttribute"], coord=(((n["coord"][0]+ n["coord"][2])/2 - 256)**2)**(1/2)) for n in array], key = lambda x: x["coord"])[0]
    print(f'mais a direita: {array["objectAttribute"]},{array["fileName"]}')
  def printMoreAbove(array): 
    array = sorted([dict(fileName= n["fileName"], objectAttribute= n["objectAttribute"], coord=(((n["coord"][1]+ n["coord"][3])/2 - 0)**2)**(1/2)) for n in array], key = lambda x: x["coord"])[0]
    print(f'mais acima: {array["objectAttribute"]},{array["fileName"]}')
  def printMoreBellow(array):
    array = sorted([dict(fileName= n["fileName"], objectAttribute= n["objectAttribute"], coord=(((n["coord"][1]+ n["coord"][3])/2 - 256)**2)**(1/2)) for n in array], key = lambda x: x["coord"])[0]
    print(f'mais abaixo: {array["objectAttribute"]},{array["fileName"]}')
  def printLargestArea(array): 
    array = sorted([dict(fileName= n["fileName"],objectAttribute=n["objectAttribute"], coord=((n["coord"][0]- n["coord"][2])*(n["coord"][1] - n["coord"][3])))for n in array], reverse = True, key = lambda x: x["coord"])[0]
    print(f'maior area: {array["objectAttribute"]},{array["fileName"]}')
  def printSmallestArea(array):
    array = sorted([dict(fileName= n["fileName"],objectAttribute=n["objectAttribute"], coord=((n["coord"][0]- n["coord"][2])*(n["coord"][1] - n["coord"][3])))for n in array], key = lambda x: x["coord"])[0]
    print(f'menor area: {array["objectAttribute"]},{array["fileName"]}')

  printMoreCentral(array)
  printMoreLeft(array)
  printMoreRight(array)
  printMoreAbove(array)
  printMoreBellow(array)
  printLargestArea(array)
  printSmallestArea(array)

def busca_images(array):
    has_tree = []
    has_field = []
    for each in array:
        if each['objectAttribute'] == 'tree':
            has_tree.append(each['fileName'])
    for each in array:
        if each['fileName'] in has_tree and each['objectAttribute'] in ['green-field', 'yellow-field', 'snowy-field']:
            has_field.append(each['fileName'])
    final = [n for n in has_tree if n not in has_field]
    final = list(dict.fromkeys(final))
    return final if len(final)!= 0 else 'nada'

T, N = map(int, input().split())
objetos = ['black-bison', 'elephant', 'white-horse', 'brown-horse', 'scarlet-ibis', 'black-ibis', 'white-ibis', 'blue-sky', 'overcast-sky', 'cloudy-sky', 'dusthaze-sky', 'rocky-mountain', 'snowy-mountain', 'birdseye-building', 'perspective-building', 'front-building', 'red-flower', 'purple-flower', 'pink-flower', 'sand', 'tree', 'green-field', 'snowy-field', 'yellow-field', 'road', 'tower', 'blue-ocean', 'green-cliff', 'black-cliff', 'waterfall']

if T == 1:
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    printCSV(nome_arquivo,atributo_objeto,x1, y1, x2, y2)

if T == 2:
  frequencia_objetos = []
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    frequencia_objetos.append(atributo_objeto)
  printPercentages(frequencia_objetos,objetos)

if T == 3:
  coordenadas = []
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    coordenadas.append([x1, y1, x2, y2])
  calculaMedias(coordenadas)

if T == 4:
  coordenadas = []
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    coordenadas.append(dict(fileName = nome_arquivo, objectAttribute=atributo_objeto,coord = [x1, y1, x2, y2]))
  prinPositions(coordenadas)

if T == 5:
  images = []
  for i in range(N) :
    input()
    nome_arquivo = input()
    atributo_objeto = input()
    x1, y1, x2, y2 = map(int, input().split())
    images.append(dict(fileName= nome_arquivo, objectAttribute=atributo_objeto))
    result = busca_images(images)
  if isinstance(result,  list):
    for n in result: print(n)
  else:
    print(result)