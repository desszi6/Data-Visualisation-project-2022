#%%
#external imports
import PySimpleGUI as sg
from PIL import Image,ImageTk
import numpy as np
import os
import random
#internal imports
import ui_constants as ui_c
from utils import get_data


"""
IMPORT PREPROCESSED DATA HERE
"""
DataBase = get_data("E:\98_GitRepo\02_DataVis\Data-Visualisation-project-2022\Data")

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

#While loop for panel
while True:
    event,values = window.read()

    #example event:
    #if event == sg.event_you_want
    #   things happen here
    
    #put events here:
    if event == sg.

    #close the layout
    if event == sg.WIN_CLOSED or event == 'Exit':
            break

def choose_random_player(df):
    while True:
        random_id=random.randint(0,len(df))
        if (df['Overall'].loc(random_id) >= 80) or (df['Position'] != 'GK'):
            break
    random_player=df.loc(random_id)
    return random_player
def load_player2layout(layoutH,df):
    player = choose_random_player(df)
    #country name
    layoutH["-NAT-"].update(player[''])
    #club names
    layoutH["-CLUB-"].update()
    #overall
    layoutH["-OVR-"].update()
    #Position
    layoutH['-POS-'].update()


