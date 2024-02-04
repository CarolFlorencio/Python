# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 09:43:59 2024

@author: carol
"""
from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        
    def __str__(self):
        sob ='Sobremesa: '
        return f'{sob.ljust(20)}{super().__str__()} | Tipo:{self._tipo.ljust(20)} | Tamanho:{self._tamanho.ljust(20)}'
        
    def aplicar_desconto(self):
        self._preco = self._preco * 0.90