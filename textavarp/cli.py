#!/usr/bin/env python
# -*- coding: utf-8

import urwid


def main():
    txt = urwid.Text(u"Hello World")
    fill = urwid.Filler(txt, 'top')
    loop = urwid.MainLoop(fill)
    loop.run()


if __name__ == '__main__':
    main()
