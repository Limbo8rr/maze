def on_overlap_tile(sprite, location):
    tiles.place_on_random_tile(mySprite, myTiles.tile5)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile2, on_overlap_tile)

def on_overlap_tile2(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile3, on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    tiles.place_on_random_tile(mySprite, myTiles.tile4)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile4, on_overlap_tile3)

def on_overlap_tile4(sprite, location):
    tiles.place_on_random_tile(mySprite, myTiles.tile8)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile8, on_overlap_tile4)

def on_overlap_tile5(sprite, location):
    info.change_life_by(-1)
    info.change_score_by(-20)
    tiles.set_tile_at(location, myTiles.transparency16)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile7, on_overlap_tile5)

def on_overlap_tile6(sprite, location):
    music.ba_ding.play()
    info.change_score_by(99)
    tiles.set_tile_at(location, myTiles.tile2)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile5, on_overlap_tile6)

mySprite: Sprite = None
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
tiles.set_tilemap(tilemap("""
    level
"""))
tiles.place_on_random_tile(mySprite, myTiles.tile2)
scene.camera_follow_sprite(mySprite)
info.set_score(0)
info.set_life(3)