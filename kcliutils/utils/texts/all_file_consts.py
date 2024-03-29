# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from enum import Enum
from typing import List

# Local
from .file_consts import FileConsts

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ enum: AllFileConsts ----------------------------------------------------- #

class AllFileConsts(Enum):

    # -------------------------------------------------------- Values -------------------------------------------------------- #

    PY = FileConsts('.py', '#',  '-')
    TS = FileConsts('.ts', '/*', '-')
    JS = FileConsts('.js', '/*', '-')


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    @classmethod
    def all(cls) -> List[FileConsts]:
        return [
            cls.PY,
            cls.TS,
            cls.JS
        ]


# -------------------------------------------------------------------------------------------------------------------------------- #