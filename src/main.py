# Imports
from os import getenv
from dotenv import load_dotenv
from bot import BOT

# Initial functions
load_dotenv()

# Initial constants
KEY = getenv("BOTKEY")

# Main function
def main():
    BOT.run(KEY)

main()
