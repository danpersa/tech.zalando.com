.. title: Entering Kernel Namespaces with Python
.. slug: entering-kernel-namespaces-with-python
.. date: 2014/09/16 10:55:29
.. tags: python
.. link:
.. description:
.. author: Henning Jacobs
.. type: text
.. image: python-logo.png

When working with Docker_ containers usually the question arises on how to connect into a running container without starting an explicit SSH daemon (which is considered `a bad idea`_).
This leads us to Linux Kernel namespaces.

.. TEASER_END

Docker uses Linux Kernel namespaces to restrict the view from within containers:

* IPC namespace: isolate interprocess communication resources (IPC)
* Mount namespace: isolate filesystem mounts, i.e. containers only see their own mounts
* Net namespace: isolate network devices, e.g. containers have own IP addresses and iptables rules
* PID namespace: isolate the process ID number space, e.g. the same PID can be used for different processes
* User: isolate the user and group ID number spaces
* UTS namespace: isolate hostname and domain name

You can use the ``nsenter`` command line utility which is provided in the ``util-linux`` package. Sadly ``nsenter`` is `not yet part of Ubuntu 14.04 LTS`_.
Jérôme Petazzoni provides a `Docker recipe for nsenter on GitHub`_ or you can `compile nsenter from source`_.

As there is only one simple syscall to enter a namespace, we can do the call directly from within Python using the ``ctypes`` module:


.. code:: python

    import ctypes
    libc = ctypes.CDLL('libc.so.6')
    # replace MYPID with the container's PID
    fd = open('/proc/<MYPID>/ns/net')
    libc.setns(fd.fileno(), 0)
    # we are now inside MYPID's network namespace


We bundled this syscall in a new Python package ``nsenter``, which is `available on PyPI`_.

You can install it from PyPI (it requires Python 3.4) and use the command line utility to connect to a running container:

.. code:: bash

    pip3 install nsenter
    # replace MYPID with the container's PID:
    sudo nsenter --net --target=MYPID /bin/ip a

You can use the Docker ``inspect`` command to make it more convenient:

.. code:: bash

    # start a new Redis server in the background
    docker run -d --name=redis -t redis
    # connect to the running Redis container
    sudo nsenter --all --target=`docker inspect --format '{{ .State.Pid }}' redis` /bin/bash

Obviously you might want to inspect or manipulate containers without executing another command line tool.
You can use the provided context manager to do this:

.. code:: python

    import subprocess
    from nsenter import Namespace

    with Namespace(mypid, 'net'):
        # output network interfaces as seen from within the mypid's net NS:
        subprocess.check_output(['ip', 'a'])


You can find the `source code on GitHub`_.

We are currently building our own Docker-based PaaS (Platform as a Service) with IPv6 --- so stay tuned...

.. _Docker: https://www.docker.com/
.. _a bad idea: http://jpetazzo.github.io/2014/06/23/docker-ssh-considered-evil/
.. _not yet part of Ubuntu 14.04 LTS: http://askubuntu.com/questions/439056/why-there-is-no-nsenter-in-util-linux
.. _Docker recipe for nsenter on GitHub: https://github.com/jpetazzo/nsenter
.. _compile nsenter from source: http://askubuntu.com/questions/439056/why-there-is-no-nsenter-in-util-linux
.. _available on PyPI: https://pypi.python.org/pypi/nsenter
.. _source code on GitHub: https://github.com/zalando/python-nsenter
.. _Cloud Specialist: https://jobs.zalando.de/jobportal/index.php?ac=jobad&id=2097
