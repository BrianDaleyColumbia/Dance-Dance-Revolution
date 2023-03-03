from sprites import *


pg.init()
fps_clock = pg.time.Clock()
DISPLAYSURF = pg.display.set_mode((0, 0), pg.FULLSCREEN)

FPS = 60
ARROW_PADDING = 10
ARROW_DIM = 150
GHOST_YPADDING = 25
SCREEN_HEIGHT = DISPLAYSURF.get_height()
SCREEN_WIDTH = DISPLAYSURF.get_width()
COL1_POS = int(DISPLAYSURF.get_width() / 2) - 3 * int(ARROW_PADDING / 2) - 3 * int(ARROW_DIM / 2)
COL2_POS = int(DISPLAYSURF.get_width() / 2) - int(ARROW_PADDING / 2) - int(ARROW_DIM / 2)
COL3_POS = int(DISPLAYSURF.get_width() / 2) + int(ARROW_PADDING / 2) + int(ARROW_DIM / 2)
COL4_POS = int(DISPLAYSURF.get_width() / 2) + 3 * int(ARROW_PADDING / 2) + 3 * int(ARROW_DIM / 2)

left_arrow_img = pg.image.load("assets/leftArrows/tile003.png")
down_arrow_img = pg.image.load("assets/downArrows/tile003.png")
up_arrow_img = pg.image.load("assets/upArrows/tile003.png")
right_arrow_img = pg.image.load("assets/rightArrows/tile003.png")
left_static_img = pg.image.load("assets/staticArrows/staticLeft.png")
down_static_img = pg.image.load("assets/staticArrows/staticDown.png")
up_static_img = pg.image.load("assets/staticArrows/staticUp.png")
right_static_img = pg.image.load("assets/staticArrows/staticRight.png")

dynamic_sprites = pg.sprite.Group()
dynamic_sprites.add(DynamicArrow(COL3_POS, SCREEN_HEIGHT, up_arrow_img, ARROW_DIM))

static_sprites = pg.sprite.Group()
static_sprites.add(StaticArrow(COL1_POS, GHOST_YPADDING, left_static_img, ARROW_DIM))
static_sprites.add(StaticArrow(COL2_POS, GHOST_YPADDING, down_static_img, ARROW_DIM))
static_sprites.add(StaticArrow(COL3_POS, GHOST_YPADDING, up_static_img, ARROW_DIM))
static_sprites.add(StaticArrow(COL4_POS, GHOST_YPADDING, right_static_img, ARROW_DIM))


def draw_background():
    DISPLAYSURF.fill((0, 0, 0))
    for entity in static_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)


def make_note(dir):
    if dir == "left":
        dynamic_sprites.add(DynamicArrow(COL1_POS, SCREEN_HEIGHT, left_arrow_img, ARROW_DIM))
    if dir == "down":
        dynamic_sprites.add(DynamicArrow(COL2_POS, SCREEN_HEIGHT, down_arrow_img, ARROW_DIM))
    if dir == "up":
        dynamic_sprites.add(DynamicArrow(COL3_POS, SCREEN_HEIGHT, up_arrow_img, ARROW_DIM))
    if dir == "right":
        dynamic_sprites.add(DynamicArrow(COL4_POS, SCREEN_HEIGHT, right_arrow_img, ARROW_DIM))


starting_tick = pg.time.get_ticks()
while True:
    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pg.quit()
            sys.exit()

    for entity in dynamic_sprites:
        entity.move(10)

    time = pg.time.get_ticks() - starting_tick
    if 200 <= time <= 200 + (1000 / FPS):
        make_note("left")
    if 400 <= time <= 400 + (1000 / FPS):
        make_note("down")
    if 600 <= time <= 600 + (1000 / FPS):
        make_note("up")
    if 800 <= time <= 800 + (1000 / FPS):
        make_note("right")

    draw_background()
    for entity in dynamic_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    pg.display.update()
    fps_clock.tick(FPS)
