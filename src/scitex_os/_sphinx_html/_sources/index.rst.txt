scitex-os
=============

Host check + safe file move helpers — zero-dep, pure stdlib.

``check_host(keyword)`` returns ``True`` if *keyword* is a substring of the
local hostname; ``is_host`` is an alias; ``verify_host`` prints a success
message or calls ``sys.exit(1)`` on mismatch. ``mv(src, tgt)`` moves a file
or directory, auto-creating the target parent and falling back to copy+unlink
when the source and destination are on different filesystems.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api

API Reference
-------------

.. autosummary::
   :toctree: api
   :recursive:

   scitex_os
