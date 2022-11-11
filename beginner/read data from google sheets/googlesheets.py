!pip install google-colab

from google.colab import auth
auth.authenticate_user()

import requests
import gspread

from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())

import pandas as pd

# Enter sheetname without using extension
sheetname = "Pokémon Go IV Calculator"
sh = gc.open(sheetname)

worksheet = sh.sheet1
values_list = worksheet.get_all_values()

df = pd.DataFrame(values_list)
df.head()