# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 06:48:04 2024

@author: carol
"""

from modelos.carro import Carro
from modelos.moto import Moto

veiculo_exemplo = Carro("Honda", "Lambreto", "Casual")
print(veiculo_exemplo)
veiculo_exemplo2 = Carro("Honda", "Civic", 4)
print(veiculo_exemplo2)
veiculo_exemplo.liga_desliga()
print(veiculo_exemplo)