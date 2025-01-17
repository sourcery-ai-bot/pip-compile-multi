"""
Custom Header
=============

``pip-compile-multi`` adds a brief header into generated files.
Override it with

.. code-block:: text

    -h, --header TEXT      File path with custom header text for generated files
"""

from .base import BaseFeature, ClickOption


DEFAULT_HEADER = """
#
# This file is autogenerated by pip-compile-multi
# To update, run:
#
#    pip-compile-multi
#
""".lstrip()


class CustomHeader(BaseFeature):
    """Put custom header at the beginning of locked files."""

    OPTION_NAME = 'header_file'
    CLICK_OPTION = ClickOption(
        long_option='--header',
        short_option='-h',
        default='',
        help_text='File path with custom header text for generated files.',
    )

    def __init__(self):
        self._header_text = None

    @property
    def text(self):
        """Text to put in the beginning of each generated file."""
        if self._header_text is None:
            self._header_text = self._read_header_text() if self.value else DEFAULT_HEADER
        return self._header_text

    def _read_header_text(self):
        with open(self.value) as fp:
            return fp.read()
