# Shiphead
- Shiphead is a card game I learned when I was younger, I have been enjoying it for years and have adapted the rules over time. The game is played with a regular deck of 52 cards in which some cards are given special abilities. I have attempted to recreate Shiphead using `Python` and make it playable
- The rules for the original card game can be found [here](#game-rules)
- The controls for the the electronic version of the game can be found [here](#game-controls)

# Installation

### Simple Install (Windows)
- Navigate to the latest release [here](https://github.com/scarletti-ben/shiphead/releases/latest) and you can find the `.exe` file in the `Assets` section below
- Alternatively you can download `shiphead-v0.1.1-alpha.exe` [here](https://github.com/scarletti-ben/shiphead/releases/download/v0.1.1-alpha/shiphead-v0.1.1-alpha.exe)
- Once downloaded, simply find the installed file and open the game by double-clicking the `.exe` file

### Windows Warning Message
- Windows often shows warnings for unsigned `.exe` files that look like this:
```
Windows protected your PC
Microsoft Defender SmartScreen prevented an unrecognised app from starting. Running this app might put your PC at risk.
[More info]
```
- This should only happen the first time you open the game, and you can simply click `More info` and then `Run anyway`
- A better explanation of code-signing issues and false-postive warnings can be found [here](https://stackoverflow.com/a/45316660)

### Testing GIF
![GIF](assets/test.gif)

### Alternative Install

- Ensure you have `python` installed, the recommended version is `Python 3.12.1`
  - Once installed, you can check your python version via `python --version`
- Install the repository via `git clone https://github.com/scarletti-ben/shiphead`
- Change directory into the repository via `cd .\shiphead\` 
- Set up a virtual environment [**Optional**]
  -  Initialise the virtual environment via `python -m venv venv`
  -  Activate the virtual environment via `.\venv\Scripts\activate`
- Install required packages via `pip install -r requirements.txt`
- Run the python script via `python main.py`

# Game Rules
### **(Section is a Work in Progress)**
Ignoring most of the "why" of each rule, a simple reference of what can be played on what is below

### What Can be Played on a...
- 2 => 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
- 3 => 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
- 4 => 2, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
- 5 => 2, 5, 6, 7, 8, 9, 10, J, Q, K, A
- 6 => 2, 6, 7, 8, 9, 10, J, Q, K, A
- 7 => Look at the number on the pile before the 7
- 8 (Active) => 8
- 8 (Inactive) => 2, 7, 8, 9, 10, J, Q, K, A
- 9 (Active) => 2, 3, 4, 5, 6, 7, 8, 9
- 9 (Inactive) => 2, 7, 9, 10, J, Q, K, A
- 10 => Clears the pile, it will never be face up on the pile
- J => 2, 7, 10, J, Q, K, A
- Q => 2, 7, 10, Q, K, A
- K => 2, 7, 10, K, A
- A => 2, 7, 10, A

### What Can it Play on (ignoring 7 and 10)?
- 2 => 2, 3, 4, 5, 6, (8), 9, J, Q, K, A
- 3 => 2, 3, 9
- 4 => 2, 3, 4, 9
- 5 => 2, 3, 4, 5, 9
- 6 => 2, 3, 4, 5, 6, 9
- 7 => 2, 3, 4, 5, 6, (8), 9, J, Q, K, A
- 8 => 2, 3, 4, 5, 6, 8, 9
- 9 => 2, 3, 4, 5, 6, (8), 9
- 10 => 2, 3, 4, 5, 6, (8), J, Q, K, A
- J => 2, 3, 4, 5, 6, (8), J
- Q => 2, 3, 4, 5, 6, (8), J, Q
- K => 2, 3, 4, 5, 6, (8), J, Q, K
- A => 2, 3, 4, 5, 6, (8), J, Q, K, A

The rule "8 or wait" means that if an 8 is on the pile you can either play an 8 or you must wait, if you wait then you skip your turn, but do not pick up the pile, and the player that played the 8 plays again, but now the 8 is disabled, effectively the waiting has disabled the 8's power

The rule "9 or lower" means that if a 9 is on the pile you must play a card that is lower than it, and once you do, play returns to normal, this also means that if you play a 7 on a 9, the next card will not have to play lower than a 9, effectively the 7 has disabled the 9's power

2s essentially reset the table and play on most
7s are invisible and keep the value of the card beneath then, and play on most
8s start "8 or wait" which is described above
9s start "9 or lower" and are described above
10s clear the table and play on mose

Suits do not matter

Four of a kind burns the deck

# Game Controls
### **(Section is a Work in Progress)**
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
- The AI is not especially adept and will make sub-par decisions

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
