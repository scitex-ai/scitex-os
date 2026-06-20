---
description: |
  [TOPIC] First scitex-os call in 30 seconds
  [DETAILS] Gate a script to a specific host with `check_host`; do a cross-filesystem-safe rename with `mv`.
tags: [scitex-os-quick-start]
---

# Quick Start

## Host check

```python
import scitex_os

# Boolean check — returns True if keyword appears in hostname
assert scitex_os.check_host("bm198") is True  # if on "bm198"
assert scitex_os.is_host("bm198") is True      # alias, also bool

# Hard gate — prints + sys.exit(1) on mismatch
scitex_os.verify_host("bm198")
```

## Safe move (atomic same-fs, copy+unlink across devices)

```python
import scitex_os

scitex_os.mv("/tmp/data.csv", "/mnt/results/data.csv")
```

`os.rename` raises `OSError: [Errno 18] Invalid cross-device link` when
src and dst are on different filesystems. `scitex_os.mv` falls back to
`shutil.copy2` + `os.unlink` in that case.

## See also

- [03_python-api.md](03_python-api.md)
