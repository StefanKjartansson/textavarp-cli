#!/usr/bin/env python
# -*- coding: utf-8

css = '''
span.c00    { color: #000000; background-color: #000000 }
span.c10    { color: #ff0000; background-color: #000000 }
span.c20    { color: #00ff00; background-color: #000000 }
span.c30    { color: #ffff00; background-color: #000000 }
span.c40    { color: #0000ff; background-color: #000000 }
span.c50    { color: #ff00ff; background-color: #000000 }
span.c60    { color: #00ffff; background-color: #000000 }
span.c70    { color: #ffffff; background-color: #000000 }

span.c01    { color: #000000; background-color: #ff0000 }
span.c11    { color: #ff0000; background-color: #ff0000 }
span.c21    { color: #00ff00; background-color: #ff0000 }
span.c31    { color: #ffff00; background-color: #ff0000 }
span.c41    { color: #0000ff; background-color: #ff0000 }
span.c51    { color: #ff00ff; background-color: #ff0000 }
span.c61    { color: #00ffff; background-color: #ff0000 }
span.c71    { color: #ffffff; background-color: #ff0000 }

span.c02    { color: #000000; background-color: #00ff00 }
span.c12    { color: #ff0000; background-color: #00ff00 }
span.c22    { color: #00ff00; background-color: #00ff00 }
span.c32    { color: #ffff00; background-color: #00ff00 }
span.c42    { color: #0000ff; background-color: #00ff00 }
span.c52    { color: #ff00ff; background-color: #00ff00 }
span.c62    { color: #00ffff; background-color: #00ff00 }
span.c72    { color: #ffffff; background-color: #00ff00 }

span.c03    { color: #000000; background-color: #ffff00 }
span.c13    { color: #ff0000; background-color: #ffff00 }
span.c23    { color: #00ff00; background-color: #ffff00 }
span.c33    { color: #ffff00; background-color: #ffff00 }
span.c43    { color: #0000ff; background-color: #ffff00 }
span.c53    { color: #ff00ff; background-color: #ffff00 }
span.c63    { color: #00ffff; background-color: #ffff00 }
span.c73    { color: #ffffff; background-color: #ffff00 }

span.c04    { color: #000000; background-color: #0000ff }
span.c14    { color: #ff0000; background-color: #0000ff }
span.c24    { color: #00ff00; background-color: #0000ff }
span.c34    { color: #ffff00; background-color: #0000ff }
span.c44    { color: #0000ff; background-color: #0000ff }
span.c54    { color: #ff00ff; background-color: #0000ff }
span.c64    { color: #00ffff; background-color: #0000ff }
span.c74    { color: #ffffff; background-color: #0000ff }

span.c05    { color: #000000; background-color: #ff00ff }
span.c15    { color: #ff0000; background-color: #ff00ff }
span.c25    { color: #00ff00; background-color: #ff00ff }
span.c35    { color: #ffff00; background-color: #ff00ff }
span.c45    { color: #0000ff; background-color: #ff00ff }
span.c55    { color: #ff00ff; background-color: #ff00ff }
span.c65    { color: #00ffff; background-color: #ff00ff }
span.c75    { color: #ffffff; background-color: #ff00ff }

span.c06    { color: #000000; background-color: #00ffff }
span.c16    { color: #ff0000; background-color: #00ffff }
span.c26    { color: #00ff00; background-color: #00ffff }
span.c36    { color: #ffff00; background-color: #00ffff }
span.c46    { color: #0000ff; background-color: #00ffff }
span.c56    { color: #ff00ff; background-color: #00ffff }
span.c66    { color: #00ffff; background-color: #00ffff }
span.c76    { color: #ffffff; background-color: #00ffff }

span.c07    { color: #000000; background-color: #ffffff }
span.c17    { color: #ff0000; background-color: #ffffff }
span.c27    { color: #00ff00; background-color: #ffffff }
span.c37    { color: #ffff00; background-color: #ffffff }
span.c47    { color: #0000ff; background-color: #ffffff }
span.c57    { color: #ff00ff; background-color: #ffffff }
span.c67    { color: #00ffff; background-color: #ffffff }
span.c77    { color: #ffffff; background-color: #ffffff }
'''


def make_palette():

    def hex_to_urwid(c):
        return '#%s' % c.strip(';#')[::2]

    for i in css.splitlines():
        if not i:
            continue
        x = i.strip().split()
        yield (x[0][5:], '', '', '',
            hex_to_urwid(x[3]),
            hex_to_urwid(x[5]))


if __name__ == '__main__':
    print('palette = [')
    for i in make_palette():
        print('    %s,' % repr(i))
    print(']')
