namespace SpriteKind {
    export const Fon = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -20
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    otherSprite.destroy(effects.hearts, 100)
    info.changeLifeBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    timer.throttle("action", 2000, function () {
        scene.cameraShake(4, 100)
        otherSprite.destroy()
        info.changeLifeBy(-1)
    })
})
let fons: Sprite = null
let mySprite: Sprite = null
info.setLife(3)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
let Hole = 0
let score2 = 10
animation.runImageAnimation(
mySprite,
[img`
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
    `,img`
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
    `,img`
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
    `,img`
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
    `],
100,
true
)
mySprite.x = 30
scene.setBackgroundColor(8)
mySprite.ay = 30
mySprite.setStayInScreen(true)
game.onUpdateInterval(2000, function () {
    if (Math.percentChance(99)) {
        fons = sprites.create(img`
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
            `, SpriteKind.Fon)
    } else {
        fons = sprites.create(img`
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
            `, SpriteKind.Food)
    }
    fons.z = -1
    fons.setPosition(160, randint(0, 120))
    fons.setVelocity(-20, 0)
    fons.startEffect(effects.bubbles)
    fons.setFlag(SpriteFlag.AutoDestroy, true)
})
game.onUpdateInterval(1000, function () {
    info.changeScoreBy(0.5)
    if (info.score() == 300) {
        game.over(true, effects.bubbles)
    }
})
game.onUpdateInterval(1000, function () {
    if (Math.percentChance(score2)) {
        score2 += 1
        Hole = randint(0, 4)
        for (let index = 0; index <= 5; index++) {
            if (index != Hole && index != Hole + 1) {
                let wall: Sprite[] = []
                wall.unshift(sprites.create(img`
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
                    `, SpriteKind.Enemy))
                wall[0].setPosition(170, 10 + index * 20)
                wall[0].setVelocity(-15 - score2, 0)
                wall[0].setFlag(SpriteFlag.AutoDestroy, true)
            }
        }
    }
})
