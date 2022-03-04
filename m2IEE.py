def moyenne(donnees):
    """
    Cette fonction calcule la moyenne d'une série de valeurs. 
    """
    somme = 0
    n = 0
    for valeur in donnees:
        n = n+1
        somme = somme + valeur
        #print(f"La valeur actuelle de somme est : {somme}")
    print()
    moyenne = somme / n
    #print(f"La moyenne est {moyenne}")
    return moyenne


def variance(valeur_variance:list):
    """
    Cette fonction calcule la variance d'une série de données.
    Prend en argument une séquence de valeur
    """
    # Nous calculons n et la moyenne de la liste
    n = len(valeur_variance)
    moyenne_list = moyenne(valeur_variance)
    # Logique pour calculer la variance
    sommesqEM = 0
    
    for var in valeur_variance : 
        sqEM = (var - moyenne_list)**2
        #print(f"l'écart à la moyenne au carré est {sqEM}")
        sommesqEM = sommesqEM + sqEM
        #print(f"la somme des carrés des EM est {sommesqEM}")
    variance_list = sommesqEM / n
    return variance_list