from api_catfact import CatFactApi


def main():
    print("Welcome to the Cat Facts Generator!")
    print("Press ENTER to receive a random cat fact.")
    input(">> ")

    api = CatFactApi()
    result = api.get_results("")
    print(result)


if __name__ == "__main__":
    main()
