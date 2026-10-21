# docs: public app policies (GitHub Pages)

Served at https://lmsoftwaresolutions.github.io/docs/. Public repo: only things Play/App Store need to link to. No keys, no internal notes.

- PaperCheck pages stay at the root (`privacy_policy.html`, `delete-account.html`): those URLs are already registered in Play. Do not move them.
- Every other app gets a folder: `<slug>/privacy.html` and `<slug>/delete-account.html`.

## Add an app
1. Copy `_apps/billbridge.json` to `_apps/<slug>.json` and edit it to match what the app really does.
2. `python3 _template/new_app.py <slug>`
3. Add the links to `index.html`, open a PR, merge, then paste the URLs into the Play Console.
Re-run step 2 after editing the JSON; the generated HTML is committed, not built by CI.
