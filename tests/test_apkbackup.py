# tests/test_apkbackup.py

import unittest
from unittest.mock import patch
import sys
import os
import subprocess


def get_installed_packages():
    try:
        result = subprocess.check_output(['adb', 'shell', 'pm', 'list', 'packages'], text=True)
        packages = [line.split(":")[1].strip() for line in result.splitlines()]
        return packages
    except subprocess.CalledProcessError as e:
        print(f"Error executing adb command: {e}")
        return []

# Example usage
packages = get_installed_packages()
print(packages)


# Adjust the sys.path to include the root directory of your project.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apkbackup import get_installed_packages, backup_apk

class TestAPKBackup(unittest.TestCase):

    @patch('subprocess.run')
    def test_some_functionality(self, mock_run):
        mock_run.return_value = "Expected adb output"

        # Call your function that interacts with ADB.
        result = backup_apk(foobar.apk)

        # Assert the expected behavior/output.
        self.assertEqual(result, "Expected output based on mock")

if __name__ == "__main__":
    unittest.main()
