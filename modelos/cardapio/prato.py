# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:26:44 2024

@author: carol
"""
from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self):
        sob = 'Prato: '
        return f'{sob.ljust(20)}{super().__str__()} | Descrição:{self._descricao}'
    
    def aplicar_desconto(self):
        self._preco = self._preco * 0.95