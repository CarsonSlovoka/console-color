.. raw:: html

    <p align="left">

        <a href="https://pypi.org/project/console-color/">
        <img src="https://img.shields.io/static/v1?&style=plastic&logo=pypi&label=App&message=console-color&color=00FFFF"/></a>

        <a href="https://pypi.org/project/console-color/">
        <img src="https://img.shields.io/pypi/v/console-color.svg?&style=plastic&logo=pypi&color=00FFFF"/></a>

        <a href="https://pypi.org/project/console-color/">
        <img src="https://img.shields.io/pypi/pyversions/console-color.svg?&style=plastic&logo=pypi&color=00FFFF"/></a>

        <a href="https://github.com/CarsonSlovoka/console-color/blob/master/LICENSE">
        <img src="https://img.shields.io/pypi/l/console-color.svg?&style=plastic&logo=pypi&color=00FFFF"/></a>

        <br>

        <a href="https://github.com/CarsonSlovoka/console-color">
        <img src="https://img.shields.io/github/last-commit/CarsonSlovoka/console-color?&style=plastic&logo=github&color=00FF00"/></a>

        <img src="https://img.shields.io/github/commit-activity/y/CarsonSlovoka/console-color?&style=plastic&logo=github&color=0000FF"/>

        <a href="https://github.com/CarsonSlovoka/console-color">
        <img src="https://img.shields.io/github/contributors/CarsonSlovoka/console-color?&style=plastic&logo=github&color=111111"/></a>

        <a href="https://github.com/CarsonSlovoka/console-color">
        <img src="https://img.shields.io/github/repo-size/CarsonSlovoka/console-color?&style=plastic&logo=github"/></a>

        <br>

        <a href="https://pepy.tech/project/console-color">
        <img src="https://pepy.tech/badge/console-color"/></a>

        <!--

        <a href="https://pepy.tech/project/console-color/month">
        <img src="https://pepy.tech/badge/console-color/month"/></a>

        <a href="https://pepy.tech/project/console-color/week">
        <img src="https://pepy.tech/badge/console-color/week"/></a>

        -->

        <!--
            <img src="https://img.shields.io/github/commits-since/m/CarsonSlovoka/console-color/Dev?label=commits%20to%20be%20deployed"/></a>
        -->

    </p>

==================
Console Color
==================

**print with color on the console.**

Install
============

``pip install console-color``

Features
============

- It allows you to register your own styles.
- Supports fore, background, style (Bold, Italic, URL, ...), and you can do **permutations**, really flexible.
- Well documented, you can find all the usage form `test.py`_ folder and `console_color.ipynb`_

.. note:: Github page may not show ipynb well, you can go `here <https://colab.research.google.com/drive/1cAYcC6DyiMCyD0RDcEo25LDFCh527TUQ?usp=sharing>`_ to see another resource that I put on Google Colab

Usage
------

.. code-block:: python

    from console_color import *

    # cprint(text, fg=, bg=, style=)
    cprint('...', RGB.WHITE, '#ff0000', Style.BOLD + Style.URL)
    cprint('...', (255, 0, 0), RGB.YELLOW, Style.BOLD + Style.URL)

    # you can do permutations, for example, you only need style only then
    cprint('...', style=Style.BOLD)

    # combine with normal text
    print('123' + cprint('...', '#ff0000', pf=False) + '~~~')

.. note:: get more help; please reference the `test.py`_  and `console_color.ipynb`_

Demo
==========

.. image:: https://raw.githubusercontent.com/CarsonSlovoka/console-color/release/doc/_static/nav_bar.logo.png

.. raw:: html
    :url: https://carsonslovoka.github.io/console-color/demo/console_color.html


Contributing
===============

If you want to contribute, please use the ``release`` branch as the stable branch. ``dev`` is the future branch for the maintainer.

Be sure to **write tests** for new features. If you have any difficulties, you can ask me or discuss with me. I am glad if you want to join us.

By the way, I'm very friendly! (You can ask me questions with Chinese)

Useful Reference
==================

The below link may help you to understand how do you write, such as this library by yourself.

- `★ ANSI_escape_code <https://en.wikipedia.org/wiki/ANSI_escape_code>`_
- `stackoverflow: how to print colored text in terminal in python <https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python>`_


More
===========

See the `documentation <https://carsonslovoka.github.io/console-color/>`_

.. _test.py: https://github.com/CarsonSlovoka/console-color/blob/release/console_color/test/test.py
.. _console_color.ipynb: https://github.com/CarsonSlovoka/console-color/blob/release/console_color/demo/console_color.ipynb
