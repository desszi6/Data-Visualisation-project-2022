#%%
#external imports
import PySimpleGUI as sg
from PIL import Image,ImageTk
import numpy as np

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

new_height = 300
new_width = int(np.ceil(img.size[0]*new_height/img.size[1]))

print(img.size)
print(new_width,new_height)
img = img.resize((new_width,new_height))
print(img.size)
""" 
layout = [  [sg.Text(init_player.name)],
            [sg.Image(source=init_player.Photo,size=img.size,key = "-PLAYER_IMAGE-",)],
            [sg.Button('OK'),sg.Button('Cancel')]
            ]
"""
layout = [  [sg.Text('asd')],
            [sg.Image(source='Data\image.png',size=img.size,key = "-IMAGE-",)],
            [sg.Button('OK'),sg.Button('Cancel')]
            ]
window = sg.Window(ui_c.MAIN_TITLE,layout).read()


# %%
