"""permet de de recuperer des fichier csv et de les annalyser"""

#### Imports et définition des variables globales
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>
    Args:
        filename (str): nom du fichier à lire
    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open (filename) as f:
        r= csv.reader(f)
        l = []
        l=list(r)
    for i in range (len(l)):
        l[i]= l[i][0].split(';')
        for j in range (len(l[i])):
            l[i][j]= int(l[i][j])
    return l

def get_list_k(data, k):
    """renvoit la k-ieme liste du fichier"""
    l= []
    l=data[k]
    return l

def get_first(l):
    """renvoit le premier element de la liste"""
    return l[0]

def get_last(l):
    """renvoit le dernier element de la liste"""
    return l[len(l)-1]

def get_max(l):
    """renvoit l'element max de la liste"""
    return max(l)

def get_min(l):
    """renvoit l'element min de la liste"""
    return min(l)

def get_sum(l):
    """renvoit la somme des element de la liste"""
    somme = 0
    for elemement in l:
        somme += elemement
    return somme


#### Fonction principale


def main():
    """appelle de la fonction principale"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
