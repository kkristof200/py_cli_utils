# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import List

# Pip
from kdependencies import InstalledPackage

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

def new_requirements_file(packages: List[InstalledPackage]) -> str:
    return '\n'.join([p.get_install_name(include_version=True) for p in packages])


# ---------------------------------------------------------------------------------------------------------------------------------------- #