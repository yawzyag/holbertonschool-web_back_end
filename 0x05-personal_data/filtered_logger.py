#!/usr/bin/env python3
"""
filter specific data
"""
from typing import List


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
    parsedMessage = []
    for item in message.split(separator):
        itemcp = item.split("=")
        if (itemcp[0] in fields):
            itemcp[1] = redaction
            print(item.split("="))
        parsedMessage.append("=".join(itemcp))
    return separator.join(parsedMessage)
