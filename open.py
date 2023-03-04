import os
import sys
import json

path_reference = 'C:\\development\\commands\\FolderOpener\\paths.json'
sys.tracebacklimit = 0


def main(arg: str):
    arg = process_arg(arg)
    path = get_folder(arg)

    open_folder(path)


def process_arg(arg):
    """Returns a processed command line argument"""
    if arg == '':
        return 'default'

    return arg.strip().lower()


def get_folder(prefix: str) -> str:
    folders = get_folder_paths(path_reference)
    folder_path = folders[prefix]

    return folder_path


def get_folder_paths(reference_path: str) -> dict:
    with open(reference_path, "r") as json_file:
        return_dict = json.load(json_file)

    return return_dict


def open_folder(path: str) -> None:
    """Open the folder in File Explorer specified by path"""
    path = os.path.realpath(path)
    try:
        os.startfile(path + "1")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Can't find file at \"{path}\"") from None


if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg)
