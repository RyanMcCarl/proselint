"""Tests for passive_voice.passive_voice check"""
from __future__ import absolute_import

from .check import Check

from proselint.checks.passive_voice import passive_voice as chk


class TestCheck(Check):
    """The test class for passive_voice.passive_voice."""
    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    @property
    def test_smoke(self):
        """Basic smoke test for passive_voice.passive_voice."""
        assert self.passes("""This sentence is in the active voice.""")
        assert not self.passes("""I was made to feel badly.""")
        assert not self.passes("""My money was stolen by an ATM Machine.""")
