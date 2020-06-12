# Imports
from os import getenv
from bot.crow import CROW

# Constants
KEY = getenv("BOTKEY")

# Main function
def main():
    CROW.run(KEY)

main()
