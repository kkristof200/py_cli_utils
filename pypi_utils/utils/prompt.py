# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import List, Optional, Tuple, Union

# Pip
from bullet import SlidePrompt, Bullet, Input, colors

# Local
from .constants import Constants


# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: Prompt ------------------------------------------------------------- #

class Prompt:

    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    @classmethod
    def min_default_python_version(cls) -> float:
        return cls.__prompt((cls.__get_min_default_python_version_prompt(), float))
    
    @classmethod
    def max_default_python_version(cls) -> float:
        return cls.__prompt((cls.__get_max_default_python_version_prompt(), float))

    @classmethod
    def username(cls, default_username: Optional[str] = None) -> Optional[str]:
        return cls.__prompt((cls.__get_username_prompt(), str)) or default_username

    @classmethod
    def config(cls, default_username: Optional[str] = None) -> Tuple[Optional[str], float, float]:
        username, min_v, max_v = cls.__prompt([
            (cls.__get_username_prompt(), str),
            (cls.__get_min_default_python_version_prompt(), float),
            (cls.__get_max_default_python_version_prompt(), float)
        ])

        return username or default_username, min_v, max_v

    @classmethod
    def _config(cls, default_username: Optional[str] = None) -> Tuple[Optional[str], float, float]:
        username, min_v, max_v = cls.__prompt([
            (cls.__get_username_prompt(), str),
            (cls.__get_min_default_python_version_prompt(), float),
            (cls.__get_max_default_python_version_prompt(), float)
        ])

        return username or default_username, min_v, max_v


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    # Prompts
    @staticmethod
    def __prompt(
        prompts_with_types: Union[List[Tuple[Union[Bullet, Input], any]], Tuple[Union[Bullet, Input], any]],
        summarize: bool = True
    ) -> Union[List[any], any]:
        if not isinstance(prompts_with_types, list):
            prompts_with_types = [prompts_with_types]
        
        prompts = [p[0] for p in prompts_with_types]
        types = [p[1] for p in prompts_with_types]

        cli = SlidePrompt(prompts)
        results = [res[0] if isinstance(res[0], types[i]) else types[i](res[0]) for i, res in enumerate(cli.launch())]

        if summarize:
            cli.summarize()

        return results if len(results) > 1 else results[0]


    # Getters

    @staticmethod
    def __get_package_name_prompt(default_package_name: Optional[str] = None) -> Input:
        return Input(
            "Enter package name (will be useed on pip when published): ",
            default=default_package_name,
            word_color=colors.foreground["yellow"],
            pattern='.*'
        )

    @staticmethod
    def __get_package_description_prompt(default_package_description: Optional[str] = None) -> Input:
        return Input(
            "Enter package description: ",
            default=default_package_description,
            word_color=colors.foreground["yellow"],
            pattern='.*'
        )

    @staticmethod
    def __get_username_prompt(default_username: Optional[str] = None) -> Input:
        return Input(
            "Username (preferably git): ",
            default=default_username,
            word_color=colors.foreground["yellow"],
            pattern='.*'
        )

    @classmethod
    def __get_min_default_python_version_prompt(cls) -> Bullet:
        return cls.__get_bullet_prompt('Minimum default supported python vesion?', choices=Constants.PYTHON_VERSIONS)

    @classmethod
    def __get_max_default_python_version_prompt(cls) -> Bullet:
        return cls.__get_bullet_prompt('Maximum default supported python vesion?', choices=Constants.PYTHON_VERSIONS[::-1])

    @staticmethod
    def __get_bullet_prompt(
        question: str,
        choices: List[str]
    ) -> Bullet:
        return Bullet(
            question,
            choices=choices,
            bullet=">",
            margin=2,
            bullet_color=colors.foreground["black"],
            word_color=colors.foreground["cyan"],
            word_on_switch=colors.foreground["black"],
            background_on_switch=colors.background["cyan"],
            indent=0,
            shift=1,
            pad_right=1,
            return_index=True
        )


# ---------------------------------------------------------------------------------------------------------------------------------------- #