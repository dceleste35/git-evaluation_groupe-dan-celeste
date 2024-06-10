#!/usr/bin/env python3

def main():

    while True:
        try:
            input_str = input("> ")
            calculator(input_str)
        except EOFError:
            break

    print("Fin des calculs")

def calculator(input_str):

    for operator in '+-*/':
        if operator in input_str:
            left, right = input_str.split(operator)
            break
    else:
        print("Erreur de syntaxe pour le calcul: " + input_str)
        return


    try:
        left_num = int(left)
        right_num = int(right)
    except ValueError:
        print("Erreur de syntaxe pour le calcul: " + input_str)
        return

    input_str = input_str.replace(' ', '')

    if operator == '+':
        result = left_num + right_num
    elif operator == '-':
        result = left_num - right_num
    elif operator == '*':
        result = left_num * right_num
    elif operator == '/':
        result = left_num / right_num

    print(result)

if __name__ == "__main__":
    main()
