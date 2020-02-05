# Imports
from os import getenv
from dotenv import load_dotenv
from bot import BOT

# Functions
load_dotenv('.env')

# Constants
KEY = getenv("BOTKEY")

# Main function
def main():
    BOT.run(KEY)

main()
