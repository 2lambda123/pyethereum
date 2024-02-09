# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# pyethereum is free software: you can redistribute it and/or modify it
# under the terms of the The MIT License


"""Utilities used by more than one test."""


import json
import os
import tempfile
from ethereum.db import DB as DB
from ethereum.config import Env
__TESTDATADIR = "../tests"

tempdir = tempfile.mkstemp()


def load_test_data(fname):
    """Loads test data from a specified file.
    Parameters:
        - fname (str): Name of the file to load test data from.
    Returns:
        - dict: A dictionary containing the loaded test data.
    Processing Logic:
        - Loads test data from a file.
        - Uses json.loads() to parse the data.
        - Uses os.path.join() to create the file path.
        - Returns the loaded test data."""
    
    return json.loads(open(os.path.join(__TESTDATADIR, fname)).read())


def new_db():
    """Creates a new database object.
    Parameters:
        - None
    Returns:
        - DB: A new database object.
    Processing Logic:
        - Creates a new database object.
        - No parameters needed.
        - Returns the new database object.
        - Only one line of code needed."""
    
    return DB()


def new_env():
    """"Creates a new environment with a new database and returns it.
    Parameters:
        - None
    Returns:
        - Env: A new environment with a new database.
    Processing Logic:
        - Creates a new database.
        - Initializes a new environment.
        - Returns the new environment.""""
    
    return Env(new_db())
