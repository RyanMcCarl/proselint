# -*- coding: utf-8 -*-
"""Doublets pairs of words meaning the same thing. They are redundant and cliche.

Resources:
Garner, Modern American Usage
Garner, The Redbook: A Manual on Legal Style
https://www.amazon.com/Redbook-Manual-Legal-Style-Coursebook/dp/0314289011

---
layout:     post
source:     Various Brian Garner sources
source_url: https://www.amazon.com/Redbook-Manual-Legal-Style-Coursebook/dp/0314289011
title:      Brian Garner - Doublets
date:       2018-11-19 15:35:00
categories: writing
---

"""

@memoize
def check(text):
    """Check the text."""
    err = "garner.doublets"
    msg = u"'{}' is a doublet or triplet. Choose one."

    doublets = [
        "aid and abet",
        "aid and comfort"
        "each and every",
        "one and only",
    ]

    return existence_check(text, doublets, err, msg, join=True)
