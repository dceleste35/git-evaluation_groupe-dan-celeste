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

    #Fonction qui effectue les calculs
    return

if __name__ == "__main__":
    main()
