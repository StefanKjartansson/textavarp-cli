#!/usr/bin/env python
# -*- coding: utf-8

import urwid

from pyquery import PyQuery as pq
import requests


urwid.set_encoding('utf-8')

BASE_URL = 'http://www.textavarp.is/%d/'
WIDTH = 40
START_PAGE = 100


palette = [
    ('c00', '', '', '', '#000', '#000'),
    ('c10', '', '', '', '#f00', '#000'),
    ('c20', '', '', '', '#0f0', '#000'),
    ('c30', '', '', '', '#ff0', '#000'),
    ('c40', '', '', '', '#00f', '#000'),
    ('c50', '', '', '', '#f0f', '#000'),
    ('c60', '', '', '', '#0ff', '#000'),
    ('c70', '', '', '', '#fff', '#000'),
    ('c01', '', '', '', '#000', '#f00'),
    ('c11', '', '', '', '#f00', '#f00'),
    ('c21', '', '', '', '#0f0', '#f00'),
    ('c31', '', '', '', '#ff0', '#f00'),
    ('c41', '', '', '', '#00f', '#f00'),
    ('c51', '', '', '', '#f0f', '#f00'),
    ('c61', '', '', '', '#0ff', '#f00'),
    ('c71', '', '', '', '#fff', '#f00'),
    ('c02', '', '', '', '#000', '#0f0'),
    ('c12', '', '', '', '#f00', '#0f0'),
    ('c22', '', '', '', '#0f0', '#0f0'),
    ('c32', '', '', '', '#ff0', '#0f0'),
    ('c42', '', '', '', '#00f', '#0f0'),
    ('c52', '', '', '', '#f0f', '#0f0'),
    ('c62', '', '', '', '#0ff', '#0f0'),
    ('c72', '', '', '', '#fff', '#0f0'),
    ('c03', '', '', '', '#000', '#ff0'),
    ('c13', '', '', '', '#f00', '#ff0'),
    ('c23', '', '', '', '#0f0', '#ff0'),
    ('c33', '', '', '', '#ff0', '#ff0'),
    ('c43', '', '', '', '#00f', '#ff0'),
    ('c53', '', '', '', '#f0f', '#ff0'),
    ('c63', '', '', '', '#0ff', '#ff0'),
    ('c73', '', '', '', '#fff', '#ff0'),
    ('c04', '', '', '', '#000', '#00f'),
    ('c14', '', '', '', '#f00', '#00f'),
    ('c24', '', '', '', '#0f0', '#00f'),
    ('c34', '', '', '', '#ff0', '#00f'),
    ('c44', '', '', '', '#00f', '#00f'),
    ('c54', '', '', '', '#f0f', '#00f'),
    ('c64', '', '', '', '#0ff', '#00f'),
    ('c74', '', '', '', '#fff', '#00f'),
    ('c05', '', '', '', '#000', '#f0f'),
    ('c15', '', '', '', '#f00', '#f0f'),
    ('c25', '', '', '', '#0f0', '#f0f'),
    ('c35', '', '', '', '#ff0', '#f0f'),
    ('c45', '', '', '', '#00f', '#f0f'),
    ('c55', '', '', '', '#f0f', '#f0f'),
    ('c65', '', '', '', '#0ff', '#f0f'),
    ('c75', '', '', '', '#fff', '#f0f'),
    ('c06', '', '', '', '#000', '#0ff'),
    ('c16', '', '', '', '#f00', '#0ff'),
    ('c26', '', '', '', '#0f0', '#0ff'),
    ('c36', '', '', '', '#ff0', '#0ff'),
    ('c46', '', '', '', '#00f', '#0ff'),
    ('c56', '', '', '', '#f0f', '#0ff'),
    ('c66', '', '', '', '#0ff', '#0ff'),
    ('c76', '', '', '', '#fff', '#0ff'),
    ('c07', '', '', '', '#000', '#fff'),
    ('c17', '', '', '', '#f00', '#fff'),
    ('c27', '', '', '', '#0f0', '#fff'),
    ('c37', '', '', '', '#ff0', '#fff'),
    ('c47', '', '', '', '#00f', '#fff'),
    ('c57', '', '', '', '#f0f', '#fff'),
    ('c67', '', '', '', '#0ff', '#fff'),
    ('c77', '', '', '', '#fff', '#fff'),
    ('listbox', 'light blue', 'black'),
]


def exit_on_q(input):
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    elif input in ('esc'):
        if current_page == START_PAGE:
            raise urwid.ExitMainLoop()
        try:
            navstack.pop()
            loop.widget = load_page(navstack.pop())
        except IndexError:
            loop.widget = load_page(START_PAGE)


navstack = []
current_page = START_PAGE
loop = urwid.MainLoop(None, palette,
    unhandled_input=exit_on_q)


class MenuItem(urwid.Text):

    def __init__(self, label):
        urwid.Text.__init__(self, label)
        self.state = False

    def selectable(self):
        return True

    def keypress(self, size, key):
        if key == "enter":
            self.state = True
            text, _ = self.get_text()
            loop.widget = load_page(int(text))
        return key

    def get_state(self):
        return self.state

    def get_label(self):
        text, attr = self.get_text()
        return text


def get_page_content(number):
    return pq(requests.get(BASE_URL % number).content)('pre.vt')


def load_page(number):

    navstack.append(number)
    global current_page
    current_page = number

    def get_curses(number, links):
        stack = []
        stack_length = 0

        for e in get_page_content(number)[0].getchildren()[:-1]:
            tc = e.text_content()

            if stack_length + len(tc) > WIDTH:
                yield urwid.Text(stack)
                stack = []
                stack_length = 0

            stack_length += len(tc)

            if e.getchildren():
                l = e.getchildren()[0].attrib['href'].strip('\/\\')
                if not l.startswith('0'):
                    links.append(l)

            stack.append((e.attrib['class'], tc))

        if stack:
            yield urwid.Text(stack)

        yield urwid.Text('-' * WIDTH)

    page_links = []
    page = urwid.Pile(list(get_curses(number, page_links)))

    content = urwid.SimpleListWalker(
        [urwid.AttrMap(w, None, 'reveal focus')
        for w in (MenuItem(i)
        for i in page_links)])

    listbox = urwid.ListBox(content)
    listbox = urwid.AttrWrap(listbox, 'listbox')
    listbox.set_focus(0, 'above')
    frame = urwid.Frame(listbox, page)
    return frame


def main():
    view = load_page(START_PAGE)
    loop.widget = view
    loop.screen.set_terminal_properties(colors=256)
    loop.run()


if __name__ == '__main__':
    main()
