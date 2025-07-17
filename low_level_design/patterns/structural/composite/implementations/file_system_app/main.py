"""Client runner"""

from components.file import File
from components.folder import Folder

def build_file_system():
    print("\nBuilding File System\n")

    # Root folder
    root = Folder("workspace")
    root.add(File('Readme.md'))  # Leaf
    
    # react_app folder (composite)
    react_app = Folder("react_app")
    react_app.add(File("index.html"))
    react_app.add(File("package.json"))
    react_app.add(File("package-lock.json"))

    # src folder with some files
    src = Folder("src")
    src.add(Folder("assets"))
    src.add(File("App.jsx"))
    src.add(File("main.jsx"))
    src.add(File("index.css"))

    # public folder
    public = Folder("public")
    public.add(File("favicon.ico"))
    public.add(File("index.html"))

    # node_modules folder (simulate nested depth)
    node_modules = Folder("node_modules")
    node_modules.add(Folder("react"))
    node_modules.add(Folder("react-dom"))
   

    # Add folders to react_app
    react_app.add(src)
    react_app.add(public)
    react_app.add(node_modules)

    # Add react_app to root
    root.add(react_app)

    # Trigger listing
    root.ls()


if __name__ == "__main__":
    print("\nComposite Design Pattern Demo")
    build_file_system()
