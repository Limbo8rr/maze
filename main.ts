scene.onOverlapTile(SpriteKind.Player, myTiles.tile2, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, myTiles.tile5)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile3, function (sprite, location) {
    game.over(true)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile4, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, myTiles.tile4)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile8, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, myTiles.tile8)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile7, function (sprite, location) {
    info.changeLifeBy(-1)
    info.changeScoreBy(-20)
    tiles.setTileAt(location, myTiles.transparency16)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile5, function (sprite, location) {
    music.baDing.play()
    info.changeScoreBy(99)
    tiles.setTileAt(location, myTiles.tile2)
})
let mySprite: Sprite = null
mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . 3 3 f . . 
    . . . . . . . 3 3 f 3 3 f 3 . . 
    . . . . . . . 3 3 3 3 3 f f . . 
    . . . . 3 f 3 3 3 3 3 . . . . . 
    . . . . . . . . 3 . 3 . . . . . 
    . . . . . . . . f . f . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
tiles.setTilemap(tilemap`level`)
tiles.placeOnRandomTile(mySprite, myTiles.tile2)
scene.cameraFollowSprite(mySprite)
info.setScore(0)
info.setLife(3)
