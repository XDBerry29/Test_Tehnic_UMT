from math import comb


def add_point(coords,points_dict):
    # functia add_point adauga puntele intr-un dictionar in care x e cheia si valoarea e o lista de coordonate y asociate lui x
    # De exemplu (1,2) (1,3) (2,3) => {1 : [2,3], 2:[3]}
    (x,y)=coords
    if points_dict.get(x) == None:
        points_dict[x] = [y]
    else:
        points_dict[x].append(y)


def how_many_rectangles(points_dict):
    rez = 0
    for i, (key_x,list_y) in enumerate(points_dict.items()):
        for key_x2,list_y2 in list(points_dict.items())[i+1:]:
            intersection = set(list_y).intersection(list_y2)
            if len(intersection) >= 2:
                rez+= comb(len(intersection),2)
    
    return rez
#dupa formarea dictionarului facem intersectia a tuturor perechilor de liste din dictionar
#daca cardinalul intersectiei listelor e mai mare de 2 adaugam la rezultat combinari de card(intersectie) luate cate 2
# explicatie:
# pentru exemplu dat avem urmatoul dictionar :
# key value
# X  list(Y)
# 1  [1,3]
# 2  [1,3]
# 3  [1,3]
# facand intersectia primelor 2 valori adica listele cu cheile 1 si 2 avem [1,3] ∩ [1,3] = [1,3] din asta putem deduce ca:
# axa X = 1 si X = 2 sunt intersectate de 2 axe Y , Y = 1 si Y = 3 in puntele (1,1) (1,3) si (2,1) (2,3) => dreptunghi
# Daca in alt exemplu am fi avut: intersectie valorilor cheilor x1 si x2 = [p1,p2,p3] putem construi 3 dreptunghiuri pe 
# axele paralele X = x1 si X = x2 luand toate perechile de 2 ale axelor Y adica (p1,p2), (p1,p3), (p2,p3) => se pot forma 3 dreptunghiuri
# deci nr de dreptunghiuri ce se pot forma intre 2 axe X = comb(card(dict[x1] ∩ dict[x2]),2)
# repetand asta pentru fiecacare pereche de chei si adunand rezultatele obtinem solutia problemei


points_dict ={}

file = open("data.in","r")


for line in file:
    coords = tuple(map(int,line.strip().strip('()').split(',')))
    add_point(coords,points_dict)

file.close()

print(how_many_rectangles(points_dict))