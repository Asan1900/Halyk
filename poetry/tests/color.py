import sys

def load_banner(file):
    with open(file, 'r') as f:
        return f.read()

def colorize_string(string, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }

    reset_color = '\033[0m'
    colored_string = ''
    for letter in string:
        colored_letter = colors.get(color, '') + letter + reset_color
        colored_string += colored_letter
    return colored_string

def generate_ascii_art(string, color=None, letters=None):
    if color and letters:
        colored_string = colorize_string(letters, color)
        string = string.replace(letters, colored_string)
    print(string)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 color.py "string" --color=<color> <letters to be colored>')
        sys.exit(1)

    string = sys.argv[1]
    color_option = '--color='
    color_index = next((i for i, arg in enumerate(sys.argv) if arg.startswith(color_option)), None)
    if color_index is not None:
        color = sys.argv[color_index].replace(color_option, '')
        letters = sys.argv[color_index + 1] if len(sys.argv) > color_index + 1 else None
        generate_ascii_art(string, color, letters)
    else:
        generate_ascii_art(string)
