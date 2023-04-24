from sprites import *
from pygame import mixer
import random
import cv2

pg.init()
mixer.init()
mixer.music.load("Stay.mp3")
mixer.music.set_volume(0.5)
fps_clock = pg.time.Clock()
video = cv2.VideoCapture("driving-slow.mp4")
DISPLAYSURF = pg.display.set_mode((0, 0), pg.FULLSCREEN)

BEAT_INDICES = [0, 4, 8, 12, 16, 20, 24, 26, 28, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 67, 72, 75, 80, 83, 88, 89, 90, 91, 92, 96,
                97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
                118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
                139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159,
                166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186,
                187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
                208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 224, 227, 232, 235, 240, 243, 248, 249,
                250, 251, 256, 260, 262, 264, 270, 272, 276, 278, 280, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295,
                296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316,
                317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337,
                338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352]

beat_indices = BEAT_INDICES.copy()

FPS = 60
MS_PER_FRAME = (1 / FPS) * 1000
BPM = 170.2
INTERVAL = (60000 / BPM)
NUM_NOTES = 353
LOW_INTERVAL = INTERVAL - (1000 / (FPS * 2))
# LOW_INTERVAL = (1000 / (FPS * 2))
SCORES = {"perfect": 999999, "great": 777777, "good": 555555, "boo": 0, "miss": -333333}
ARROW_PADDING = 10
ARROW_DIM = 150
GHOST_YPADDING = 25
SCREEN_HEIGHT = DISPLAYSURF.get_height()
SCREEN_WIDTH = DISPLAYSURF.get_width()
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
COL1_POS = int(SCREEN_WIDTH / 2) - 3 * int(ARROW_PADDING / 2) - 3 * int(ARROW_DIM / 2)
COL2_POS = int(SCREEN_WIDTH / 2) - int(ARROW_PADDING / 2) - int(ARROW_DIM / 2)
COL3_POS = int(SCREEN_WIDTH / 2) + int(ARROW_PADDING / 2) + int(ARROW_DIM / 2)
COL4_POS = int(SCREEN_WIDTH / 2) + 3 * int(ARROW_PADDING / 2) + 3 * int(ARROW_DIM / 2)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

left_imgs = []
for i in range(16):
    img = pg.image.load("assets/leftArrows/tile" + str(i).zfill(3) + ".png")
    img = pg.transform.scale(img, (ARROW_DIM, ARROW_DIM))
    left_imgs.append(img)
down_imgs = []
for i in range(16):
    img = pg.image.load("assets/downArrows/tile" + str(i).zfill(3) + ".png")
    img = pg.transform.scale(img, (ARROW_DIM, ARROW_DIM))
    down_imgs.append(img)
up_imgs = []
for i in range(16):
    img = pg.image.load("assets/upArrows/tile" + str(i).zfill(3) + ".png")
    img = pg.transform.scale(img, (ARROW_DIM, ARROW_DIM))
    up_imgs.append(img)
right_imgs = []
for i in range(16):
    img = pg.image.load("assets/rightArrows/tile" + str(i).zfill(3) + ".png")
    img = pg.transform.scale(img, (ARROW_DIM, ARROW_DIM))
    right_imgs.append(img)

# left_arrow_img = pg.image.load("assets/leftArrows/tile003.png")
# down_arrow_img = pg.image.load("assets/downArrows/tile003.png")
# up_arrow_img = pg.image.load("assets/upArrows/tile003.png")
# right_arrow_img = pg.image.load("assets/rightArrows/tile003.png")
left_static_imgs = [pg.transform.scale(pg.image.load("assets/staticArrows/staticLeft.png"), (ARROW_DIM, ARROW_DIM))]
left_static_imgs.append(
    pg.transform.scale(pg.transform.rotate(pg.image.load("OldNote/Down Tap Explosion Dim.png"), 270),
                       (ARROW_DIM, ARROW_DIM)))
down_static_imgs = [pg.transform.scale(pg.image.load("assets/staticArrows/staticDown.png"), (ARROW_DIM, ARROW_DIM))]
down_static_imgs.append(pg.transform.scale(pg.transform.rotate(pg.image.load("OldNote/Down Tap Explosion Dim.png"), 0),
                                           (ARROW_DIM, ARROW_DIM)))
