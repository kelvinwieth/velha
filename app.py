import printer
import velha
import config

jogo = velha.novo_jogo()

printer.mostrar_jogo(jogo)

while not config.vencedor:
    velha.nova_jogada(jogo)
    printer.mostrar_jogo(jogo)
