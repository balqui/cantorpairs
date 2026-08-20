'''
Project started: mid Germinal 2023.
This module started: early Fructidor 2026.
Current version: 1.0.
Not pip-installable as of today. 
See README at `https://github.com/balqui/cantorpairs`

Author: Jose L Balcazar, ORCID 0000-0003-4248-4528
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Ancillary functions for PReFScript, the Partial Recursive Functions lab.

Implements a variant of "assert" that is not disabled from the command line.

After each push, the following extra incantation is most likely 
necessary in the local copy of the git repo for `prefscript`:
`git submodule update --remote`
'''

class Failed(Exception): pass

class Ensure:

    class Failed(Exception): pass

    def that(cls, assertion, message):
        if not assertion:
            raise cls.Failed(message)
