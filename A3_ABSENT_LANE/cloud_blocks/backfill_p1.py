import csv, sys, os

OUT = "/home/user/claude/A3_ABSENT_LANE/cloud_blocks/EMAMI_STATUS_BACKFILL_P1.csv"
HEADER = ["ABSENT_CIN","ABSENT_NAME","STATUS_2026","SOURCE_URL","QUOTE","DESIGNATED_PARTNERS","EMAMI_LINKED_PARTNER","NOTE"]

def init():
    if not os.path.exists(OUT):
        with open(OUT, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(HEADER)

def append_row(row):
    init()
    with open(OUT, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow(row)

if __name__ == "__main__":
    init()
    print("initialized", OUT)
