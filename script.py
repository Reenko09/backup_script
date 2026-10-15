from datetime import datetime
from pathlib import Path
import shutil 

# INTERFACE --------------------------------------------

# edit files for backup
backup_list = [
    r"C:\Users\lfree\OneDrive\Desktop\Projetos\testes de script\arquivo 1.txt",
    r"C:\Users\lfree\OneDrive\Desktop\Projetos\testes de script\arquivo 2.txt"
]

# Chose option:
# DEFAULT: Destiny folder will be created in the parent of the file
# CUSTOM: Destiny folder will be created in the path specified in the config dictionary, recommended to goup diferent files backups in a same folder
# PARENT: Destiny folder willl be created in the parent folder where the sript is running.

# CUSTOM PATH; put the folder where the script must crate a backup folder, if you use the custom option.

config = {
    "backup_option" : "PARENT",
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
                case "PARENT":
                    destiny_folder = Path(__file__).parent / "backups" / TODAY
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


input(f"Starting BACKUP process, please close every .OFFICE file you want to backup.\n" \
      f"The backup save options is setted to: {config['backup_option']}.\n" \
      f"Press ENTER to continue...\n")
create_backups()
input("\nPress ENTER to exit...")


# Author: luigifernando.reenkober@zf.com