# Author: Austin Coules (C23444946)

# Git did not support the .mo binaries well
# As a workaround we excluded the binaries from the repo
# Which requires the end user to compile it themselves
# This script also runs the flask server for convenience

import os

def main():
    # Install dependencies
    os.system('pip install flask')
    os.system('pip install babel')

    # Run website
    os.system('pybabel compile -d app/translations')
    os.system('flask run')

if __name__ == '__main__':
    main()
