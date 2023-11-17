import os
import shutil
import subprocess

DOCS_DIR = "docs/"
STATIC_DIR = "mycore/static/mycore/"
MEDIA_DIR = "media/"


def main(rendered_template, instance):
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)

    html_file_path = f"{DOCS_DIR}index.html"
    # Save the rendered HTML to a file
    with open(html_file_path, "w") as file:
        file.write(rendered_template)
    # create new path to static file directory
    static_dir_components = STATIC_DIR.split("/")
    static_dir_components[0] = DOCS_DIR
    new_static_dir = "/".join(static_dir_components)
    # create new path to media directory
    new_media_dir = f"{DOCS_DIR}{MEDIA_DIR}"
    # copy relevant folders
    shutil.copytree(STATIC_DIR, new_static_dir, dirs_exist_ok=True)
    shutil.copytree(MEDIA_DIR, new_media_dir, dirs_exist_ok=True)

    # Stage, commit, and push changes to github
    commit_msg = f"Static File Update: {instance}"
    try:
        # stage files
        result = subprocess.run(["git", "add", DOCS_DIR], check=True, text=True)
        # commit
        result = subprocess.run(
            ["git", "commit", "-m", commit_msg], check=True, text=True
        )
        # push
        result = subprocess.run(["git", "push"], check=True, text=True)
        print("Git push successful!")
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")
