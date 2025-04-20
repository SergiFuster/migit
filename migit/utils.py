import platform
import subprocess


def hide(path):
    if platform.system() == "Windows":
        subprocess.run(["attrib", "+h", path])
