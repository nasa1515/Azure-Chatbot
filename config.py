#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    #APP_ID = os.environ.get("MicrosoftAppId", "60e15acf-0a7b-4532-9b94-29c2eb1299ac") --Service 추가한거
    APP_ID = os.environ.get("MicrosoftAppId", "f3ade0ca-57c2-4b6f-9008-f4dabcc1ae36")
    # 밑에는 Client Secret
    
    #APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "aU4c~Q3Ze87ACC.SGWh6j230~.AKfw84.Q")
