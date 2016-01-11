Setting up TechBlog
###################

:Date: 2016-01-10
:Tags: Blog, Pelican
:Category: Python

..  include::   ../../../../references.inc

I want to have a place where I can write short technical articles that lay out
how to do a variety of things as a software developer. That sounds like a blog,
and I already have such a place at `Random Ramblings
<http://www.co-pylit.org/blog>`_. That blog is more personal, and was
originally set up as a motivational site for my students. Lately, it has become
a place where I tell stories about my life, and my ongoing battle with cancer. 

This blog, which will be named `TechBlog <http://blog.black-devops.org>`_ will
focus on technologies I am exploring as part of my teaching work at |ACC|_.

Getting Started
***************

Since most of my development work is done in Python, I am using Pelican_ as the
engine to build my blog. Pelican_ creates static HTML pages that are simple to
host on many different setups. For this blog, I will build a server at
DigitalOcean_, as an experiment. I have heard good things about this company,
and want to give them a try. I use other services to host my other web applications.

Project Setup
=============

The first step involves creating a directory to hold the project, and setting
up a Python virtualenv. I use a MacBook Pro as my development system, and have
both Python and virtualenv_ installed. Since I create a lot of Python projects,
I have set up two aliases to make creating and working on them simple:

These two entries are in my ``.bash_profile`` file:

..  code-block:: bash

    alias venv='virtualenv _venv && workon'
    alias workon='source _venv/bin/activate'

All I need to do to start a new project is this:

..  code-block:: bash

    $ mkdir project_name
    $ cd project_dir
    $ venv
    (_venv) $

The prompt changes when the virtualenv_ is active to remind you that you are
working on your project. You can prove that this is correct by doing this:

..  code-block:: bash

    (_venv) $ which python
    /Users/rblack/_projects/project_dir/_venv/bin/python

That tells you that the python interpreter is the one installed in the project
``_venv`` directory.

Installing Pelican
==================

We install Pelican_ and a plugin used for comments as follows:

..  code-block:: bash

    (_venv) $ pip install pelican
    (_venv) $ pip install git+git://github.com/bstpierre/pelican-comments#egg=pelican_comments

Initial Blog Setup
==================

With Pelican_ installed, we can create the basic blog structure by doing this:

..  code-block:: bash

    (_venv) $ 
..  vim:filetype=rst spell:
