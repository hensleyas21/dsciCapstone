import pandas as pd

from statistics import mean, median, stdev
from typing import Sequence, Callable, Any, Dict

import os
import sys
scriptdir = os.path.abspath(os.path.dirname(__file__))
if scriptdir not in sys.path: sys.path.append(scriptdir)
from data_inspector import count_categories

def transform_feature(df: pd.DataFrame, col_name: str, action: str, args: list[Any], kwargs: dict[str,Any]):
    """Transforms a single column of the dataframe using the specified modification

    Positional Arguments:
    df       - The dataframe on which an attribute will be transformed (may be modified in place)
    col_name - The name of the column whos values will be changed
    action   - One of the following function names (defined in this file)
                  1. z_score_norm
                  2. min_max_norm
                  3. make_named_bins
                  4. make_mean_bins
                  5. make_median_bins
                  6. make_min_bins
                  7. make_max_bins
    args     - A list of the positional arguments required by the action function
    kwargs   - A dictionary of the keyword arguments required by the action function
    """
    # identify the correct function to call given the specified action
    if action == 'z_score_norm': func = z_score_norm
    elif action == 'min_max_norm': func = min_max_norm
    elif action == 'merge_uncommon': func = merge_uncommon
    elif action == 'make_named_bins': func = make_named_bins
    elif action == 'make_mean_bins': func = make_mean_bins
    elif action == 'make_median_bins': func = make_median_bins
    elif action == 'make_min_bins': func = make_min_bins
    elif action == 'make_max_bins': func = make_max_bins
    else: raise ValueError(f"Unrecognized transformation action: {action}")
    # apply this function to the specified column
    df[col_name] = func(df[col_name], *args, **kwargs) # type: ignore

def z_score_norm(items: Sequence[int|float]) -> Sequence[float]:
    """Translates all values into standard deviations above and below the mean"""
    m = mean(items)
    s = stdev(items)
    return [(item - m) / s for item in items]

def min_max_norm(items: Sequence[int|float]) -> Sequence[float]:
    """Scales all items into the range [0, 1]"""
    minimum = min(items)
    maximum = max(items)
    diff = maximum - minimum
    return [(item - minimum) / diff for item in items]

def merge_uncommon(items: Sequence[str], default: str = 'OTHER',
                   max_categories: int|None = None,
                   min_count: int|None = None,
                   min_pct: float|None = None) -> Sequence[str]:
    """Merges infrequent categorical labels into a single miscellaneous category

    Positional Arguments:
    items   - A sequence if categorical labels to be transformed
    default - The default value with which to replace uncommon labels

    Keyword Arguments:
    max_categories - The maximum number of distinct labels to be kept (keep most common)
    min_count      - The minimum number of examples a label must have to be kept
    min_pct        - The minimum percentage of the dataset a label must represent to be kept

    returns a transformed version of items where uncommon labels are replaced with the default value
    """
    # NOTE: Exactly ONE of the keyword arguments should be specified!
    #       More or less should result in an exception!
    if len([kwarg for kwarg in [max_categories, min_count, min_pct] if kwarg is None]) != 2:
        raise Exception('Only one keyword argument should be specified')

    return_items = None

    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1

    if max_categories is not None:
        top_categories = [tup[0] for tup in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:max_categories]]
        return_items = [item if item in top_categories else default for item in items]

    if min_count is not None:
        return_items = [item if counts[item] >= min_count else default for item in items]

    if min_pct is not None:
        percentages = {item: counts[item] / len(items) for item in counts.keys()}
        return_items = [item if percentages[item] >= min_pct else default for item in items]

    return return_items


def make_named_bins(items: Sequence[int|float], cut: str, names: Sequence[str]):
    """Bins items using the specified strategy and represents each with one of the given names"""
    # HINT: you should make use of the _find_bins function defined below
    return [names[b] for b in _find_bins(items, cut, len(names))]

def make_mean_bins(items: Sequence[int|float], cut: str, bin_count: int) -> Sequence[int|float]:
    """Bins items using the specified cut strategy and represents each bin with its mean"""
    # HINT: you should make use of the _find_bins function defined below
    bins = [b for b in _find_bins(items, cut, bin_count)]
    values_by_bin = [[] for _ in range(bin_count)]
    for value, b in zip(items, bins):
        values_by_bin[b].append(value)
    averages_by_bin = [mean(bin_values) for bin_values in values_by_bin]
    return [averages_by_bin[b] for b in bins]

def make_median_bins(items: Sequence[int|float], cut: str, bin_count: int) -> Sequence[int|float]:
    """Bins items using the specified cut strategy and represents each bin with its median"""
    # HINT: you should make use of the _find_bins function defined below
    bins = [b for b in _find_bins(items, cut, bin_count)]
    values_by_bin = [[] for _ in range(bin_count)]
    for value, b in zip(items, bins):
        values_by_bin[b].append(value)
    medians_by_bin = [median(bin_values) for bin_values in values_by_bin]
    return [medians_by_bin[b] for b in bins]

