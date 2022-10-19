from asyncore import loop
from math import dist
from statistics import median_grouped
while True:
    class asteroides:
        def asteroide():
            return input('Informe o nome do Asteroid:  ')
        def distancias():
            return
        distancia1 = float(input('Informe a primeira distância:  '))
        distancia2 = float(input('Informe a segunda distância:  '))
        distancia3 = float(input('Informe a terceira distância:  '))
        distancia4 = float(input('Informe a quarta distância: '))
        distancia5 = float(input('Informe a quinta distância: '))
        distancia = []
        distancia.append(distancia1)
        distancia.append(distancia2)
        distancia.append(distancia3)
        distancia.append(distancia4)
        distancia.append(distancia5)
        print(distancia)
        distanciaSum = sum(distancia)
        dividirpor = float(5)
        media_dist = distanciaSum / dividirpor
        key_list= [asteroide()]
        value_list = [distancia]
        dict_from_list = dict(zip(key_list, value_list))
        print(dict_from_list)
        print(f'O asteroide está com uma média de  {media_dist} Kms. de distância da Terra!')
    while True:
        resp = input('Deseja lançar mais um asteroide? [S/N?] ').upper()[0]
        if  resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break