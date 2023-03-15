# SatFisa

Réalisé par **Laurent NGETH** et **Christophe WANG**.
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
```

Si vous ne possédez pas toutes les librairies ci-dessus, exécuter la commande suivante, **dans le dossier SatFisa**, pour les installer :

```bash
# sous windows
make init
# sous linux, avec PIP
make linux-init
```

### Lancer le programme

Dans le **dossier SatFisa**, exécuter dans votre terminal la commande suivante :  

```bash
# sous windows
make
# sous linux
make linux
```

## Exercices

Pour plus de détails, voir le PDF se trouvant dans la racine du projet.

### 3. Les graphes

Exécuter l'algorithmes sur les 3 graphes (copier-coller directement) :
- __figure 1 :__ 6 10 1 2 1 4 1 5 2 3 2 4 3 4 3 6 4 5 4 6 5 6
- __figure 2 :__ 10 15 1 2 1 5 1 9 2 3 2 4 3 6 3 10 10 8 10 9 9 7 7 4 4 8 5 6 6 7 5 8
- __figure 3 :__ 12 24 1 2 1 3 1 5 1 11 2 4 2 6 2 12 12 8 12 10 12 11 11 7 11 9 3 4 3 8 3 10 4 7 4 9 5 7 5 8 5 10 6 7 6 8 6 9 9 10

### 5. La carte à colorier

__carte :__ 7 9 1 2 1 4 2 3 2 4 3 4 3 5 4 5 4 6 5 6

### 6. Les produits chimiques et les wagons

__produit :__ 6 7 1 2 1 3 1 4 2 5 2 3 3 4 5 6