import os

for root, dirs, files in os.walk("projets"):
    for dir_name in dirs:
        if dir_name == "solutions":
            path = os.path.join(root, dir_name, ".gitkeep")
            if not os.path.exists(path):
                open(path, "w").close()
                print("Added:", path)