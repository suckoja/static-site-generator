import os
import shutil

def copy_static_to_public(static_dir="static", public_dir="public"):
    """
    Copy all files and subdirectories from static_dir to public_dir.
    Cleans the public_dir before copying.
    """
    # If public_dir exists, remove it completely
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    # Recreate an empty public_dir
    os.makedirs(public_dir, exist_ok=True)

    # Walk through static_dir and copy everything
    for root, dirs, files in os.walk(static_dir):
        # Relative path from static_dir to current root
        relative_path = os.path.relpath(root, static_dir)
        dest_root = os.path.join(public_dir, relative_path)

        # Create corresponding subdirectory in public
        os.makedirs(dest_root, exist_ok=True)

        # copy all files in the current folder
        for file in files:
            source = os.path.join(root, file)
            destination = os.path.join(dest_root, file)
            shutil.copy2(source, destination)