__version__ = '1.0.0'

reset = '\033[0m'

text = {
    'reset': reset,
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'sky': '\033[36m',
    'gray': '\033[37m',
    'corral': '\033[90m',
    'light_green': '\033[91m',
    'light_yellow': '\033[92m',
    'indigo': '\033[93m',
    'pink': '\033[94m',
    'cyan': '\033[95m',
}

background = {
    'reset': reset,
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'purple': '\033[45m',
    'sky': '\033[46m',
    'white': '\033[47m',
    'gray': '\033[100m',
    'corral': '\033[101m',
    'light_green': '\033[102m',
    'light_yellow': '\033[103m',
    'indigo': '\033[104m',
    'pink': '\033[105m',
    'cyan': '\033[106m',
}


def colorize(_text):
    for i in text:
        _text = _text.replace('{{text_' + i + '}}', text[i])

    for i in background:
        _text = _text.replace('{{bg_' + i + '}}', background[i])

    _text += reset

    return _text


__all__ = ['text', 'background', 'colorize', '__version__']
