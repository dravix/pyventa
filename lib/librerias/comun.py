#!/usr/bin/env python3
# lib/librerias/comun.py
# Common variables and functions shared across the application.

import os
import sys

# Resolve the per-user data directory based on platform.
# Replaces the old sys.platform == 'linux2' branching.
if sys.platform == "linux":
    home = os.path.join(os.path.expanduser("~"), ".pyventa")
else:
    home = os.path.join(os.path.expanduser("~"), "pyventa")
