# Minitrice

## Table des matières

1. [Introduction](#introduction)
2. [Installation](#installation)
   1. [Prérequis](#prérequis)
   2. [Instructions](#instructions)
3. [Exécution](#exécution)
4. [Questions](#quesitons)

## Introduction

Minitrice est un programme de calcul interactif qui prend en entrée une chaîne de caractères contenant deux nombres positifs (entiers ou rationnels) séparés par un opérateur (+, -, * ou /) et affiche le résultat du calcul. Le programme supporte les espaces autour des nombres et arrondit les résultats à deux chiffres après la virgule lorsque nécessaire.

## Installation

### Prérequis

- Python 3.x

#### Installer Python 3

##### Windows

1. Allez sur le site officiel de Python à l'adresse [python.org](https://www.python.org/).
2. Téléchargez le programme d'installation de Python pour Windows.
3. Exécutez le programme d'installation et suivez les instructions. Assurez-vous de cocher la case "Add Python to PATH" pendant l'installation.

##### macOS

1. Ouvrez le Terminal.
2. Utilisez [Homebrew](https://brew.sh/) pour installer Python 3 :

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install python
    ```

##### Linux

- **Debian/Ubuntu** :

    ```sh
    sudo apt update
    sudo apt install python3
    ```

### Instructions

1. Clonez le dépôt Git sur votre machine locale.

    ```sh
    git clone https://github.com/dceleste35/git-evaluation_groupe-dan-celeste/tree/v1.2
    ```

2. Rendez vous dans le projet

3. Rendez le script exécutable.

    ```sh
    chmod +x minitrice.py
    ```

## Exécution

### Utilisation interactive

1. Lancer le programme en mode interactif.

    ```sh
    ./minitrice.py
    ```

2. Entrez vos calculs directement dans le terminal.

    ```sh
    > 2 + 2
    4
    > 4 * 5
    20
    > 3.14159 / 2
    1.57
    >
    Fin des calculs
    ```

### Utilisation avec un fichier

1. Créez un fichier `calculs.txt` contenant les opérations.

    ```sh
    echo "2 + 2\n4 * 5\n3.14159 / 2" > calculs.txt
    ```

2. Utilisez `cat` pour rediriger le contenu du fichier vers le programme.

    ```sh
    cat calculs.txt | ./minitrice
    ```

3. Vous devriez voir la sortie suivante.

    ```sh
    4
    20
    1.57
    Fin des calculs
    ```

## Questions

### 1)
Cela signifie que Git permet à n'importe quel utilisateur d'avoir une copie complète de l'historique de développement d'un projet sur sa propre machine. Ce qui leur donne une autonomie complète pour travailler sans avoir à être connecté à un réseau.
Les plateformes telles que GitHub ou GitLab, permet de jouer le rôle de convergence, mais pas forcément de contrôle centralisé. Ces plateformes permet aux contributeurs de partager leurs modifications et de le synchroniser avec celui des autres. Mais ces dépôts ne sont pas indispensable pour le fonctionnement de Git.

### 2)
 Elle permet de faire un nettoyage des branches qui ont été supprimé sur le dépôt distant.

### 3)
 Il peux se passer un conflit lorsqu'une modification c'est faite sur le même fichier sur 2 branches différente, dans ce cas un conflit se créer et nous devrons sélectionner la partie à garder.

### 4)
 il y a 2 commandes possible 
 ```sh 
 git commit 
 ````
pour terminer la fusion ou 
```sh
git rebase --continue 
````
pour continuer un rebase

### 5)
Premièrement nous devons nous mettre sur la branche principal avec 
```sh 
git checkout main
```
Puis 
```sh
git pull origin main
````
Pour récupérer les dernières modifications depuis Github

### 6)
```sh
git reset --soft
```
Réinitialise uniquement la zone de staging et le répertoire reste inchangé 
```sh
git reset --hard
````
Réinitialise la zone de staging et le répertoire de travail. C'est à dire que toutes les modications non commit et les commits après le point de réinitialisation sont perdus.

### 7)
```sh
git rebase -i HEAD~3
```
Remplacer le contenu par :
```sh
pick d47267f 1
squash 68cd016 2
squash 9f64652 3
```
Sauvegarder et quitter l'éditeur pour appliquer les changements

### 8)
Il est déconseillé de rebase une branche publique car on pourait réecrite l'historique de commit et donc supprimer les modifications des précédents contributeurs
