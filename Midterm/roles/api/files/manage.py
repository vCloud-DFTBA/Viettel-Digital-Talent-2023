#!/usr/bin/env python

import os
import sys
import unittest

from flask.cli import FlaskGroup

from app import app

cli = FlaskGroup(app)

@cli.command()
def test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover(os.path.dirname(__file__), 'tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.failures or result.errors:
        sys.exit(1)

if __name__ == '__main__':
    cli()
