# Minitrice

## Table des matières

1. [Introduction](#introduction)
2. [Installation](#installation)
   1. [Prérequis](#prérequis)
   2. [Instructions](#instructions)
3. [Exécution](#exécution)
4. [Licence](#licence)

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
