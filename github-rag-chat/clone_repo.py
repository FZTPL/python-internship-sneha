from git import Repo

repo_url=input("Enter Github URL:")

Repo.clone_from(
    repo_url,
    "repos/project"
)

print("Repository cloned successfully")

