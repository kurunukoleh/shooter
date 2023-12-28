#import launcher
import json
with open('data.json' , 'r' , encoding='utf-8') as f:
    dota = json.load(f)

#textures
rocket_texture = "pixelartship.png"
mateor_texture = "pixelartmeteor.png"
bull_texture =  "tnt1.png"
fon_texture = "pixelartspase.png"
lose_texture = "pixelartlose.png"
win_texture = "pixelartwin.png"
#sounds
fire_sound = 'vystrel-iz-pistoleta-zvuk-puli.mp3'
lose_sound = '583699913672e65.mp3'
win_sound = 'zvuk-tadam-na-trube.mp3'
musick = "space.ogg"
#dificult
#asteroid_count = 30
#asteroid_speed = 2
#asteroid_size = 50
#player_speed = 5
#bull_speed = 10
#fps = 60
#musik_volume = 0.6

#json

asteroid_count = int(dota['asteroid_count'])
asteroid_speed = int(dota['asteroid_speed'])
asteroid_size = int(dota['asteroid_size'])
player_speed = int(dota['player_speed'])
bull_speed = int(dota['bull_speed'])
fps = int(dota['fps'])
musik_volume = int(dota['musik_volume'])/100