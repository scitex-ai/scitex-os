# scitex-os

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Host check + safe file move helpers — minimal deps.</b></p>

<p align="center">
  <a href="https://scitex-os.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-os[all]</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-os/"><img src="https://img.shields.io/pypi/v/scitex-os?label=pypi" alt="pypi"></a>
  <a href="https://pypi.org/project/scitex-os/"><img src="https://img.shields.io/pypi/pyversions/scitex-os?label=python" alt="python"></a>
  <a href="https://github.com/scitex-ai/scitex-os/actions/workflows/rtd-sphinx-build-on-ubuntu-latest.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-os/rtd-sphinx-build-on-ubuntu-latest.yml?branch=develop&label=docs" alt="docs"></a>
  <a href="https://scitex-os.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/scitex-os?label=docs" alt="docs-rtd"></a>
</p>
<p align="center">
  <a href="https://github.com/scitex-ai/scitex-os/actions/workflows/pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-os/pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml?branch=develop&label=tests" alt="tests"></a>
  <a href="https://github.com/scitex-ai/scitex-os/actions/workflows/import-smoke-on-ubuntu-py3-12.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-os/import-smoke-on-ubuntu-py3-12.yml?branch=develop&label=install-check" alt="install-check"></a>
  <a href="https://codecov.io/gh/scitex-ai/scitex-os"><img src="https://img.shields.io/codecov/c/github/scitex-ai/scitex-os/develop?label=cov" alt="cov"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Scattered host checks** — every repo hand-rolls `socket.gethostname() == 'X'` with its own style and no consistent failure message | **`scitex_os.check_host` / `is_host` / `verify_host`** -- single canonical helper triple; `check_host` and `is_host` return bool, `verify_host` calls `sys.exit(1)` on mismatch |
| 2 | **Fragile renames** — `os.rename` fails across filesystems with "Invalid cross-device link" | **`scitex_os.mv(src, dst)`** -- atomic when same filesystem, copy+unlink fallback otherwise; auto-creates parent dir |

## Quick Start

```python
import scitex_os as sxos

if sxos.is_host("compute-01"):
    sxos.mv(src, tgt)
```

## Demo

```mermaid
flowchart LR
    A[script.py] -->|is_host| B{hostname<br/>matches?}
    B -- yes --> C[sxos.mv src → tgt<br/>auto mkdir parent]
    B -- no --> D[skip / raise]
```

<p align="center"><sub><b>Figure 1.</b> Demo path. Host match gates the move; mismatch skips or raises before anything runs.</sub></p>

```python
import scitex_os as sxos

if sxos.is_host("compute-01"):
    sxos.mv("results/run.csv", "/shared/runs/2026-05-07/run.csv")
# parent dir is auto-created; cross-filesystem moves are handled.
```

```bash
$ python -c "import scitex_os; print(scitex_os.is_host('laptop'))"
True
```

## Installation

```bash
uv pip install "scitex-os[all]"
```

<details>
<summary><b>Per-module extras</b></summary>

<br>

| Extra | Pulls in |
|---|---|
| `all` | `dev` + `docs` (recommended) |
| `dev` | pytest, pytest-cov, ruff |
| `docs` | Sphinx + RTD theme + myst-parser (docs build only) |

```bash
uv pip install -e ".[dev]"               # editable install for contributors
```

</details>
## Architecture

```mermaid
flowchart LR
    H[keyword] --> C[check_host / is_host]
    C --> B{hostname<br/>matches?}
    B -- yes --> M[mv src to tgt]
    B -- no --> X[verify_host exits 1]
    M --> OK[moved + parent auto-created]
```

<p align="center"><sub><b>Figure 2.</b> Helper flow. Host gating decides whether the move runs; moves auto-create parents and survive cross-filesystem targets.</sub></p>

## 1 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
import scitex_os as sxos

sxos.is_host("hostname")          # bool
sxos.check_host("hostname")       # bool
sxos.verify_host("hostname")      # sys.exit(1) on mismatch

sxos.mv(src, tgt)                 # shutil.move with mkdir(tgt)
```

</details>

## Status

Standalone fork of `scitex.os`. Minimal deps (scitex-logging for output).
The umbrella package's
`scitex.os` import path is preserved via a `sys.modules`-alias bridge.

## Part of SciTeX

`scitex-os` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[os]` to use as
`scitex.os` (Python) or `scitex os ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
