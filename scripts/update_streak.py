"""
Updates the streak section in README.md from this repo's own commit history.
Runs in GitHub Actions on every push and once a day.

- A "streak day" is any day (Pakistan time) with at least one commit by me.
- Bot commits (the ones this script makes) are ignored.
- "Days done" counts the ticked days (- [x] **Day ...) in the README.
"""
import datetime as dt
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

README = Path("README.md")
START = dt.date(2026, 11, 1)          # Day 1 of the roadmap
TOTAL_DAYS = 162
PKT = dt.timezone(dt.timedelta(hours=5))
BEGIN, END = "<!-- STREAK:START -->", "<!-- STREAK:END -->"


def commit_days() -> set:
    out = subprocess.run(
        ["git", "log", "--format=%an|%aI"], capture_output=True, text=True, check=True
    ).stdout
    days = set()
    for line in out.splitlines():
        author, stamp = line.split("|", 1)
        if "[bot]" in author:
            continue
        days.add(dt.datetime.fromisoformat(stamp).astimezone(PKT).date())
    return days


def streaks(days: set, today: dt.date):
    # current streak: count back from today (or from yesterday if today has no commit yet)
    day = today if today in days else today - dt.timedelta(days=1)
    current = 0
    while day in days:
        current += 1
        day -= dt.timedelta(days=1)

    best = run = 0
    prev = None
    for d in sorted(days):
        run = run + 1 if prev and (d - prev).days == 1 else 1
        best = max(best, run)
        prev = d
    return current, best


def badge(label: str, value: str, color: str) -> str:
    return (f"![{label}](https://img.shields.io/badge/{quote(label)}-"
            f"{quote(value, safe='').replace('-', '--')}-{color}?style=for-the-badge)")


def calendar(days: set, today: dt.date) -> list:
    rows = ["| Week of | Mon | Tue | Wed | Thu | Fri | Sat | Sun |",
            "|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|"]
    monday = START - dt.timedelta(days=START.weekday())
    while monday <= today:
        cells = []
        for i in range(7):
            d = monday + dt.timedelta(days=i)
            if d < START or d > today:
                cells.append(" " if d < START else "⬜")
            elif d in days:
                cells.append("🟩")
            elif d == today:
                cells.append("⬜")
            else:
                cells.append("🟥")
        rows.append(f"| {monday.strftime('%b %-d')} | " + " | ".join(cells) + " |")
        monday += dt.timedelta(days=7)
    return rows


def main():
    text = README.read_text(encoding="utf-8")
    today = dt.datetime.now(PKT).date()
    days = {d for d in commit_days() if d >= START}
    current, best = streaks(days, today)
    done = len(re.findall(r"- \[x\] \*\*Day \d+", text))
    filled = round(done / TOTAL_DAYS * 30)

    block = [
        BEGIN,
        '<div align="center">',
        "",
        " ".join([
            badge("🔥 Current streak", f"{current} days", "FF6B35"),
            badge("🏆 Best streak", f"{best} days", "F7B32B"),
            badge("📅 Days done", f"{done} / {TOTAL_DAYS}", "3B82F6"),
        ]),
        "",
        f"**{done} / {TOTAL_DAYS} days** · {done * 100 // TOTAL_DAYS}% complete",
        "",
        "`" + "█" * filled + "░" * (30 - filled) + "`",
        "",
        *calendar(days, today),
        "",
        "<sub>🟩 pushed · ⬜ not yet · 🟥 missed · updates automatically on every push</sub>",
        "",
        "</div>",
        END,
    ]
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        raise SystemExit("Streak markers not found in README.md")
    new = pattern.sub(lambda _: "\n".join(block), text)
    if new != text:
        README.write_text(new, encoding="utf-8")
        print(f"Updated: streak {current}, best {best}, done {done}")
    else:
        print("No change")


if __name__ == "__main__":
    main()
