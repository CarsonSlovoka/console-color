__all__ = (
    'RGB', 'cprint', 'create_print',
    'Style', 'Fore', 'BG',
    'clear_console',)
__version__ = '0.0.3'
__author__ = ['Carson', ]
__description__ = 'print with color on the console.'

from sys import platform
from os import system
from .core import RGBColor, ColorPrinter, Style, Fore, BG


def clear_console():
    is_win = platform.startswith('win')
    system('cls') if is_win else system('clear')


RGB, cprint, zprint, create_print = RGBColor(), ColorPrinter.print, ColorPrinter.zprint, ColorPrinter.create_print
