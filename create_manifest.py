import io
import os
import json


if __name__ == "__main__":
    HOME = os.path.dirname(__file__)
    directory = r"wordlists/"

    dirname = os.path.join(HOME, directory)

    files = [
        os.path.join(dp, f)
        for dp, dn, filenames in os.walk(dirname)
        for f in filenames
        if os.path.splitext(f)[1].lower() == ".txt"
    ]
    print("Found {} files".format(len(files)))

    out = io.open(os.path.join(HOME, "manifest.json"), "w+", encoding="utf8")

    files = sorted(
        [
            f.replace(HOME, "").replace("\\", "/").replace("/wordlists/", "")
            for f in files
        ]
    )

    out.write(json.dumps(files, ensure_ascii=False, indent=4))
    out.close()
