.. title: Building System Packages
.. slug: building-system-packages
.. date: 2015/03/17 10:00:00
.. tags: packaging, vagrant, fpm, fpm-cookery
.. link:
.. description: package building made easy with Vagrant and fpm-cookery
.. author: Felix Mueller
.. type: text
.. image: building-system-packages.jpg

Packaging and deploying software has always been a somewhat important topic for both developers and system engineers. We here at Zalando prefer native system packages over language specific package formats to deploy software in a fast, reliable and consistent way. It is also a benefit to have only one toolkit for managing all (or most) software, by reducing the confusion between pip / npm / gem and apt-get / yum who is managing which files.

.. TEASER_END

**TL;DR**: We will see that system packages can be built fairly easy with tools like `fpm`_ - if your goal is not to build policy-compliant packages but just get your software deployable. With the scriptable virtual boxes provided by `Vagrant`_ this process can be automated further, so you could build, update and publish your packages just with a commit into the SCM.
Whether we create packages to manage our own software, build or modify packages for 3rd party software or just backport a version of a package for an older distribution, we can do that with a couple of `simple scripts`_.

Motivation
==========

There are many ways to build native packages for various operating systems. For Debian and Ubuntu you could use `debuild`_, for CentOS and RedHat `rpmbuild`_ and there are also some hosted build services, like `OpenBuildService`_.
Unfortunately, building native system packages is not as easy as it could be. One of the reasons for this is the sheer amount of different tools makes it hard to choose the right one: there is `debhelper`, `dpkg-buildpackage`, `dh`, `debuild`, `dh_make` and some others the `Debian New Maintainer's Guide`_ is referring to.

Even the most basic process to build a native Debian package from source, consists of these steps:

- download the tar.gz
- run ``dh_make --yes --indep --createorig``
- manipulate control files, add init script and config files ...
- run ``debuild -us -uc -b``

`dh_make` is a wrapper which creates templates and helps you to fill them out by asking questions, when not running in interactive mode - but still may require some manual configuration, which tends to be repetitious. `debuild` comes from the `devscripts` package which provides some other tools to "make the life of a Debian Package maintainer easier". Anyhow for both tools you have still have to pass some flags and you have to touch files in different locations to build a package which fulfills the requirements of the `Debian Policy`_.
This was just the .deb packages part, but you may have to build that same package for RedHat-like systems also and the then you have to cope with .rpm SPECS. And then the same story if you have to build the package for Solaris, OSX or one of this BSD flavors.

Then you should always build in a clean, well defined environment with all the build dependencies for the package you want to create. This is important to keep your packaging process repeatable and consistent, so you may want to build packages in disposable virtual machines.

Luckily, for there are tools for each of this problems: `Vagrant`_ and `fpm`_.

Vagrant
=======

In order to always have a fresh build environment for our packaging process, we're making heavily usage of `Vagrant`, which allows to set up the build boxes via different provisioning providers which helps to automate preparing the environment.

fpm-cookery
===========

`fpm` is a ruby gem for having a simple interface to build native packages for multiple platforms such as .deb, .rpm and many more. You may find more examples in the `fpm wiki`_. It saves lots of time having without having to worry about the platform you want to build a package for.

`fpm-cookery`_ provides the possibility to automate fpm builds using manifests, so-called recipes. It's benefit is that you have reusable scripts, which you can use to maintain your packages. As it is influenced by homebrew recipe style it may feel already familiar to you.

If you want to add changes to your packages all you have to do is to apply your desired changes, update the revision, build and release your package.

The downside is, fpm-cookery has little or no documentation, so you should better read some example recipes and the source code.

Tasty Recipes
=============

Here is a very basic ``recipe.rb`` example. It converts a RubyGem to a package. Depending on the distribution you're using fpm-cookery will produce a package, matching it by itself. Just run the command ``fpm-cook`` in the path, where the ``recipe.rb`` is located.

.. code-block:: ruby

  class FacterRubyGem < FPM::Cookery::RubyGemRecipe
    name    'facter'
    version '1.6.16'
  end

