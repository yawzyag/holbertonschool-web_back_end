#!/usr/bin/env python3
"""
filter specific data
"""
from typing import List
import re
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """[constructor]

        Args:
            fields (List[str]): [fileds to check]
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """[format log]

        Args:
            record (logging.LogRecord): [record to format]

        Returns:
            str: [format logger]
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


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
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """[get logger of specific type]

    Returns:
        logging.Logger: [logger data]
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler().setFormatter(
        RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
