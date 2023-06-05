import os
from pathlib import Path

from termcolor import colored

import utils
from config import IS_VERBOSE
from config import PATH_TO_ALL


def remove_currently_present_symlinks():
    """Remove all symbolic links currently present in `<ORG_DIRECTORY>/A_all`."""
    paths = utils.paths_to_symlinks_in_all_directory()
    for path in paths:
        os.unlink(path) # Note: This is assured to always be a symlink!
        if IS_VERBOSE:
            text = f"Removed symbolic link at \"{path}\"."
            print(colored(text, "red"))
    text = f"Removed {len(paths)} symbolic links from \"{PATH_TO_ALL}\"."
    print(colored(text, "red"))


def create_links_for_org_category_directories():
    """Create symbolic links to `<ORG_DIRECTORY/A_all>`for all categories in `<ORG_DIRECTORY>`."""
    paths = utils.paths_to_org_category_directories()
    for path in paths:
        create_links_for_org_category_directory(path)
    symlinks = utils.paths_to_symlinks_in_all_directory()
    text = f"Created {len(symlinks)} symbolic links at \"{PATH_TO_ALL}\"."
    print(colored(text, "green"))


def create_links_for_org_category_directory(category: Path):
    """Create symbolic links to `<ORG_DIRECTORY/A_all>`for all projects in `category`."""
    paths = utils.paths_to_project_directories(category)
    for path in paths:
        project_title = os.path.basename(path)
        target = Path(PATH_TO_ALL, project_title)
        os.symlink(path, target)
        if IS_VERBOSE:
            text = f"Created symbolic link at \"{target}\"."
            print(colored(text, "green"))


if __name__ == "__main__":
    remove_currently_present_symlinks()
    create_links_for_org_category_directories()
