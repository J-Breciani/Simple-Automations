import os 
from tkinter.filedialog import askdirectory # For the pop up.

path = askdirectory(title="Select a folder") # returns the path of the folder selected.
list_files = os.listdir(path) # Lists the documents inside of the folder that was selected. 

locations = {
    "images": [".pnj", ".jpg"],
    "spreadsheets": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"]
}

for file in list_files:
    name, extension = os.path.splitext(f"{path}/{file}")
    for local in locations:
        if extension in locations[local]:
            if not os.path.exists(f"{path}/{local}"):
                os.mkdir(f"{path}/{local}")
            os.rename(f"{path}/{file}", f"{path}/{local}/{file}")