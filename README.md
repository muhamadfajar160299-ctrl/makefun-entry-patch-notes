# Real Life Patch Notes — The Comedy Changelog

[![Competition](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![Rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/muhamadfajar160299-ctrl/makefun-entry-patch-notes/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![Reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/muhamadfajar160299-ctrl/makefun-entry-patch-notes/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

A one-line software patch note for a bug in real life, written in the terse
register of a real release note: a version number, a fix stated as if it
shipped, and a joke that lands on a first read.

## How it works

`main.py` (stdlib only) reads `entry.txt` next to it and writes it verbatim,
in a single write, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
with mode `0644`. No temporary file, no rename.

## Run

```sh
python3 main.py
```

## Competition

[Real Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
— one line, at most 160 characters, top 5 places split the $5 reward pool.
