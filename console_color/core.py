from typing import NamedTuple, Union, Type, Tuple, TypeVar, Callable
import warnings

T_print_flag = TypeVar('T_print_flag', bound=bool)
T_RGB = TypeVar('T_RGB', Tuple[int, int, int], str)


class RGBColor:
    """
    USAGE::

        rgb = RGBColor(tuple)
        rgb.RED  # (255, 0, 0)
        rgb.change_format(str)
        rgb.RED  # '#FF0000'
    """
    __slots__ = ('_out_format', )
    BLACK = (0, 0, 0)
    AZURE = (0, 127, 255)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (255, 255, 0)

    def __init__(self, out_format: Type[Union[str, tuple]] = tuple):
        self._out_format = out_format

    def change_format(self, new_type: Type[Union[str, tuple]]):
        self._out_format = new_type

    def __getattribute__(self, item):
        iv = super().__getattribute__(item)
        if not item.isupper() or item.startswith('_'):
            return iv

        assert isinstance(iv, (tuple, str)), ValueError(iv)

        out_format = super(RGBColor, self).__getattribute__('_out_format')
        if isinstance(iv, out_format):
            # item format same as the out_format
            return iv

        if isinstance(out_format, tuple):  # mean item format is str
            return tuple(int(iv[i:i+2], 16) for i in range(0, 6, 2))

        return f'#{"".join(["%0.2X" % i for i in iv])}'


class SchemeStyle(NamedTuple):
    # https://en.wikipedia.org/wiki/ANSI_escape_code
    NORMAL = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    URL = '\33[4m'
    BLINK_SLOW = '\33[5m'  # less than 150 per minute
    BLINK_RAPID = '\33[6m'  # MS-DOS ANSI.SYS, 150+ per minute; not widely supported
    SELECTED = '\33[7m'
    HIDDEN = '\033[8m'
    STRIKE = '\033[9m'


class SchemeBG(NamedTuple):
    BLACK = '\33[40m'
    RED = '\33[41m'
    GREEN = '\33[42m'
    YELLOW = '\33[43m'
    BLUE = '\33[44m'
    VIOLET = '\33[45m'
    BEIGE = '\33[46m'
    WHITE = '\33[47m'

    GREY = '\33[100m'
    RED2 = '\33[101m'
    GREEN2 = '\33[102m'
    YELLOW2 = '\33[103m'
    BLUE2 = '\33[104m'
    VIOLET2 = '\33[105m'
    BEIGE2 = '\33[106m'
    WHITE2 = '\33[107m'


class SchemeFore(NamedTuple):
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'

    GREY = '\33[90m'
    RED2 = '\33[91m'
    GREEN2 = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2 = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2 = '\33[96m'
    WHITE2 = '\33[97m'


Fore = SchemeFore()
BG = SchemeBG()
Style = SchemeStyle()


class ColorPrinter:

    __slots__ = ()

    warnings_show = True

    @classmethod
    def create_print(
        cls, fore: T_RGB = None, bg: T_RGB = None, style: Style = '', pf: T_print_flag = True
    ) -> Callable[[str], Union[None, str]]:
        """
        Usage::

            from console_color import *
            my_print = ColorPrinter.create_print(fore='#FF0000', bg=(0, 128, 255), style=Style.ITALIC)
            my_print('text')
        """
        return lambda text: cls.print(text, fore, bg, style, pf)

    @staticmethod
    def _set_color(text, target: int, rgb: Tuple[int, int, int], end_tag=True):
        r, g, b = rgb
        return f"\033[{target};2;{r};{g};{b}m{text}{Style.NORMAL if end_tag else ''}"

    @classmethod
    def fore_color(cls, text, rgb: Tuple[int, int, int], end_tag=True):
        """
        :param text:
        :param rgb:
        :param end_tag: auto add end tag or not.
        :return:
        """
        return cls._set_color(text, 38, rgb, end_tag)

    @classmethod
    def back_color(cls, text, rgb: Tuple[int, int, int], end_tag=True):
        """
        :param text:
        :param rgb:
        :param end_tag: auto add end tag or not.
        :return:
        """
        return cls._set_color(text, 48, rgb, end_tag)

    @classmethod
    def print(cls, text: str, fore: T_RGB = None, bg: T_RGB = None,
              style: Style = '',
              pf: T_print_flag = True, end_flag=True):
        """
        print with color

        :param text:
        :param fore: you can use `RGB.` or something like `#FF0000`
        :param bg: background color. `RGB.` or `#FF0000`
        :param style: Style.BOLD, Style.Italic, Style.URL ...
        :param pf: print_flag. It will print when it is True. Otherwise, return the value.
        :param end_flag: Auto-add end flag unless you want keep the style continue. Otherwise, make it to True.
        :return:
        """

        if isinstance(fore, str):
            # fore = tuple(int(fore.replace('#', '')[i:i + 2], 16) for i in (0, 2, 4))  # IDE Type checker is not working well.
            r, g, b = tuple(int(fore.replace('#', '')[i:i + 2], 16) for i in (0, 2, 4))
            fore = tuple((r, g, b))

        if isinstance(bg, str):
            r, g, b = tuple(int(bg.replace('#', '')[i:i + 2], 16) for i in (0, 2, 4))
            bg = tuple((r, g, b))
        fore = cls.fore_color('', fore, end_tag=False) if fore else ''
        bg = cls.back_color('', bg, end_tag=False) if bg else ''
        text = bg + fore + style + text + (Style.NORMAL if end_flag else '')
        return print(text) if pf else text

    @classmethod
    def zprint(cls, text: str,
               fore: Fore = '', bg: BG = '', style: Style = '',
               pf: T_print_flag = True, end_flag=True):
        """

        **Zenburn** is a color scheme created for Vim.

        :param text:
        :param fore: Please choose from the ``Fore.``
        :param bg: Please choose from the ``BG.``
        :param style: Style.BOLD, Style.Italic, Style.URL ...
        :param pf: It will print when it is True. Otherwise, return the value.
        :param end_flag: Auto-add end flag unless you want keep the style continue. Otherwise, make it to True.
        :return:
        """

        if cls.warnings_show:
            warnings.warn("zprint is not better than cprint, consider use cprint to instead of it.", DeprecationWarning)
            cls.warnings_show = False

        text = bg + fore + style + text + (Style.NORMAL if end_flag else '')
        return print(text) if pf else text
