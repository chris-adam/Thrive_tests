Just a little program to update Thrive simulation_parameters files easlisy. This program updates Thrive files from the following Google Sheet:
https://docs.google.com/spreadsheets/d/1N7HGkyCrN2DA5ZhZNdCsEuxcBBWIb5_c7nrDHtFTUbQ/edit#gid=1822977730

If you want to have your own google sheet, make a copy, follow this tutorial and add client_secret.json in the files. I don't share mine as I'm using it for other sheets.
https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
Don't forget to install gspread and oauth2client:
- pip install gspread oauth2client

The sheet was designed only for slight changes. There might be bugs if you change the sheet too much. To avoid prolem, don't delete or add values, only edit them.

Don't forget to change DEST_PATH to your Thrive/simulation_parameters folder in main.py
