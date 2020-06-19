__all__ = ('test_setup',)

import unittest
from unittest import TestCase

if 'env path':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from console_color import __version__, RGB, cprint, zprint, create_print
    from console_color.core import Fore, BG, Style, ColorPrinter
    sys.path.remove(sys.path[0])


class CoreTests(TestCase):

    def test_basic(self):
        cprint('cp fore.red + bg.blue\n123', fore=RGB.RED, bg=RGB.BLUE)
        cprint('cp fore.red\n123', RGB.RED)
        cprint('cp bg.PURPLE\n123', bg=RGB.PURPLE)
        zprint('zp fore.yellow\n123', Fore.YELLOW)
        zprint('zp fore.violet + bg.red\n123', Fore.VIOLET, BG.RED)
        zprint('zp bg.violet\n123', bg=BG.RED)

    def test_combine(self):
        print('cp fore.red abc' + cprint('RED', RGB.RED, pf=False) + '456')
        print('cp fore.white + bg.black abc' + cprint('RED', RGB.WHITE, RGB.BLACK, pf=False) + '456')
        print('zp fore.yellow + bg.red ' + zprint('RED', Fore.YELLOW, BG.RED, '', False) + '456')
        print('zp style only: italic' + zprint('No fore, no bg, and style is ITALIC', style=Style.ITALIC, pf=False) + '  456')
        print('zp style only: italic' + zprint('No fore, no bg, and style is ITALIC', style=Style.BOLD + Style.ITALIC, pf=False) + '  456')

    def test_style(self):
        zprint('zp fore: yellow\n bg: red, style:bold', Fore.YELLOW, BG.RED, style=Style.BOLD)
        zprint('zp fore: yellow, style:Italic', Fore.YELLOW, style=Style.ITALIC)
        zprint('zp style url', style=Style.URL)
        zprint('zp style strike', style=Style.STRIKE)
        cprint('cp fore: yellow, style: Italic', RGB.YELLOW, style=Style.ITALIC)
        cprint('cp style: URL', style=Style.URL)
        cprint('cp, fore: (102, 255, 204), style: Italic ', fore=(102, 255, 204), style=Style.ITALIC)
        cprint('cp fore: #6666ff, s: Italic', fore='#6666ff', style=Style.ITALIC)
        cprint('cp fore: #6666ff bg: #66ff33', fore='#6666ff', bg='#66ff33', style=Style.ITALIC)
        cprint('cp style: strike', style=Style.STRIKE)

    def test_create_print(self):
        my_print = ColorPrinter.create_print(fore='#FF0000', bg='#0080ff', style=Style.ITALIC)
        red_print = ColorPrinter.create_print(fore=(255, 0, 0), bg=(0, 128, 255), style=Style.ITALIC)
        bi_print = ColorPrinter.create_print(style=Style.BOLD + Style.ITALIC, pf=False)
        my_print("red print fore='#FF0000', bg='#0080ff', style=Style.ITALIC")
        red_print("red print fore=(255, 0, 0), bg=(0, 128, 255), style=Style.ITALIC")
        print(f'This is {bi_print("Italic and Bold")} !!!')

    def test_end_flag(self):
        """
        With end-flag, it makes the print normal. Otherwise, it will keep the style that you last used.
        """
        cprint('cp fore.red + bg.blue', fore=RGB.RED, bg=RGB.BLUE, end_flag=False)
        print('fore.red + bg.blue')
        print(Style.NORMAL + 'normal')

    def test_basic_usage(self):
        print('#only Fore test#')
        cprint('red: RGB.RED', RGB.RED)
        cprint('red: #FF0000', bg='#FF0000')  # It doesn't matter for string upper or lower, and if you don't want to add the sign of #, it's ok too.
        cprint('red: (255, 0, 0)', (255, 0, 0))

        print('#only Background test#')
        cprint('red: RGB.RED', bg=RGB.RED)
        cprint('red: #FF0000', bg='#ff0000')
        cprint('red: (255, 0, 0)', bg=(255, 0, 0))

        print('#fore + bg#')
        cprint('red: RGB.RED, RGB.YELLOW', RGB.RED, RGB.YELLOW)
        cprint('red: FF0000, #FFFF00', 'FF0000', '#FFFF00')
        cprint('red: (255, 0, 0), (255, 255, 0)', (255, 0, 0), (255, 255, 0))

        print('#style test#')
        cprint('Italic', style=Style.ITALIC)
        cprint('Italic and Bold', style=Style.BOLD + Style.ITALIC)
        cprint('Strike', style=Style.STRIKE)
        cprint('URL', style=Style.URL)

        print('#combine normal text#')  # set pf=False
        print(f"123 {cprint('Fore=Red, bg=Yellow, Style=Italic and Bold', RGB.RED, RGB.YELLOW, Style.BOLD + Style.ITALIC, False)} 456")
        print(f"123 {cprint('BOLD', style=Style.BOLD, pf=False)} 456")

        print('#keeping the setting#')
        ry_print = create_print(fore='FF0000', bg='#FFFF00')
        inner_ry_text = create_print('FF0000', '#FFFF00', Style.BOLD + Style.ITALIC, pf=False)
        msg = "fore='FF0000', bg='#FFFF00'"
        print(msg)
        ry_print(msg)
        print('...')
        ry_print(msg)

        print(f'123 {inner_ry_text("fore=red, bg=yellow, style=bold+italic")} !!!')


class CLITests(TestCase):

    def test_show_version(self):
        print(__version__)
        self.assertTrue(len(__version__) > 0)


def test_setup():
    # suite_list = [unittest.TestLoader().loadTestsFromTestCase(class_module) for class_module in (CLITests, )]
    # suite_class_set = unittest.TestSuite(suite_list)

    suite_function_set = unittest.TestSuite()
    suite_function_set.addTest(CLITests('test_show_version'))

    suite = suite_function_set  # pick one of two: suite_class_set, suite_function_set
    # unittest.TextTestRunner(verbosity=1).run(suite)  # self.verbosity = 0  # 0, 1, 2.  unittest.TextTestResult
    return suite


def try_by_yourself():
    """
    If you have no idea how to use this library, you can input by indicate, and then it will tell you what the grammar you should write.
    """

    text = chr(34) + input('text:') + chr(34)
    in_fore = input('Fore (#XXYYRR) (r, g, b):')
    if in_fore:
        in_fore = str(eval(in_fore)) if in_fore.find(',') != -1 else chr(34) + in_fore + chr(34)

    in_bg = input('Background (#XXYYRR) (r, g, b):')
    if in_bg:
        in_bg = str(eval(in_bg)) if in_bg.find(',') != -1 else chr(34) + in_bg + chr(34)

    in_style = input('Style (BOLD, ITALIC, URL, STRIKE) sep=" ":').split(' ')
    if in_style:
        in_style = '+'.join([f'Style.{_.upper()}' for _ in in_style])
    print_cmd = f"cprint({text}{', fore=' + in_fore if in_fore else ''}" \
                f"{', bg=' + in_bg if in_bg else ''}" \
                f"{', style=' + in_style if in_style else ''})"
    print(f'grammar: {cprint(print_cmd, RGB.GREEN, RGB.BLACK, pf=False)}')
    exec(print_cmd)


if __name__ == '__main__':
    try_by_yourself()
