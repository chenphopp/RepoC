import re
import csv
import sys

def parse_log(logfile, output_csv="warnings.csv"):
    
    pattern = re.compile(r"(.+):(\d+):\s*warning:\s*(.+)")

    with open(logfile, "r", encoding="utf-8") as f, \
         open(output_csv, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["Line", "File", "Message"])

        for raw_line in f:
            match = pattern.match(raw_line.strip())
            if match:
                file, lineno, msg = match.groups()
                writer.writerow([lineno, file, msg])
            else:
                # ignore not standard lines
                continue

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <warnings.log>")
        sys.exit(1)

    parse_log(sys.argv[1])
    print("Parsing complete warnings.csv generated")

