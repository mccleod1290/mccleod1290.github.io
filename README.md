# mccleod1290.github.io

**Site:** https://mccleod1290.github.io/

Static site on the root of `main`. Deployed with **GitHub Actions** (`.github/workflows/pages.yml`).

## Pages settings (if site is 404 / stale)

1. https://github.com/mccleod1290/mccleod1290.github.io/settings/pages  
2. **Source:** **GitHub Actions** (preferred — matches `pages.yml`)  
3. Actions → **Deploy Pages** → ensure latest run is green  
4. Hard-refresh: https://mccleod1290.github.io/ (`Ctrl+Shift+R`)

Do **not** open `blob/main/index.html` on github.com — that is the source browser, not Pages.

See [PAGES-FIX.md](./PAGES-FIX.md) for permissions, Stack Overflow causes, and URL checklist.

## Permissions (local)

```bash
find . -path ./.git -prune -o -type d -exec chmod 755 {} +
find . -path ./.git -prune -o -type f -exec chmod 644 {} +
```

## Content

| Track | Path |
|-------|------|
| HackSmarter · Health Smarter | `hack-smarter-labs/health-smarter/` |
| HackSmarter · Embedded | `hack-smarter-labs/embedded/` |
| HackSmarter · Implicit | `hack-smarter-labs/implicit/` |
| HackSmarter · Verbose | `hack-smarter-labs/verbose/` |
| HackSmarter · Polution | `hack-smarter-labs/polution/` |
| HackSmarter · Hunter | `hack-smarter-labs/hunter/` |
| HackSmarter · Slayer | `hack-smarter-labs/slayer/` |
| Intigriti · July 2026 | `writeup-intigriti-july.html` |
| HTB / THM / other CTF | TBD on home index |

## Local preview

```bash
python3 -m http.server 8765
# http://127.0.0.1:8765/
```
