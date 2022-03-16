def obter_letras(colunas: int) -> list: 
    return [chr(col + 97) for col in range(colunas)]


def obter_mensagem_final(status: str) -> str:
    if status == 'x' or status == 'o':
        return f'A partida terminou em vitoria do jogador {status}! Deseja jogar novamente? S/N:'
    
    if status == 'empate':
        return 'A partida terminou empatada! Deseja jogar novamente? S/N:'
    
    if status == 'jogando':
        return 'Partida em andamento...'
