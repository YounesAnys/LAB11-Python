#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

  
def initliste(L,n):
    if n!=0:
        initliste(L,n-1)
        L.append(n-1)
n = int(input("SVP entier n:"))
L = []
initliste(L,n)
print(L)

        
        
