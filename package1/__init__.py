# __init__.py
from .module import greet
from.module import factorial
from .utils import add

__version__ = '1.0.0'
__doc__ = 'Это пакет, который содержит...'
__author__ = 'John'
__all__ = ['greet', 'add', 'factorial']  # для импорта со *
