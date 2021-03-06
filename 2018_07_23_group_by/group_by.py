"""Revised solution to Group By exercise
   - Make use of setdefault() method of dict

07/27/2018
"""


def group_by(iterable, key_func=lambda x: x):
    """Given an iterable, return a dict-like object
    where elements in the iterable are grouped
    according to their value when passed to key_func

    - When no key_func is passed, key_func is identity
    """
    groups = {}
    for item in iterable:
        groups.setdefault(key_func(item), []).append(item)
    return groups
