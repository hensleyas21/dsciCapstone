#!/usr/bin/env python3
from __future__ import annotations

import unittest
import pandas as pd
import pandas.testing as pd_testing

# ensure that the current directory is in the Python path
import os
import sys
scriptdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(scriptdir)

# load all the necessary functions for this package
from data_cleaner import remove_missing, replace_missing_with_value
from data_cleaner import replace_missing_with_mean, replace_missing_with_median, replace_missing_with_mode
from data_transformer import z_score_norm, min_max_norm
from data_transformer import make_named_bins, make_mean_bins, make_median_bins
from data_transformer import make_min_bins, make_max_bins, merge_uncommon

class CleanerTests(unittest.TestCase):
    # add support for equality testing DataFrame objects
    def assertDataframeEqual(self, a, b, msg):
        try:
            pd_testing.assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e
    def setUp(self):
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataframeEqual)

    def test_remove_missing(self):
        df = self.get_incomplete_dataframe()
        df = remove_missing(df, 'name')
        self.assertEqual(df, self.get_correct_drop_name())
    
    def test_replace_missing_with_value(self):
        df = self.get_incomplete_dataframe()
        replaced = replace_missing_with_value(df, 'group', 'AB')
        self.assertListEqual(list(replaced), ['A', 'AB', 'A', 'AB', 'B'])
        replaced = replace_missing_with_value(df, 'name', 'Luke')
        self.assertListEqual(list(replaced), ['Mike', 'Jane', 'Andy', 'Luke', 'Ellen'])
        replaced = replace_missing_with_value(df, 'age', 29)
        self.assertListEqual(list(replaced), [36, 29, 36, 32, 29])
        
    def test_replace_missing_with_mode(self):
        df = self.get_incomplete_dataframe()
        replaced = replace_missing_with_mode(df, 'group')
        self.assertListEqual(list(replaced), ['A', 'A', 'A', 'A', 'B'])
        replaced = replace_missing_with_mode(df, 'age')
        self.assertListEqual(list(replaced), [36, 36, 36, 32, 36])

    def test_replace_missing_with_median(self):
        df = self.get_incomplete_dataframe()
        replaced = replace_missing_with_median(df, 'age')
        self.assertListEqual(list(replaced), [36, 36, 36, 32, 36])

    def test_replace_missing_with_mean(self):
        df = self.get_incomplete_dataframe()
        replaced = replace_missing_with_mean(df, 'age')
        fill_value = (36+36+32)/3
        self.assertListEqual(list(replaced), [36, fill_value, 36, 32, fill_value])

    # add a helper function to get an example dataframe missing values from each column
    def get_incomplete_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame({
            'name': ['Mike', 'Jane', 'Andy', None, 'Ellen'],
            'group': ['A', None, 'A', None, 'B'],
            'age': [36, None, 36, 32, None]
        })
    # add a helper function to get the ground truth of what the example looks like after dropping missing
    def get_correct_drop_name(self) -> pd.DataFrame:
        return pd.DataFrame({
            'name': ['Mike', 'Jane', 'Andy', 'Ellen'],
            'group': ['A', None, 'A', 'B'],
            'age': [36, None, 36, None],
        }, index=[0, 1, 2, 4])
    
