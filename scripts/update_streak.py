"""
Updates the streak section in README.md from my roadmap progress.
Runs in GitHub Actions on every push and once a day.

- Day N of the roadmap is planned for Nov 1 + (N - 1) days.
- A day counts as completed when it is ticked in the README: - [x] **Day N**
- Current streak = completed days in a row, counting back from the latest planned day.
- 🟥 = a planned day that has passed but isn't ticked yet.
"""
import datetime as dt
import re
from pathlib import Path
from urllib.parse import quote

README = Path("README.md")
START = dt.date(2026, 11, 1)          # Day 1 of the roadmap
TOTAL_DAYS = 162
PKT = dt.timezone(dt.timedelta(hours=5))
BEGIN, END = "<!-- STREAK:START -->", "<!-- STREAK:END -->"


def completed_days(text: str) -> set:
    """Dates of the roadmap days that are ticked in the README."""
    numbers = {int(n) for n in re.findall(r"- \[x\] \*\*Day (\d+)\*\*", text)}
    return {START + dt.timedelta(days=n - 1) for n in numbers}


def streaks(days: set, today: dt.date):
    # current streak: count back from today (or yesterday if today isn't done yet)
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
            if d < START:
                cells.append(" ")
            elif d in days:
                cells.append("🟩")
            elif d >= today:
                cells.append("⬜")
            else:
                cells.append("🟥")
        rows.append(f"| {monday.strftime('%b %-d')} | " + " | ".join(cells) + " |")
        monday += dt.timedelta(days=7)
    return rows


def main():
    text = README.read_text(encoding="utf-8")
    today = dt.datetime.now(PKT).date()
    days = completed_days(text)
    current, best = streaks(days, today)
    done = len(days)
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
        "<sub>🟩 day's topic completed · ⬜ upcoming · 🟥 behind schedule · updates automatically</sub>",
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
