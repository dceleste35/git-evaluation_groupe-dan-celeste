def main():

    while True:
        try:
            input_str = input("> ")
            calculator(input_str)
        except EOFError:
            break

    calculator(input_str)

    print("Fin des calculs")

def calculator(input_str):

    input_str = input_str.replace(' ', '')

if __name__ == "__main__":
    main()
