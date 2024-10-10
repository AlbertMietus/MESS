# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017- 2024 Part of my MESS project
# -*- coding: utf-8 -*-

DEBUG=False

# read STD config ...
#==========================================
import sys; sys.path.append('_std_settings/conf')
from std_conf import *

# For sphinx.ext.autodoc':
import os.path; sys.path.append('pyMESS/training/dPID')

# General information about the project.
#======================================
project = 'MESS'
copyright = "ALbert Mietus, 2017- 2024"

from datetime import datetime
release = datetime.now().strftime("%Y%m%d.%H")
version = release

# Overrule std_conf, where needed
#================================

html_title = project + " | " + release # DEFAULT: '<project> v<revision> documentation' -- Strip "documentation"

html_sidebars = {
    '**': [ 'recentposts.html', 'tagcloud.html', 'postcardHeader.html'],
}


# ABlog
#------
extensions.append('ablog')
extensions.append('sphinx.ext.intersphinx') # GAM: workaround?

fontawesome_link_cdn = "https://use.fontawesome.com/releases/v5.0.10/css/all.css"
post_date_format = '%Y/%m/%d'
post_date_format_short = '%Y/%m'

blog_authors = {'GAM' : ('ALbert Mietus', 'http://albert.mietus.nl') }
blog_default_author = 'GAM'
blog_languages = {
    'nl'  : ('Nederlands', None),
    'en'  : ('English', None),
}
language='en' # As workaround for ABlog.post.generate_atom_feeds -- see: https://github.com/sunpy/ablog/issues/137
blog_default_language = 'nl'
post_always_section = True

blog_baseurl = 'http://mess.softwarebetermaken.nl/'
disqus_shortname = 'mess-swbmnl'
disqus_pages = True                                                 # All pages have a disqus-section
disqus_drafts = False                                               # .. but the draft (blog) pages (.. post:: without date )




html_static_path.append('_slides')

if DEBUG:
    print("Debug: show all packages:")
    import os
    os.system("pip list")
    print("Debug: Outdates packages:")
    os.system("pip list --outdated")
    print("Done =====")

## SOURCE: https://about.readthedocs.com/blog/2024/07/addons-by-default/
import os

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

