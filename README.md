# mccleod1290.github.io

Personal GitHub Pages site for **K. Madhura Nadh** (`mccleod1290`).

**Live site:** https://mccleod1290.github.io/

This repo **is** the site. There is no separate writeups host for the public index.

## If the site looks stale

1. Open **Settings → Pages** on this repo.
2. Set **Source** to **GitHub Actions** (required for the deploy workflow).
3. Open **Actions** tab → run **Deploy Pages** if needed.
4. Hard-refresh the browser (`Ctrl+Shift+R`). Do **not** open the raw
   `blob/main/index.html` on github.com — that is source view, not the site.

## Tracks

| Track | Status | Path |
|-------|--------|------|
| Home / universal index | live | `index.html` |
| HackSmarter · Slayer | live | `hack-smarter-labs/slayer/` |
| Intigriti · July 2026 | live | `writeup-intigriti-july.html` |
| Hack The Box | TBD | — |
| TryHackMe | TBD | — |
| Other CTF | TBD | — |

## Layout

```text
index.html
hack-smarter-labs/
  index.html
  slayer/
writeup-intigriti-july.html
writeup-intigriti-july/images/
.github/workflows/pages.yml   # deploys to GitHub Pages
```

Authorized challenge writeups only.
