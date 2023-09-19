#!/usr/bin/env python3
import sys

def devices():
    return "List of devices attached\nemulator-5554\tdevice\n"

def shell_command(cmd):
    if cmd == "find /data/app/ -name *.apk":
        return "/data/app/com.example.myapp/base.apk\n"
    elif cmd == "tar -czf /tmp/backup.tar.gz /data/app/com.example.myapp/base.apk":
        return ""
    else:
        return "Unknown command"

def main():
    command = sys.argv[1] if len(sys.argv) > 1 else ""

    if command == "devices":
        print(devices())
    elif command.startswith("shell"):
        cmd = " ".join(sys.argv[2:])
        print(shell_command(cmd))
    else:
        print(f"Command '{command}' not recognized")

if __name__ == "__main__":
    main()
