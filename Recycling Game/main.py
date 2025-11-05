import pgzrun
import random


WIDTH = 500
HEIGHT = 400
CENTRE_x = WIDTH//2
CENTRE_y = HEIGHT//2    
CENTRE   = (CENTRE_x,CENTRE_y)
FINAL_LEVEL = 6
START_SPEED = 7
game_over = False 
game_complete = False
current_level = 1
items = []
animations = []
ITEMS = ["battery", "bottle","chips","plasticbag"]

def draw():
    global game_over,game_complete,current_level,items
    screen.clear()
    screen.blit("recycle_bg",(0,0))
    if game_over:
        display_message("game over", "Try again")
    elif game_complete:
        display_message("You won","Well done")
    else:
        for item in items:
            item.draw()
   

def update():
    global items
    if len(items)==0:
        items = make_items(current_level)
    

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items       = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["paperbag"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
    
def create_items(items_to_create):
    pass

def layout_items(items_to_layout):
    pass

def animate_items(items_to_animate):
    pass

def handle_game_over():
    pass

def on_mouse_down(pos):
    pass

def handle_game_complete():
    pass

def stop_animations(animations_to_stop):
    pass

def display_message(heading_Text_sub_heading_text):
    pass

pgzrun.go()