
# < ======================================================================================================
# < Imports
# < ======================================================================================================

import pygame
import os
import sys
import random
import ctypes
import string

# < ======================================================================================================
# < Initialisation
# < ======================================================================================================

pygame.init()
ctypes.windll.user32.SetProcessDPIAware()
# pygame.display.set_icon(pygame.Surface([32,32], pygame.SRCALPHA))
pygame.display.set_caption('shiphead')

# < ======================================================================================================
# < Constants and Variables
# < ======================================================================================================

__DIR__ = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__))) + "\\"
# ASSETS: str = __DIR__ # * ENABLE IF FREEZING TO MAIN.EXE
ASSETS: str = __DIR__ + "assets\\" # * ENABLE IF RUNNING MAIN.PY
pygame.display.set_icon(pygame.image.load(ASSETS + "shiphead.png"))
PLAYING_CARDS: str = ASSETS + ""
FONTS: str = ASSETS + ""
W: int = 1920
H: int = 1080
FPS: int = 60
CENTER = CX, CY = W // 2, H // 2
GREY = [63,63,63]
tile_w = 53
tile_h = 70
scale = 3
TW, TH = tile_w * scale, tile_h * scale
font_name = FONTS + "monogram.ttf"
CHARACTERS = set(string.ascii_letters + string.digits + string.punctuation)
suits = 'hearts', 'spades', 'diamonds', 'clubs'
ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
table_values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
sort_values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
start_values = [30, 20, 0, 1, 2, 3, 25, 15, 10, 50, 4, 5, 6]
symbols = {
    "spades": "♠️",
    "hearts": "♥",
    "clubs": "♣",
    "diamonds": "♦"}
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (100, 80, 90)
CRIMSON = (220, 20, 60)
DARK_CRIMSON = (110, 10, 30)
DARK_GREY = (63, 63, 63)
DARK_GREEN = (0, 100, 0)
MED_GREEN = (0,170,0)
BRIGHT_GREEN = (0, 200, 0)

# < ======================================================================================================
# < Pygame Objects
# < ======================================================================================================

# ~ Objects
clock = pygame.time.Clock()
display = pygame.display.set_mode([W,H], pygame.FULLSCREEN)
user_event = pygame.USEREVENT + 1
font = pygame.font.Font(font_name, 28)
font_small = pygame.font.Font(font_name, 18)

# < ======================================================================================================
# < Settings Menu Loop
# < ======================================================================================================

