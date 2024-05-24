def get_level(xp: int) -> str:
    if xp < 1000: return "Ferro"
    elif xp <= 2000: return "Bronze"
    elif xp <= 5000: return "Prata"
    elif xp <= 7000: return "Ouro"
    elif xp <= 8000: return "Platina"
    elif xp <= 9000: return "Ascendente"
    elif xp <= 10000: return "Imortal"
    else: return "Radiante"

def compare_level(original:str, novo:str) -> int:
    levels = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"]
    return levels.index(novo) - levels.index(original)

dict_herois = {}
while True:
    nome = input("Digite o nome do herói: ")
    xp = input("Digite a quantidade de experiência do herói: ")
    if not xp.isdigit(): 
        print("Digite um número inteiro positivo para a experiência", end="\n\n")
        continue
    nivel = get_level(int(xp))

    if nome in dict_herois:
        print("Esse herói já está cadastrado, deseja atualizar o nível dele?")
        resposta = input("Digite 's' para sim e 'n' para não: ")
        if resposta == "s":
            leve_diff = compare_level(dict_herois[nome], nivel)
            if leve_diff < 0:
                print(f'O herói de nome {nome} foi rebaixado de {dict_herois[nome]} para {nivel}', end="\n\n")
            elif leve_diff > 0:
                print(f'O herói de nome {nome} foi promovido de {dict_herois[nome]} para {nivel}', end="\n\n")
            else:
                print(f'O herói de nome {nome} continua no nível de {nivel}', end="\n\n")       
            dict_herois[nome] = nivel
    
    else:
        print(f"O Herói de nome {nome} está no nível de {nivel}", end="\n\n")
        dict_herois[nome] = nivel