class TransformerTests(unittest.TestCase):
    nums: tuple[int,...] = (24, -38, 9, -24, -20, -7, 64, 51, -7, -93, -55, 86, 
                            -39, -96, 64, -36, 72, -53, 93, 17, 13, -64, -10, -93)
    labels: tuple[str,...] = ('A', 'B', 'A', 'C', 'A', 'C', 'A', 'A', 'B', 'C', 'B', 
                              'D', 'A', 'B', 'A', 'B', 'C', 'A', 'A', 'B', 'D', 'A', 
                              'B', 'B', 'E', 'A', 'A', 'A', 'B', 'C', 'B', 'A', 'A')
    def test_z_score_norm(self):
        answer: tuple[float,...] = (0.5268001664074762, -0.5649528246988255, 
                                    0.2626663782365968, -0.31842795573933796, 
                                    -0.24799227889377012, -0.01907632914567462, 
                                    1.2311569348631548, 1.002240985115059, 
                                    -0.01907632914567462, -1.5334433813253834, 
                                    -0.8643044512924889, 1.618553157513778, 
                                    -0.5825617439102174, -1.5862701389595593, 
                                    1.2311569348631548, -0.5297349862760415, 
                                    1.3720282885542905, -0.829086612869705, 
                                    1.7418155919935217, 0.4035377319277325, 
                                    0.3331020550821646, -1.0227847241950165, 
                                    -0.07190308677985051, -1.5334433813253834)
        self.assertSequenceEqual(z_score_norm(self.nums), answer)
    
    def test_min_max_norm(self):
        answer: tuple[float,...] = (0.6349206349206349, 0.30687830687830686, 
                                    0.5555555555555556, 0.38095238095238093, 
                                    0.4021164021164021, 0.4708994708994709, 
                                    0.8465608465608465, 0.7777777777777778, 
                                    0.4708994708994709, 0.015873015873015872, 
                                    0.21693121693121692, 0.9629629629629629, 
                                    0.30158730158730157, 0.0, 0.8465608465608465, 
                                    0.31746031746031744, 0.8888888888888888, 
                                    0.2275132275132275, 1.0, 0.5978835978835979, 
                                    0.5767195767195767, 0.1693121693121693, 
                                    0.455026455026455, 0.015873015873015872)
        self.assertSequenceEqual(min_max_norm(self.nums), answer)
        
    def test_make_named_bins(self):
        freq_answer = ('high', 'low', 'med', 'med', 'med', 'med', 'high', 
                       'high', 'med', 'low', 'low', 'high', 'low', 'low', 
                       'high', 'med', 'high', 'low', 'high', 'high', 
                       'med', 'low', 'med', 'low')
        width_answer = ('high', 'low', 'high', 'low', 'low', 'low', 'high', 
                        'high', 'low', 'low', 'low', 'high', 'low', 'low', 
                        'high', 'low', 'high', 'low', 'high', 'high', 'high', 
                        'low', 'low', 'low')
        self.assertSequenceEqual(make_named_bins(self.nums, 'freq', ('low','med','high')), freq_answer)
        self.assertSequenceEqual(make_named_bins(self.nums, 'width', ('low','high')), width_answer)
    
    def test_make_mean_bins(self):
        bin_means = (-75.66666666666667, -27.833333333333332, 8.166666666666666, 71.66666666666667)
        correct_bins = (2, 1, 2, 1, 1, 2, 3, 3, 2, 0, 0, 3, 1, 0, 3, 1, 3, 0, 3, 2, 2, 0, 1, 0)
        answer = tuple((bin_means[b] for b in correct_bins))
        self.assertSequenceEqual(make_mean_bins(self.nums, 'freq', 4), answer)
    
    def test_make_median_bins(self):
        bin_medians = (-78.5, -30, 11, 68)
        correct_bins = (2, 1, 2, 1, 1, 2, 3, 3, 2, 0, 0, 3, 1, 0, 3, 1, 3, 0, 3, 2, 2, 0, 1, 0)
        answer = tuple((bin_medians[b] for b in correct_bins))
        self.assertSequenceEqual(make_median_bins(self.nums, 'freq', 4), answer)

    def test_make_min_bins(self):
        bin_mins = (-96, -39, -7, 51)
        correct_bins = (2, 1, 2, 1, 1, 2, 3, 3, 2, 0, 0, 3, 1, 0, 3, 1, 3, 0, 3, 2, 2, 0, 1, 0)
        answer = tuple((bin_mins[b] for b in correct_bins))
        self.assertSequenceEqual(make_min_bins(self.nums, 'freq', 4), answer)
    
    def test_make_max_bins(self):
        bin_maxes = (-53, -10, 24, 93)
        correct_bins = (2, 1, 2, 1, 1, 2, 3, 3, 2, 0, 0, 3, 1, 0, 3, 1, 3, 0, 3, 2, 2, 0, 1, 0)
        answer = tuple((bin_maxes[b] for b in correct_bins))
        self.assertSequenceEqual(make_max_bins(self.nums, 'freq', 4), answer)

    def test_merge_uncommon(self):
        # require at least three of a label replacing E with O
        min2 = merge_uncommon(self.labels, 'O', min_count=2)
        min2_gt = ['O' if e == 'E' else e for e in self.labels]
        self.assertSequenceEqual(min2, min2_gt)
        # keep at most 2 labels replacing C, D, and E with O
        keep2 = merge_uncommon(self.labels, 'O', max_categories=2)
        keep2_gt = [e if e in ('A','B') else 'O' for e in self.labels]
        self.assertSequenceEqual(keep2, keep2_gt)
        # keep only labels representing at least 15% of the data i.e. (A, B, and C)
        pct_15 = merge_uncommon(self.labels, 'O', min_pct=0.15)
        pct_15_gt = [e if e not in ('D','E') else 'O' for e in self.labels]
        self.assertSequenceEqual(pct_15, pct_15_gt)

if __name__=='__main__':
    unittest.main()