up_static_imgs = [pg.transform.scale(pg.image.load("assets/staticArrows/staticUp.png"), (ARROW_DIM, ARROW_DIM))]
up_static_imgs.append(pg.transform.scale(pg.transform.rotate(pg.image.load("OldNote/Down Tap Explosion Dim.png"), 180),
                                         (ARROW_DIM, ARROW_DIM)))
right_static_imgs = [pg.transform.scale(pg.image.load("assets/staticArrows/staticRight.png"), (ARROW_DIM, ARROW_DIM))]
right_static_imgs.append(
    pg.transform.scale(pg.transform.rotate(pg.image.load("OldNote/Down Tap Explosion Dim.png"), 90),
                       (ARROW_DIM, ARROW_DIM)))

font = pg.font.Font("serpentine.ttf", 50)
combo_font = pg.font.Font("serpentine_reg.ttf", 100)
score_font = pg.font.Font("serpentine_reg.ttf", 50)
perfect_msg = font.render("Perfect!!", True, YELLOW)
perfect_rect = perfect_msg.get_rect()
perfect_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
great_msg = font.render("Great!", True, GREEN)
great_rect = great_msg.get_rect()
great_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
good_msg = font.render("Good", True, BLUE)
good_rect = good_msg.get_rect()
good_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
boo_msg = font.render("Boo", True, PURPLE)
boo_rect = boo_msg.get_rect()
boo_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
miss_msg = font.render("Miss...", True, RED)
miss_rect = miss_msg.get_rect()
miss_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
combo_msg = font.render("combo", True, WHITE)
combo_rect = combo_msg.get_rect()
combo_rect.centery = SCREEN_HEIGHT // 2 + 50
combo_rect.left = SCREEN_WIDTH // 2 + 20

dynamic_sprites = pg.sprite.Group()
left_arrows, right_arrows, up_arrows, down_arrows = \
    pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group(), pg.sprite.Group()
static_arrows = pg.sprite.Group()
left_static_arrow = StaticArrow(COL1_POS, GHOST_YPADDING, left_static_imgs, LEFT)
down_static_arrow = StaticArrow(COL2_POS, GHOST_YPADDING, down_static_imgs, DOWN)
up_static_arrow = StaticArrow(COL3_POS, GHOST_YPADDING, up_static_imgs, UP)
right_static_arrow = StaticArrow(COL4_POS, GHOST_YPADDING, right_static_imgs, RIGHT)
static_arrows.add(left_static_arrow)
static_arrows.add(down_static_arrow)
static_arrows.add(up_static_arrow)
static_arrows.add(right_static_arrow)

speed = 10 / 17


