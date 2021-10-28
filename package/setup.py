#!/usr/bin/env python

import os, sys
import re

from setuptools import setup


def setup_package():
    setup(
        name="raft",
        version="1.0",
        description="RAFT optical flow",
        packages=[
            "raft",
            "raft.core",
            "raft.core.utils",
        ],
        package_dir={
            "raft": "./raft",
            "raft.core": "./raft/core",
            "raft.core.utils": "./raft/core/utils",
        },
    )


if __name__ == "__main__":
    setup_package()
