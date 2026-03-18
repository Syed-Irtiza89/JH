import os
import re
import sys
from glob import glob


def is_external(url: str) -> bool:
    return url.startswith(
        (
            "http://",
            "https://",
            "mailto:",
            "tel:",
            "data:",
            "javascript:",
            "#",
            "/cdn-cgi/",
        )
    )


def strip_fragment_query(url: str) -> str:
    url = url.split("#", 1)[0]
    url = url.split("?", 1)[0]
    return url


def main() -> int:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_files = [os.path.join(root, "index.html")] + sorted(glob(os.path.join(root, "services", "*.html")))

    pat = re.compile(r'\b(?:href|src)\s*=\s*"([^"]+)"')
    missing: list[tuple[str, str, str]] = []

    for html_path in html_files:
        with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        for raw_url in pat.findall(text):
            url = raw_url.strip()
            if not url or is_external(url):
                continue
            # Avoid false positives from JS string concatenations like: src="' + img.src + '"
            if "' +" in url or "+ '" in url or '"+' in url:
                continue

            url2 = strip_fragment_query(url)
            if not url2:
                continue

            resolved = os.path.normpath(os.path.join(os.path.dirname(html_path), url2))
            if not os.path.exists(resolved):
                missing.append(
                    (
                        os.path.relpath(html_path, root),
                        url,
                        os.path.relpath(resolved, root),
                    )
                )

    print(f"Checked {len(html_files)} HTML files")
    print(f"Missing refs: {len(missing)}")
    for file_rel, url, resolved_rel in missing:
        print(f"- {file_rel}: {url} -> {resolved_rel}")

    return 0 if not missing else 2


if __name__ == "__main__":
    raise SystemExit(main())