def make_min_bins(items: Sequence[int|float], cut: str, bin_count: int) -> Sequence[int|float]:
    """Bins items using the specified cut strategy and represents each bin with its minimum value"""
    # HINT: you should make use of the _find_bins function defined below
    bins = [b for b in _find_bins(items, cut, bin_count)]
    values_by_bin = [[] for _ in range(bin_count)]
    for value, b in zip(items, bins):
        values_by_bin[b].append(value)
    averages_by_bin = [min(bin_values) for bin_values in values_by_bin]
    return [averages_by_bin[b] for b in bins]

def make_max_bins(items: Sequence[int|float], cut: str, bin_count: int) -> Sequence[int|float]:
    """Bins items using the specified cut strategy and represents each bin with its maximum value"""
    # HINT: you should make use of the _find_bins function defined below
    bins = [b for b in _find_bins(items, cut, bin_count)]
    values_by_bin = [[] for _ in range(bin_count)]
    for value, b in zip(items, bins):
        values_by_bin[b].append(value)
    averages_by_bin = [max(bin_values) for bin_values in values_by_bin]
    return [averages_by_bin[b] for b in bins]

def _find_bins(items: Sequence[int|float], cut: str, bin_count: int) -> Sequence[int]:
    """Bins the items and returns a sequence of bin numbers in the range [0,bin_count)"""
    # identify the bin cutoffs based on strategy
    if cut == 'width':
        boundaries = _get_equal_width_cuts(items, bin_count)
    elif cut == 'freq':
        boundaries = _get_equal_frequency_cuts(items, bin_count)
    else:
        raise ValueError(f"Unrecognized bin cut strategy: {cut}")
    # determine the bin of each item using those cutoffs and return the list of bins
    return [_find_bin(item, boundaries) for item in items]

def _find_bin(item: int|float, boundaries: list[tuple[float,float]]) -> int:
    """Assigns a given item to one of the bins defined by the given boundaries bin_min <= x < bin_max"""
    # check edge cases outside the range of the bins
    if item < boundaries[0][0]: return 0
    if item >= boundaries[-1][-1]: return len(boundaries)-1
    # otherwise find the correct bin
    for bin_num,(bin_min,bin_max) in enumerate(boundaries):
        if bin_min <= item and item < bin_max:
            return bin_num
    # this point should never be reached so raise an exception
    raise ValueError(f"Unable to place {item} in any of the bins")

def _get_equal_width_cuts(items: Sequence[int|float], bin_count: int) -> list[tuple[float,float]]:
    """Returns a list of the lower and upper cutoffs for each of the equal width bins"""
    # find the minimum and maximum values in items
    low: float = min(items)
    high: float = max(items)
    # define the bin width as 1/bin_count of the difference between the min and max values
    width: float = (high - low) / bin_count
    # compute the bin boundaries using this width
    boundaries: list[tuple[float,float]] = []
    for bin_num in range(bin_count):
        # identify the boundaries for this bin and add them to the list
        bin_min = low + bin_num * width
        bin_max = low + (bin_num+1) * width
        boundaries.append((bin_min, bin_max))
    return boundaries

def _get_equal_frequency_cuts(items: Sequence[int|float], bin_count: int) -> list[tuple[float,float]]:
    """Returns a list of the lower and upper cutoffs for each of the equal frequency bins"""
    # get a sorted list of the items to help identify where cuts should be made
    sorted_items: list[int|float] = list(sorted(items))
    # use a cursor to track the index of the last cut made
    last_cut: int = 0
    # use a variables to track how many more bins and items are left
    bins_remaining: int = bin_count
    items_remaining: int = len(sorted_items)
    # create a variable to hold the identified boundaries
    boundaries: list[tuple[float,float]] = []
    # loop to find more cuts until finished
    while bins_remaining > 0:
        # determine how many items should be in this next bin
        items_in_bin: int = min(items_remaining, int(round(items_remaining/bins_remaining)))
        # determine the index where the next cut should be made to include that many items
        next_cut = last_cut + items_in_bin
        # get the values at the relevant indices to make bin cuts
        bin_min = sorted_items[max(0,last_cut)]
        bin_max = sorted_items[min(next_cut, len(sorted_items)-1)]
        # add these values to the boundaries to be returned
        boundaries.append((bin_min, bin_max))
        # decrement bins and items remaining
        bins_remaining -= 1
        items_remaining -= items_in_bin
        # mark this cut as the last cut for the next iteration
        last_cut = next_cut
    return boundaries
