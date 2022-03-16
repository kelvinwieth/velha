import config
from utils import obter_letras


def mostrar_jogo(jogo: dict,) -> None:
    letras = obter_letras(config.COLUNAS)
    print('  ', end='')
    print(*letras, sep=' ')

    for coord, slot in jogo.items():
        ultima_letra = letras[-1]
        primeira_letra = letras[0]

        start = f'{coord[1]} ' if coord[0] == primeira_letra else ''
        end = '\n' if coord[0] == ultima_letra else ' '

        print(start + slot, end=end)
