# Fix 404 / stale site on https://mccleod1290.github.io/

## Live check (2026-08-07)

All published paths return **HTTP 200** from the CDN (not local-only):

| URL | Status |
|-----|--------|
| `/` (`index.html`) | 200 |
| `/hack-smarter-labs/` | 200 |
| `/hack-smarter-labs/health-smarter/` | 200 |
| `/hack-smarter-labs/embedded/` | 200 |
| `/hack-smarter-labs/implicit/` | 200 |
| `/hack-smarter-labs/verbose/` | 200 |
| `/hack-smarter-labs/polution/` | 200 |
| `/hack-smarter-labs/hunter/` | 200 |
| `/hack-smarter-labs/slayer/` | 200 |
| Image files under `*/images/*.png` | 200 |

**Normal 404s (not bugs):**

| Path | Why |
|------|-----|
| `/hack-smarter-labs/*/images/` (directory only) | GitHub Pages has **no directory listing** |
| `/favicon.ico`, `/robots.txt` | Not shipped yet |
| `github.com/.../blob/main/index.html` | **Source browser**, not the live site |

## Correct directory / file permissions (static site)

GitHub Pages serves blobs from git; local perms still matter for local preview and for some CI rsync paths:

```bash
cd ~/mccleod1290.github.io
# directories: rwxr-xr-x  (owner walk + world list/execute)
find . -path ./.git -prune -o -type d -exec chmod 755 {} +
# files: rw-r--r--  (world readable)
find . -path ./.git -prune -o -type f -exec chmod 644 {} +
# keep root entry points explicit
chmod 644 index.html .nojekyll
chmod 755 .
```

| Type | Mode | Why |
|------|------|-----|
| Directories | `755` | Apache/nginx/Pages need execute-on-dir to traverse |
| HTML/CSS/JS/images | `644` | World-readable static content |
| Never | `600` / missing o+r | Would 403/404 if a server used FS perms |
| Never | git `100755` on HTML | Unnecessary; use normal files |

Also keep **`.nojekyll`** at repo root (and under `_site/` via workflow) so Jekyll does not ignore folders that start with `_` or rewrite paths.

## Stack Overflow / common GitHub Pages 404 causes

1. **Wrong Pages source**  
   [SO: 404 despite successful deployment](https://stackoverflow.com/questions/79242654/github-pages-404-error-despite-successful-deployment)  
   This repo uses **GitHub Actions** (`.github/workflows/pages.yml` → `actions/deploy-pages`).  
   Settings → Pages → **Source: GitHub Actions** (not only “Deploy from a branch”).

2. **`index.html` not at published root**  
   [SO: provide index.html](https://stackoverflow.com/questions/59939993/404-error-provide-index-html-file-with-github-pages)  
   User pages (`username.github.io`) need `index.html` at the **artifact root**. Workflow rsyncs repo root → `_site/` excluding `.git` / `.github`.

3. **Case-sensitive paths**  
   [SO: folder Grammatik vs grammatik](https://stackoverflow.com/questions/67256234/github-pages-is-giving-me-404-instead-of-linking-to-a-different-page)  
   Linux Pages is case-sensitive. Use exact folder names: `health-smarter`, not `Health-Smarter`.

4. **Opening `blob/main/...` on github.com**  
   That is **not** Pages. Live site is only `https://mccleod1290.github.io/...`.

5. **Browser / CDN cache**  
   `Cache-Control: max-age=600` on the edge. Hard refresh: `Ctrl+Shift+R` (or Chrome DevTools → Network → Disable cache).

6. **Trailing slash vs no slash**  
   Prefer directory URLs with trailing slash: `/hack-smarter-labs/hunter/` (serves that folder’s `index.html`).

## One-time fix if the whole site 404s again

1. Open https://github.com/mccleod1290/mccleod1290.github.io/settings/pages  
2. **Build and deployment → Source → GitHub Actions**  
3. Actions → **Deploy Pages** workflow → Run on `main` (or push any commit)  
4. Hard-refresh https://mccleod1290.github.io/

## Local preview

```bash
cd ~/mccleod1290.github.io
python3 -m http.server 8765
# http://127.0.0.1:8765/
# http://127.0.0.1:8765/hack-smarter-labs/health-smarter/
```

## Chrome quick check

```bash
google-chrome --new-window \
  https://mccleod1290.github.io/ \
  https://mccleod1290.github.io/hack-smarter-labs/ \
  https://mccleod1290.github.io/hack-smarter-labs/health-smarter/ \
  https://mccleod1290.github.io/hack-smarter-labs/embedded/ \
  https://mccleod1290.github.io/hack-smarter-labs/implicit/ \
  https://mccleod1290.github.io/hack-smarter-labs/verbose/ \
  https://mccleod1290.github.io/hack-smarter-labs/polution/ \
  https://mccleod1290.github.io/hack-smarter-labs/hunter/ \
  https://mccleod1290.github.io/hack-smarter-labs/slayer/
```
