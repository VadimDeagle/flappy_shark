@namespace
class SpriteKind:
    Fon = SpriteKind.create()

def on_a_pressed():
    mySprite.vy = -20
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.hearts, 100)
    info.change_life_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    
    def on_throttle():
        scene.camera_shake(4, 100)
        otherSprite.destroy()
        info.change_life_by(-1)
    timer.throttle("action", 2000, on_throttle)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

fons: Sprite = None
mySprite: Sprite = None
info.set_life(3)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
Hole = 0
score2 = 10
animation.run_image_animation(mySprite,
    [img("""
            ..............fffcc.............
                ..............fcbddcc...........
                ...............fbbddcc..........
                ...............fcbbccf..........
                ..ccc.........ffccccccfffff.....
                ..cbbcc....fffcbbbbcbbbbbbbff...
                ...cbbdc.ffcccbbbbcbcbbbbbbbbf..
                ...fbbdcfcccccbbbcbcbbffbbbbbbff
                ....fbbffcccccbbbbbcb1ff11bbbcbf
                ....fcbbcccccccbbbbb11111111bbbf
                ....fcccccccccccbbbb11cc33111bf.
                ...fcbbffbdbcccccbbb111c13cccf..
                ...fbbf..ccddddcfbbbc111c31cf...
                ..fbbf.....ccdccbbdbf111cccf....
                ..fff........ccbbdcfcccc........
                ..............fffff.............
        """),
        img("""
            ..............fffcc.............
                ..............fbbddc............
                ...............fbbddc...........
                ccc............fcbbccf..........
                cbbcc.........ffccccccffffff....
                .cbbdc.....fffcbbbbbbbbbbbbbff..
                .fbbddc..ffcccbbbbcbcbbbbbbbbbff
                ..fbbdfffcccccbbbcbcbbffbbbbbcbf
                ..fcbbbcccccccbbbcbcb1ff1111bbbf
                ..fccbcccccccccbbbbbb11111111bf.
                .fcbbfffccccccccbbbb11cc33cccf..
                .fbbf...cbdbcccccbbb111c131cf...
                fbbf.....ccdddddfbbbc111c33f....
                fff........ccddfbbdbf1111ff.....
                .............cfbbdbfccccc.......
                ..............fffff.............
        """),
        img("""
            ..............fffc..............
                ..............fbddcc............
                ..ccc.........ffbddbc...........
                ..cbbc.........fcbbccf..........
                ...cbdc.......ffccccccfffffff...
                ...fbdc....fffcbbbbbbbbbbbbbcff.
                ....fbdc.ffcccbbbbbbcbbbbbbbbbcf
                ....fcdffcccccbbbcbcbbbffbbbbcbf
                ....fcbbccccccbbbcbcbbbff1111bbf
                ...fcbbccccccccbbbcbb11111111bf.
                ...fbbfffcccccccbbbb11bc33cccf..
                ..fbbf..cbdbcccccbbb111c131cf...
                ..fff....cbdddddccbbc111c33f....
                ..........ccbddccbbdf1111ff.....
                ............ccfbbbdfccccc.......
                ..............fffff.............
        """),
        img("""
            ..............fffcc.............
                ..............fbbddc............
                ...............fbbddc...........
                ccc............fcbbccf..........
                cbbcc.........ffccccccffffff....
                .cbbdc.....fffcbbbbbbbbbbbbbff..
                .fbbddc..ffcccbbbbcbcbbbbbbbbbff
                ..fbbdfffcccccbbbcbcbbffbbbbbcbf
                ..fcbbbcccccccbbbcbcb1ff1111bbbf
                ..fccbcccccccccbbbbbb11111111bf.
                .fcbbfffccccccccbbbb11cc33cccf..
                .fbbf...cbdbcccccbbb111c131cf...
                fbbf.....ccdddddfbbbc111c33f....
                fff........ccddfbbdbf1111ff.....
                .............cfbbdbfccccc.......
                ..............fffff.............
        """)],
    100,
    True)
mySprite.x = 30
scene.set_background_color(8)
mySprite.ay = 30
mySprite.set_stay_in_screen(True)

def on_update_interval():
    global fons
    if Math.percent_chance(99):
        fons = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . 6 6 6 6 6 . . . 6 6 . . . 
                            . . 6 9 6 6 6 6 6 . 6 6 6 . . . 
                            . 6 6 6 6 6 6 6 6 6 6 6 . . . . 
                            . . 6 6 6 6 6 6 6 . 6 6 6 . . . 
                            . . . 6 6 6 6 6 . . . 6 6 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Fon)
    else:
        fons = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . 4 4 4 4 4 . . . 4 4 . . . 
                            . . 4 9 4 4 4 4 4 . 4 4 4 . . . 
                            . 4 4 4 4 4 4 4 4 4 4 4 . . . . 
                            . . 4 4 4 4 4 4 4 . 4 4 4 . . . 
                            . . . 4 4 4 4 4 . . . 4 4 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
    fons.z = -1
    fons.set_position(160, randint(0, 120))
    fons.set_velocity(-20, 0)
    fons.start_effect(effects.bubbles)
    fons.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(2000, on_update_interval)

def on_update_interval2():
    info.change_score_by(0.5)
    if info.score() == 300:
        game.over(True, effects.bubbles)
game.on_update_interval(1000, on_update_interval2)

def on_update_interval3():
    global score2, Hole
    if Math.percent_chance(score2):
        score2 += 1
        Hole = randint(0, 4)
        for index in range(6):
            if index != Hole and index != Hole + 1:
                wall: List[Sprite] = []
                wall.unshift(sprites.create(img("""
                            66666666666666666666
                                                66666666666666666666
                                                66666666666666666666
                                                66699999999999999666
                                                66699999999999999666
                                                66699666999966699666
                                                66699666999966699666
                                                66699666999966699666
                                                66699999666699999666
                                                66699999666699999666
                                                66699999666699999666
                                                66699999666699999666
                                                66699666999966699666
                                                66699666999966699666
                                                66699666999966699666
                                                66699999999999999666
                                                66699999999999999666
                                                66666666666666666666
                                                66666666666666666666
                                                66666666666666666666
                        """),
                        SpriteKind.enemy))
                wall[0].set_position(170, 10 + index * 20)
                wall[0].set_velocity(-15 - score2, 0)
                wall[0].set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(1000, on_update_interval3)
