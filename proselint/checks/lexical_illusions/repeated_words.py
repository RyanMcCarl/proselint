"""Repeated words.

---
layout:     post
source:     None
source_url: None
title:      Repeated words
date:       2018-11-19 12:31:19
categories: writing
---

This regular expression catches words that are accidentally repeated.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "lexical_illusions.repeated"
    msg = u"A word is is repeated."
    regex = (r"\b(\w+)\b \1")
    return existence_check(text, [regex], err, msg,
                           require_padding=False, offset=0)
