# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:50:48 2024

@author: carol
"""
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    """Representa um restaurante e suas características."""
    def __init__(self, nome, categoria):
        """
            Inicializa uma instância de Restaurante.
            
            Parâmetros:
            - nome (str): O nome do restaurante.
            - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
       
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        nome = 'Nome do restaurante'
        cat = 'Categoria'
        sts = 'Avaliações'
        print(f'{nome.ljust(25)} | {cat.ljust(25)} | {sts.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else: 
            print('Nota fora do padão avaliação recusada')
    
    @property    
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media
    
    def listar_avaliacao(self):
        """Exibe uma lista formatada de todas as avaliações do restaurante."""
        nome = 'Nome do restaurante'
        print(f'{nome.ljust(25)} | {self._nome.ljust(25)}')
        separador = '*'*len(f'{nome.ljust(25)} | {self._nome.ljust(25)}')
        print(separador)
        cat = 'Cliente'
        sts = 'Nota'
        print(f'{cat.ljust(25)} | {sts}')
        separador = '*'*len(f'{cat.ljust(25)} | {sts}')
        print(separador)
        for avaliacao in self._avaliacao:
            print(f'{avaliacao._cliente.ljust(25)} | {avaliacao._nota}')
    
    def mostrar_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}')
        for item in self._cardapio:
            print(item)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}')
        for i,item in enumerate(self._cardapio, start=1):
            mensagem = f'{i}. Nome:{item._nome.ljust(20)} | Preço:{str(item._preco).ljust(20)}'
            if hasattr(item, '_tamanho'):
                mensagem = mensagem + f' | Tamanho:{item._tamanho}'
            elif hasattr(item, '_descricao'):
                mensagem = mensagem + f' | Descrição:{item._descricao}'
            elif hasattr(item, '_tipo'):
                mensagem = mensagem + f' | Descrição:{item._tipo}'
            print(mensagem)
    
    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return 'Ativado' if self._ativo else 'Desativado'