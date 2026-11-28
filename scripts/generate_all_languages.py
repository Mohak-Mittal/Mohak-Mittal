#!/usr/bin/env python3
"""Generate an SVG chart of all languages across public and private owned repositories."""
import colorsys
import html
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

USERNAME = os.environ.get("GITHUB_USERNAME", "Mohak-Mittal")
TOKEN = os.environ.get("LANGUAGE_SCAN_TOKEN", "").strip()
OUTPUT = Path("all_languages.svg")
API = "https://api.github.com"
PER_PAGE = 100

# Set to True to show "X private repositories included" in the chart subtitle.
SHOW_PRIVATE_COUNT = False
# Set to True to skip forked repositories.
EXCLUDE_FORKS = False

KNOWN_COLORS = {
    "C": "#555555", "C++": "#f34b7d", "C#": "#178600", "CSS": "#663399",
    "HTML": "#e34c26", "Java": "#b07219", "JavaScript": "#f1e05a",
    "Jupyter Notebook": "#DA5B0B", "Kotlin": "#A97BFF", "PHP": "#4F5D95",
    "Python": "#3572A5", "Ruby": "#701516", "Rust": "#dea584",
    "Shell": "#89e051", "TypeScript": "#3178c6", "Go": "#00ADD8",
    "Dart": "#00B4AB", "Swift": "#F05138", "R": "#198CE7",
    "PowerShell": "#012456", "Vue": "#41b883", "SCSS": "#c6538c",
    "Batchfile": "#C1F12E", "Lua": "#000080", "GLSL": "#5686a5",
    "HLSL": "#aace60", "ShaderLab": "#222c37", "Makefile": "#427819",
    "Dockerfile": "#384d54", "Svelte": "#ff3e00", "Astro": "#ff5a03",
}


