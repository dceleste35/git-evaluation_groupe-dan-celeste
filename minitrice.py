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

    input_str = input_str.replace(' ', '')

    for operator in '+-*/':
        if operator in input_str:
            left, right = input_str.split(operator)
            break
    else:
        print("Erreur de syntaxe pour le calcul: " + input_str)
        return


    left_num = int(left)
    right_num = int(right)

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
