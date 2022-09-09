'''
Utility methods
'''

import json
import pandas as pd
import numpy as np


def load_input_args(file):
    '''
    Read json input file
    Args:
        file (string): json file
    '''
    try:
        input_args = json.loads(open(file).read())
    except Exception as ex:
        print(file, 'does not exist!')
        print(ex)

    return input_args