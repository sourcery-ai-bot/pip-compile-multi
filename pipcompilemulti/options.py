"""
Global dictionary holding configuration options
"""

OPTIONS = {
    'add_hashes': [],
    'allow_unsafe': False,
    'base_dir': 'requirements',
    'compatible_patterns': [],
    'forbid_post': [],
    'header_file': None,
    'in_ext': 'in',
    'include_names': [],
    'out_ext': 'txt',
    'upgrade': True,
    'upgrade_packages': [],
    'use_cache': False,
}

DEFAULT_HEADER = """
#
# This file is autogenerated by pip-compile-multi
# To update, run:
#
#    pip-compile-multi
#
""".lstrip()