This one was simple, but in some cases, we need to do a little bit more. For building Oracle JDK into a native package, we first have to download the according tar.gz file. Sadly, fpm-cookery's ``curl`` source handler is not capable of sending custom headers, which are required to execute the download programmatically. So here we do this in ``prepare.sh``:

.. code-block:: bash

  #!/bin/bash
  set -e

  LONGVERSION=$(sed -n 's|\s*version\s*"\(.*\)"|\1|p' recipe.rb)
  LONGVERSION=${LONGVERSION/-/_}
  VERSION=${LONGVERSION##*_}
  TARGET="cache/jdk-7u${VERSION}-linux-x64.tar.gz"

  [ -d cache ] || mkdir -p cache
  [ -f $TARGET ] || curl -jkLH 'Cookie: oraclelicense=accept-securebackup-cookie' --progress-bar -o $TARGET http://download.oracle.com/otn-pub/java/jdk/7u${VERSION}-b13/jdk-7u${VERSION}-linux-x64.tar.gz

`(Ignore the $VERSION and $LONGVERSION variables, this is just for naming convention)`

The ``recipe.rb`` example below then can build the package from the fetched tar.gz.

.. code-block:: ruby

  #!/bin/env ruby
  # encoding: utf-8

  class ZalandoJDK < FPM::Cookery::Recipe
    description "Tomcat meta package for Zalando"

    version   "1.7.0-76"
    revision   0
    arch      "all"
    name      "zalando-jdk-#{version}"
    homepage  "http://www.oracle.com/"
    source    "cache/jdk-7u#{version[-2..-1]}-linux-x64.tar.gz"
    md5	      "5a98b1a3e4c48363d03f664f173bbb9a"

    maintainer "Sören König <soeren.koenig@zalando.de>"
    section   "non-free/net"
    depends   "libtcnative-1", "cronolog"

    def build
    end

    def install
       root("/server/jdk/#{version.gsub('-','_')}").install Dir["*"]
    end
  end

We wrote some simple shell scripts to automate this process, they can be found in our `GitHub repository`_. Here is how it works:

- ``boxes``: a list of supported build boxes with URLs to download the Virtualbox images.
- ``setup.sh``: installs all needed packages, iterates over ``boxes`` and downloads the Vagrant boxes.
- ``Vagrantfile``: init file for Vagrant, It starts all boxes listed in ``boxes`` and provisions them with ``provision*sh``
- ``provision*sh``: Simple shell scripts used to install the needed build tools on the Vagrant boxes. You may specify provision scripts per Vagrant box, creating one named like ``provision-$hostname.sh``, otherwise default script is used. All of them call ``cook-recipe.sh``.
- ``recipes.list``: Lists the names of subdirs under ``recipes/`` to jump into and build packages.
- ``cook-recipe.sh``: iterates over ``recipes.list`` and execute ``prepare.sh`` and ``fpm-cookery``, if appropriate files are existing.
- ``prepare.sh``: "pre-build" tasks, which are needed before the ``fpm-cookery`` can build the packages.
- ``recipe.rb``: finally, the recipe for ``fpm-cookery``.

So you only have to list the foldernames of the recipes you want to build in the ``recipes.list`` and run ``vagrant up ubuntu14.04`` or whatever target distro you want to build you package for. If everything went fine, you'll see lines like this and your package is ready to be uploaded to your repositories:

.. code-block::

    ===> Created package: /vagrant/recipes/libtcnative-1/pkg/libtcnative-1_1.1.32-0_amd64.deb

.. _debuild: http://manpages.ubuntu.com/manpages/trusty/man1/debuild.1.html
.. _rpmbuild: http://www.rpm.org/max-rpm-snapshot/rpmbuild.8.html
.. _OpenBuildService: https://build.opensuse.org
.. _vagrant: https://www.vagrantup.com/
.. _fpm: https://github.com/jordansissel/fpm
.. _fpm-cookery: https://github.com/bernd/fpm-cookery
.. _fpm wiki: https://github.com/jordansissel/fpm/wiki
.. _GitHub repository: https://github.com/zalando/package-build
.. _simple scripts: https://github.com/zalando/package-build
.. _Debian New Maintainer's Guide: https://www.debian.org/doc/manuals/maint-guide/
.. _Debian Policy: https://www.debian.org/doc/debian-policy/