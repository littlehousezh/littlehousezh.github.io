# Zihan Fang’s academic website

A single-page, al-folio-inspired website for GitHub Pages. All academic content is rendered into `index.html`; it remains available without JavaScript. JavaScript only enhances the theme toggle, active navigation, and old hash links. No npm packages, CDN assets, or framework runtime are required.

## Update content

Edit the appropriate JSON file in `data/`:

| File | Content |
| --- | --- |
| `profile.json` | Biography, affiliation, portrait, email, CV, social links, education |
| `news.json` | Year groups and news items, newest first |
| `publications.json` | Every publication’s title, venue, year, Link and PDF URLs |
| `awards.json` | Awards, years, and institutions |
| `service.json` | Venues, roles, and service details |
| `teaching.json` | Courses, roles, institutions, and terms |

Then run from the repository root:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

Commit both your data changes and the regenerated `index.html`. A Python 3 standard-library installation is sufficient; no packages need installing. The build is deterministic. `python3 scripts/build.py --check` detects stale generated HTML.

News and biography text support `**bold**`, `*italic*`, and `[label](https://example.com)` links. Raw HTML is escaped. Preserve the requested order within each news year; the build sorts year groups in descending order. News displays in a keyboard-focusable container with a maximum height of 440px on desktop and 400px on phones. A fresh page starts at the top with 2026.

For a new publication, add an object with a unique `id`, `title`, `venue`, and numeric `year`. Set `link` or `pdf` to `null` if unavailable: no empty button is shown. Only Link and PDF actions are rendered. Put local PDFs in `attaches/` and use root-relative paths, e.g. `/attaches/pub14.pdf`. Do not replace working old paths when adding new papers. `missing_pdf_path` and `pdf_source` are maintenance notes only and are not displayed.

To update the CV, replace `attaches/CV.pdf`. To adjust appearance, edit `css/index.css`; to change structure, edit `templates/index.html`, then rebuild. Theme preferences are saved locally in the visitor’s browser; the initial theme follows their system preference. Reduced-motion settings disable animated scrolling.

## Preview and validate

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. Check phone, tablet, desktop, both themes, anchor links, and keyboard scrolling inside News.

Optional external-link audit:

```sh
python3 scripts/validate.py --external --report link-checks.json
```

The audit checks HTML targets and PDF signatures locally. External HTTP 403/418/429 responses mean automated access was blocked, not proof that a paper is unavailable; these require manual review. HTTP 404/410 responses fail the audit. The script prints all outcomes, including timeouts.

## GitHub Pages

The existing repository root remains the publishable site. No deployment workflow, repository setting, domain, or Pages branch has been changed. The checked-in HTML can be served directly with the existing GitHub Pages configuration. There was no tracked `CNAME` or deployment workflow in the original checkout.

Old URLs redirect to the corresponding homepage section:

- `/about/` → `/#about`
- `/publications/` → `/#publications`
- `/Releases/` → `/#teaching`

GitHub Pages also resolves the corresponding extensionless directory URLs. The compatibility documents contain redirects, not duplicate content or unused feature pages. Old capitalized homepage anchors are supported; the old `#News` anchor pointed to Awards and retains that destination.

## Content and attribution

The source site’s biography, profile image, education, academic links, CV, and all 13 publications have been retained. News, awards, and service follow the supplied redesign request. The Fall 2026 teaching assignment and expanded CodeACT-R title are supported by the repository’s CV. No under-review manuscripts were added to the accepted/published list.

The visual inspiration is [al-folio](https://alshedivat.github.io/al-folio/). This implementation uses original HTML, CSS, and JavaScript; no al-folio code, fonts, icons, or assets were copied. The existing portrait and favicon remain the user’s assets. Research PDFs retain their original authorship and licensing notices.

See `SOURCE_NOTES.md` for publication-link provenance and verification limits.
