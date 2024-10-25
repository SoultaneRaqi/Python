def recherche_dichotomique(tableau, n, valeur):
    bas = 0
    haut = n - 1
    
    while bas <= haut:
        milieu = (bas + haut) // 2  
        
        if tableau[milieu] == valeur:
            return f"Valeur trouvée à la position {milieu}"
        elif tableau[milieu] < valeur:
            haut = milieu - 1  
        else:
            bas = milieu + 1   
  
    return "Valeur non trouvée"

# Exemple 
tableau = [9, 7, 5, 3, 1 ]  
n = len(tableau)
valeur = int(input("Donnez une valeur: "))
print(recherche_dichotomique(tableau, n, valeur))
