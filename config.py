#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 8080
    APP_ID = os.environ.get("MicrosoftAppId", "0ccb5bb4-479b-41d9-8658-256b4281b390")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "wtBUn*k5#Y=zusp+)20a33q^_sE")
    WEBSITE_HTTPLOGGING_RETENTION_DAYS = os.environ.get("WEBSITE_HTTPLOGGING_RETENTION_DAYS", "7")
    WEBSITES_CONTAINER_START_TIME_LIMIT = os.environ.get("WEBSITES_CONTAINER_START_TIME_LIMIT", "400")
    WEBSITES_PORT = os.environ.get("WEBSITES_PORT", "8080")