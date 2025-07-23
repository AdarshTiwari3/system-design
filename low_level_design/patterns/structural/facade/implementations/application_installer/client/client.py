from installer_facade.installer_facade import ApplicationInstaller

def run_installation():
    print("\nApp installer is running...")
    installer=ApplicationInstaller()
    installer.install()