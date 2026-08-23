
from pathlib import Path

def get_fonts_dir() -> Path:
    """Returns absolute path to the installed fonts directory."""
    return Path(__file__).parent / "fonts"