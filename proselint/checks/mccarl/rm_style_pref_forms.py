# -*- coding: utf-8 -*-
"""Style checks for the existence of certain words.

---
layout:     post
source:     Ryan McCarl
source_url: http://ryanmccarl.com
title:      McCarl StyleChecks - Preferred Forms
date:       2019-03-12
categories: style, usage
---

Points out preferred form.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "mccarl.stylecheck"
    msg = "Consider '{}' instead."

    list = [
        ["(a waste of )?the Court's time( and resources)?", ["judicial resources"]],
        ["(agents|employees) (and|or) (agents|employees)", ["agents"]],
        ["\s\s+", ["using single space"]],
        ["CITE", ["the actual citation"]],
        ["each also", ["each"]],
        ["executed", ["signed"]],
        ["fail(ed|s|ing)? to", ["did not / does not"]],
        ["inter alia", ["among others"]],
        ["inter alia", ["among others"]],
        ["plain and straightforward", ["straightforward"]],
        ["pretending not to understand", ["deliberately misconstruing"]],
        ["prior to", ["before"]],
        ["reach agreement", ["agree"]],
        ["utilize", ["use"]],
    ]

    return preferred_forms_check(text, list, err, msg)
