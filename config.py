#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    #APP_ID = os.environ.get("MicrosoftAppId", "60e15acf-0a7b-4532-9b94-29c2eb1299ac") --Service 추가한거
    APP_ID = os.environ.get("MicrosoftAppId", "720a067a-381a-4661-a644-1d3ad670f69a")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "AHzvB_0YcvUL2.yic.4K_H5~qb05H4F-Rv")
