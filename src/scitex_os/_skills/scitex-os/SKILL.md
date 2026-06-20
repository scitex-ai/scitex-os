---
name: scitex-os
description: |
  [WHAT] Host-check helpers (`check_host`, `is_host`, `verify_host`) and a path-aware safe `mv(src, dst)`.
  [WHEN] Use at the top of host-specific scripts instead of `socket.gethostname() == 'X'` checks; use `mv` for cross-filesystem renames.
  [HOW] `import scitex_os; scitex_os.check_host("bm198")` (bool) or `scitex_os.is_host("bm198")` (bool); `scitex_os.verify_host("bm198")` (sys.exit(1) on mismatch); `scitex_os.mv(src, dst)` (atomic same-fs, copy+unlink across devices).
primary_interface: python
interfaces:
  python: 2
  cli: 0
  mcp: 0
  skills: 2
  hook: 0
  http: 0
canonical-location: scitex-os/src/scitex_os/_skills/scitex-os/SKILL.md
tags: [scitex-os]
---

# scitex-os

Host-check helpers + safe file move. `check_host(name)` returns bool; `is_host(name)` is the boolean alias; `verify_host(...)` calls `sys.exit(1)` on mismatch. `mv(src, dst)` is a path-aware safe rename (atomic when same filesystem, copy+unlink across devices). Drop-in replacement for `socket.gethostname() == 'X'` checks at the top of host-specific scripts.

## Index

- [01_installation.md](01_installation.md) — pip install and verify
- [02_quick-start.md](02_quick-start.md) — host gate + safe move in 30 seconds
- [03_python-api.md](03_python-api.md) — `check_host`, `is_host`, `verify_host`, `mv`
