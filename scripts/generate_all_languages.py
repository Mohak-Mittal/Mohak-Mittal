#!/usr/bin/env python3
"""Generate an SVG showing every language detected across a GitHub user's owned repositories."""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import colorsys
import html
from pathlib import Path

USERNAME = os.environ.get("GITHUB_USERNAME", "mohak-mittal")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUTPUT = Path(os.environ.get("LANGUAGE_SVG_OUTPUT", "all_languages.svg"))
API = "https://api.github.com"
PER_PAGE = 100

# Familiar language colors where available; deterministic neon colors for everything else.
KNOWN_COLORS = {
    "C": "#555555", "C++": "#f34b7d", "C#": "#178600", "CSS": "#663399",
    "HTML": "#e34c26", "Java": "#b07219", "JavaScript": "#f1e05a",
    "Jupyter Notebook": "#DA5B0B", "Kotlin": "#A97BFF", "PHP": "#4F5D95",
    "Python": "#3572A5", "Ruby": "#701516", "Rust": "#dea584",
    "Shell": "#89e051", "TypeScript": "#3178c6", "Go": "#00ADD8",
    "Dart": "#00B4AB", "Swift": "#F05138", "R": "#198CE7",
    "PowerShell": "#012456", "Vue": "#41b883", "SCSS": "#c6538c",
}

def api_get(path: str):
    url = API + path
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "all-repository-languages-generator",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    request = urllib.request.Request(url, headers=headers)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 429) and attempt < 3:
                reset = exc.headers.get("X-RateLimit-Reset")
                wait = max(2, min(60, int(reset) - int(time.time()))) if reset else 10 * (attempt + 1)
                print(f"Rate limited; waiting {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"GitHub API request failed: {url}")

def get_repositories():
    repositories = []
    page = 1
    while True:
        batch = api_get(
            f"/users/{urllib.parse.quote(USERNAME)}/repos"
            f"?type=owner&per_page={PER_PAGE}&page={page}&sort=full_name"
        )
        if not batch:
            break
        repositories.extend(batch)
        if len(batch) < PER_PAGE:
            break
        page += 1
    return repositories

def language_color(name: str) -> str:
    if name in KNOWN_COLORS:
        return KNOWN_COLORS[name]
    # Stable color based on the language name, with a saturated neon hue.
    hue = (sum((i + 1) * ord(ch) for i, ch in enumerate(name)) % 360) / 360
    red, green, blue = colorsys.hsv_to_rgb(hue, 0.62, 0.96)
    return "#{:02x}{:02x}{:02x}".format(round(red * 255), round(green * 255), round(blue * 255))

def make_svg(totals, repo_count, scanned_count):
    entries = sorted(totals.items(), key=lambda item: (-item[1], item[0].lower()))
    total_bytes = sum(totals.values())
    width = 1120
    columns = 2
    per_column = (len(entries) + 1) // 2
    row_height = 58
    height = max(220, 160 + per_column * row_height + 34)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#090516"/><stop offset="1" stop-color="#170826"/></linearGradient>',
        '<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#ff4fd8"/></linearGradient></defs>',
        f'<rect width="{width}" height="{height}" rx="18" fill="url(#bg)" stroke="#33204d"/>',
        '<text x="38" y="48" fill="#f4eaff" font-family="Segoe UI,Arial,sans-serif" font-size="25" font-weight="700">ALL REPOSITORY LANGUAGES</text>',
        f'<text x="38" y="78" fill="#b9a6d2" font-family="Segoe UI,Arial,sans-serif" font-size="13">{len(entries)} languages detected  •  {scanned_count} repositories scanned  •  {total_bytes:,} bytes of code</text>',
        f'<rect x="38" y="96" width="{width-76}" height="3" rx="2" fill="url(#accent)"/>',
    ]

    if not entries:
        parts.append('<text x="38" y="150" fill="#d9c8ef" font-family="Segoe UI,Arial,sans-serif" font-size="16">No language data was returned by GitHub for the scanned repositories.</text>')
    else:
        col_width = 520
        for index, (name, byte_count) in enumerate(entries):
            col = index // per_column
            row = index % per_column
            x = 38 + col * 540
            y = 133 + row * row_height
            pct = byte_count / total_bytes * 100 if total_bytes else 0
            color = language_color(name)
            safe_name = html.escape(name)
            label = safe_name if len(name) <= 27 else html.escape(name[:24] + "…")
            parts.extend([
                f'<text x="{x}" y="{y}" fill="#f3eaff" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="600">{label}</text>',
                f'<text x="{x+col_width}" y="{y}" text-anchor="end" fill="#cbb8e4" font-family="Segoe UI,Arial,sans-serif" font-size="13">{pct:.2f}%</text>',
                f'<rect x="{x}" y="{y+10}" width="{col_width}" height="9" rx="5" fill="#30213f"/>',
                f'<rect x="{x}" y="{y+10}" width="{col_width * pct / 100:.2f}" height="9" rx="5" fill="{color}"/>',
            ])
    parts.append('<text x="38" y="{}" fill="#806b9d" font-family="Segoe UI,Arial,sans-serif" font-size="11">Language sizes are aggregated from GitHub Linguist data across owned repositories. Updated automatically by GitHub Actions.</text>'.format(height - 18))
    parts.append("</svg>")
    return "\n".join(parts)

def main():
    print(f"Scanning owned repositories for {USERNAME}...")
    repositories = get_repositories()
    totals = {}
    scanned = 0
    for repo in repositories:
        full_name = repo.get("full_name", "")
        if not full_name:
            continue
        # GitHub's language endpoint reports byte counts per detected language.
        owner, name = full_name.split("/", 1)
        path = f"/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(name)}/languages"
        try:
            languages = api_get(path)
        except Exception as exc:
            print(f"WARNING: Could not scan {full_name}: {exc}", file=sys.stderr)
            continue
        scanned += 1
        for language, byte_count in languages.items():
            totals[language] = totals.get(language, 0) + int(byte_count)
        print(f"Scanned {full_name}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(make_svg(totals, len(repositories), scanned), encoding="utf-8")
    print(f"Generated {OUTPUT} with {len(totals)} detected languages across {scanned} repositories.")

if __name__ == "__main__":
    main()
