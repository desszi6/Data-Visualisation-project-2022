#%%
#external imports
import PySimpleGUI as sg
from PIL import Image,ImageTk
import numpy as np
import os
#internal imports
import ui_constants as ui_c


"""
IMPORT PREPROCESSED DATA HERE
"""
#DataBase = loadDataBase()

""" Variables used from .csv
ID	Name	Age	Photo	Nationality	Flag	Overall	Potential	Club	Club Logo
Value	Wage	Special	Preferred Foot	International Reputation	Weak Foot
Skill Moves	Work Rate	Body Type	Real Face	Position	Joined	Loaned From
Contract Valid Until	Height	Weight	Release Clause	Kit Number	Best Overall Rating
"""

# %%
# Define window contents
sg.theme('SystemDefaultForReal')
#init_player = DataBase.get_player_data(np.random.randint(0,130))

## Load Image here
img= Image.open('Data\image.png')
#resize image

new_height = 100
new_width = int(np.ceil(img.size[0]*new_height/img.size[1]))

print(img.size)
print(new_width,new_height)
img = img.resize((new_width,new_height))
print(img.size)

radar_col = [
    [
        sg.Canvas(key='-RADAR_CANVAS-')
        ]
]
player_left_col = [
    [sg.Image(source='Data\image.png',size=img.size,key='-NAT_FLAG-')], #country flag
    [sg.Text("country",key ='-NAT-')], #country
    [sg.Text("Overal rating",key ='-OVR-')]#overal rating of the player
]
player_right_col = [
    [sg.Image(source='Data\image.png',size=img.size,key='-CLUB_FLAG-')], #club flag
    [sg.Text("club",key ='-CLUB-')], #club
    [sg.Text("position",key ='-POS-')]#Player position
]
player_col =[
    [sg.Text("Player Name",key ='-PLAYER_NAME-')], #Player name
    [sg.Image(source='Data\image.png',size=img.size,key ='-PLAYER_FACE-')], #Player face
    [sg.Column(player_left_col),sg.VSeperator(),sg.Column(player_right_col)]
]
layout = [[sg.Column(radar_col),sg.VSeperator(),sg.Column(player_col)]]
"""
layout = [  [sg.Text(init_player.name)],
            [sg.Image(source=init_player.Photo,size=img.size,key = "-PLAYER_IMAGE-",)],
            [sg.Button('OK'),sg.Button('Cancel')]
            ]

layout = [  [sg.Text('asd')],
            [sg.Image(source='Data\image.png',size=img.size,key = "-IMAGE-",)],
            [sg.Button('OK'),sg.Button('Cancel')]
            ]
"""
window = sg.Window(ui_c.MAIN_TITLE,layout).read()


# %%
