import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Path to the files to update
DEST_PATH = "C:/Users/Chris/Desktop/Thrive/simulation_parameters/"


def flatten_lst(lst):
    """Transform a multidimensionnal list to a 1D list, filter empty values and convert str to float or int"""
    flat_list = []
    for sublist in lst:
        for item in sublist:
            if item != "":
                flat_list.append(abs(float(item)))
                if flat_list[-1] == round(flat_list[-1]):
                    flat_list[-1] = int(flat_list[-1])
    return flat_list


def update_files(client, file_name, sheet_name=None, dest_path=DEST_PATH, extension=".json"):
    """
    Retrieve data from Google sheet and update Thrive files
    :param client: Google sheet client
    :param file_name: file to update
    :param sheet_name: sheet where to retrive data
    :param dest_path: where to write updated file
    :param extension: extension of the final file
    :return: None
    """
    if sheet_name is None:
        sheet_name = file_name

    # Retrieve data
    sheet = client.open_by_key("1N7HGkyCrN2DA5ZhZNdCsEuxcBBWIb5_c7nrDHtFTUbQ").worksheet(sheet_name)
    values = flatten_lst(sheet.get(file_name+"_values"))

    # Read template file and update values
    with open("parameters_files/"+file_name+"_copy.txt") as file_r:
        text = file_r.read().format(*values).replace("~", "{").replace("@", "}")
    # Write file in the dest_path folder
    with open(dest_path+file_name+extension, "w") as file_w:
        file_w.write(text)


# Connect to google sheet
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Update files
for file in ("bio_processes", "biomes", "membranes", "organelles"):
    update_files(client, file, dest_path=DEST_PATH+"microbe_stage/")
update_files(client, "Constants", "bio_processes", extension=".cs")
