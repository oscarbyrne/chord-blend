from itertools import product
from functools import partial

import pandas as pd

from .data import CHROMATIC_CARDINALITY
from .models import Key


def get_all_pitch_classes():
    return pd.Series(
        range(CHROMATIC_CARDINALITY)
    )

def get_pitch_classes_from(pitches):
    pitches = pd.Series(pitches)
    return pitches.mod(
        CHROMATIC_CARDINALITY
    )

def get_all_keys():
    return pd.Series(
        Key(tonic, color)
        for tonic, color
        in product(
            get_all_pitch_classes(),
            Key.Color
        )
    )

def get_key_correlation(pitches, key):
    return key.profile.corr(
        get_pitch_classes_from(pitches).value_counts()
    )

def get_keys_from(pitches):
    keys = get_all_keys()
    correlation_to_these = partial(
        get_key_correlation,
        pitches
    )
    corr = keys.apply(correlation_to_these)
    keys = pd.concat(
        [keys, corr],
        keys=['key', 'correlation'],
        axis=1
    )
    return keys.sort_values('correlation')
