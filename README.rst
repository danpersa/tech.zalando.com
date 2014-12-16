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


Getting started
===============

You need Git and Docker_ to build static HTML (should also work now with latest version of boot2docker and Docker 1.3+):

.. code-block:: bash

    $ git clone https://github.com/zalando/tech.zalando.com.git
    $ cd tech.zalando.com
    $ docker run -v $(pwd):/workdir -t hjacobs/nikola build

Now open the generated HTML files in the "output" directory.

You can also use the provided Makefile to achieve the same:

.. code-block:: bash

    $ make clean
    $ make

Editing files on Windows
========================

Please see http://stackoverflow.com/questions/2746692/restructuredtext-tool-support for editor support.


.. _tech.zalando.com: http://tech.zalando.com/
.. _Docker: https://www.docker.com/
