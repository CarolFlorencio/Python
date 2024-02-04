# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 06:33:06 2024

@author: carol
"""
from modelos.banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero
        