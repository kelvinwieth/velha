import velha


jogo = velha.novo_jogo()
velha.mostrar_jogo(jogo)

while True:
    velha.nova_jogada(jogo)
    velha.mostrar_jogo(jogo)

    status = velha.status_jogo(jogo)

    if status == 'jogando': continue

    continuar = velha.finalizar_jogo(status)

    if not continuar: break
    else:
        jogo = velha.novo_jogo()
        velha.mostrar_jogo(jogo)
