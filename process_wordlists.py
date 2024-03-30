import io
import re
import os


def process_fpath(fpath):
    fstream = io.open(fpath, "r", encoding="utf8")
    lines = fstream.read()
    fstream.close()
    lines_out = re.sub(r"^ +| +$|^\n", "", lines, flags=re.MULTILINE)
    lines_out = re.sub(r"\r", "", lines_out, flags=re.MULTILINE)
    lines_out_lower = lines_out.lower()
    out = io.open(fpath, "w+", encoding="utf8")
    out.write(lines_out_lower)
    out.close()


if __name__ == "__main__":
    HOME = os.path.dirname(__file__)
    for item in os.walk(os.path.join(HOME, "wordlists/")):
        if len(item[-1]):
            for filename in item[-1]:
                fpath = os.path.join(item[0], filename)
                if os.path.isfile(fpath):
                    print(f"processing {fpath}")
                    process_fpath(fpath)