def draw_background(success, video_image):
    if success:
        video_surf = pg.image.frombuffer(video_image.tobytes(), video_image.shape[1::-1], "BGR")
        video_surf = pg.transform.scale(video_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
        DISPLAYSURF.blit(video_surf, (0, 0))
    else:
        video.set(cv2.CAP_PROP_POS_MSEC, 0)
    for entity in static_arrows:
        DISPLAYSURF.blit(entity.get_image(), entity.rect)


def make_note(dir):
    if dir == "left":
        arrow = DynamicArrow(COL1_POS, SCREEN_HEIGHT, left_imgs, LEFT)
        dynamic_sprites.add(arrow)
        left_arrows.add(arrow)
    if dir == "down":
        arrow = DynamicArrow(COL2_POS, SCREEN_HEIGHT, down_imgs, DOWN)
        dynamic_sprites.add(arrow)
        down_arrows.add(arrow)
    if dir == "up":
        arrow = DynamicArrow(COL3_POS, SCREEN_HEIGHT, up_imgs, UP)
        dynamic_sprites.add(arrow)
        up_arrows.add(arrow)
    if dir == "right":
        arrow = DynamicArrow(COL4_POS, SCREEN_HEIGHT, right_imgs, RIGHT)
        dynamic_sprites.add(arrow)
        right_arrows.add(arrow)


def get_hit(arrow, bound):
    pos = arrow.get_pos()
    if GHOST_YPADDING - bound * 3 <= pos <= GHOST_YPADDING + bound * 3:
        return "perfect"
    elif GHOST_YPADDING - bound * 5 <= pos <= GHOST_YPADDING + bound * 5:
        return "great"
    elif GHOST_YPADDING - bound * 7 <= pos <= GHOST_YPADDING + bound * 7:
        return "good"
    else:
        return "boo"


def display_score(score):
    score_msg = score_font.render(str(score).zfill(10), True, WHITE)
    score_rect = score_msg.get_rect()
    score_rect.bottomleft = (25, SCREEN_HEIGHT - 25)
    DISPLAYSURF.blit(score_msg, score_rect)


def display_feedback(feedback):
    global score
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


def combo_active():
    global combo
    if combo >= 5:
        return True
    return False


def display_combo(combo_disp):
    num_msg = combo_font.render(str(combo_disp), True, WHITE)
    num_rect = num_msg.get_rect()
    num_rect.centery = SCREEN_HEIGHT // 2 + 50
    num_rect.right = SCREEN_WIDTH // 2 - 20
    DISPLAYSURF.blit(num_msg, num_rect)
    DISPLAYSURF.blit(combo_msg, combo_rect)


def restart():
    global combo, score, last_note_time, feedback_tick, beat_pos, beat_indices
    beat_indices = BEAT_INDICES.copy()
    beat_pos = 0
    combo = 0
    last_note_time = 32 * INTERVAL - 1600
    score = 0
    feedback_tick = -1000
    mixer.music.stop()
    mixer.music.play(start=0.25)
    for entity in dynamic_sprites:
        entity.kill()
        feedback = ""


def handle_hits(key):
    hit_val = ""
    global combo
    global score
    collisions = {}
    if key == K_LEFT or key == K_a:
        collisions = pg.sprite.groupcollide(left_arrows, static_arrows, False, False)
        if collisions:
            left_static_arrow.collision()
    if key == K_DOWN or key == K_s:
        collisions = pg.sprite.groupcollide(down_arrows, static_arrows, False, False)
        if collisions:
            down_static_arrow.collision()
    if key == K_UP or key == K_w:
        collisions = pg.sprite.groupcollide(up_arrows, static_arrows, False, False)
        if collisions:
            up_static_arrow.collision()
    if key == K_RIGHT or key == K_d:
        collisions = pg.sprite.groupcollide(right_arrows, static_arrows, False, False)
        if collisions:
            right_static_arrow.collision()
    if collisions:
        hit_val = get_hit(list(collisions.keys())[0], dt * speed)
        list(collisions.keys())[0].kill()
    else:
        combo = 0
        score = max(score - 333333, 0)
    return hit_val


dt = 0
feedback_tick = -1000
feedback = ""
mixer.music.play(start=0.25)
last_note_time = 32 * INTERVAL - 1600
# last_note_time = -1600
combo = 0
score = 0
beat_pos = 0
while True:
    cur_tick = pg.time.get_ticks()
    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                restart()
            else:
                hit = handle_hits(event.key)
                if hit != "":
                    score = min(9999999999, int(score + SCORES[hit] * ((1 + combo / 5) if combo_active() else 1)))
                    feedback = hit
                    feedback_tick = cur_tick
                    combo = combo + 1 if hit != "boo" else 0

    for entity in dynamic_sprites:
        entity.move(dt * speed)
        if entity.check_death():
            feedback = "miss"
            feedback_tick = cur_tick
            combo = 0
            score = max(score - 333333, 0)
    # Takes 1515 ms to reach bottom

    for entity in static_arrows:
        entity.update()

    # if (INTERVAL * song_beats[0]) - LOW_INTERVAL <= mixer.music.get_pos() - last_note_time:
    if LOW_INTERVAL <= mixer.music.get_pos() - last_note_time and len(beat_indices) != 0:
        if beat_indices[0] == beat_pos:
            make_note(random.choice(["left", "down", "up", "right"]))
            beat_indices.pop(0)
        beat_pos += 1
        last_note_time += INTERVAL
        # last_note_time += INTERVAL * song_beats[0]
        # song_beats.pop(0)
    # note to self, have starting arrow position be when it should be, not time issue

    success, video_image = video.read()
    draw_background(success, video_image)
    display_score(score)
    for entity in dynamic_sprites:
        DISPLAYSURF.blit(entity.get_image(), entity.rect)

    if cur_tick - feedback_tick <= 500:
        display_feedback(feedback)
        if combo_active():
            display_combo(combo)
    else:
        feedback = ""

    pg.display.update()
    dt = fps_clock.tick(FPS)
