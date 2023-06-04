import os
from pathlib import Path

import utils
from config import IS_VERBOSE
from config import PATH_TO_ALL


def remove_currently_present_symlinks():
    """Remove all symbolic links currently present in `<ORG_DIRECTORY>/A_all`."""
    paths = utils.paths_to_symlinks_in_all_directory()
    for path in paths:
        os.unlink(path) # Note: This is assured to always be a symlink!
        if IS_VERBOSE:
            print(f"Removed symbolic link at \"{path}\".")
    print(f"Removed {len(paths)} symbolic links from \"{PATH_TO_ALL}\".")


def create_links_for_org_category_directories():
    """Create symbolic links to `<ORG_DIRECTORY/A_all>`for all categories in `<ORG_DIRECTORY>`."""
    paths = utils.paths_to_org_category_directories()
    for path in paths:
        create_links_for_org_category_directory(path)
    symlinks = utils.paths_to_symlinks_in_all_directory()
    print(f"Created {len(symlinks)} symbolic links at \"{PATH_TO_ALL}\".")


def create_links_for_org_category_directory(category: Path):
    """Create symbolic links to `<ORG_DIRECTORY/A_all>`for all projects in `category`."""
    paths = utils.paths_to_project_directories(category)
    for path in paths:
        project_title = os.path.basename(path)
        target = Path(PATH_TO_ALL, project_title)
        os.symlink(path, target)
        if IS_VERBOSE:
            print(f"Created symbolic link at \"{target}\".")


if __name__ == "__main__":
    print()
    remove_currently_present_symlinks()
    print()
    create_links_for_org_category_directories()
