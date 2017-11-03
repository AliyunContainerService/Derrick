#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os
import re

from derrick.core.detector import Detector
from derrick.core.logger import Logger


class GopathDetector(Detector):
    def execute(self, *args, **kwargs):
        cwd = os.getcwd()
        project_folder_path = re.findall(r"src/(.+?)", cwd)
        if project_folder_path == "":
            Logger.error("Please place the source code to go path.")
            return {"project_folder": project_folder_path}
        return {"project_folder": project_folder_path}
