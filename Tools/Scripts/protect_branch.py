__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

import os
import sys

from github3 import login
from github3.exceptions import NotFoundError


if __name__ == "__main__":
    access_token = os.environ.get("ACCESS_TOKEN")
    github_repository = os.environ.get("GITHUB_REPOSITORY")
    branch_name = "master"

    if len(sys.argv) > 1:
        branch_name = sys.argv[1]

    owner = github_repository.split("/")[0]
    repo_name = github_repository.split("/")[1]

    gh = login(token=access_token)
    if gh is None:
        print("Could not login. Have you provided credentials?")
        exit(1)

    try:
        repo = gh.repository(owner, repo_name)
    except NotFoundError:
        print(f"Could not find repo https://github.com/{owner}/{repo_name}")
        raise

    branch = repo.branch(branch_name)
    state = branch.protect(enforcement="everyone")
    exit(int(state))
