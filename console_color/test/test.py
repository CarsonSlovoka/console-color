__all__ = ('test_setup',)

import unittest
from unittest import TestCase
from pathlib import Path

if 'env path':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from console_color import __version__, clear_console
    from console_color.core import RGB, Fore, BG, cprint, zprint, Style
    sys.path.remove(sys.path[0])


class CoreTests(TestCase):

    def test_basic(self):
        cprint('123\n456', fore=RGB.RED, bg=RGB.BLUE)
        cprint('123\n456', RGB.RED)
        zprint('123\n456', Fore.YELLOW)
        zprint('123\n456', Fore.VIOLET, BG.RED)

    def test_combine(self):
        print('abc' + cprint('RED', RGB.RED, pf=False) + '456')
        print('abc' + cprint('RED', RGB.WHITE, RGB.BLACK, pf=False) + '456')
        print('abc' + zprint('RED', Fore.YELLOW, BG.RED, '', False) + '456')
        print('abc' + zprint('No fore, no bg, and style is ITALIC', style=Style.ITALIC, pf=False) + '456')

    def test_style(self):
        zprint('zp fore: yellow\n bg: red, style:bold', Fore.YELLOW, BG.RED, style=Style.BOLD)
        zprint('zp fore: yellow, style:Italic', Fore.YELLOW, style=Style.ITALIC)
        zprint('zp style url', style=Style.URL)
        cprint('cp fore: yellow, style: Italic', RGB.YELLOW, style=Style.ITALIC)
        cprint('cp style: URL', style=Style.URL)
        cprint('cp, fore: (102, 255, 204), style: Italic ', fore=(102, 255, 204), style=Style.ITALIC)
        cprint('cp fore: #6666ff, s: I', fore='#6666ff', style=Style.ITALIC)
        cprint('cp fore: #6666ff bg: #66ff33', fore='#6666ff', bg='#66ff33', style=Style.ITALIC)


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
