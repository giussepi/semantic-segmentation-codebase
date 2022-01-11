# ----------------------------------------
# Written by Yude Wang
# ----------------------------------------

from lib.utils.registry import DATASETS


def generate_dataset(cfg, **kwargs):
    dataset = DATASETS.get(cfg.DATA_NAME)(cfg, **kwargs)
    return dataset
