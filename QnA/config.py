#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "test1111222")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "test")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "test")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "485a20ffda3d492da3ee7584255cee5a")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://nasaqna.cognitiveservices.azure.com/")
