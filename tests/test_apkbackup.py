# tests/test_apkbackup.py

import unittest
from unittest.mock import patch
import sys
import os

# Adjust the sys.path to include the root directory of your project.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apkbackup import get_installed_packages, backup_apk

class TestAPKBackup(unittest.TestCase):

    @patch('subprocess.run')
    def test_backup_apk(self, mock_run):
        mock_package_name = "com.example.app"
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="Expected adb output", stderr="")

        # Call your function that interacts with ADB.
        backup_apk('mock_package_name')

        # Assert the expected behavior/output.
        # For example, check if the mock_run was called with the expected arguments.
        mock_run.assert_called_with(['adb', 'shell', 'pm', 'path', mock_package_name], capture_output=True, text=True)

if __name__ == "__main__":
    unittest.main()
