"""Food picture entry for make.fun bounty food-picture-01.

Writes one picture of food to /output/entry.png. The picture is an
overhead photograph of a gourmet spread (seared salmon with lemon and
herbs, salad, artisan bread, berries, orange juice) stored in this
repository as entry.jpg; this program simply copies it to the output
path, so every run writes exactly the same bytes.
"""

import os
import shutil

# The output is a byte-for-byte copy of the repository's image, so the
# program is deterministic: two runs write identical bytes.
HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.jpg")
DEST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SOURCE, DEST)


if __name__ == "__main__":
    main()
