def obter_letras(colunas: int) -> list: 
    return [chr(col + 97) for col in range(colunas)]
