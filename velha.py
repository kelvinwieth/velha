import utils
import regras
import config


def novo_jogo() -> dict:
    jogo = {}
    letras = utils.obter_letras(config.TAMANHO)

    for lin in range(config.TAMANHO):
        for col in range(config.TAMANHO):
            letra = letras[col]
            jogo[f'{letra}{lin + 1}'] = '-'

    return jogo


def mostrar_jogo(jogo: dict) -> None:
    letras = utils.obter_letras(config.TAMANHO)

    print('  ', end='')
    print(*letras, sep=' ')

    for coord, slot in jogo.items():
        ultima_letra = letras[-1]
        primeira_letra = letras[0]

        start = f'{coord[1]} ' if coord[0] == primeira_letra else ''
        end = '\n' if coord[0] == ultima_letra else ' '

        print(start + slot, end=end)


def nova_jogada(jogo: dict) -> None:
    jogada = 'x' if regras.ultima_jogada == 'o' else 'o'

    while True:
        print(f'Jogador {jogada.upper()}: ', end='')
        coordenada = input()

        if coordenada in jogo.keys() and jogo[coordenada] == '-': break

        print('Coordenada invalida. Tente novamente.')

    jogo[coordenada] = jogada
    regras.ultima_jogada = jogada


def status_jogo(jogo: dict) -> str:
    for sequencia in regras.sequencias_vitoria:
        contem_x = 0
        contem_o = 0

        for coord in sequencia:
            if jogo[coord] == 'x': contem_x += 1
            elif jogo[coord] == 'o': contem_o += 1

        if contem_x == config.TAMANHO: return 'x'
        if contem_o == config.TAMANHO: return 'o'

    if '-' in jogo.values(): return 'jogando'
    return 'empate'


def finalizar_jogo(status: str) -> bool:
    mensagem = utils.obter_mensagem_final(status)
    print(mensagem, end=' ')

    while True:
        continuar = input().lower()
        
        if continuar == 's': return True
        elif continuar == 'n': return False

        print('Entrada invalida. Insira S ou N.')
