import os
import glob
from .helper import make_consecutive_pairs


def walk_files_of_dir(root: str, ext=None):
    """Walk through all files in a directory

    Args:
        root (str): root directory to start from
        ext (list[str], optional): extension names to filter. Defaults to None.

    Returns:
        dict: directory (relative path) -> list of files
    """
    files = {}

    # Walk through the directory tree
    for dirpath, _, filenames in os.walk(root):
        # Add directory path to the dictionary
        relative_path = os.path.relpath(dirpath, root)
        filenames = sorted(filenames)
        # Filter files by extension
        if ext:
            filenames = [f for f in filenames if str(f).lower().endswith(tuple(ext))]
        files[relative_path] = filenames

    return files


def walk_pairs_of_dir(root: str, ext=None):
    """Walk through all pairs of files in a directory

    Args:
        root (str): root directory to start from
        ext (list[str], optional): extension names to filter. Defaults to None.

    Returns:
        dict: directory (relative path) -> list of pairs of files
    """
    files = walk_files_of_dir(root, ext)

    # Make consecutive pairs of files
    pairs = {relative_path: make_consecutive_pairs(files) for relative_path, files in files.items()}

    return pairs
