#!/usr/bin/env python3

import sys

from pathlib import Path

sys.path.insert(0, str(Path(__file__).absolute().parent.parent))

from accuconf import db

db.create_all()
