import os

JOKE = (
    '"It works on my machine," said my AI coding agent. '
    "Its machine is a sandbox that gets deleted every night \u2014 "
    "along with the bug, the logs, and the only witness."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
