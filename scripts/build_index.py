"""CLI xây dựng artifact Dense/BM25 hiện hành."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.config import parse_args
from src.index import build_index
from src.utils import configure_utf8_console

if __name__ == "__main__":
    configure_utf8_console()
    build_index(parse_args())
