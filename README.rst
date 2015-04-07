=====================================
Zalando Technology public "Tech Blog"
=====================================

This repository contains the source files for our public Tech Blog (tech.zalando.com_).

Writing blog posts
==================

Create (or copy) a ".rst" file in the "posts" folder.
All new blog posts will be written in plain text reStructured Text format (very similar to Markdown, but extensible and therefore more powerful):

* http://docutils.sourceforge.net/rst.html
* http://sphinx-doc.org/rest.html
* http://getnikola.com/quickstart.html

Please make sure your blog post contains all necessary meta information (in the header):

* author name ("..author: Henning Jacobs")
* teaser image ("..image: my-example-image.jpg")


Deploy the blog
===============

You need Git and Docker_ to build static HTML (should also work now with latest version of boot2docker and Docker 1.3+):

Important: to deploy on tech.zalando.com your public ssh key needs to be deployed there first!

Clone the sources on your local machine (if not done already):

.. code-block:: bash

    $ git clone https://github.com/zalando/tech.zalando.com.git
    $ cd tech.zalando.com

Get latest changes from git repository:

.. code-block:: bash

    $ git pull

Build the blog:

.. code-block:: bash

    $ docker run -v $(pwd):/workdir -t zalando/nikola build

The generated HTML files are in the "output" directory.

You can also use the provided Makefile to achieve the same:

.. code-block:: bash

    $ make clean
    $ make

Deploy the blog to tech.zalando.com:

.. code-block:: bash

    $ rsync -av -4 --no-owner --no-group --no-perms output/* root@tech.zalando.com:/data/www/tech.zalando.com/htdocs


Hints:
======

You can create aliases to make deployments even faster:

.. code-block:: bash

    $ alias cleanblog="docker run -v `pwd`:/workdir -t zalando/nikola clean"
    $ alias buildblog="docker run -v `pwd`:/workdir -t zalando/nikola build"
    $ alias deployblog="rsync -av -4 --no-owner --no-group --no-perms output/* root@tech.zalando.com:/data/www/tech.zalando.com/htdocs"

Now you can deploy by just typing:

.. code-block:: bash

    $ buildblog
    $ deployblog


Editing files on Windows
========================

Please see http://stackoverflow.com/questions/2746692/restructuredtext-tool-support for editor support.


.. _tech.zalando.com: http://tech.zalando.com/
.. _Docker: https://www.docker.com/
