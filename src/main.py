# Imports
from os import getenv
from bot import BOT

# Constants
KEY = getenv("BOTKEY")

# Main function
def main():
    BOT.run(KEY)

main()
