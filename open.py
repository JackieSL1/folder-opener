import os
import sys
import json
import re
from config import REFERENCES_PATH


# Suppress stack trace
sys.tracebacklimit = 0


def main():
    arg = sys.argv[1]
    arg = process_arg(arg)

    if arg[0] != '-':
        path = get_folder_path(arg)
        open_folder(path)

    if arg == '-add':
        print("Adding")
        # add_path()


def process_arg(arg):
    """Returns a processed command line argument"""
    if arg == '':
        return 'default'

    return arg.strip().lower()


def get_folder_path(prefix: str) -> str:
    """Return the folder path associated with prefix"""
    folders = create_folder_dict(REFERENCES_PATH)
    prefix = autocomplete(prefix, folders.keys())
    folder_path = folders[prefix]

    return folder_path


def create_folder_dict(reference_path: str) -> dict:
    """Return a dictionary storing the different folder paths and their prefixes from the JSON file at REFERENCES"""
    with open(reference_path, "r") as json_file:
        return_dict = json.load(json_file)

    return return_dict


def autocomplete(prefix: str, references: list[str]) -> str:
    """Return an autocompleted version of the prefix

    Raises a ValueError if zero or multiple results are found
    """
    r_start_of_line = re.compile(f"{prefix}.*")
    r_in_line = re.compile(f".*{prefix}.*")

    for r in (r_start_of_line, r_in_line):

        match_results = list(filter(r.match, references))

        if len(match_results) > 1:
            raise ValueError(
                f"Multiple prefixes were found for arg \"{prefix}\":\n\n" +
                f"   {', '.join(match_results)}\n\n" +
                "Narrow down your search")

        elif len(match_results) == 1:
            return match_results[0]

    raise ValueError(f"No prefix found for arg \"{prefix}\"")


def open_folder(path: str) -> None:
    """Open the folder in File Explorer specified by path"""
    path = os.path.realpath(path)
    try:
        os.startfile(path)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Can't find file at \"{path}\"") from None


if __name__ == '__main__':
    main()
