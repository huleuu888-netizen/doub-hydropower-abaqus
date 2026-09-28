"""
V15.29 Geometry Closure Audit
Check material-to-geology traceability in Abaqus inp files.

Purpose:
1. Extract material names from inp.
2. Compare with predefined engineering geology mapping.
3. Report materials without traceable sources.

This is an audit template. It does not modify inp files.
"""

import re
from pathlib import Path


def extract_materials(inp_file):
    text = Path(inp_file).read_text(encoding="utf-8", errors="ignore")
    return sorted(set(re.findall(r"\*Material, name=([^\n,]+)", text)))


if __name__ == "__main__":
    print("V15.29 material mapping audit template")
    print("Please provide inp path and engineering mapping table before execution.")
