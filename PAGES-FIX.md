# Fix stale https://mccleod1290.github.io/

## Diagnosis (2026-08-06)

| Check | Result |
|-------|--------|
| `main` on GitHub | Has universal index + Slayer (`9af2950`) |
| `raw.githubusercontent.com/.../main/index.html` | **New** content (HackSmarter, tracks) |
| `https://mccleod1290.github.io/` | **Old** content (Intigriti only), `Last-Modified: 2026-07-30` |
| Branch Pages builds after 07-30 | **Cancelled / stuck** |
| Actions workflow `Deploy Pages` | **Failed at deploy-pages** — Pages source not set to Actions |

## One-time fix (you must click this in GitHub UI)

1. Open: https://github.com/mccleod1290/mccleod1290.github.io/settings/pages  
2. Under **Build and deployment → Source**, choose **GitHub Actions**.  
3. Open: https://github.com/mccleod1290/mccleod1290.github.io/actions/workflows/pages.yml  
4. **Run workflow** on `main` (or push any empty commit).  
5. When green, hard-refresh: https://mccleod1290.github.io/ (`Ctrl+Shift+R`).

### Do **not** open

`https://github.com/mccleod1290/mccleod1290.github.io/blob/main/index.html`  

That is the **GitHub file browser**, not the published site. It never “is” the Pages homepage.

## After fix you should see

- Track chips: HackSmarter, Intigriti, HTB/THM/CTF (TBD)
- **Slayer** card + Intigriti card  
- https://mccleod1290.github.io/hack-smarter-labs/slayer/ (currently 404 on live CDN)

## Local preview (works now)

```bash
cd ~/mccleod1290.github.io
python3 -m http.server 8765
# open http://127.0.0.1:8765/
```
