import alabaster

import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..', '..')))

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'alabaster',
    'releases',
]

# Alabaster theme + mini-extension
html_theme_path = [alabaster.get_path()]
html_theme = 'alabaster'
html_theme_options = {
    'description': "A Python implementation of SSHv2.",
    'github_user': 'ploxiln',
    'github_repo': 'paramiko-ng',
    'github_type': 'star',
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}

# Regular settings
project = 'Paramiko-NG'
copyright = 'Paramiko contributors'
master_doc = 'index'
templates_path = ['_templates']
exclude_trees = ['_build']
source_suffix = '.rst'
default_role = 'obj'

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'special-members': "__init__, __eq__",
}

# Intersphinx connection to stdlib
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.7', None),
}

# just used for old changelog
releases_github_path = "paramiko/paramiko"
releases_document_name = ["old_changelog"]
