# -*- coding: utf-8 -*-
"""Brian Garner recommended substitutions from various sources.

Resources:
Garner, Modern American Usage
Garner, Modern Legal Usage
Garner, Lawprose Blog
http://www.lawprose.org/lawprose-blog/
https://abajournal.com/magazine/article/ax_these_terms_from_your_legal_writing/

---
layout:     post
source:     Various Brian Garner sources
source_url: http://www.lawprose.org/lawprose-blog/
title:      Brian Garner - Preferred Forms
date:       2018-11-19 13:35:00
categories: writing
---

"""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "garner.substitutions"
    msg = "Consider '{}' instead."

    preferences = [
        # From https://abajournal.com/magazine/article/ax_these_terms_from_your_legal_writing/
        ["or", ["and/or"]],
        ["delete it or substitute 'are' or 'mean'", ["deem"]],
        ["'if,' 'however,' or 'also'", ["provided that"]],
        ["Insert period and then start a new sentence with 'But.'", ["provided, however, that"]],
        ["in this agreement", ["herein"]],
        ["it", ["the same"]],
        ["the agreement", ["said agreement"]],
        ["'must,' 'should,' 'is,' 'will,' or 'may'", ["shall"]],
        ["Subsection beginning 'Recitals:' or 'Background:'", ["Whereas"]],
        ["'under X' or 'X requires'", ["pursuant to"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
