#!/usr/bin/env python3
#this belongs in root /launch_dp5_workshop.py - Version: 1
# X-Seti - September30 2026 - DP5 Workshop - Root Launcher

"""
Root launcher: runs apps/components/DP5_Workshop/dp5_workshop.py as the main program.
"""

##Methods list -

import runpy
import sys
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

if __name__ == "__main__":
    runpy.run_module('apps.components.DP5_Workshop.dp5_workshop', run_name='__main__')
