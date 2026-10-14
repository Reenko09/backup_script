from datetime import datetime
from pathlib import Path
import shutil 

# INTERFACE --------------------------------------------

# edit files for backup
backup_list = [
    r"<set files to backup here>",
    r"<set files to backup here>"
]

# Chose option:
# DEFAULT: destiny folder will be created in the parent of the file
# CUSTOM: destiny folder will be created in the path specified in the config dictionary, recommended to goup diferent files backups in a same folder

# CUSTOM PATH; put the folder where the script must crate a backup folder, if you use the custom option.

config = {
    "backup_option" : "DEFAULT",
    "custom_path" : r"<set a custom path here>"
}


# SCRIPT --------------------------------------------
 
NOW = datetime.now().strftime("%d-%m-%Y_%H-%M")
TODAY = datetime.now().strftime("%d-%m-%Y")

def create_backups():
    for file in backup_list:
        file_path = Path(file)
        if not file_path.exists():
            print(f"error: file {file} does not exist")
            continue
        else: 
            # decide cackup folder destiny
            match config["backup_option"].upper():
                case "DEFAULT":
                    destiny_folder = file_path.parent / "backups" / TODAY
                case "CUSTOM":
                    destiny_folder = Path(config["custom_path"]) / TODAY
            destiny_folder.mkdir(parents=True, exist_ok=True) 

            # config the new name to the choosen folder
            destiny_name = file_path.stem + "_" + NOW + file_path.suffix
            destiny_file_path = destiny_folder / destiny_name

            # read the file and copy to the destiny folder, even if its a office open file
            try:
                with open(file_path, "rb") as f_origem, open(destiny_file_path, "wb") as f_destino:
                    shutil.copyfileobj(f_origem, f_destino)
                print(f"backup {destiny_name} created in {destiny_folder}")
            except Exception as e:
                print(f"error to create bacup file for {file}. Motivo: {e}")

create_backups()


# Author: luigifernando.reenkober@zf.com