# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 06:41:26 2024

@author: carol
"""

from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas
        
    def __str__(self):
        return f"{super().__str__()}| {self._portas}"
    
    def liga_desliga(self):
        self._ligado = not self._ligado