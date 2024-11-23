import re
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import List


def wrap_line(line: str, max_length: int, subsequent_indent: str) -> List[str]:
    """Wrap a single line of text, preserving indentation."""
    if len(line) <= max_length:
        return [line]

    # Preserve initial whitespace
    initial_space = re.match(r"^\s*", line).group(0)

    # Handle comment lines
    if line.lstrip().startswith("#"):
        content = line.lstrip()[1:].lstrip()  # Remove # and following space
        wrapped = textwrap.wrap(
            content,
            width=max_length - len(initial_space) - 2,  # Account for "# "
            subsequent_indent=subsequent_indent,
            break_long_words=False,
            break_on_hyphens=False,
        )
        return [f"{initial_space}# {line}" for line in wrapped]

    # Handle normal lines
    wrapped = textwrap.wrap(
        line.lstrip(),
        width=max_length - len(initial_space),
        subsequent_indent=subsequent_indent,
        break_long_words=False,
        break_on_hyphens=False,
    )
    return [f"{initial_space}{line}" for line in wrapped]


def fix_file_content(content: str, max_length: int = 88) -> str:
    """Fix long lines in a file's content."""
    lines = content.splitlines()
    new_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip empty lines
        if not line.strip():
            new_lines.append(line)
            i += 1
            continue

        # Determine indentation for continuation lines
        initial_space = re.match(r"^\s*", line).group(0)
        subsequent_indent = initial_space + "    "

        # Handle comment lines
        if line.lstrip().startswith("#"):
            wrapped_lines = wrap_line(line, max_length, subsequent_indent)
            new_lines.extend(wrapped_lines)
            i += 1
            continue

        # Collect multi-line strings (potential docstrings)
        if '"""' in line or "'''" in line:
            string_lines = []
            string_start = i

            # Find the end of the multi-line string
            while i < len(lines):
                string_lines.append(lines[i])
                if i > string_start and ('"""' in lines[i] or "'''" in lines[i]):
                    break
                i += 1

            # Join the string lines and rewrap them
            string_content = "\n".join(string_lines)
            if len(string_content) > max_length:
                # Use docformatter to format docstrings
                with subprocess.Popen(
                    ["docformatter", "--wrap-summaries", str(max_length), "--wrap-descriptions", str(max_length), "-"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                ) as proc:
                    formatted_content, err = proc.communicate(string_content)
                    if not err:
                        new_lines.extend(formatted_content.splitlines())
                    else:
                        # Fallback to manual wrapping if docformatter fails
                        wrapped = wrap_line(string_content, max_length, subsequent_indent)
                        new_lines.extend(wrapped)
            else:
                new_lines.extend(string_lines)
            i += 1
            continue

        # Handle regular lines
        wrapped_lines = wrap_line(line, max_length, subsequent_indent)
        new_lines.extend(wrapped_lines)
        i += 1

    return "\n".join(new_lines)


def process_directory(directory: str, max_length: int = 88) -> None:
    """Process all Python files in a directory recursively."""

    try:
        subprocess.run(["docformatter", "--help"], capture_output=True)
    except FileNotFoundError:
        print("Mandatory dependency 'docformatter' not found. Please install it using 'pip install docformatter'")
        sys.exit(1)

    dir_path = Path(directory)
    python_files = list(dir_path.rglob("*.py"))

    if not python_files:
        print(f"No Python files found in {directory}")
        return

    print(f"Found {len(python_files)} Python files to process")

    for file_path in python_files:
        try:
            print(f"Processing {file_path}")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Fix the content
            new_content = fix_file_content(content, max_length)

            # Write back only if changes were made
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Fixed long lines in {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")


# input_path = "src/bbsky/crm_constituent_client"
if not len(sys.argv) == 2:
    print("Usage: python docformatter.py <directory>")
    sys.exit(1)

input_path = sys.argv[1]
process_directory(input_path, max_length=110)
