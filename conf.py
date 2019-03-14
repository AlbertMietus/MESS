# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017, 2019. Part of my MESS project
# -*- coding: utf-8 -*-

# read STD config ...
#==========================================
import sys; sys.path.append('_external_templates/conf')
from std_conf import *


# For sphinx.ext.autodoc':
import os.path; sys.path.append('pyMESS/training/dPID')

# General information about the project.
#======================================
project = 'MESS'
copyright = "ALbert Mietus, 2017, 2019"

from datetime import datetime
release = datetime.now().strftime("%Y%m%d.%H")
version = release

# Overrule std_conf, where needed
#================================

#html_title = project + " | " + release # DEFAULT: '<project> v<revision> documentation' -- Strip "documentation"


def setup(app):
    app.add_stylesheet('../_static/SwBMnl+rtfd.css')

if True:
    # ABlog
    #------
    extensions.append('ablog')
    import ablog; templates_path.append(ablog.get_html_templates_path())
    fontawesome_link_cdn = "http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css"
    post_date_format = '%Y/%m/%d'
    post_date_format_short = '%Y/%m'

    blog_authors = {'GAM' : ('ALbert Mietus', 'http://albert.mietus.nl') }
    blog_default_author = 'GAM'
    blog_languages = {'nl'  : ('Nederlands', None) }
    blog_default_language = 'nl'
    post_always_section = True

    blog_baseurl = 'http://mess.softwarebetermaken.nl/'
    disqus_shortname = 'mess-swbmnl'
    disqus_pages = True                                                 # All pages have a disqus-section
    disqus_drafts = False                                               # .. but the draft (blog) pages (.. post:: without date )

    html_sidebars = {
        '**': [ 'recentposts.html', 'tagcloud.html', 'postcardHeader.html'],
    }