def settings_loop():
    """Loop for user to change settings before the game starts"""

    class Button:
        def __init__(self, x, y, width, height, name):
            self.rect = pygame.Rect(x, y, width, height)
            self.rect.center = x, y
            self.enabled = False
            self.name = name
            self.font = font  # choose a font and size

        def draw(self, surface):
            paste = lambda *args: pygame.draw.rect(surface, *args)
            cx = self.rect.centerx
            x = self.rect.x
            y = self.rect.y
            w = self.rect.width // 2
            h = self.rect.height

            if self.name == 'Confirm':
                paste(MED_GREEN, (cx, y, w, h))
                paste(MED_GREEN, (x, y, w, h))
            elif self.enabled:
                paste(BRIGHT_GREEN, (cx, y, w, h))
                paste(DARK_GREEN, (x, y, w, h))
            else:
                paste(CRIMSON, (x, y, w, h))
                paste(DARK_CRIMSON, (cx, y, w, h))

            text_surf = self.font.render(self.name, True, WHITE)
            back_surf = pygame.Surface([w * 2, h // 1]).convert_alpha()
            back_surf.fill([130,130,130,130])
            back_rect = back_surf.get_rect()
            text_rect = text_surf.get_rect(center = back_rect.center).move(0,-1)
            back_surf.blit(text_surf, text_rect)
            back_rect.midbottom = self.rect.midtop
            surface.blit(back_surf, back_rect)

        def toggle(self):
            self.enabled = not self.enabled
        
    class CounterButton(Button):
        def __init__(self, x, y, width, height, name, min_val=0, max_val=10, value=0):
            super().__init__(x, y, width, height, name)
            self.min_val = min_val
            self.max_val = max_val
            self.value = value

        def draw(self, surface):

            paste = lambda *args: pygame.draw.rect(surface, *args)
            cx = self.rect.centerx
            x = self.rect.x
            y = self.rect.y
            w = self.rect.width // 2
            h = self.rect.height
            right = self.rect.right
            paste(DARK_GREY, (cx, y, w, h))
            paste(DARK_GREY, (x, y, w, h))

            arrow_height = h // 2
            arrow_width = arrow_height // 2
            arrow_color = CRIMSON
            arrow_x = x + 1.5 * arrow_width
            arrow_y = y + h // 2
            arrow_points = [(arrow_x, arrow_y), (arrow_x + arrow_width, arrow_y - arrow_height // 2), 
                            (arrow_x + arrow_width, arrow_y + arrow_height // 2)]
            pygame.draw.polygon(surface, arrow_color, arrow_points)


            arrow_height = h // 2
            arrow_width = arrow_height // 2
            arrow_color = MED_GREEN
            arrow_x = right - 2.5 * arrow_width
            arrow_y = y + h // 2
            arrow_points = [(arrow_x, arrow_y - arrow_height // 2), (arrow_x + arrow_width, arrow_y), 
                            (arrow_x, arrow_y + arrow_height // 2)]
            pygame.draw.polygon(surface, arrow_color, arrow_points)

            text = f"{self.name}: {self.value}"
            text_surf = self.font.render(text, True, WHITE)
            back_surf = pygame.Surface([w * 2, h // 1]).convert_alpha()
            back_surf.fill([130,130,130,130])
            back_rect = back_surf.get_rect()
            text_rect = text_surf.get_rect(center = back_rect.center).move(0,-1)
            back_surf.blit(text_surf, text_rect)
            back_rect.midbottom = self.rect.midtop
            surface.blit(back_surf, back_rect)

        def toggle(self):
            cx = self.rect.centerx
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    if mouse_pos[0] < cx:
                        self.decrease_value()
                    elif mouse_pos[0] > cx:
                        self.increase_value()
    
        def increase_value(self):
            self.value += 1
            if self.value > self.max_val:
                self.value = self.max_val

        def decrease_value(self):
            if self.value > self.min_val:
                self.value -= 1

    button_width = 190
    button_height = 40
    button_x = W // 2
    button_dict = {
        'Clear Deck': 'toggle',
        'Pick Cards': 'toggle',
        'Shuffle': 'toggle',
        'Hand Size': 'counter',
        'Table Cards': 'counter',
        'Hide AI': 'toggle',
        'Confirm': 'toggle'}
    button_spacing = H / (len(button_dict) + 1)
    buttons = []
    for i, (k, v) in enumerate(button_dict.items()):
        button_y = (i + 1) * button_spacing
        if v == 'toggle':
            button = Button(button_x, button_y, button_width, button_height, k)
        else:
            button = CounterButton(button_x, button_y, button_width, button_height, k)
        buttons.append(button)

    buttons[0].enabled = True
    buttons[1].enabled = False
    buttons[2].enabled = True
    buttons[3].value = 5
    buttons[4].value = 3
    buttons[5].enabled = True
    buttons[6].enabled = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        button.toggle()

        display.fill(GREY)
        for button in buttons:
            button.draw(display)

        if buttons[6].enabled == True:
            global changing_settings, ENDGAME, PICK_STARTING_CARDS, SHUFFLE, HAND_CARDS, DOWN_CARDS, HIDE_AI
            changing_settings = False
            ENDGAME = buttons[0].enabled
            PICK_STARTING_CARDS = buttons[1].enabled
            SHUFFLE = buttons[2].enabled
            HAND_CARDS = buttons[3].value
            DOWN_CARDS = buttons[4].value
            HIDE_AI = buttons[5].enabled
            return

        pygame.display.flip()
        clock.tick(FPS)

# < ======================================================================================================
# < Card Class
# < ======================================================================================================

class Card:

    def __init__(self, images, suit, rank, symbols, ranks, sort_values, start_values):
        """Create a card with suit, rank and appropriate image"""
        self.suit = suit
        self.rank = rank
        self.symbol = symbols[suit]
        rank_index = ranks.index(rank)
        self.sort_value = sort_values[rank_index]
        self.start_value = start_values[rank_index]
        self.image = images[f'{suit}_{rank}']
        self.back = images['card_back']
        self.rectangle = self.image.get_rect()
        self.style = 3

    @property
    def surface(self):
        """Access internal image"""
        return self.image
    
    def center(self, x = None, y = None):
        """Alter the center position of the card rectangle"""
        x = self.rectangle.centerx if x is None else x
        y = self.rectangle.centery if y is None else y
        self.rectangle.center = x, y

    def under(self, position):
        """Check if card rectangle is under a given point"""
        return self.rectangle.collidepoint(position)

    def __repr__(self) -> str:
        """Get the print name of a card"""
        if self.style == 0:
            return f'{self.rank} of {self.suit}'
        elif self.style == 1:
            return f'{str(self.rank).upper()}{Card.suits[self.suit]}'
        elif self.style == 2:
            return f'{str(self.rank)[0].upper()} of {self.suit}'
        elif self.style == 3:
            if str(self.rank).isdigit():
                rank = str(self.rank)
            else:
                rank = self.rank[0].upper()
            return f'{rank}{self.symbol}'
        elif self.style == 4:
            return f'{str(self.rank).title()}'
    
    def draw_transparent(self, display, alpha = 100):
        """Draw a transparent surface at current rectangle position"""
        surface = self.surface.copy()
        surface.set_alpha(alpha)
        display.blit(surface, self.rectangle)

    def draw_offset(self, display, dx = 0, dy = 0):
        """Draw surface with an x and or y offset"""
        rectangle = self.rectangle.copy()
        rectangle.y += dy
        rectangle.x += dx
        display.blit(self.surface, rectangle)

    def draw_highlighted(self, display, colour = [0,100,255]):
        """Draw a surface with colour overlay at current rectangle position"""
        surface = self.surface.copy()
        surface.fill(colour, special_flags = pygame.BLEND_RGB_MAX)
        display.blit(surface, self.rectangle)

    def draw_lowlighted(self, display, colour = [0,250,0]):
        """Draw a surface with colour overlay at current rectangle position"""
        surface = self.surface.copy()
        surface.fill(colour, special_flags = pygame.BLEND_RGB_MIN)
        display.blit(surface, self.rectangle)

    def draw_dimmed(self, display, percentage = 80):
        """Draw a surface with colour overlay at current rectangle position"""
        dimmed = int(255 * (percentage / 100))
        colour = [dimmed, dimmed, dimmed]
        surface = self.surface.copy()
        surface.fill(colour, special_flags = pygame.BLEND_RGB_MIN)
        display.blit(surface, self.rectangle)

    def draw_special(self, display, colour, blending):
        """Draw a surface with colour overlay at current rectangle position"""
        surface = self.surface.copy()
        surface.fill(colour, special_flags = getattr(pygame, blending))
        display.blit(surface, self.rectangle)

    def draw_special(self, display, colour, blending, decimal = 1):
        """Draw a surface with colour overlay at current rectangle position"""
        decimal = min(decimal + 0.01, 1)
        surface = self.surface.copy()
        rectangle = surface.get_rect()
        height = rectangle.height * decimal
        subsurface_rect = pygame.Rect(0, 0, rectangle.width, height)
        subsurface = surface.subsurface(subsurface_rect).copy()
        subsurface.fill(colour, special_flags = getattr(pygame, blending))
        surface.blit(subsurface, [0,0])
        display.blit(surface, self.rectangle)

    def draw_highlighted_back(self, display, colour = [255,100,0]):
        """Draw a surface with colour overlay at current rectangle position"""
        surface = self.back.copy()
        surface.fill(colour, special_flags = pygame.BLEND_RGB_MAX)
        display.blit(surface, self.rectangle)

    def draw_back(self, display):
        """Draw card reverse / back surface at current rectangle position"""
        surface = self.back
        display.blit(surface, self.rectangle)

    def draw(self, display):
        """Draw a card surface at current rectangle position"""
        display.blit(self.surface, self.rectangle)

# < ======================================================================================================
# < Timer Class
# < ======================================================================================================

class Timer:

    def __init__(self, seconds, fps = FPS):
        """Create a timer with an end time in seconds"""
        self.seconds = seconds
        self.end = fps * seconds
        self.counter = 0

    @property
    def decimal(self):
        """Return the ratio of current counter time and end"""
        return min(self.counter / self.end, 1)

    @property
    def complete(self):
        """Dynamic property to return True if timer complete"""
        return self.counter >= self.end

    @property
    def ended(self):
        """Dynamic property to return True if timer ended"""
        return self.counter >= self.end

    @property
    def finished(self):
        """Dynamic property to return True if timer finished"""
        return self.counter >= self.end

    def count(self, value = 1):
        """Increase the counter by a given value each frame"""
        self.counter += value

    def reset(self):
        """Set the counter to 0"""
        self.counter = 0

# < ======================================================================================================
# < Pile Class and Subclasses
# < ======================================================================================================

class Pile:

    def __init__(self, **kwargs):
        """Create a pile of cards"""
        self.cards = kwargs.get('cards', [])
        self.cx = kwargs.get('cx', display.get_rect().centerx)
        self.cy = kwargs.get('cy', display.get_rect().centery)
        self.spacing = kwargs.get('spacing', 1)
        self.reverse = kwargs.get('reverse', False)
        self.sliced = kwargs.get('sliced', False)
        self.vertical = kwargs.get('vertical', False)
        self.fixed = kwargs.get('fixed', False)
        self.hidden = kwargs.get('hidden', False)

    @property
    def base_rectangle(self):
        """Get a rectangle of the same size and scale as a single card"""
        rectangle = pygame.Rect(0, 0, tile_w * scale, tile_h * scale)
        rectangle.center = self.cx, self.cy
        return rectangle
    
    @property
    def bounding_rectangle(self):
        """Get bounding rectangle containing the area of all rectangles"""
        rectangles = [getattr(item, 'rectangle', item) for item in self.cards]
        rectangles = [rect for rect in rectangles if rect is not None]
        x_min = min(rectangle.left for rectangle in rectangles)
        y_min = min(rectangle.top for rectangle in rectangles)
        x_max = max(rectangle.right for rectangle in rectangles)
        y_max = max(rectangle.bottom for rectangle in rectangles)
        return pygame.Rect(x_min, y_min, x_max - x_min, y_max - y_min)
    
    def __len__(self):
        """Get the length of the internal set of cards"""
        return len(self.cards)
    
    @property
    def rectangle(self):
        """Property to return the appropriate rectangle for the pile"""
        if not any(self.cards):
            return self.base_rectangle
        else:
            return self.bounding_rectangle
        
    def clear(self):
        """Clear the internal set of cards"""
        self.cards.clear()

    def append(self, card):
        """Add card to internal set of cards"""
        self.cards.append(card)

    def align_vertical(self, spacing = 4):
        """Align all cards in the current pile"""
        x, y = self.cx, self.cy
        for card in self.draw_list:
            if card is not None:
                card.center(x, y)
                y -= spacing

    def remove_or_replace(self, card):
        """Remove card or replace with None"""
        if self.fixed:
            index = self.cards.index(card)
            self.cards[index] = None
        else:
            self.cards.remove(card)

    def align_horizontal(self):
        """Align cards along a horizontal, with spacing"""
        cards = self.draw_list
        spacing = self.spacing
        cx = display.get_rect().centerx if self.cx is None else self.cx
        total_cards = len(cards)
        center_index = int((total_cards + 1) / 2 - 1)
        odd = False if total_cards % 2 == 0 else True
        for index, card in enumerate(cards):
            if card is not None:
                w = card.rectangle.width
                offset = 0 if odd else w // 2
                delta_i = index - center_index
                cx = self.cx + (delta_i * w * spacing) - (offset * spacing)
                card.rectangle.center = cx, self.cy

    def sort(self):
        """Sort all cards in the pile by sort value"""
        sort_key = lambda card: card.sort_value
        self.cards.sort(key = sort_key, reverse = self.reverse)

    @property
    def draw_list(self):
        """Dynamic property to get relevant cards to draw to display"""
        reserved = PENDING + [HELD]
        output = [card for card in self.cards if card not in reserved]
        if self.reverse:
            output.reverse()
        return output
    
    def highlighted(self, mouse):
        """Return first card that collides with mouse, iterating in reverse"""
        cards = list(reversed(
            [card for card in self.cards if card is not None]))
        if self.reverse:
            cards.reverse()
        for card in cards:
            if card.under(mouse):
                return card

    def draw_rectangle(self, display, colour = [0,255,0], width = 2):
        """Draw current rectangle to display"""
        pygame.draw.rect(display, colour, self.rectangle, width)

    def update(self):
        """Update alignment each frame"""
        self.align_vertical() if self.vertical else self.align_horizontal()

    def __repr__(self):
        """Get printout for the current pile"""
        return f'{[card for card in self.cards]}'

class Hand(Pile):

    @property
    def draw_list(self):
        """Dynamic property to get relevant cards to draw to display"""
        reserved = PENDING + [HELD]
        output = [card for card in self.cards if card not in reserved]
        if self.reverse:
            output.reverse()
        return output
    
class Blind(Pile):

    @property
    def draw_list(self):
        """Dynamic property to get relevant cards to draw to display"""
        reserved = PENDING + [HELD]
        output = [card if card not in reserved else None for card in self.cards]
        if self.reverse:
            output.reverse()
        return output
    
class Shown(Pile):

    @property
    def draw_list(self):
        """Dynamic property to get relevant cards to draw to display"""
        reserved = PENDING + [HELD]
        output = [card if card not in reserved else None for card in self.cards]
        if self.reverse:
            output.reverse()
        return output

# < ======================================================================================================
# < Player Class and Subclasses
# < ======================================================================================================

class Player:
    def pile(self):
        """Return the appropriate active list of cards"""
        if any(self.hand.cards):
            return self.hand
        elif any(self.shown.cards):
            return self.shown
        elif any(self.blind.cards):
            return self.blind
        
    def __repr__(self) -> str:
        """Useful debugging function to print card lists"""
        return f"""
-----------------------------------------------------------
Player {self.number}
Hand:      {len(self.hand)} cards: {self.hand}
Shown:     {len(self.shown)} cards: {self.shown} 
Blind:     {len(self.blind)} cards: {self.blind} 
-----------------------------------------------------------
"""

class PlayerOne(Player):
    def __init__(self):
        """Create a player object with 3 distinct piles of cards"""
        self.hand = Hand(cy = H, spacing = 0.5)
        self.shown = Shown(cy = 3 * H // 4, spacing = 1.05, fixed = True)
        self.blind = Blind(
            cy = 3 * H // 4 + 8, spacing = 1.05, hidden = True, fixed = True)
        self.number = 1

class PlayerTwo(Player):
    def __init__(self):
        """Create a player object with 3 distinct piles of cards"""
        self.hand = Hand(cy = 0, spacing = 0.5, reverse = True)
        self.shown = Shown(
            cy = H // 4, spacing = 1.05, fixed = True)
        self.blind = Blind(
            cy = H // 4 - 8, spacing = 1.05, hidden = True, fixed = True)
        self.number = 2

# < ======================================================================================================
# < Functions
# < ======================================================================================================

def image_dictionary(tile_w, tile_h, scale, suits, ranks, flip = False):
    """Split tilesheet into image dictionary with 'suit_rank' as keys"""
    if flip:
        filepath = PLAYING_CARDS + "card_sheet_53x70_readable.png"
    else:
        filepath = PLAYING_CARDS + "card_sheet_53x70_flipped.png"
    sheet = pygame.image.load(filepath).convert_alpha()
    columns = int(sheet.get_width() / tile_w)
    rows = int(sheet.get_height() / tile_h)
    image_list = []
    for y in range(rows):
        for x in range(columns):
            left = x * tile_w
            top = y * tile_h
            rectangle = [left, top, tile_w, tile_h]
            subsurface = sheet.subsurface(rectangle)
            if scale != 1:
                dimensions = tile_w * scale, tile_h * scale
                subsurface = pygame.transform.scale(subsurface, dimensions)
            image_list.append(subsurface)  
    image_index = 0
    image_dictionary = {}
    for suit in suits:
        for rank in ranks:
            key = f'{suit}_{rank}'
            image_dictionary[key] = image_list[image_index]
            image_index += 1
    back_path = PLAYING_CARDS + "card_sheet_53x70_back_alt.png"
    card_back = pygame.image.load(back_path).convert_alpha()
    if scale != 1:
        dimensions = tile_w * scale, tile_h * scale
        card_back = pygame.transform.scale(card_back, dimensions)
    image_dictionary['card_back'] = card_back
    return image_dictionary

def get_valid_ranks(rank, active):
    """Get list of the valid ranks that can play on a card rank"""
    if rank == None:
        valid = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 2:
        valid = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 3:
        valid = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 4:
        valid = [2, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 5:
        valid = [2, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 6:
        valid = [2, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 7:
        valid = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 8:
        if active:
            valid = [8]
        else:
            valid = [2, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 9:
        if active:
            valid = [2, 3, 4, 5, 6, 7, 8, 9] # Postit - OPTIONAL 10 DOES NOT PLAY ON A 9
        else:
            valid = [2, 7, 9, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 10:
        valid = [2, 7, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 'jack':
        valid = [2, 7, 10, 'jack', 'queen', 'king', 'ace']
    elif rank == 'queen':
        valid = [2, 7, 10, 'queen', 'king', 'ace']
    elif rank == 'king':
        valid = [2, 7, 10, 'king', 'ace']
    elif rank == 'ace':
        valid = [2, 7, 10, 'ace']
    return valid

def check_four_in_a_row(cards):
    """Check if four cards in a row are same row, discard 7s if needed"""
    
    def four_in_a_row(cards):
        """Check if all cards in a set are the same rank"""
        result = False
        if len(cards) >= 4:
            top_four = cards[-4:]
            result = len(set(card.rank for card in top_four)) == 1
        return result
    
    result = False
    if four_in_a_row(cards):
        result = True
    else:
        cards = [card for card in cards if card.rank != 7]
        result = four_in_a_row(cards)
    return result

def check_for_rank(cards, rank):
    """Check if there is a specific rank at the top of the pile"""
    if cards:
        top_card = cards[-1]
        if top_card.rank == rank:
            return True
        
def check_for_rank_any(cards, rank, pending = None):
    """Check if any of a rank exist in a given set of cards"""
    cards = [card for card in cards if card is not None]
    if pending:
        cards = [card for card in cards if card not in pending]
    return any(card.rank == rank for card in cards)

def check_burned(cards):
    """Check for a 10 or a four in a row"""
    if check_for_rank(cards, 10):
        print('10 burns the deck, take another turn')
        return True
    else:
        if check_four_in_a_row(cards):
            print('Four in a row burns the deck, take another turn')
            return True

def populate(pile):
    """Fill a pile with 4 suits of 13 cards each with images"""
    for suit in suits:
        for rank in ranks:
            card = Card(images, suit, rank, symbols, ranks, sort_values, start_values)
            pile.append(card)

def deal(players, in_hand = 5, face_down = 3):
    """Deal cards evenly to players, alternating each card"""
    for _ in range(face_down):
        for player in players:
            card = DECK.pop()
            player.blind.append(card)
        for player in players:
            card = DECK.pop()
            player.shown.append(card)
    for _ in range(in_hand):
        for player in players:
            card = DECK.pop()
            player.hand.append(card)

def shuffle(iterable):
    """Shuffle a given iterable"""
    random.shuffle(iterable)

def start(players, stacks):
    """Clear attributes, create a deck, shuffle and deal"""
    global HELD, HIGHLIGHTED, TABLE_ACTIVE
    HELD = None
    HIGHLIGHTED = None
    TABLE_ACTIVE = False
    for stack in stacks:
        stack.clear()
    populate(DECK)
    if SHUFFLE:
        shuffle(DECK)
    deal(players, HAND_CARDS, DOWN_CARDS)

def align_horizontal(cards, cx, cy, spacing):
    """Align all cards in pile horizontally"""
    total_cards = len(cards)
    center_index = int((total_cards + 1) / 2 - 1)
    odd = False if total_cards % 2 == 0 else True
    for index, card in enumerate(cards):
        if card is not None:
            w = card.rectangle.width
            offset = 0 if odd else w // 2
            delta_i = index - center_index
            centerx = cx + (delta_i * w * spacing) - (offset * spacing)
            card.rectangle.center = centerx, cy
            # card.draw(display)

def align_vertical(pile, cx, cy, spacing = 4):
    """Align all cards in the current pile vertically"""
    for card in pile:
        if card is not None:
            card.center(cx, cy)
            cy -= spacing

def draw_pile(cards, hidden = False, reverse = False):
    """Draw all cards in the pile"""
    cards = cards[:]
    if reverse:
        cards.reverse()

    if PENDING:
        valid_ranks = [PENDING_RANK]
    else:
        valid_ranks = VALID_RANKS

    for card in cards:
        if card is not None:
            if card is not HIGHLIGHTED:
                if not hidden:
                    if PILE_HOVERED and card.rank in valid_ranks and card in ACTIVE_PILE.cards:
                        card.draw_special(
                            display, (47, 216, 73, 120), 'BLEND_RGBA_MIN', decimal = 1)
                    else:
                        card.draw(display)
                else:
                    card.draw_back(display)
            else:
                if not hidden:
                    card.draw_highlighted(display)
                else:
                    card.draw_highlighted_back(display)

def unreserved(pile):
    """Remove reserved cards from list"""
    cards = [card for card in pile.cards if card not in RESERVED]
    return cards

def fixed_list(pile):
    """Remove reserved cards from list and replace with None"""
    cards = [card if card not in RESERVED else None for card in pile.cards]
    return cards

def get_table_rank():
    """Get the current rank of the pile, discarding all 7s if necessary"""
    cards = PILE[:]
    rank = None
    while cards:
        card = cards.pop()
        if card.rank != 7:
            rank = card.rank
            break
    return rank

def get_table_card():
    """Get the current card of the pile, discarding all 7s if necessary"""
    cards = PILE[:]
    output = None
    while cards:
        card = cards.pop()
        if card.rank != 7:
            output = card
            break
    return output

def get_pending_rank():
    """Get the current rank of pending cards"""
    rank = None
    if PENDING:
        rank = PENDING[0].rank
    return rank

def next_player():
    """Switch the active player"""
    global ACTIVE_PLAYER
    if ACTIVE_PLAYER is PLAYER_ONE:
        ACTIVE_PLAYER = PLAYER_TWO
    else:
        ACTIVE_PLAYER = PLAYER_ONE

def left_mouse_down(event):
    return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

def left_mouse_up(event):
    return event.type == pygame.MOUSEBUTTONUP and event.button == 1

def right_mouse_down(event):
    return event.type == pygame.MOUSEBUTTONDOWN and event.button == 3

def right_mouse_up(event):
    return event.type == pygame.MOUSEBUTTONUP and event.button == 3

def key_down(event):
    return event.type == pygame.KEYDOWN

def handle_quit(event):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()

def align_sort_blit():
    """Function to be called in the main loop to handle sorting / alignment and blitting cards"""

    global HIGHLIGHTED

    PLAYER_ONE.hand.sort()
    PLAYER_TWO.hand.sort()
    align_vertical(DECK, W // 8, CY)
    draw_pile(DECK, True)

    align_vertical(BURNED, 7 * W // 8, CY)
    draw_pile(BURNED)

    cards = PILE + PENDING
    align_horizontal(cards, CX, CY, 0.25)
    eight_or_wait = TABLE_ACTIVE and check_for_rank(PILE, 8)
    
    if eight_or_wait and not PENDING:
        for card in PILE:
            # card.draw_special(
            #     display, [22,4,146], 'BLENDMODE_ADD', timer.decimal)
            card.draw_special(
                display, [200,14,18], 'BLEND_SUB', timer.decimal)
    else:
        for card in PILE:
            if card is TABLE_CARD:
                card.draw_highlighted(display)
            else:
                card.draw(display)
    for card in PENDING:
        card.draw_special(display, [48,96,4], 'BLENDMODE_ADD', timer.decimal)

    cards = unreserved(PLAYER_ONE.hand)
    align_horizontal(cards, CX, H, 0.25)
    draw_pile(cards)

    cards = fixed_list(PLAYER_ONE.blind)
    align_horizontal(cards, CX, 3 * H // 4 + 6, 1.05)
    draw_pile(cards, True)

    cards = fixed_list(PLAYER_ONE.shown)
    align_horizontal(cards, CX, 3 * H // 4, 1.05)
    draw_pile(cards)

    cards = unreserved(PLAYER_TWO.hand)
    align_horizontal(cards, CX, 0, 0.25)
    draw_pile(cards, reverse = True, hidden = HIDE_AI)

    cards = fixed_list(PLAYER_TWO.blind)
    align_horizontal(cards, CX, H // 4 - 6, 1.05)
    draw_pile(cards, True)

    cards = fixed_list(PLAYER_TWO.shown)
    align_horizontal(cards, CX, H // 4, 1.05)
    draw_pile(cards)

    HIGHLIGHTED = None
    if not HELD:
        cards = [card for card in ACTIVE_PILE.cards if card not in PENDING]
        if ACTIVE_PLAYER is PLAYER_ONE:
            for card in list(reversed(cards)):
                if card is not None:
                    if card.rectangle.collidepoint(mouse):
                        HIGHLIGHTED = card
                        break
        elif ACTIVE_PLAYER is PLAYER_TWO:
            for card in cards:
                if card is not None:
                    if card.rectangle.collidepoint(mouse):
                        HIGHLIGHTED = card
                        break

def game_end(player = None):
    print('\n --- WIN ---')
    if player:
        print(f'{player} has no cards remaining, they have won the game.')
    else:
        print('Player has no cards remaining.')
    sys.exit()

def draw_held():
    if HELD:
        HELD.center(mx, my)
        if ACTIVE_PILE.hidden:
            HELD.draw_back(display)
        else:
            HELD.draw(display)

def end_timer():
    global HELD, HIGHLIGHTED, PILE, TABLE_ACTIVE, BURNED
    print('\n-- TIMER --')

    PILE += PENDING
    if ACTIVE_PILE.hidden and PENDING[0].rank not in VALID_RANKS:
        print('\n--- BLIND ---')
        print('Blind card not valid')
        index = ACTIVE_PILE.cards.index(PENDING[0])
        ACTIVE_PILE.cards[index] = None
        pickup(ACTIVE_PLAYER)
        PENDING.clear()
        HELD = None
        HIGHLIGHTED = None
        timer.reset()
        return

    for card in PENDING:
        if ACTIVE_PILE.fixed:
            index = ACTIVE_PILE.cards.index(card)
            ACTIVE_PILE.cards[index] = None
        else:
            ACTIVE_PILE.cards.remove(card)

    counter = 0
    while len(ACTIVE_PILE.cards) < 5:
        if not DECK:
            print('There are no more cards in the deck to draw')
            break
        else:
            card = DECK.pop()
            ACTIVE_PILE.cards.append(card)
            counter += 1
    if counter > 0:
        print(f'{counter} card(s) drawn from deck')

    PENDING.clear()
    HELD = None
    HIGHLIGHTED = None
    timer.reset()
    TABLE_ACTIVE = True

    if check_burned(PILE):
        number = len(PILE)
        BURNED += PILE
        PILE.clear()
        print(f'{number} card(s) burned, player takes another turn')
        TABLE_ACTIVE = False
        return
    elif check_for_rank(PILE, 7):
        if TABLE_ACTIVE:
            print('Seven on top of the pile, pile has been deactivated')
        TABLE_ACTIVE = False

    next_player()
    print('Turn ended due to timer, next player')

    if not any(PLAYER_ONE.hand.cards):
        if not any(PLAYER_ONE.shown.cards):
            if not any(PLAYER_ONE.blind.cards):
                game_end('Player One')
    if not any(PLAYER_TWO.hand.cards):
        if not any(PLAYER_TWO.shown.cards):
            if not any(PLAYER_TWO.blind.cards):
                game_end('Player Two')

def skip_turn():
    global HELD, HIGHLIGHTED, TABLE_ACTIVE
    print('\n-- SKIPPED --')
    PENDING.clear()
    HELD = None
    HIGHLIGHTED = None
    TABLE_ACTIVE = False
    timer.reset()
    next_player()
    print('Turn skipped due to 8 or wait, timer reset, table deactivated, next player')

def pickup(player):
    """Add all pile cards to player hand"""
    global HELD, PENDING, HIGHLIGHTED
    print('\n--- PICKUP ---')
    player.hand.cards.extend(PILE)
    HELD = None
    HIGHLIGHTED = None
    PENDING.clear()
    PILE.clear()
    timer.reset()
    next_player()
    print("Player picked up the pile, next player's turn")

def process_held():
    global TABLE_ACTIVE
    print('\n-- HELD --')
    rectangle = get_pile_rectangle()
    rectangle.center = CX, CY
    if HELD.rectangle.colliderect(rectangle):

        if ACTIVE_PILE.hidden:
            if len(PENDING) < 1:
                PENDING.append(HELD)
                print(f'Any hidden card is valid', end = ' ')
                print(f'{HELD} added to pending cards [{len(PENDING)}], pile activated')
                TABLE_ACTIVE = True
            else:
                print('You may only play one hidden card per turn', end = ' ')
                print('returned to blind cards')
        else:
            if any(PENDING):
                CARD = PENDING[0]
                if HELD.rank == PENDING_RANK:
                    PENDING.append(HELD)
                    print(
                        f'{HELD} is pending rank: {CARD}', end = ' ')
                    print(f'added to pending [{len(PENDING)}], pile activated')
                    TABLE_ACTIVE = True
                else:
                    print(f'{HELD} not pending rank: {CARD}')
                    print('returned to hand')
            elif HELD.rank in VALID_RANKS:
                PENDING.append(HELD)
                print(f'{HELD} beats {TABLE_CARD}', end = ' ')
                print(f'added to pending [{len(PENDING)}], pile activated')
                TABLE_ACTIVE = True
            else:
                print(f'{HELD} does not beat {TABLE_CARD}', end = ' ')
                print('returned to hand')
    else:
        print('Not over pile, returned to hand')

    print('Card play attempted or completed, timer reset')
    timer.reset()

def get_pile_rectangle():
    """Get bounding rectangle for of all rectangles in list"""
    if not PILE and not PENDING:
        rect = pygame.Rect(0, 0, tile_w * scale, tile_h * scale)
        rect.center = CX, CY
        return rect
    cards = PILE + PENDING
    rectangles = [getattr(card, 'rectangle') for card in cards]
    x_min = min(rectangle.left for rectangle in rectangles)
    y_min = min(rectangle.top for rectangle in rectangles)
    x_max = max(rectangle.right for rectangle in rectangles)
    y_max = max(rectangle.bottom for rectangle in rectangles)
    return pygame.Rect(x_min, y_min, x_max - x_min, y_max - y_min)

def draw_text(*sentences):
    x, y = 10, 10
    for sentence in sentences:
        surface = font.render(sentence, True, [0,255,0])
        rectangle = surface.get_rect(topleft = [x, y])
        y += rectangle.height
        display.blit(surface, rectangle)

def pick_cards():
    global HELD, HIGHLIGHTED, PICK_STARTING_CARDS
    
    display.fill(GREY)
    events = pygame.event.get()
    mouse = mx, my = pygame.mouse.get_pos()
    HIGHLIGHTED = None

    PLAYER_ONE.hand.sort()
    PLAYER_TWO.hand.sort()

    align_vertical(DECK, W // 8, CY)
    draw_pile(DECK, True)

    one_hand = [card for card in PLAYER_ONE.hand.cards if card is not HELD]
    align_horizontal(one_hand, CX, H, 0.25)

    two_hand = [card for card in PLAYER_TWO.hand.cards if card is not HELD]
    align_horizontal(two_hand, CX, 0, 0.25)

    align_horizontal(PLAYER_ONE.blind.cards, CX, 3 * H // 4 + 6, 1.05)

    align_horizontal(PLAYER_ONE.shown.cards, CX, 3 * H // 4, 1.05)

    align_horizontal(PLAYER_TWO.blind.cards, CX, H // 4 - 6, 1.05)

    align_horizontal(PLAYER_TWO.shown.cards, CX, H // 4, 1.05)

    if not HELD:
        cards = ACTIVE_PLAYER.hand.cards
        if ACTIVE_PLAYER is PLAYER_ONE:
            cards = list(reversed(cards))
        for card in cards:
            if card.rectangle.collidepoint(mouse):
                HIGHLIGHTED = card
                break
        OVERLAP = None
    else:
        HIGHLIGHTED = None
        HELD.center(mx, my)
        for card in ACTIVE_PLAYER.shown.cards:
            if HELD.rectangle.collidepoint(card.rectangle.center):
                OVERLAP = card
                break
        else:
            OVERLAP = None
    
    inactive_player = PLAYER_ONE if ACTIVE_PLAYER is PLAYER_TWO else PLAYER_TWO

    active_hand = [
        card for card in ACTIVE_PLAYER.hand.cards if card is not HELD]
    if ACTIVE_PLAYER is PLAYER_TWO:
        active_hand = list(reversed(active_hand))
    for card in active_hand:
        if card is HIGHLIGHTED:
            card.draw_highlighted(display)
        else:
            card.draw(display)
    for card in ACTIVE_PLAYER.blind.cards:
        card.draw_back(display)
    for card in ACTIVE_PLAYER.shown.cards:
        if card is OVERLAP:
            card.draw_highlighted(display)
        else:
            card.draw(display)

    cards = inactive_player.hand.cards[:]
    if inactive_player is PLAYER_TWO:
        cards = list(reversed(cards))
    for card in cards:
        if not HIDE_AI:
            card.draw(display)
        else:
            card.draw_back(display)
    for card in inactive_player.blind.cards:
        card.draw_back(display)
    for card in inactive_player.shown.cards:
        card.draw(display)

    if HELD:
        HELD.draw(display)

    for event in events:
        handle_quit(event)
        if left_mouse_down(event):
            if HIGHLIGHTED:
                HELD = HIGHLIGHTED
        elif left_mouse_up(event):
            if HELD:
                if OVERLAP:
                    ACTIVE_PLAYER.hand.cards.remove(HELD)
                    index = ACTIVE_PLAYER.shown.cards.index(OVERLAP)
                    ACTIVE_PLAYER.shown.cards[index] = HELD
                    ACTIVE_PLAYER.hand.cards.append(OVERLAP)
                    print('\n--- PICKING ---')
                    print(f"{HELD} placed in Player {ACTIVE_PLAYER.number}'s shown cards")

            HELD = None
            HIGHLIGHTED = None
        
        elif key_down(event) or right_mouse_up(event):
            print('\n--- PICKING ---')
            print(f"Player {ACTIVE_PLAYER.number} has confirmed their shown cards")

            def update_starting_cards(player, n = DOWN_CARDS):
                """Put the n cards of highest importance in shown cards"""
                cards = player.hand.cards + player.shown.cards
                cards.sort(key = lambda card: card.start_value)
                best_cards = cards[-n:]
                player.shown.cards = best_cards
                player.hand.cards = [
                    card for card in cards if card not in best_cards]
            update_starting_cards(PLAYER_TWO)
            PICK_STARTING_CARDS = False
            return
            
    draw_text(
        'Left Mouse Button to drag and replace cards.',
        f'Press any key to start the game.',
        f'Current Player: {ACTIVE_PLAYER.number}',
        f'Cards in deck: {len(DECK)}')

    pygame.display.flip()	
    clock.tick(FPS)

# < ======================================================================================================
# < Pre-Execution Setup
# < ======================================================================================================

images = image_dictionary(tile_w, tile_h, scale, suits, ranks)
timer = Timer(5)
DECK = []
PILE = []
BURNED = []
PENDING = []
HIGHLIGHTED = None
HELD = None
TABLE_ACTIVE = False
PLAYER_ONE = PlayerOne()
PLAYER_TWO = PlayerTwo()
PLAYERS = PLAYER_ONE, PLAYER_TWO
ACTIVE_PLAYER = PLAYER_ONE
STACKS = DECK, PILE, BURNED, PENDING, PLAYER_ONE.hand, PLAYER_ONE.blind, PLAYER_ONE.shown, PLAYER_TWO.hand, PLAYER_TWO.blind, PLAYER_TWO.shown
PILE_HOVERED = False

changing_settings = True
if changing_settings:
    settings_loop()
start(PLAYERS, STACKS)
if ENDGAME:
    DECK.clear()

# < ======================================================================================================
# < Main Loop Execution
# < ======================================================================================================

while True:

    TABLE_RANK = get_table_rank()
    VALID_RANKS = get_valid_ranks(TABLE_RANK, TABLE_ACTIVE)

    if PICK_STARTING_CARDS:
        pick_cards()
        continue

    display.fill(GREY)
    events = pygame.event.get()
    mouse = mx, my = pygame.mouse.get_pos()
    
    ACTIVE_PILE = ACTIVE_PLAYER.pile()
    RESERVED = [card for card in PENDING + [HELD] if card is not None]
    TABLE_CARD = get_table_card()
    TABLE_RECTANGLE = get_pile_rectangle()
    PENDING_RANK = get_pending_rank()
    PILE_HOVERED = TABLE_RECTANGLE.collidepoint(mouse) and not HELD

    draw_text(
        f'Valid Ranks: {VALID_RANKS}',
        f'Table Active: {TABLE_ACTIVE}',
        f'Table Current Rank: {TABLE_RANK}',
        f'Cards in deck: {len(DECK)}',
        f'Cards Burned: {len(BURNED)}',
        f'Card Pending: {len(PENDING)}',
        f'Cards in Pile: {len(PILE)}',
        f'Current Player: {ACTIVE_PLAYER.number}',
        f'Press Spacebar to pickup the cards in the center')

    align_sort_blit()
    draw_held()

    if ACTIVE_PLAYER is PLAYER_TWO and not PENDING:
        cards = [card for card in ACTIVE_PILE.cards if card is not None and card not in RESERVED]
        valid = lambda card: card.rank in VALID_RANKS
        no_valid = not any(valid(card) for card in cards)
        if not PENDING:
            valid_cards = [card for card in cards if valid(card)]
        else:
            valid_cards = [card for card in cards if card.rank == PENDING[0].rank]

        eight_or_wait = TABLE_ACTIVE and check_for_rank(PILE, 8)
        if ACTIVE_PILE.hidden:
            print('--- AI ---')
            print('AI has chosen a blind card at random')
            card = random.choice(cards)
            PENDING.append(card)
        elif no_valid:
            if not eight_or_wait:
                print('--- AI ---')
                print('AI has no valid cards and must pick up')
                pickup(PLAYER_TWO)
            else:
                print('--- AI ---')
                print('AI has no 8 and chooses to wait')
                skip_turn()
        else:
            if timer.counter == 0:
                print('--- AI ---')
                print('AI has chosen a valid card at random')
                card = random.choice(valid_cards)
                PENDING.append(card)

    for event in events:
        handle_quit(event)
        if left_mouse_down(event):
            if HIGHLIGHTED:
                HELD = HIGHLIGHTED
        elif left_mouse_up(event):
            if HELD:
                process_held()
            HELD = None
            HIGHLIGHTED = None
        
        if right_mouse_up(event):
            if PILE:
                if not PENDING:
                    pickup(ACTIVE_PLAYER)
                else:
                    print('\n --- ERROR ---')
                    print('You cannot pickup with valid pending cards')
            else:
                print('\n --- ERROR ---')
                print('There are no cards to pick up')
        
        if key_down(event):
            if event.key == pygame.K_EQUALS:
                PLAYER_ONE.blind.cards.append(None)
                PLAYER_ONE.shown.cards.append(
                    Card(images, 'spades', 6, symbols, ranks, sort_values, start_values))
            if event.key == pygame.K_7:
                print('--- ACTIVE ---')
                print(f'Table Active: {TABLE_ACTIVE}')
            if event.key == pygame.K_r:
                start(PLAYERS, STACKS)
                DECK.clear()
            elif event.key == pygame.K_SPACE:
                if PILE:
                    if not PENDING:
                        pickup(ACTIVE_PLAYER)
                    else:
                        print('\n --- ERROR ---')
                        print('You cannot pickup with valid pending cards')
                else:
                    print('\n --- ERROR ---')
                    print('There are no cards to pick up')
            elif event.key == pygame.K_BACKSPACE:
                if PENDING:
                    PENDING.clear()
                    HELD = None
                    HIGHLIGHTED = None
                    print('\n --- CANCEL ---')
                    print('Pending cards cleared')
                else:
                    print('\n --- ERROR ---')
                    print('There are no pending cards to cancel')
    
    eight_or_wait = TABLE_ACTIVE and check_for_rank(PILE, 8)
    
    if PENDING or eight_or_wait:
        if eight_or_wait and not PENDING:
            if check_for_rank_any(ACTIVE_PILE.cards, 8) and not ACTIVE_PILE.hidden and ACTIVE_PLAYER is not PLAYER_TWO:
                timer.count(0.5)
            else:
                timer.count(4)
        else:
            if check_for_rank_any(ACTIVE_PILE.cards, PENDING_RANK, PENDING) and not ACTIVE_PILE.hidden and ACTIVE_PLAYER is not PLAYER_TWO:
                timer.count(1)
            else:
                timer.count(4)
    else: 
        timer.reset()
    if timer.complete:               
        if eight_or_wait and not PENDING:
            skip_turn()
        else:
            end_timer()

    pygame.display.flip()	
    clock.tick(FPS)