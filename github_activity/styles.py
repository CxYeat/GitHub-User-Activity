class Colors:
    def __init__(self):
        # Regular colors
        self.red = '\033[91m'
        self.green = '\033[92m'
        self.blue = '\033[94m'
        self.yellow = '\033[93m'
        self.magenta = '\033[95m'
        self.cyan = '\033[96m'
        self.white = '\033[97m'
        self.reset = '\033[0m'

    def colorize(self, text, color):
        """Add color to text and handle reset automatically"""
        color_code = getattr(self, color.lower(), '')
        return f"{color_code}{text}{self.reset}"

class TextStyle:
    def __init__(self):
        # Text styles
        self.bold = '\033[1m'
        self.underline = '\033[4m'
        self.reversed = '\033[7m'
        self.reset = '\033[0m'

        # Colors from our previous class
        self.colors = Colors()

    def format(self, text, color=None, bold=False, underline=False, reverse=False):
        """Apply multiple text styles at once"""
        style = ''
        if bold:
            style += self.bold
        if underline:
            style += self.underline
        if reverse:
            style += self.reversed
        if color:
            style += getattr(self.colors, color.lower(), '')

        return f"{style}{text}{self.reset}"