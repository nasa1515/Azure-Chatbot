#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "0ccb5bb4-479b-41d9-8658-256b4281b390")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "wtBUn*k5#Y=zusp+)20a33q^_sE")