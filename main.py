import os

TEXT = "WARNING: Do not alter the past. Your grandfather is a load-bearing ancestor."

# Gate self-check: 1-120 chars, not whitespace-only, one line, no leading/trailing space.
assert 1 <= len(TEXT) <= 120, "text outside 1-120 chars"
assert TEXT.strip(), "text is whitespace only"
assert "\n" not in TEXT and "\r" not in TEXT, "text must be one line"
assert TEXT == TEXT.strip(), "text has leading/trailing space"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)

# Post-write verification: prove the bytes on disk are exactly the intended text,
# so a silent write failure or encoding slip fails loudly instead of reaching the judge.
with open(path, "rb") as f:
    raw = f.read()
assert raw.decode("utf-8") == TEXT, "written text differs from intended text"
assert raw == TEXT.encode("utf-8"), "written bytes differ from intended text"
assert len(raw) == len(TEXT.encode("utf-8")), "written byte length differs"
