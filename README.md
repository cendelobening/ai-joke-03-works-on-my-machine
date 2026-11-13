# Works On My Machine

An entry for the make.fun **ai-joke-03** competition ("Make the AI judge laugh").

The program writes one joke about AI coding agents to `entry.txt`:

> "It works on my machine," said my AI coding agent. Its machine is a sandbox that gets deleted every night — along with the bug, the logs, and the only witness.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

If `MAKEFUN_OUTPUT_DIR` is unset, output goes to `/output/entry.txt`.
Python 3.13, standard library only, no arguments or stdin. Output is
deterministic: repeated runs produce byte-identical files.
