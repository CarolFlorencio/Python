# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 06:57:57 2024

@author: carol
"""
from modelos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo
        
    def __str__(self):
        return f"{super().__str__()}| {self._tipo}"
    
    def liga_desliga(self):
        self._ligado = not self._ligado