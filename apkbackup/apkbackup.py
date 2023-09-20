import os
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_installed_packages():
    """
    Fetch the list of installed packages on the device using ADB.
    """
    try:
        result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], capture_output=True, text=True)
        packages = [line.split(":")[1].strip() for line in result.stdout.splitlines()]
        return packages
    except Exception as e:
        logging.error(f"Error fetching installed packages: {e}")
        return []

def backup_apk(package_name, backup_dir="backups"):
    """
    Backup the APK of the specified package to the backup directory.
    """
    try:
        os.makedirs(backup_dir, exist_ok=True)
        cmd = f"adb pull $(adb shell pm path {package_name} | cut -d':' -f2) {backup_dir}/{package_name}.apk"
        subprocess.run(cmd, shell=True)
        logging.info(f"Backed up {package_name} to {backup_dir}/{package_name}.apk")
    except Exception as e:
        logging.error(f"Error backing up {package_name}: {e}")

def main():
    """
    Main function to backup all APKs from the device.
    """
    packages = get_installed_packages()
    for package in packages:
        backup_apk(package)

if __name__ == "__main__":
    main()
