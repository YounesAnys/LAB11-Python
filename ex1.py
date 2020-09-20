#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

  

def verifchiffres(a,n):
    if n==0 :
        touschiffres = True
    else:
        if a[n-1] >= 0 and a[n-1] <= 9:
            touschiffres = verifchiffres(a,n-1)
        else:
            touschiffres = False
    return touschiffres
    
        
        
