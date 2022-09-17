import colorama
from colorama import Fore, Back, Style
from pyfiglet import Figlet

colorama.init(autoreset=True)

preguntas = {
    "¿Quién pintó la mona lisa?":
    "A",
    "Autor de \"Moby Dick\"":
    "D",
    "Sistema operativo para telefonos más usado":
    "B",
    "¿Cuál es la ciencia que estudia la aplicación de la informática y las comunicaciones al hogar?":
    "C",
    "¿De cuál de estas plantas se extrae la marihuana?":
    "B",
    "¿Cómo se conoce comúnmente al compuesto químico NaCl?":
    "A"
}

alternativas = [
    ["A. Leonardo da Vinci", "B. Picasso", "C. Miguel Ángel", "D. Monet"],
    [
        "A. Ernesto Sábato", "B. Ernest Hemingway", "C. Julio Verner",
        "D .Herman Melville"
    ], ["A. IOS", "B. Android", "C. Microsoft", "D. Windows"],
    ["A. Robótica", "B. Casática", "C. Domótica", "D. Autología"],
    ["A. Violeta Africana", "B. Cannabis", "C. Girasol", "D. Amapola"],
    ["A. Sal", "B. Azúcar ", "C. Leche ", "D. Pimienta"]
]

def nuevo_juego():

    ascii_banner = Figlet(font='graffiti')
    print(ascii_banner.renderText('Trivia Silabuz'))
    print('-----------------------------------------------')

    adivinar = []
    correctas = 0
    num_pregunta = 1

    for key in preguntas:
        print("-------------------------------")
        print(f'{Fore.GREEN}Pregunta numero {num_pregunta}')
        print(f'{Fore.YELLOW}{key}')
        for i in alternativas[num_pregunta - 1]:
            print(i)
        resp = input(f'{Fore.YELLOW}ingrese una alternativa:')
        resp = resp.upper()
        adivinar.append(resp)
        correctas += verificar_resp(preguntas.get(key), resp)
        num_pregunta+=1

    mostar_resultado(correctas, adivinar)


def verificar_resp(alternativa, resp):
    if alternativa == resp:
        print(f'{Fore.GREEN}Respuesta Correcta!!')
        return 1
    else:
        print(f'{Fore.RED}Respuesta Incorrecta')
        return 0


def mostar_resultado(correctas, adivinar):
    incorrectas = len(preguntas) - correctas
    print("-------------------------")
    print("RESULTADOS")
    print("-------------------------")
    print(f'{Fore.GREEN}Respuestas Correctas : {correctas}')
    print(f'{Fore.RED}Respuestas Incorrectas : {incorrectas}')

nuevo_juego()