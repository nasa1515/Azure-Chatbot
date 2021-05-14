#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "60e15acf-0a7b-4532-9b94-29c2eb1299ac")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", ";xeWO2AeCFm$$C!Gc+ota+|::z@>0K>")
