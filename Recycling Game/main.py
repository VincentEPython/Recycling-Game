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
    actors_to_create = get_option_to_create(number_of_extra_items)
    new_actors       = create_actors(actors_to_create)
    layout_actors(new_actors)
    animate_actors(new_actors)
    return new_actors

def get_option_to_create(number_of_extra_actors):
    items_to_create = ["paperbag"]
    for i in range(0,number_of_extra_actors):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
    
def create_actors(items_to_create):
    new_actors = []
    for actor_img in items_to_create:
        actor = Actor(actor_img)
        new_actors.append(actor)

    return new_actors
 
    
def layout_actors(items_to_layout):
    num_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH/num_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos = (index + 1 )* gap_size
        item.x = new_x_pos

def animate_actors(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ("center","bottom")
        animation = animate(item, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)
def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global current_level
    global items

    for item in items:
        if item.collidepoint(pos):
            if "paperbag" in item.image:
                handle_game_complete()
            else:
                handle_game_over()


        

def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True

    else:
        current_level+=1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations:
        if animation.running:
            animation.stop()

def display_message(heading_Text,sub_heading_text):
    screen.draw.text(heading_Text,sub_heading_text,(0,0),color = "white", fontsize = 20)

pgzrun.go()
