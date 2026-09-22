#!/usr/bin/env python3
"""Tests for scitex_os._check_host.

PA-306: no `monkeypatch`. The single mutation we need is to replace
``socket.gethostname`` with a deterministic stub. We do that with a
save / restore pair (``swap_gethostname`` fixture) that records the
real callable and restores it on teardown.

TQ cleanup: every test follows Arrange / Act / Assert with a single
assertion. Multi-fact tests are split so the failing-line tells you
which contract regressed.
"""

import socket
from typing import Callable

import pytest

from scitex_os._check_host import check_host, is_host, verify_host

# ---------------------------------------------------------------------------
# swap_gethostname fixture (replaces monkeypatch.setattr(socket, ...))
# ---------------------------------------------------------------------------


@pytest.fixture
def swap_gethostname():
    """Yield a setter that swaps ``socket.gethostname`` and auto-restores."""
    saved: list[Callable[[], str]] = [socket.gethostname]

    def _set(value: str) -> None:
        socket.gethostname = lambda: value  # type: ignore[assignment]

    try:
        yield _set
    finally:
        socket.gethostname = saved[0]  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# check_host
# ---------------------------------------------------------------------------


class TestCheckHost:
    def test_returns_true_when_keyword_is_substring_of_hostname(self, swap_gethostname):
        # Arrange
        swap_gethostname("ywata-note-win")
        # Act
        result = check_host("ywata")
        # Assert
        assert result is True

    def test_returns_false_when_keyword_absent_from_hostname(self, swap_gethostname):
        # Arrange
        swap_gethostname("ywata-note-win")
        # Act
        result = check_host("nope")
        # Assert
        assert result is False

    def test_is_host_alias_points_to_check_host_function(self):
        # Arrange
        expected = check_host
        # Act
        actual = is_host
        # Assert
        assert actual is expected


# ---------------------------------------------------------------------------
# verify_host
# ---------------------------------------------------------------------------


class TestVerifyHost:
    def test_returns_none_when_hostname_matches_keyword(self, swap_gethostname):
        # Arrange
        swap_gethostname("ywata-note-win")
        # Act
        result = verify_host("ywata")
        # Assert
        assert result is None

    def test_logs_success_line_when_hostname_matches_keyword(
        self, swap_gethostname, capsys
    ):
        # Arrange
        swap_gethostname("ywata-note-win")
        # Act
        verify_host("ywata")
        err = capsys.readouterr().err
        # Assert
        assert "succeeded" in err

    def test_raises_systemexit_when_hostname_does_not_match(self, swap_gethostname):
        # Arrange
        swap_gethostname("ywata-note-win")
        # Act
        ctx = pytest.raises(SystemExit)
        # Assert
        with ctx:
            verify_host("nope")

    def test_systemexit_code_is_one_when_hostname_does_not_match(
        self, swap_gethostname
    ):
        # Arrange
        swap_gethostname("ywata-note-win")
        try:
            verify_host("nope")
        except SystemExit as exc:
            code = exc.code
        else:
            code = None
        # Act
        actual = code
        # Assert
        assert actual == 1

    def test_logs_failure_line_when_hostname_does_not_match(
        self, swap_gethostname, capsys
    ):
        # Arrange
        swap_gethostname("ywata-note-win")
        try:
            verify_host("nope")
        except SystemExit:
            pass
        # Act
        err = capsys.readouterr().err
        # Assert
        assert "failed" in err
