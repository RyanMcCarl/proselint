"""Tests for garner.jargon check."""
from __future__ import absolute_import

from proselint.checks.garner import substitutions as chk

from .check import Check


class TestCheck(Check):
    """The test class for passive_voice.passive_voice."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    @property
    def test_smoke(self):
        """Basic smoke test for garner.jargon."""
        assert self.passes("""This sentence contains no jargon.""")
        assert not self.passes("""Herein we agree on the agreement at issue in the above-captioned case, provided, however, that all parties have no objections to same.""")
