# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:26:20 2024

@author: carol
"""
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    def __str__(self):
        return f'Item:{self._nome.ljust(20)} | Preço:{str(self._preco).ljust(20)}'
    
    @abstractmethod
    def aplicar_desconto(self):
        pass