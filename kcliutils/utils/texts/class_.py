# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Local
from .core_texts import class_
from .utils import comment_line, multi_replace

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

def new_class(class_name: str) -> str:
    return multi_replace(
        class_,
        {
            '[CLASS_NAME]': class_name,
            '[CLASS_NAME_COMMENT_LINE]': comment_line('class: {}'.format(class_name))
        }
    )


# ---------------------------------------------------------------------------------------------------------------------------------------- #