import unittest
from unittest.mock import patch
import sys
import os
import subprocess  # Ensure this import is present

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apkbackup import backup_apk

class TestAPKBackup(unittest.TestCase):

    @patch('subprocess.run')
    def test_backup_apk(self, mock_run):
        mock_package_name = "com.example.app"
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout="Expected adb output", stderr="")
        backup_apk(mock_package_name)
        mock_run.assert_called_with(['adb', 'shell', 'pm', 'path', mock_package_name], capture_output=True, text=True)

if __name__ == "__main__":
    unittest.main()
