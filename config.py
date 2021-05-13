#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "0d6cf071-d21d-4969-b482-5f2b41afb7d9")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "]_CR%mBAc$Aygb3-[K|z2pCPZk+")
