from __future__ import print_function

import os
import glob

if __name__ == '__main__':
    path = os.path.join("..", "base", "python-base", "*", "Dockerfile*")
    files = glob.glob(path)
    for dockerfile_path in files:
        cmd = "floydker push {}".format(dockerfile_path)
        p = os.popen(cmd)
        xs = p.readlines()
        for x in xs:
            print(x)
