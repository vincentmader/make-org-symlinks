import os
from pathlib import Path

from config import PATH_TO_ORG
from config import PATH_TO_ALL


def paths_to_org_category_directories():
    """Return list of org category directories."""
    # Get list of entries in org directory, then sort the list.
    entries = os.listdir(PATH_TO_ORG)
    entries = sorted(entries)
    # Remove all entries which do not start with a numeric character.
    entries = [e for e in entries if e[0].isnumeric()]
    # Convert entries from filename strings to `Pathlib.Path` instances.
    entries = [Path(PATH_TO_ORG, e) for e in entries]
    # Remove all entries which are not directories.
    entries = filter(os.path.isdir, entries)
    return entries


def paths_to_symlinks_in_all_directory():
    """Return list of paths for all symbolic links in `<ORG_DIRECTORY/A_all>`."""
    # Get list of entries in `A_all` directory, then sort the list.
    entries = os.listdir(PATH_TO_ALL)
    entries = sorted(entries)
    # Convert entries from filename strings to `Pathlib.Path` instances.
    entries = [Path(PATH_TO_ALL, e) for e in entries]
    # Remove all entries which are not symlinks.
    entries = [e for e in entries if os.path.islink(e)]
    return entries


def paths_to_project_directories(path_to_org_category_directory):
    """Return list of paths for all project directories in a given org-category directory."""
    # Get list of entries in category directory, then sort the list.
    entries = os.listdir(path_to_org_category_directory)
    entries = sorted(entries)
    # Convert entries from filename strings to `Pathlib.Path` instances.
    entries = [Path(path_to_org_category_directory, e) for e in entries]
    # Remove all entries which are not directories.
    entries = [e for e in entries if os.path.isdir(e)]
    return entries
