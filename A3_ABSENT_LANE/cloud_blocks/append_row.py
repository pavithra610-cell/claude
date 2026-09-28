import csv, sys, json, os

OUT = "/home/user/claude/A3_ABSENT_LANE/cloud_blocks/EMAMI_STATUS_BACKFILL_P1.csv"
HEADER = ["ABSENT_CIN","ABSENT_NAME","STATUS_2026","SOURCE_URL","QUOTE","DESIGNATED_PARTNERS","EMAMI_LINKED_PARTNER","NOTE"]

def init():
    if not os.path.exists(OUT):
        with open(OUT, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(HEADER)

if __name__ == "__main__":
    init()
    data = json.load(sys.stdin)
    row = [data.get(k, "") for k in HEADER]
    with open(OUT, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow(row)
    print("appended", row[0])
