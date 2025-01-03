import os
import shutil

# Define the base project folder
base_folder = "Data_Analysis_Project"

# Define the folder structure and files
folder_structure = {
    "Cricket_Test_Match_Analysis": {
        "data": ["CricketTestMatchData.csv"],
        "notebooks": ["Cricket Test Clean.ipynb"],
        "visuals": [],
        "README.md": "Cricket Test Match Analysis project-specific details."
    },
    "COVID_Data_Analysis": {
        "data": ["covid_19_india.csv", "covid_vaccine_statewise.csv"],
        "notebooks": ["Covid Data Analysis Project.ipynb"],
        "visuals": [],
        "README.md": "COVID Data Analysis project-specific details."
    },
}

# Create the LICENSE and root README.md files
root_files = {
    "README.md": "Data Analysis Projects Repository overview details.",
    "LICENSE": "MIT License text here."
}

def delete_existing_structure(folder):
    """Delete existing folder structure if it exists."""
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"Deleted existing folder: {folder}")

def create_folder_structure(base_folder, structure, root_files):
    """Create the folder structure and add specified files."""
    os.makedirs(base_folder, exist_ok=True)
    
    # Add root-level files
    for filename, content in root_files.items():
        with open(os.path.join(base_folder, filename), "w") as f:
            f.write(content)
    
    # Create subfolders and files
    for subfolder, contents in structure.items():
        subfolder_path = os.path.join(base_folder, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)
        
        for inner_folder, files in contents.items():
            if isinstance(files, list):  # It's a folder
                inner_path = os.path.join(subfolder_path, inner_folder)
                os.makedirs(inner_path, exist_ok=True)
                
                for file in files:
                    file_path = os.path.join(inner_path, file)
                    with open(file_path, "w") as f:
                        f.write(f"Placeholder content for {file}")
            
            elif isinstance(files, str):  # It's a README.md
                readme_path = os.path.join(subfolder_path, inner_folder)
                with open(readme_path, "w") as f:
                    f.write(files)

# Delete existing structure and create new one
delete_existing_structure(base_folder)
create_folder_structure(base_folder, folder_structure, root_files)

print(f"New folder structure created under: {base_folder}")

