#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    #APP_ID = os.environ.get("MicrosoftAppId", "60e15acf-0a7b-4532-9b94-29c2eb1299ac") --Service 추가한거
    APP_ID = os.environ.get("MicrosoftAppId", "4b33c554-8c5d-4017-a915-2f67550fc89f")
    # 밑에는 Client Secret
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "lVzdd7W~BiW9I.sX2--5.vsCsx6-_09~3U")
