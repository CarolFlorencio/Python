# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:27:04 2024

@author: carol
"""

from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        
    def __str__(self):
        sob = 'Bebida: '
        return f'{sob.ljust(20)}{super().__str__()} | Tamanho:{self._tamanho}'
    
    def aplicar_desconto(self):
        self._preco = self._preco * 0.92