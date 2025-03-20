import os


apps_folder = "apps"  

#add the path here :)
apps = {
    "Discord": os.path.join(apps_folder, "Discord.lnk"),  
    "Epic Games": os.path.join(apps_folder, "Epic Games Launcher.lnk"),
    "Google Chrome": os.path.join(apps_folder, "Google Chrome.lnk"),
    "VS Code": os.path.join(apps_folder, "Visual Studio Code.lnk")
}

# Open all applications
for name, path in apps.items():
    if os.path.exists(path):  # Check if the file exists
        os.startfile(path)  # Open the application
        print(f"Opening {name}...")
    else:
        print(f"{name} not found at {path}")
