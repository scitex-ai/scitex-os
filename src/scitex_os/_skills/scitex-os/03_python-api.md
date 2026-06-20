---
description: |
  [TOPIC] Public Python API of scitex-os
  [DETAILS] Host-check trio (`check_host`, `is_host`, `verify_host`) and the path-aware safe `mv`.
tags: [scitex-os-python-api]
---

# Python API

```python
import scitex_os
```

## `check_host(keyword: str) -> bool`

Returns ``True`` when *keyword* is a substring of ``socket.gethostname()``.

```python
if scitex_os.check_host("bm198"):
    ...
```

## `is_host(keyword: str) -> bool`

Alias for ``check_host``.

```python
if scitex_os.is_host("bm198"):
    ...
```

## `verify_host(keyword: str) -> None`

Prints a success message when *keyword* matches the current hostname;
otherwise prints a failure message and calls ``sys.exit(1)``. Meant for
scripts that should hard-stop on the wrong host.

```python
scitex_os.verify_host("bm198")  # hard exit on mismatch
```

## `mv(src, tgt)`

Path-aware safe move. Atomic `os.rename` when src and tgt are on the
same filesystem; falls back to `shutil.copy2` + `os.unlink` across
devices to avoid `OSError: [Errno 18] Invalid cross-device link`.

```python
scitex_os.mv("/tmp/data.csv", "/mnt/results/data.csv")
```

Accepts `str` or `pathlib.Path` for both arguments. The parent of *tgt* is
auto-created via ``os.makedirs``.

## See also

- [01_installation.md](01_installation.md)
- [02_quick-start.md](02_quick-start.md)
