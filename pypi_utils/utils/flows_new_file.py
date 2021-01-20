# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Local
from .utils import Utils
from .texts import new_class, new_enum, new_file_text, new_flow_text

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

def create_new_class():
    file_path, _, _class = Utils.get_path_name_class(Utils.get_args(1)[0])

    Utils.create_file(file_path, new_class(_class))

def create_new_enum():
    file_path, _, _class = Utils.get_path_name_class(Utils.get_args(1)[0])

    Utils.create_file(file_path, new_enum(_class))

def create_new_file():
    file_path, _, _ = Utils.get_path_name_class(Utils.get_args(1)[0])

    Utils.create_file(file_path, new_file_text)

def create_new_flow():
    file_path, _, _ = Utils.get_path_name_class(Utils.get_args(1)[0])

    Utils.create_file(file_path, new_flow_text)


# ---------------------------------------------------------------------------------------------------------------------------------------- #