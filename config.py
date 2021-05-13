#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "04a1c21a-2875-4a81-870c-d595b20c0b1d")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "cMi.1-7yTjSirAlD62C_0QOZGx0H-B7-K9")
