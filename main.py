""""""

# Working with this google sheet:
# https://docs.google.com/spreadsheets/d/1N7HGkyCrN2DA5ZhZNdCsEuxcBBWIb5_c7nrDHtFTUbQ/edit#gid=1822977730

# if you want to have your own google sheet, follow this tutorial and replace client_secret.json with yours
# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

# The sheet was designed only for slight changes. There might be bugs if you change the sheet too much.

# Don't forget to change DEST_PATH to your Thrive/simulation_parameters folder below


import gspread
from oauth2client.service_account import ServiceAccountCredentials

DEST_PATH = "C:/Users/Chris/Desktop/Thrive/simulation_parameters/"


def flatten_lst(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            if item != "":
                flat_list.append(abs(float(item)))
                if flat_list[-1] == round(flat_list[-1]):
                    flat_list[-1] = int(flat_list[-1])
    return flat_list


def update_files(client, file_name, sheet_name=None, dest_path=DEST_PATH, extension=".json"):
    if sheet_name is None:
        sheet_name = file_name

    sheet = client.open_by_key("1N7HGkyCrN2DA5ZhZNdCsEuxcBBWIb5_c7nrDHtFTUbQ").worksheet(sheet_name)
    values = flatten_lst(sheet.get(file_name+"_values"))

    with open("parameters_files/"+file_name+"_copy.txt") as file_r:
        text = file_r.read().format(*values).replace("~", "{").replace("@", "}")
    with open(dest_path+file_name+extension, "w") as file_w:
        file_w.write(text)


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

for file in ("bio_processes", "biomes", "membranes", "organelles"):
    update_files(client, file, dest_path=DEST_PATH+"microbe_stage/")
update_files(client, "Constants", "bio_processes", extension=".cs")
