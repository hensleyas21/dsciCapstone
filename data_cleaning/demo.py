#!/usr/bin/env python3
from __future__ import annotations

import pandas as pd
import numpy as np
from numpy.typing import DTypeLike

import json
from typing import Any, NamedTuple
from argparse import Namespace, ArgumentParser

# ensure that the current directory is in the Python path
import os
import sys
scriptdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(scriptdir)

# load all the necessary functions for this package
from data_loader import load_data, save_data
from data_cleaner import remove_missing, fix_missing
from data_transformer import transform_feature
from data_inspector import make_plot

def main(args: Namespace):
    # load the configuration from the JSON config file
    config: Config = load_config(args.config)
    # load the columns specified into a DataFrame
    dtypes: dict[str,DTypeLike] = {attr_name:get_datatype(attr_config.type) \
            for attr_name,attr_config in config.attributes.items()}
    missing: dict[str,set[str]] = {attr_name:set(attr_config.missing_values) \
            for attr_name,attr_config in config.attributes.items() \
                if attr_config.missing_values is not None}
    df: pd.DataFrame = load_data(config.raw_dataset_path, columns=dtypes, missing=missing)
    # rename any attributes with the rename attribute
    col_renames = {attr_name:attr_config.rename \
                        for attr_name,attr_config in config.attributes.items() \
                            if attr_config.rename is not None}
    df = df.rename(columns=col_renames)
    # fix missing vaules according to the attribute specifications
    for clean_step in config.clean_steps:
        if clean_step.missing_strategy == 'remove':
            df = remove_missing(df, clean_step.attribute)
        else:
            df = fix_missing(df, clean_step.attribute, clean_step.missing_strategy)
    # apply any transformations in order the are specified
    for ts in config.transform_steps:
        transform_feature(df, ts.attribute, ts.action, ts.args, ts.kwargs)
    # save the data at the determined location
    save_data(df, config.clean_dataset_path)
    # make all requested plots saving them in the plot directory
    for plot_step in config.plotting_steps:
        # create the requested plot image
        img = make_plot(df, plot_step.attribute, plot_step.action, plot_step.args, plot_step.kwargs)
        # save this image in the plots directory with the requested file name
        img.save(os.path.join(config.plot_directory_path, f"{plot_step.name}.png"))

class Config(NamedTuple):
    raw_dataset_path: str
    clean_dataset_path: str
    plot_directory_path: str
    attributes: dict[str,AttributeConfig]
    clean_steps: list[CleanConfig]
    transform_steps: list[TransformConfig]
    plotting_steps: list[PlotConfig]
    @staticmethod
    def parse(d: dict[str,Any]) -> Config:
        return Config(
            str(d['raw_dataset_path']),
            str(d['clean_dataset_path']),
            str(d['plot_directory_path']),
            {k:AttributeConfig.parse(v) for k,v in d['attributes'].items()},
            [CleanConfig.parse(e) for e in d['cleaning']],
            [TransformConfig.parse(e) for e in d['transforming']],
            [PlotConfig.parse(e) for e in d['plotting']]
        )

class AttributeConfig(NamedTuple):
    type: str
    rename: str|None
    missing_values: set[str]|None
    @staticmethod
    def parse(d: dict[str,Any]) -> AttributeConfig:
        return AttributeConfig(
            d['type'],
            d.get('rename'),
            d.get('missing_values')
        )

class CleanConfig(NamedTuple):
    attribute: str
    missing_strategy: str
    @staticmethod
    def parse(d: dict[str,Any]) -> CleanConfig:
        return CleanConfig(
            d['attribute'],
            d['missing_strategy']
        )

class TransformConfig(NamedTuple):
    action: str
    attribute: str
    args: list[Any]
    kwargs: dict[str,Any]
    @staticmethod
    def parse(d: dict[str,Any]) -> TransformConfig:
        return TransformConfig(
            d['action'],
            d['attribute'],
            d.get('args', []),
            d.get('kwargs', {})
        )

class PlotConfig(NamedTuple):
    action: str
    attribute: str
    name: str
    args: list[Any]
    kwargs: dict[str,Any]
    @staticmethod
    def parse(d: dict[str,Any]) -> PlotConfig:
        return PlotConfig(
            d['action'],
            d['attribute'],
            d['name'],
            d.get('args', []),
            d.get('kwargs', {})
        )

def load_config(path: str) -> Any:
    with open(path, 'rt', encoding='utf-8') as fin:
        return Config.parse(json.load(fin))

def get_datatype(name: str) -> DTypeLike:
    match name:
        case 'real': return np.float32
        case 'nominal': return np.unicode_
        case _: raise ValueError(f"Unrecognized attribute type {name}")

if __name__=='__main__':
    parser = ArgumentParser(description=(
        "Run a data cleaning and transformation pipeline on the specified dataset "
        "using the proceedures defined in the provided configuration file."
    ))
    parser.add_argument('config', type=str, help='path to JSON config file with proceedures')
    args = parser.parse_args()
    main(args)
