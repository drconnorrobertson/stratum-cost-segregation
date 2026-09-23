#!/usr/bin/env python3
"""Apply the shared accessible navigation, footer, and interaction scripts."""

from pathlib import Path
import re

from stratum_render import SCRIPTS, footer, nav

ROOT = Path(__file__).parent


def page_depth(path: Path) -> int:
    rel = path.relative_to(ROOT)
    return max(0, len(rel.parts) - 1)


def apply() -> int:
    changed = 0
    for path in ROOT.rglob("*.html"):
        text = path.read_text()
        if "<html" not in text.lower():
            continue
        old = text
        depth = page_depth(path)
        text = re.sub(r'<nav class="nav".*?</nav>', nav(depth), text, count=1, flags=re.S)
        text = re.sub(r'<footer class="footer".*?</footer>', footer(depth), text, count=1, flags=re.S)
        text = re.sub(
            r'<script>\s*(?:(?:// Nav scroll effect)|(?:// Navigation behavior)).*?</script>',
            '', text, flags=re.S,
        )
        text = re.sub(
            r'<script>\s*document\.addEventListener\(\'click\'.*?AE Discovery Click.*?</script>',
            '', text, flags=re.S,
        )
        text = text.replace("</body>", SCRIPTS + "\n</body>")
        text = "\n".join(line.rstrip() for line in text.splitlines()) + "\n"
        if text != old:
            path.write_text(text)
            changed += 1
    return changed


if __name__ == "__main__":
    print(f"Applied shared design system to {apply()} pages.")
