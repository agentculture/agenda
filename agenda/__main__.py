"""Entry point for ``python -m agenda``."""

from __future__ import annotations

import sys

from agenda.cli import main

if __name__ == "__main__":
    sys.exit(main())
