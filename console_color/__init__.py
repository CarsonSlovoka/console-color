__all__ = ('__version__', '__author__', '__description__', 'clear_console',)
__version__ = '0.0.0'
__author__ = ['Carson', ]
__description__ = '...'

from sys import platform
from os import system


def clear_console():
    is_win = platform.startswith('win')
    system('cls') if is_win else system('clear')
