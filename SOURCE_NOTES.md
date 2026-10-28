# Source notes — 27 October 2026

The redesign starts from commit `f8478eb` of https://github.com/littlehousezh/littlehousezh.github.io.

## Preserved material

- All 13 papers on the original homepage, including the accepted ICSE 2027 paper; the older `/publications/` page contained a subset.
- The actual displayed portrait was `img/profile.png`: `img/avatar.jpg` was missing and the old site fell back to this file. The redesign directly uses the existing working image.
- CV, original PDF files (`pub1`, `pub2`, `pub3`, `pub5`), favicon, education, profile links, and research description.
- All original teaching terms. The existing CV also documents CS3892/5892, Fall 2026, which is included.
- Supplied news text and order within each year. No unsupported dates have been assigned to undated entries.

## Publication links

| Paper/file | Source |
| --- | --- |
| pub1 | Existing PDF, DOI `10.1145/3611643.3616250` |
| pub2 | Existing PDF, DOI `10.1145/3686990` |
| pub3 | Existing PDF, DOI `10.1145/3696630.3727244` |
| pub4 | Restored from https://zyueek.github.io/pdf/ASE_nier__ACTR%20%284%29.pdf |
| pub5 | Existing PDF, DOI `10.1145/3788046` |
| pub6 | Google Scholar: https://ieeexplore.ieee.org/iel8/32/11440029/11329486.pdf ; DOI `10.1109/TSE.2026.3651615`, also confirmed by Vanderbilt’s VALIANT publication page |
| pub7 | Official EASE program: https://conf.researchr.org/details/ease-2026/ease-2026-research-papers/25/Locating-Software-Vulnerabilities-With-Static-Analyzers-How-Far-Are-We- |
| pub8 | Coauthor page and Google Scholar, DOI `10.1145/3808150` |
| pub9 | Crossref title record and Google Scholar, DOI `10.1145/3815582` |
| pub10 | Google Scholar links to the ACM publication and PDF, DOI `10.1145/3832783.3834377` |
| pub11 | Coauthor Yuhang Zhao’s publication page, Crossref, and Google Scholar, DOI `10.1145/3832783.3834414` |
| pub12 | Coauthor page and Google Scholar, DOI `10.1145/3803437.3806703` |
| pub13 | Restored from https://zyueek.github.io/pdf/Unclaimed_Territory.pdf |

The profile https://scholar.google.com/citations?user=s82MO1wAAAAJ&hl=en was inspected in the browser. Its individual article records provide the exact ACM `/doi/pdf/` URLs for pub8, pub9, pub10, pub11, and pub12 and the IEEE PDF URL for pub6. These external PDF links are used rather than the old missing local files. No PDF URL was invented. The EASE paper does not appear in the inspected Scholar profile and has no verified PDF, so only Link is shown.

The coauthor page listed an EASE DOI `10.1145/3816483.3816508` that returned 404. The redesign uses the working official conference page instead.

## Verification limits

The 6 publisher-hosted PDFs listed by Scholar could not be independently downloaded: ACM returned HTTP 403 and IEEE returned HTTP 418 to automated requests. Their exact URLs and associated titles were confirmed on Scholar; direct PDF delivery remains unverified. Several DOI landing pages likewise returned 403, and a batch Crossref verification encountered 429 rate limits. These are documented limits rather than successful endpoint checks.

The two restored coauthor PDFs pass PDF-signature checks; original local PDF/CV paths remain intact. No custom domain or deployment settings were changed.

## News and typography refinements — October 27, 2026

The user supplied the June 2026 EASE attendance announcement and confirmed support for the inaugural HumanAISE workshop at FSE 2025. The [official 2025 contributor index](https://conf.researchr.org/people-index/humanaise-2025) provides no named contributors or committee roles. The [2025 workshop listing](https://conf.researchr.org/home/fse-2025/humanaise-2025) redirects to the workshop homepage, which currently describes the 2026 edition. No specific 2025 role could be verified, so the announcement uses the user's wording “helped support” without adding an official designation. At the user’s final request, FSE attendance and workshop support are separate June 2025 announcements, the workshop name links to its homepage in a new tab, and the original second sentence has been removed.

The new June announcement appears between the October and April dated updates, adjacent to the existing EASE publication news. Undated announcements retain their existing relative order. Eight of the twenty entries have one emoji each; no other news wording was changed.
