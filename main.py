"""Write the patch-note entry to the grader output directory.

Reads entry.txt next to this file and writes it verbatim, in a single
write, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). No temporary
file and no rename: a temp file would be created mode 0600 and the
grader could not read it. The output is chmodded 0644 explicitly.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

try:
    data = (HERE / "entry.txt").read_bytes()
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "entry.txt"
    target.write_bytes(data)
    os.chmod(target, 0o644)
except OSError:
    raise
