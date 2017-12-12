# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2011-2017
#  STANDARD CONFiguration for Sphinx-doc
# -*- coding: utf-8 -*-

import os
on_rtd = os.environ.get('READTHEDOCS') == 'True'

print("Using std_conf [%s-version]" % ('RTfD' if on_rtd else 'local'))

###
### File/Project layout
###

master_doc = 'index'
source_suffix = '.rst'
exclude_patterns = ['**/.#*', '**/_*']
html_static_path = ['_external_templates/static/']
templates_path = ['templates']

###
### Kick off
###
try:    extensions = extensions
except NameError: extensions=[]

show_authors = False # Always me

rst_epilog = None
rst_prolog = """
.. include:: /_generic.inc

"""

###
### Normal HTML output
###

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
    #    'style_external_links': False, # available in next release
    'prev_next_buttons_location': 'both',
}
html_style = 'SwBMnl+rtfd.css'


#html_logo= ...file...
#html_theme_options['logo_only']=True # True: only logo, False: Logo & name

# sphinx.ext.todo
#-----------------
extensions.append('sphinx.ext.todo')
todo_include_todos=True

# sphinx.ext.autodoc'
#--------------------
extensions.append('sphinx.ext.autodoc')
autodoc_member_order='bysource'


# plantUML
#---------
if not on_rtd:
    extensions.append('sphinxcontrib.plantuml')
    plantuml = 'java -jar /Users/albert/Apps/PlantUML/libexec/plantuml.jar -nogui'
