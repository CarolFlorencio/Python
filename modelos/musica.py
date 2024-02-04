# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:04:03 2024

@author: carol
"""

class Musica:
    
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = int(duracao)
    
    def __str__(self):
        return f'{self.nome} | {self.artista} | Duração: {self.duracao} segundos'
    
    