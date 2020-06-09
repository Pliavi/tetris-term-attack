import TColors


def generate_title():
    title_pattern = """
    a.---. b.----.c.----. d.-.   .-.e.-.d.-. .-.  c.--.  b.-.
    a(_   _)b| (_  c| ()  )d|  `.'  |e| |d|  `| | c/ () \ b| |
    a| |  b| (__ c| .-. \d| |\ /| |e| |d| |\  |c/  /\  \b| `--.
    a`-'  b`----'c`-' `-'d`-' ` `-'e`-'d`-' `-'c`-'  `-'b`----'
            c.--.  e.---.  a.---.  d.--.   b.---. a.-. .-.
        c/ () \e(_   _)a(_   _)d/ () \ b/  ___)a| |/ /
        c/  /\  \ e| |    a| | d/  /\  \b\     )a| |\ \
        c`-'  `-' e`-'    a`-' d`-'  `-' b`---' a`-' `-'

            z=== PRESS ANY KEY TO START ===r
    """

    colored_title = title_pattern \
        .replace("a", TColors.FG_RED) \
        .replace("b", TColors.FG_GREEN) \
        .replace("c", TColors.FG_YELLOW) \
        .replace("d", TColors.FG_BLUE) \
        .replace("e", TColors.FG_PURPLE) \
        .replace("r", TColors.RESET) \
        .replace("z", TColors.BLINK)

    return colored_title
