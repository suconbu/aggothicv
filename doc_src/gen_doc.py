import io
import sys
import json
import argparse
from jinja2 import Template

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("template")
    args = ap.parse_args()

    with open(args.json, encoding="utf_8") as f:
        fontinfo = json.load(f)

    with open(args.template, encoding="utf_8") as f:
        template = Template(f.read())

    html = template.render(fontinfo)

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf_8")
    print(html)

if __name__ == "__main__":
    main()
