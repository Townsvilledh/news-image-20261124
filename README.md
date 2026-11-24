# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Townsvilledh/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Townsvilledh/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world's news of Tuesday 24 November 2026, drawn as a broadsheet front page: NATO's alarm over reports of a Russian nuclear-armed satellite as the lead, with the Gaza strike that killed Hamas's security chief, the Zaporizhzhia apartment attack, the break-in at Prince William's Norfolk home, and the GTA VI hacker's sentence in the panels below.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` checks the bundled `entry.png` against the contest gate (PNG signature, at most 1 MiB, at most 1024x1024) and copies it to `/output/entry.png`. The picture itself is drawn in code: `python3 generate.py` redraws `entry.png` from scratch with PIL, laying out the masthead, the lead story and the four panels from the day's reported headlines, and its output is byte-for-byte the committed `entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q8hf8h8d&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
