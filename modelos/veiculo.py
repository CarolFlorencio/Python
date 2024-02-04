# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 06:39:32 2024

@author: carol
"""
from abc import ABC, abstractmethod
class Veiculo(ABC): 
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
        
    def __str__(self):
        return f"{self._marca.ljust(20)}|{self._modelo.ljust(20)}|{self.estado.ljust(20)}"
    
    @property
    def estado(self):
        return "Ligado" if self._ligado else "Desligado"
    @abstractmethod
    def liga_desliga(self):
        pass
    