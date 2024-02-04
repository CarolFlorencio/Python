# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:34:40 2024

@author: carol
"""
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praca', 'gourmet')
#restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
#Restaurante('Japa', 'Japonesa')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_tacaca = Prato('Tacaca', 20.0, 'Prato de tacaca com camarão')
sobremesa_petit = Sobremesa('Petit Gatue', 20.0, 'gelada', 'Pequena')
sobremesa_petit.aplicar_desconto()
prato_tacaca.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_tacaca)
restaurante_praca.adicionar_no_cardapio(sobremesa_petit)
#restaurante_mexicano.alternar_estado()
#restaurante_praca.mostrar_cardapio()
restaurante_praca.receber_avaliacao('Gui', 5)
restaurante_praca.receber_avaliacao('Lais', 4)
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    #Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio
    #restaurante_praca.listar_avaliacao()
    
if __name__ == '__main__':
    main()