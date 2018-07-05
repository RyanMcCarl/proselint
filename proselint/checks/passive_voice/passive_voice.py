# -*- coding: utf-8 -*-
"""Check for constructions that may signal passive voice.
# Resources:
# https://writingcenter.unc.edu/tips-and-tools/passive-voice/
# https://owl.english.purdue.edu/owl/owlprint/539/

---
layout:     post
source:     Purdue OWL
source_url: https://owl.english.purdue.edu/owl/owlprint/539/
title:      Passive voice
date:       2018-06-12 21:35:00
categories: writing
---

Check for constructions that may signal passive voice.

"""
import re
from proselint.tools import preferred_forms_check, existence_check, memoize


@memoize
def check(text):
    """Check for constructions that may signal passive voice."""
    err = "passive_voice.passive_voice"
    msg = u"Check this sentence for passive voice; " +\
        "active voice is usually better."
    regex = r"(\b(?:be|am|is|are|was|were|have|has|had|get)" +\
    r"\b[\w\s]{,15}?(?:d|(?<!whe)n|ne|left|being|made)\b(?: by\b)?)"

    return existence_check(text, [regex], err, msg,
                           require_padding=False, offset=0)
