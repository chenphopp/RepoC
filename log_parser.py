import re, csv, sys

pattern = re.compile(r"(.+):(\d+):\s*warning:\s*(.+)")

if len(sys.argv) < 2:
    print("Usage: python log_parser.py <warnings.log>")
    sys.exit(1)

with open(sys.argv[1], encoding="utf-8") as f, open("warnings.csv", "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["Line", "File", "Message"])
    for line in f:
        m = pattern.match(line.strip())
        if m: writer.writerow([m.group(2), m.group(1), m.group(3)])

print("Parsing complete: warnings.csv generated")