def api_get(path):
    """GET a GitHub API path with retries for rate limits and transient errors."""
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "all-repository-languages-generator",
    })
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            remaining = exc.headers.get("X-RateLimit-Remaining")
            rate_limited = exc.code == 429 or (exc.code == 403 and remaining == "0")
            if (rate_limited or exc.code >= 500) and attempt < 3:
                reset = exc.headers.get("X-RateLimit-Reset")
                if rate_limited and reset and reset.isdigit():
                    wait = max(2, min(120, int(reset) - int(time.time())))
                else:
                    wait = 5 * (attempt + 1)
                print(f"HTTP {exc.code}; retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                last_error = exc
                continue
            raise RuntimeError(
                f"GitHub API HTTP {exc.code} for {path}. "
                f"Check token permissions/access. Response: {body[:500]}"
            ) from exc
        except urllib.error.URLError as exc:
            last_error = exc
            if attempt < 3:
                wait = 5 * (attempt + 1)
                print(f"Network error ({exc.reason}); retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise RuntimeError(f"Network error for {path}: {exc.reason}") from exc
    raise RuntimeError(f"API request failed after retries: {path} ({last_error})")


def get_owned_repositories():
    repos, page = [], 1
    while True:
        query = urllib.parse.urlencode({
            "visibility": "all",
            "affiliation": "owner",
            "per_page": PER_PAGE,
            "page": page,
            "sort": "full_name",
        })
        batch = api_get("/user/repos?" + query)
        if not isinstance(batch, list):
            raise RuntimeError("Unexpected response while listing repositories.")
        repos.extend(batch)
        print(f"Repository listing page {page}: {len(batch)} repositories")
        if len(batch) < PER_PAGE:
            return repos
        page += 1


def language_color(name):
    if name in KNOWN_COLORS:
        return KNOWN_COLORS[name]
    hue = (sum((i + 1) * ord(ch) for i, ch in enumerate(name)) % 360) / 360
    r, g, b = colorsys.hsv_to_rgb(hue, 0.62, 0.96)
    return "#{:02x}{:02x}{:02x}".format(round(r * 255), round(g * 255), round(b * 255))


def make_svg(totals, repo_count, scanned_count, private_count):
    entries = sorted(totals.items(), key=lambda item: (-item[1], item[0].lower()))
    total_bytes = sum(totals.values()) or 1
    font = "Segoe UI,Helvetica,Arial,sans-serif"
    mono = "Consolas,'Courier New',monospace"

    width, pad = 900, 40
    inner = width - pad * 2
    col_gap, row_h = 40, 52
    col_w = (inner - col_gap) // 2
    rows = max(1, (len(entries) + 1) // 2)
    list_top = 190
    height = list_top + rows * row_h + 56

    subtitle = f"{len(entries)} LANGUAGES  //  {scanned_count}/{repo_count} REPOSITORIES"
    if SHOW_PRIVATE_COUNT:
        subtitle += f"  //  {private_count} PRIVATE"

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<defs>'
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#0a0618"/><stop offset="1" stop-color="#1a0a2e"/></linearGradient>'
        '<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#ff4fd8"/></linearGradient>'
        f'<clipPath id="barclip"><rect x="{pad}" y="118" width="{inner}" height="16" rx="8"/></clipPath>'
        '<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">'
        '<feGaussianBlur stdDeviation="2.5" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        '</defs>',
        f'<rect width="{width}" height="{height}" rx="20" fill="url(#bg)"/>',
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="20" fill="none" stroke="#3a2360"/>',
    ]

    # Corner brackets (match the hero banner style)
    c, m = 22, 14
    for (x1, y1, dx, dy) in [(m, m, 1, 1), (width - m, m, -1, 1), (m, height - m, 1, -1), (width - m, height - m, -1, -1)]:
        p.append(
            f'<path d="M{x1} {y1 + dy * c} L{x1} {y1} L{x1 + dx * c} {y1}" '
            'fill="none" stroke="#8b5cf6" stroke-opacity="0.55" stroke-width="2" stroke-linecap="round"/>'
        )

    # Header
    p += [
        f'<text x="{pad}" y="66" fill="#ffffff" font-family="{font}" font-size="28" font-weight="800" letter-spacing="2">ALL REPOSITORY LANGUAGES</text>',
        f'<text x="{pad}" y="92" fill="#a78bfa" font-family="{mono}" font-size="13" letter-spacing="1.5">{html.escape(subtitle)}</text>',
        f'<rect x="{pad}" y="104" width="64" height="3" rx="2" fill="url(#accent)"/>',
    ]

    # Segmented overview bar
    p.append(f'<rect x="{pad}" y="118" width="{inner}" height="16" rx="8" fill="#241638"/>')
    if entries:
        p.append('<g clip-path="url(#barclip)" filter="url(#glow)">')
        x = float(pad)
        for name, count in entries:
            w = max(inner * count / total_bytes, 2.0)
            p.append(f'<rect x="{x:.2f}" y="118" width="{w:.2f}" height="16" fill="{language_color(name)}"/>')
            x += w
        p.append('</g>')
        # thin separators between segments
        x = float(pad)
        for name, count in entries[:-1]:
            x += max(inner * count / total_bytes, 2.0)
            p.append(f'<rect x="{x - 0.75:.2f}" y="118" width="1.5" height="16" fill="#0a0618"/>')

    # Language list
    if not entries:
        p.append(f'<text x="{pad}" y="{list_top + 20}" fill="#d9c8ef" font-family="{font}" font-size="16">No language data was returned by GitHub.</text>')
    else:
        for i, (name, count) in enumerate(entries):
            col, row = i // rows, i % rows
            x = pad + col * (col_w + col_gap)
            y = list_top + row * row_h
            pct = count / total_bytes * 100
            color = language_color(name)
            label = html.escape(name if len(name) <= 24 else name[:21] + "…")
            fill_w = max(col_w * pct / 100, 3)
            p += [
                f'<circle cx="{x + 6}" cy="{y - 5}" r="5" fill="{color}" filter="url(#glow)"/>',
                f'<text x="{x + 20}" y="{y}" fill="#f5edff" font-family="{font}" font-size="16" font-weight="600">{label}</text>',
                f'<text x="{x + col_w}" y="{y}" text-anchor="end" fill="#d8c7f5" font-family="{mono}" font-size="15" font-weight="700">{pct:.1f}%</text>',
                f'<rect x="{x}" y="{y + 12}" width="{col_w}" height="6" rx="3" fill="#241638"/>',
                f'<rect x="{x}" y="{y + 12}" width="{fill_w:.2f}" height="6" rx="3" fill="{color}"/>',
            ]

    p.append(
        f'<text x="{width - pad}" y="{height - 24}" text-anchor="end" fill="#6d5a8c" font-family="{mono}" '
        'font-size="11" letter-spacing="1">SOURCE: GITHUB LINGUIST  //  AUTO-UPDATED DAILY</text>'
    )
    p.append("</svg>")
    return "\n".join(p)


def main():
    if not TOKEN:
        raise RuntimeError(
            "Missing LANGUAGE_SCAN_TOKEN secret. Add a fine-grained PAT with "
            "Metadata: read access to all repositories owned by this account."
        )

    print(f"Authenticating and scanning repositories owned by {USERNAME}...")
    user = api_get("/user")
    actual = user.get("login", "")
    if actual.lower() != USERNAME.lower():
        raise RuntimeError(
            f"Token belongs to '{actual}', but GITHUB_USERNAME is '{USERNAME}'. "
            "Create the token while signed in to the target account."
        )

    repos = get_owned_repositories()
    if EXCLUDE_FORKS:
        repos = [r for r in repos if not r.get("fork")]
    if not repos:
        raise RuntimeError("GitHub returned zero owned repositories. Check token repository access.")

    totals, scanned, private_count, failed = {}, 0, 0, []
    for repo in repos:
        full = repo.get("full_name", "")
        if not full or "/" not in full:
            continue
        is_private = bool(repo.get("private"))
        private_count += int(is_private)
        owner, name = full.split("/", 1)
        path = f"/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(name)}/languages"
        try:
            languages = api_get(path)
        except Exception as exc:  # keep going; report at the end
            failed.append(full)
            print(f"ERROR scanning {full}: {exc}", file=sys.stderr)
            continue
        scanned += 1
        for language, byte_count in languages.items():
            totals[language] = totals.get(language, 0) + int(byte_count)
        print(f"Scanned {full} ({'private' if is_private else 'public'}): {len(languages)} languages")

    if failed:
        print(f"WARNING: {len(failed)} repositories could not be scanned: {', '.join(failed)}", file=sys.stderr)
    if not scanned:
        raise RuntimeError("No repositories scanned successfully; refusing to publish an empty chart.")

    OUTPUT.write_text(make_svg(totals, len(repos), scanned, private_count), encoding="utf-8")
    print(
        f"SUCCESS: {OUTPUT}; {len(totals)} languages; {scanned}/{len(repos)} repos scanned; "
        f"{private_count} private repos visible to token."
    )


if __name__ == "__main__":
    main()
