import os
import subprocess
import sys
import tempfile
from pathlib import Path


def fix_long_lines(directory: str, max_line_length: int = 88) -> None:
    """
    Recursively find Python files in the given directory and fix long lines using black.

    Args:
        directory: Path to the directory containing Python files
        max_line_length: Maximum allowed line length (default: 88 to match black's default)
    """
    # Convert directory to Path object
    dir_path = Path(directory)

    # Find all Python files recursively
    python_files = list(dir_path.rglob("*.py"))

    if not python_files:
        print(f"No Python files found in {directory}")
        return

    print(f"Found {len(python_files)} Python files to process")

    # Create a temporary config file for black
    with tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False) as tmp:
        tmp.write(r"""
[tool.black]
line-length = 120
target-version = ['py310']
include = '\.py$'
""")
        config_path = tmp.name

    try:
        # Run black on all files
        cmd = ["black", "--config", config_path, directory]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print("Successfully formatted all files")
            if result.stdout:
                print("Output:", result.stdout)
        else:
            print("Error formatting files:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error running black: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Clean up temporary config file
        os.unlink(config_path)


# input_path = "src/bbsky/crm_constituent_client"
if not len(sys.argv) == 2:
    print("Usage: python fix_lines.py <directory>")
    sys.exit(1)

input_path = sys.argv[1]
fix_long_lines(input_path)
