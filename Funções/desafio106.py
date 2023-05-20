def ajuda(pala):

    help(pala)

while True:
    print("~~" * 10)
    print("    AJUDA PYHELP")
    print("~~" * 10)
    inte = str(input("Função ou biblioteca > ")).lower()

    if inte == "fim":
        print("~" * 20)
        print("     Até logo")
        print("~" * 20)
        break

    print("\033[;;41m")
    ajuda(inte)
    print("\033[m")