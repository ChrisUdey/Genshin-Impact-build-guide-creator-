import os

if __name__ == "__main__":

    import os

    root_folder = r"C:\Users\Jorge\WebstormProjects\Genshin-Impact-build-guide-creator-\backend\app\static\nation_pics"


    for artifact_name in os.listdir(root_folder):
        artifact_dir = os.path.join(root_folder, artifact_name)
        if os.path.isdir(artifact_dir):
            for file_name in os.listdir(artifact_dir):
                file_path = os.path.join(artifact_dir, file_name)
                if os.path.isfile(file_path) and not file_name.lower().endswith(".png"):
                    new_file_path = file_path + ".png"
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {file_path} -> {new_file_path}")

