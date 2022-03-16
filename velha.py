import utils
import regras
import config


def novo_jogo() -> dict:
    jogo = {}
    letras = utils.obter_letras(config.COLUNAS)
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

        if coordenada in jogo.keys() and jogo[coordenada] == '-':
            break

        print('Coordenada invalida. Tente novamente.')

    jogo[coordenada] = jogada
    config.ultima_jogada = jogada


def jogo_finalizado(jogo: dict) -> bool:
    return False


def status_jogo(jogo: dict) -> str:
    for sequencia in regras.sequencias_vitoria:
        contem_x = 0
        contem_o = 0

        for coord in sequencia:
            if jogo[coord] == 'x': contem_x += 1
            elif jogo[coord] == 'o': contem_o += 1

        if contem_x == 3: return 'x'
        if contem_o == 3: return 'o'

    if '-' in jogo.values(): return 'jogando'
    return 'empate'


def mensagem_final(status: str):
    if status == 'x' or status == 'o':
        return f'A partida terminou em vitoria do jogador {status}! Deseja jogar novamente? S/N:'
    
    if status == 'empate':
        return 'A partida terminou empatada! Deseja jogar novamente? S/N:'
    
    if status == 'jogando':
        return 'Partida em andamento...'


def mostrar_jogo(jogo: dict,) -> None:
    letras = utils.obter_letras(config.COLUNAS)
    print('  ', end='')
    print(*letras, sep=' ')

    for coord, slot in jogo.items():
        ultima_letra = letras[-1]
        primeira_letra = letras[0]

        start = f'{coord[1]} ' if coord[0] == primeira_letra else ''
        end = '\n' if coord[0] == ultima_letra else ' '

        print(start + slot, end=end)


def finalizar_jogo(status: str) -> bool:
    mensagem = mensagem_final(status)
    print(mensagem, end=' ')

    while True:
        continuar = input().lower()
        
        if continuar == 's': return True
        elif continuar == 'n': return False

        print('Entrada invalida. Insira S ou N.')
