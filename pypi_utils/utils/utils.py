# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, Union, Tuple, List
import os, sys

# Pip
from kcu.sh import sh
from kcu import strio, kjson, kpath

# Local
from .constants import Constants
from .config_keys import ConfigKeys
from .prompt import Prompt

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------- class: Utils ------------------------------------------------------------- #

class Utils:

    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    # Args

    @classmethod
    def has_arg(cls, arg: str) -> bool:
        for passed_arg in cls.get_args(minimum_needed=1):
            if arg.lower() == passed_arg.lower():
                return True

        return False

    @staticmethod
    def get_args(minimum_needed: int = 1) -> List[str]:
        args = sys.argv[1:]

        if len(args) < minimum_needed + 1:
            raise ValueError('Not enough args passed: {} out of {}'.format(len(args), minimum_needed))

        return args


    # Paths

    @staticmethod
    def create_file(
        file_path: str,
        text: Optional[str] = None
    ) -> bool:
        folder_path = kpath.folder_path_of_file(file_path)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return strio.save(file_path, text or '')

    @classmethod
    def config_file_path(cls) -> str:
        return os.path.join(cls.home_dir(), Constants.CONFIG_FILE_NAME)

    @staticmethod
    def home_dir() -> str:
        return sh('echo $HOME').strip()

    @staticmethod
    def readme_file_path() -> str:
        return sh('echo $HOME').strip()

    @staticmethod
    def demo_file_path() -> str:
        return sh('echo $HOME').strip()


    # Git

    @classmethod
    def get_git_username(cls) -> Optional[str]:
        return cls.__get_local_git_username() or cls.get_config_value(ConfigKeys.USER, create_new_config_if_none=True) or cls.__get_global_git_username()

    @classmethod
    def get_git_url(cls) -> Optional[str]:
        url = cls.__get_arg_from_file('.git/config', 'url = ')
        
        return url.replace('.git', '').strip('/') if url else None


    # Config

    @classmethod
    def get_config_value(
        cls,
        key: Union[ConfigKeys, str],
        create_new_config_if_none: bool = True
    ) -> Optional[any]:
        key = key if isinstance(key, str) else key.value
        config = cls.get_config(create_new_if_none=create_new_config_if_none)

        return config[key] if config and key in config else None

    @classmethod
    def get_config(cls, create_new_if_none: bool = True) -> Optional[dict]:
        config_path = cls.config_file_path()

        return kjson.load(config_path) if os.path.exists(config_path) else cls.create_new_config() if create_new_if_none else None

    @classmethod
    def create_new_config(cls) -> dict:
        username, min_v, max_v = Prompt.config(cls.__get_local_git_username() or cls.__get_global_git_username())
        user_input = {
            ConfigKeys.USER: username,
            ConfigKeys.DEFAULT_MIN_PYTHON_VERSION: min_v,
            ConfigKeys.DEFAULT_MAX_PYTHON_VERSION: max_v
        }

        kjson.save(cls.config_file_path(), user_input)

        return user_input


    # Strings

    @classmethod
    def get_path_name_class(cls, file_path_or_path: str) -> Tuple[str, str, str]:
        file_path = file_path_or_path.strip().strip(os.path.sep).strip()

        if not file_path.endswith('.py'):
            file_path += '.py'

        file_name = file_path.split(os.path.sep)[-1].replace('.py', '')
        file_class = cls.class_name_from_file_name(file_name)

        return file_path, file_name, file_class

    @staticmethod
    def class_name_from_file_name(file_name: str) -> str:
        return ''.join([p.title() for p in file_name.split('_')])


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    # Git

    @classmethod
    def __get_local_git_username(cls) -> Optional[str]:
        return cls.__get_arg_from_file('.git/config', 'name = ')

    @classmethod
    def __get_global_git_username(cls) -> Optional[str]:
        return cls.__get_arg_from_file(os.path.join(cls.home_dir(), '.gitconfig'), 'name = ')

    @staticmethod
    def __get_arg_from_file(path: str, splitter: str) -> Optional[str]:
        if not os.path.exists(path):
            return None

        try:
            for line in strio.load(path).split('\n'):
                if splitter in line:
                    return line.split(splitter)[1].strip()
        except Exception as e:
            print(e)

        return None


# ---------------------------------------------------------------------------------------------------------------------------------------- #