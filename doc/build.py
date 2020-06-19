from pathlib import Path
if 'eny path':
    sphinx_setting = __import__('conf')
import sphinx.cmd.build
import sphinx_intl.commands

import os


def get_text():
    src_dir = Path(__file__).parent.absolute()
    output_dir: Path = sphinx_setting.get_text_output_dir  # _gettext
    cmd_list = [str(src_dir), str(output_dir),
                '-b', 'gettext']
    sphinx.cmd.build.main(cmd_list)


def get_po_file():
    support_lang_list = sphinx_setting.support_lang_list
    lang_list = []
    [lang_list.extend(['-l', lang]) for lang, alias_name in support_lang_list]
    target_dir = sphinx_setting.get_text_output_dir  # _gettext
    cmd_list = ['update', '-p', str(target_dir)]
    cmd_list.extend(lang_list)
    print('spinx-intl ' + ' '.join(cmd_list))
    if hasattr(sphinx_setting, 'locale_dirs') is None:
        raise ValueError('Please set the **locale_dirs** in your conf.py')
    sphinx_intl.commands.main(cmd_list)
    os.startfile(target_dir)


if __name__ == '__main__':
    get_text()
    get_po_file()
