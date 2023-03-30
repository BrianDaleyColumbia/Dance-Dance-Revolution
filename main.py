from sprites import *
import random


pg.init()
fps_clock = pg.time.Clock()
DISPLAYSURF = pg.display.set_mode((0, 0), pg.FULLSCREEN)

FPS = 60
ARROW_PADDING = 10
ARROW_DIM = 150
GHOST_YPADDING = 25
SCREEN_HEIGHT = DISPLAYSURF.get_height()
SCREEN_WIDTH = DISPLAYSURF.get_width()
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
COL1_POS = int(DISPLAYSURF.get_width() / 2) - 3 * int(ARROW_PADDING / 2) - 3 * int(ARROW_DIM / 2)
COL2_POS = int(DISPLAYSURF.get_width() / 2) - int(ARROW_PADDING / 2) - int(ARROW_DIM / 2)
COL3_POS = int(DISPLAYSURF.get_width() / 2) + int(ARROW_PADDING / 2) + int(ARROW_DIM / 2)
COL4_POS = int(DISPLAYSURF.get_width() / 2) + 3 * int(ARROW_PADDING / 2) + 3 * int(ARROW_DIM / 2)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

left_arrow_img = pg.image.load("assets/leftArrows/tile003.png")
down_arrow_img = pg.image.load("assets/downArrows/tile003.png")
up_arrow_img = pg.image.load("assets/upArrows/tile003.png")
right_arrow_img = pg.image.load("assets/rightArrows/tile003.png")
left_static_img = pg.image.load("assets/staticArrows/staticLeft.png")
down_static_img = pg.image.load("assets/staticArrows/staticDown.png")
up_static_img = pg.image.load("assets/staticArrows/staticUp.png")
right_static_img = pg.image.load("assets/staticArrows/staticRight.png")

font = pg.font.Font("serpentine.ttf", 50)
perfect_msg = font.render("Perfect!!", True, YELLOW)
perfect_rect = perfect_msg.get_rect()
perfect_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
great_msg = font.render("Great!", True, GREEN)
great_rect = great_msg.get_rect()
great_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
good_msg = font.render("Good", True, BLUE)
good_rect = good_msg.get_rect()
good_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
boo_msg = font.render("Boo", True, PURPLE)
boo_rect = boo_msg.get_rect()
boo_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
miss_msg = font.render("Miss...", True, RED)
miss_rect = miss_msg.get_rect()
miss_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

dynamic_sprites = pg.sprite.Group()
left_arrows, right_arrows, up_arrows, down_arrows = \
    pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group()
static_arrows = pg.sprite.Group()
static_arrows.add(StaticArrow(COL1_POS, GHOST_YPADDING, left_static_img, ARROW_DIM, LEFT))
static_arrows.add(StaticArrow(COL2_POS, GHOST_YPADDING, down_static_img, ARROW_DIM, DOWN))
static_arrows.add(StaticArrow(COL3_POS, GHOST_YPADDING, up_static_img, ARROW_DIM, UP))
static_arrows.add(StaticArrow(COL4_POS, GHOST_YPADDING, right_static_img, ARROW_DIM, RIGHT))

speed = 10/17



def draw_background():
    DISPLAYSURF.fill((0, 0, 0))
    for entity in static_arrows:
        DISPLAYSURF.blit(entity.image, entity.rect)


def make_note(dir):
    if dir == "left":
        arrow = DynamicArrow(COL1_POS, SCREEN_HEIGHT, left_arrow_img, ARROW_DIM, LEFT)
        dynamic_sprites.add(arrow)
        left_arrows.add(arrow)
    if dir == "down":
        arrow = DynamicArrow(COL2_POS, SCREEN_HEIGHT, down_arrow_img, ARROW_DIM, DOWN)
        dynamic_sprites.add(arrow)
        down_arrows.add(arrow)
    if dir == "up":
        arrow = DynamicArrow(COL3_POS, SCREEN_HEIGHT, up_arrow_img, ARROW_DIM, UP)
        dynamic_sprites.add(arrow)
        up_arrows.add(arrow)
    if dir == "right":
        arrow = DynamicArrow(COL4_POS, SCREEN_HEIGHT, right_arrow_img, ARROW_DIM, RIGHT)
        dynamic_sprites.add(arrow)
        right_arrows.add(arrow)


def get_hit(arrow, bound):
    pos = arrow.get_pos()
    if GHOST_YPADDING - bound*2 <= pos <= GHOST_YPADDING + bound*2:
        return "perfect"
    elif GHOST_YPADDING - bound*4 <= pos <= GHOST_YPADDING + bound*4:
        return "great"
    elif GHOST_YPADDING - bound*6 <= pos <= GHOST_YPADDING + bound*6:
        return "good"
    else:
        return "boo"


def display_feedback(feedback):
    if feedback == "perfect":
        DISPLAYSURF.blit(perfect_msg, perfect_rect)
    if feedback == "great":
        DISPLAYSURF.blit(great_msg, great_rect)
    if feedback == "good":
        DISPLAYSURF.blit(good_msg, good_rect)
    if feedback == "boo":
        DISPLAYSURF.blit(boo_msg, boo_rect)
    if feedback == "miss":
        DISPLAYSURF.blit(miss_msg, miss_rect)


def handle_hits(key):
    hit_val = ""
    if key == K_LEFT or key == K_a:
        collisions = pg.sprite.groupcollide(left_arrows, static_arrows, False, False)
        if collisions:
            hit_val = get_hit(list(collisions.keys())[0], dt * speed)
            list(collisions.keys())[0].kill()
    if key == K_DOWN or key == K_s:
        collisions = pg.sprite.groupcollide(down_arrows, static_arrows, False, False)
        if collisions:
            hit_val = get_hit(list(collisions.keys())[0], dt * speed)
            list(collisions.keys())[0].kill()
    if key == K_UP or key == K_w:
        collisions = pg.sprite.groupcollide(up_arrows, static_arrows, False, False)
        if collisions:
            hit_val = get_hit(list(collisions.keys())[0], dt * speed)
            list(collisions.keys())[0].kill()
    if key == K_RIGHT or key == K_d:
        collisions = pg.sprite.groupcollide(right_arrows, static_arrows, False, False)
        if collisions:
            hit_val = get_hit(list(collisions.keys())[0], dt * speed)
            list(collisions.keys())[0].kill()
    return hit_val

dt = 0
starting_tick = pg.time.get_ticks()
feedback_tick = -1000
last_note_tick = starting_tick
feedback = ""
while True:
    cur_tick = pg.time.get_ticks()
    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            keys = pg.key.get_pressed()
            feedback = handle_hits(event.key)
            if feedback:
                feedback_tick = cur_tick

    for entity in dynamic_sprites:
        entity.move(dt * speed)
        if entity.check_death():
            feedback = "miss"
            feedback_tick = cur_tick

    if 250 <= cur_tick - last_note_tick <= 250 + (1000 // FPS):
        last_note_tick = cur_tick
        make_note(random.choice(["left", "down", "up", "right"]))


    draw_background()
    for entity in dynamic_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    if cur_tick - feedback_tick <= 500:
        display_feedback(feedback)
    else:
        feedback = ""

    pg.display.update()
    dt = fps_clock.tick(FPS)
