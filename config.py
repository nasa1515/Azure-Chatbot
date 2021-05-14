#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "e954c5dc-2691-4eb5-8882-e9c8663c96a5")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "L-1H2T69-MdMgPZa-.LtUO25m02l39.zb9")
