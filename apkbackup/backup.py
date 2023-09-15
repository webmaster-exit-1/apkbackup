import os
import subprocess

def backup_apks_via_adb(destination_path="backup_apps.tar.gz"):
    """
    Uses ADB to backup APKs from a connected Android device.
    
    Args:
        destination_path (str): Path to save the compressed APK backup.
        
    Returns:
        str: Output from the adb pull command.
    """
    
    # Constructing the adb command
    adb_cmd = 'adb shell \'find /data/app -type f -name "*.apk" -print0 | tar --null -czvf /sdcard/backup_apps.tar.gz -T -\''
    
    # Running the adb shell command
    subprocess.run(adb_cmd, shell=True, check=True)

    # Pulling the compressed archive
    pull_cmd = f"adb pull /sdcard/backup_apps.tar.gz {destination_path}"
    
    output = subprocess.run(pull_cmd, shell=True, check=True, capture_output=True)
    
    return output.stdout.decode()

if __name__ == "__main__":
    # Run the backup function
    print(backup_apks_via_adb())

