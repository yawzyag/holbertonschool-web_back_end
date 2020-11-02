#!/usr/bin/env python3
"""
filter specific data
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """[Filter data]

    Args:
        fields (List[str]): [fileds to filter]
        redaction (str): [replace string]
        message (str): [message to check]
        separator (str): [separator of message]

    Returns:
        str: [final filter message]
    """
    for val in fields:
        match = re.search(rf'{val}=([^{separator}#]*)', message)
        if match:
            message = re.sub(match.group().split("=")[1], redaction, message)
    return message
