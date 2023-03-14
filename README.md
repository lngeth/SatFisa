# SatFisa

Devoir Maison du module de Logique SAT FISA 1A S2.  
Devoir réalisé sous **Python**.

## Installation du projet

### Programme SAT

Utilisation de **Glucose**.  
Pour l'installer avec Choco, exécuter la commande suivante en terminal:  

```shell
choco install glucose
```

### Librairies requis

```python
numpy
matplotlib
networkx (pour la visualisation)
```

Si vous ne possédez pas toutes les librairies ci-dessus, exécuter la commande suivante, **dans le dossier SatFisa**, pour les installer :

```bash
make init
```

### Lancer le programme

Dans le **dossier SatFisa**, exécuter dans votre terminal la commande suivante :  

```bash
make
```

## Exercices

### 3. Fournir un 3-coloriage si possible

Exécuter l'algorithmes sur les 3 graphes (copier-coller directement) :
- __figure 1 :__ 6 10 1 2 1 4 1 5 2 3 2 4 3 4 3 6 4 5 4 6 5 6
- __figure 2 :__ 10 15 1 2 1 5 1 9 2 3 2 4 3 6 3 10 10 8 10 9 9 7 7 4 4 8 5 6 6 7 5 8
- __figure 3 :__ 12 24 1 2 1 3 1 5 1 11 2 4 2 6 2 12 12 8 12 10 12 11 11 9 11 7 3 4 3 8 3 10 4 7 4 9 5 8 5 10 5 7 6 8 6 7 6 9 9 10