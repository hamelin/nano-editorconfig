import re
from subprocess import run, PIPE, call
import sys
from typing import Optional


if __name__ == '__main__':
    cp = run(["git", "describe", "--always"], stdout=PIPE, encoding="utf-8")
    if cp.returncode != 0:
        print("Problem while gathering project version. Abort.")
        sys.exit(cp.returncode)
    print("Current version:", cp.stdout.strip())
    version_new = input("New version: ").strip()
    if not re.match(r"^[-_.+a-zA-Z0-9]{1,32}$", version_new):
        print("Given version number stinks. Not gonna help you.")
        sys.exit(100)

    with open("setup.py", "r", encoding="utf-8") as file:
        code_setup = file.readlines()

    try:
        version_changed = False
        with open("setup.py", "w", encoding="utf-8") as file:
            for line in code_setup:
                if line.startswith('    version="'):
                    line = f'    version="{version_new}",'
                    version_changed = True
                print(line.rstrip(), file=file)
        if not version_changed:
            print("Could not detect the version change in setup.py. Please debug.")
            sys.exit(101)

        run(["git", "add", "setup.py"]).check_returncode()
        run(["git", "commit", "--sign", "--message", f"Bump version to {version_new}"]).check_returncode()
        print("File setup.py updated.")
    except Exception as err:
        print("Problem while committing the version change. Undo and abort.")
        run(["git", "checkout", "setup.py"])
        sys.exit(getattr(err, "returncode", 102))

    try:
        run(["git", "tag", "--sign", "--message", f"Version {version_new}", version_new]).check_returncode()
        print("New version tagged in.")
    except Exception as err:
        print("Problem while adding the signed tag for the new version. Undo and abort.")
        run(["git", "reset", "--hard", "HEAD^"])
        sys.exit(getattr(err, "returncode", 103))
