import random

colors = random.choice(["32m", "33m", "34m", "35m", "36m"])
clear = f"\033[0m"
replace = f"\033[7;{colors}"
banner = f"""\033[5;{colors}
 █▀▄ █░█ █▀▄ █░░ ▄▀▄ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█
 █░█ █░█ █░█ █░▄ █░█ ░▀▄ █░█ █▀█ █░█░█
 ▀▀░ ░▀░ █▀░ ▀▀▀ ░▀░ ▀▀░ █▀░ ▀░▀ ▀░░░▀
{clear}"""

cursor = f"\033[1;{colors}d.hack >> "
