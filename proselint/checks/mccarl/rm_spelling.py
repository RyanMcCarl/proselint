# # -*- coding: utf-8 -*-
# """Uses the pyspellchecker library to check for misspelled words.

# To use, first run `pip install pyspellchecker`.

# ---
# layout:     post
# source:     SublimeLinter-annotations
# source_url: http://bit.ly/16Q7H41
# title:      broken links
# date:       2014-06-10 12:31:19
# categories: writing
# ---

# Check that links are not broken.


# """
# from proselint.tools import memoize
# from future import standard_library
# import sys
# import re
# try:
#     import pyspellchecker
# except ImportError as e:
#     errormsg = 'ERROR: Could not import aspell: {}.\nPlease run pip install aspell-python-py3.'.format(e)
#     print(errormsg, sys.stderr)

# @memoize
# def check(text):
#     """Check the text."""
#     err = "mccarl.rmspellcheck"
#     msg = u"May be spelled incorrectly: '{}'."
#     errors = []
#     try:
#         from spellcheck import SpellChecker
#     except ImportError as e:
#         errormsg = 'ERROR: Could not import aspell: {}.\nPlease run pip install aspell-python-py3.'.format(e)
#         print(errormsg, sys.stderr)
#         return None

#     if SpellChecker:
#         spell = SpellChecker(distance=1)
#         regex = re.compile(r'\b\w+\b')
#         for m in re.finditer(regex, text):
#             word = m.group(0).strip().casefold()
#             words.append(word)

#         misspelled = spell.unknown(words)
#         for words in misspelled:
#             errors.append((m.start(), m.end(), err, msg.format(word), None))
#         return errors

