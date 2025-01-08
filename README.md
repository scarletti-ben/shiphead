# Shiphead
- Shiphead is a card game I learned when I was younger, I have been enjoying it for years and have adapted the rules over time. The game is played with a regular deck of 52 cards in which some cards are given special abilities. I have attempted to recreate Shiphead using `Python` and make it playable
- The rules for the original card game can be found [here](#game-rules)
- The controls for the the electronic version of the game can be found [here](#game-controls)

# Installation

### Simple Install (Windows)
- Navigate to the latest releases section [here](https://github.com/scarletti-ben/shiphead/releases/latest) and click to download the latest `.exe` file
- Alternatively you can download `shiphead-v0.1.1-alpha.exe` [here](https://github.com/scarletti-ben/shiphead/releases/download/v0.1.1-alpha/shiphead-v0.1.1-alpha.exe)
- Once downloaded, simply find the installed file and open the game by double-clicking the `.exe` file

### Alternative Install

- Install the repository via `git clone https://github.com/scarletti-ben/shiphead`
- Change directory into the repository via `cd .\shiphead\` 
- Set up a virtual environment [**Optional**]
  -  Initialise the virtual environment via `python -m venv venv`
  -  Activate the virtual environment via `.\venv\Scripts\activate`
- Install required packages via `pip install -r requirements.txt`
- Run the python script via `python main.py`
- The recommended python version is `Python 3.12.1`, you can check your python version via `python --version`

# Game Rules
Test

# Game Controls
- The game is primarily controlled by your mouse
    - Left mouse button to alter settings and drag cards
    - Right mouse button to pick up cards from the middle
- Spacebar to pick up cards from the middle
- Upon opening the game you are met with settings
    - Clear Deck => Default = True
    - Pick Cards => Default = False
    - Shuffle => Default = True
    - Hand Size => Default = 5
    - Table Cards => Default = 3
    - Hide AI => Default = True
- Cards will fill with colour as a timer
    - If the colour is moving slowly it suggests you could play more of that rank of card
        - You do not have to, it may be tactical not to do so
- Drag your card from your hand to the center
- If you hover your mouse over the deck hand it will show all the valid cards in your hand that you can play
- The top left of the game has info and some debugging stats
- If picking mode is enabled then you get to pick your starting cards, swapping cards into and out of your hand until you are satisfied with your face up cards and hand, press any key to start the game when you are satisfied

# Information
- The latest release is `shiphead-v0.1.1-alpha` as of the **8th of January 2025**
- A list of all past releases can be found [here](https://github.com/scarletti-ben/shiphead/releases)
- Code for this project was written a long while ago and unceremoniously "hacked" together to create a first alpha release
- The `.exe` file is a frozen version of the python script `main.py`, and was frozen using `PyInstaller 6.6.0` and `Python 3.12.1`
- Python is embedded in the `.exe` file, this means that users will not need python installed on their system

# Asset Attribution
### Creative Commons Zero (CC0) Assets
- The font `monogram` can be found from `datagoblin` [here](https://datagoblin.itch.io/monogram)
- The card images are edited, and the originals can be found from `beemaxstudio`  [here](https://beemaxstudio.itch.io/pixel-cards-pack)

### Other Assets
- The icon for the game was created by `mangsaabguru`, it is free to use with attribution and can be found [here](https://www.flaticon.com/free-icon/card-game_4072251)
