from utils import obter_letras
import config

def novo_jogo() -> dict:
    jogo = {}
    letras = obter_letras(config.COLUNAS)
    for lin in range(config.LINHAS):
        for col in range(config.COLUNAS):
            letra = letras[col]
            jogo[f'{letra}{lin + 1}'] = '-'

    return jogo


def nova_jogada(jogo: dict) -> None:
    jogada = 'x' if config.ultima_jogada == 'o' else 'o'

    while True:
        print(f'Jogador {jogada.upper()}: ', end='')
        coordenada = input()

        if coordenada in jogo.keys():
            break

        print('Coordenada invalida. Tente novamente.')

    jogo[coordenada] = jogada
    config.ultima_jogada = jogada


def jogo_finalizado(jogo: dict) -> bool:
    return False
