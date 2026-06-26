import os

def read_repository(repo_path):
    documents = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in {
                ".git",
                "venv",
                "__pycache__",
                "node_modules",
                "dist",
                "build"
            }
        ]

        for file in files:
            if file.endswith((".py", ".md", ".txt")):
                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        documents.append(f.read())
                except Exception:
                    pass

    print(len(documents))
    return documents