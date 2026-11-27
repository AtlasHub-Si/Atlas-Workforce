"""Offline smoke checks; no external requests or user data."""
import ast
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1] / "skills"
scripts = sorted(SKILLS.glob("*/*.py"))
assert len(scripts) == 6, scripts
assert len(list(SKILLS.glob("*/SKILL.md"))) == 11
for path in scripts:
    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
assert len(json.loads((SKILLS / "yt-script/hooks.json").read_text(encoding="utf-8"))["hooks"]) == 21

def run(relative, *args):
    result = subprocess.run([sys.executable, str(SKILLS / relative), *map(str, args)],
                            capture_output=True, text=True, timeout=15, check=True,
                            encoding="utf-8")
    assert result.stdout.strip(), relative
    print("PASS", relative)

with tempfile.TemporaryDirectory() as directory:
    tmp = Path(directory)
    run("yt-script/hookscore.py", "--hook", "I tested five tools so you don't have to")
    run("yt-package/title.py", "--title", "I tested five tools", "--thumb", "ONE WINNER")
    sample = tmp / "videos.json"
    sample.write_text(json.dumps([{"channel":"Example","title":"Test "+str(i),"views":n,
                                  "url":"https://example.invalid/"+str(i),"duration":120}
                                 for i,n in enumerate([100,110,120,1000])]),encoding="utf-8")
    run("yt-viral/swipe.py", sample, "--min", "2.0", "--json")
    srt = tmp / "sample.srt"
    srt.write_text("\n\n".join(f"{i+1}\n00:{i:02d}:00,000 --> 00:{i:02d}:10,000\nSynthetic topic {i}" for i in range(8))+"\n",encoding="utf-8")
    run("yt-edit/deadair.py", srt, "--json")
    run("yt-chapters/chapters.py", srt, "--target", "4")
    csv = tmp / "retention.csv"
    csv.write_text("Elapsed video time (%),Audience retention (%)\n"+"\n".join(f"{i*10},{100-i*5}" for i in range(11)),encoding="utf-8")
    run("yt-retention/retention.py", csv, "--duration", "600")
print("PASS: offline smoke checks")
