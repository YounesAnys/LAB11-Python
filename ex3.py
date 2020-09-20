#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")


def pgcd(x,y):
    if x % y == 0:
        res = y
    else :
        res = pgcd(y,x%y)
    return res
