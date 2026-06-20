# Changelog

All notable changes to `scitex-os` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.8] - 2026-06-20

- Back-merge `main` into `develop` (release-meta + audit-compliance): adopt
  `scitex-dev` core dependency, the PS-168 secret-exception block, and the
  `GH_PERSONAL_ACCESS_TOKEN` CLA secret.
- Standardize CI/release on the canonical fleet workflow set (scitex-app
  naming): `pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml`,
  `import-smoke-on-ubuntu-py3-12.yml`,
  `scitex-os-quality-audit-on-ubuntu-latest.yml`,
  `pypi-publish-and-github-release-on-tag.yml`,
  `rtd-sphinx-build-on-ubuntu-latest.yml`,
  `newb-docs-quality-on-ubuntu-latest.yml`, `auto-merge-to-develop.yaml`;
  remove the legacy `ci.yml`/`release.yml` and the consolidated
  `pr-ci.yml`/`release-ci.yml`.
- Preserve the codecov gitconfig-race fix (per-job `HOME` +
  `disable_safe_directory: true`) in the pytest matrix.

## [0.1.7] - 2026-05-26

- Fix PS-121 violation: re-track `_sphinx_html/` in-wheel doc bundle
- Fix Sphinx duplicate-object warnings in API docs
- Fix missing `docs/sphinx/_static/` directory for Sphinx build
- Add `_sphinx_html/**` to package-data in pyproject.toml

## [0.1.2]

- Initial CHANGELOG entry — see git log for prior history.
