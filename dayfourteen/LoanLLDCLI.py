import argparse
from model import Loan
import os
from dotenv import load_dotenv
from LoanService import *
from pathlib import Path

parser = argparse.ArgumentParser(description='Loan Multilingual App')
parser.add_argument('--lang', 
                    choices=['en', 'hi', 'ta', 'kn'], 
                    default='en',
                    help='Language code')
args = parser.parse_args()
# Load the appropriate language file
env_file = f"{args.lang}.env"
load_dotenv(env_file,override=True)
print(os.getenv("WELCOME"))
data_source = input(os.getenv("SELECT_SOURCE"))
service=LoanService(data_source)
while True:
    print(os.getenv("MENU"))
    choice = int(input(os.getenv("ASK_SELECT")))
    if choice == 1:
        service.introduce(
            int(input(os.getenv("ENTER_NO"))),
            input(os.getenv("ENTER_NAME")),
            input(os.getenv("ENTER_TYPE")),
            input(os.getenv("ENTER_ELG")),
            input(os.getenv("ENTER_UP")),
            float(input(os.getenv("ENTER_ROI"))),
            int(input(os.getenv("ENTER_AMOUNT"))),
            )
    elif choice == 2: service.view()
    else: break
    