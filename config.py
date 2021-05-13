#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "21969ed9-f69a-4196-a0e5-e5cdd9d84194")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "c-H7gU9k.TR_7iy-o7pfZwqGgFc6Oh6O26")
