# mccleod1290.github.io

**Site:** https://mccleod1290.github.io/

Static site on the root of `main`. Deployed with **GitHub Actions** (`.github/workflows/pages.yml`).

## HackSmarter layout

```
hack-smarter-labs/
  windows/   # Slayer Edge Evasive Staged Kiosk Sideloaded
  web/       # Hunter Polution Verbose Implicit Embedded Health Smarter
  linux/     # placeholder
  ad/        # placeholder
```

Old flat paths redirect to the new folders.

## Pages settings (if site is 404 / stale)

1. https://github.com/mccleod1290/mccleod1290.github.io/settings/pages
2. **Source:** **GitHub Actions**
3. Hard-refresh: https://mccleod1290.github.io/

## Permissions (local)

```bash
find . -path ./.git -prune -o -type d -exec chmod 755 {} +
find . -path ./.git -prune -o -type f -exec chmod 644 {} +
```

## Local preview

```bash
python3 -m http.server 8765
```
