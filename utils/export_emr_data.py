# coding=utf-8
import json
import subprocess
from pathlib import Path


def check_installation_folders(config_path):
    """
    Checks if EMR installation folders exist and returns their Git tag versions.
    :param config_path: path to a JSON file containing {"app_name": "/path/to/app"}
    :return: dict with {app_name: tag or "unknown"}
    """
    version_dict = {}

    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_file) as f:
        apps_dir = json.load(f)

    for app_name, app_path in apps_dir.items():
        app_dir = Path(app_path)
        if app_dir.exists():
            tag = get_emr_version(app_dir)
            version_dict[app_name] = tag
        else:
            version_dict[app_name] = "missing"

    return version_dict


def get_emr_version(directory):
    """
    Runs `git describe --tags` in the repo and returns the tag.
    """
    git_dir = Path(directory) / ".git"
    if not git_dir.exists():
        return "no_git_repo"

    git_path = "/usr/bin/git"  # Full path to git (fix for systemd environment)

    try:
        result = subprocess.run(
            [git_path, "--git-dir", str(git_dir), "--work-tree", str(directory), "describe", "--tags"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # Handle cases where no tags exist or invalid repo state
        return f"error: {e.stderr.strip() or 'unknown'}"