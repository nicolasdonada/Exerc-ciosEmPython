import requests

def site(url):

    try:
        res = requests.get(url)
        
        if res.status_code == 200:
            print(f"\033[0;32mConseguimos nos conectar no site '{url}'\033[m")
        else:
            print(f"\033[0;31mNão conseguimos nos conectar no site '{url}'\033[m")
            print("Código de status: ", res.status_code)


    except requests.exceptions.RequestException as erro:
        print("\033[0;31mAconteceu algum ERRO! Tente novamente!\033[m")
