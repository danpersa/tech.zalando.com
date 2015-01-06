.. title: Berlin AWS User Group Meetup
.. slug: aws-minion-at-aws-user-group-meetup
.. date: 2014/12/11 10:00:00
.. tags: aws, docker, open-source
.. link:
.. description: Zalando presented the AWS Minion tool at the Berlin AWS User Group Meetup.
.. author: Henning Jacobs
.. type: text
.. image: aws-ug-dec-meetup.jpg

We had the chance to present our recent efforts on AWS account management and Docker application deployment at the `December Berlin AWS User Group Meetup`_.

Our main presentation topic was the `AWS Minion`_ command line tool which allows managing immutable stacks of Docker applications.

.. TEASER_END

After getting strengthened by beer and big slices of tasty pizza (thanks to the host Onefootball_),
we listened to two interesting talks (news from AWS re:Invent and a new tool to increase S3 efficiency):

* As soon as `AWS Config`_ becomes available, we will definitely check it out to get a better view across all our AWS resources
* Sadly most of the announced AWS services are either in preview or not available at all (yet).

Our presentation about `AWS Minion`_ went last and briefly described our AWS setup and the reasoning behind it:

* We have about 40 different development teams
* We want every team to be autonomous in their decisions (e.g. technology selection)
* Every team should

  * be able to **use any AWS service** (RDS, ElastiCache or any other newly announced products such as AWS CodePipeline)
  * have an **isolated sandbox**, e.g. team A should not be able to shut down EC2 instances of team B
  * be able to **access services** of other teams
  * have **separate billing** & accounting, i.e. it needs to be clear which team generates which costs

As we hit some AWS limitations such as `VPC limits`_ or `incomplete IAM support for some AWS products`_,
we went for the "one AWS account per team" solution to fulfill our above requirements:

.. image:: /images/2014-12-09-aws-account-team-vpc-setup.png

The AWS account setup is supported by our `AWS Overlord`_ tool which setups the different subnets, NAT instances and more.

Our `AWS Minion`_ complements the account setup by providing a tool to deploy Docker applications on EC2 including ELB and DNS setup:

* The team registers a new application using the ``minion`` command line tool (CLI)
* The new application is build and pushed as a Docker image to a private Docker registry
* A new application version is created with the ``minion`` CLI

  * This creates an auto scaling group and associated ELB
  * The application version is automatically deployed with Docker and made available under a HTTPS URL (e.g. https://myapp-1-0.example.org)

* As soon as the application version is ready for production, traffic can be routed to it using the CLI

  * This changes weights in the Route 53 hosted zone for the main application URL (e.g. https://myapp.example.org)

More details about the Minion workflow is described in the `AWS Minion documentation`_.

You can find both Overlord and Minion on GitHub:

* https://github.com/zalando/aws-overlord
* https://github.com/zalando/aws-minion

You can find the `slides of the AWS UG Dec Meetup online as PDF`_.


.. _December Berlin AWS User Group Meetup: http://www.meetup.com/AWS-Berlin/events/218756146/
.. _Onefootball: http://www.onefootball.com/
.. _AWS Config: https://aws.amazon.com/config/
.. _AWS Minion: https://github.com/zalando/aws-minion
.. _VPC limits: http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html
.. _incomplete IAM support for some AWS products: http://stackoverflow.com/questions/25649564/amazon-web-services-why-iam-does-not-support-arn-for-autoscaling
.. _AWS Overlord: https://github.com/zalando/aws-overlord
.. _AWS Minion documentation: http://aws-minion.readthedocs.org/
.. _slides of the AWS UG Dec Meetup online as PDF: /files/2014/12/2014-12-09-AWS-UG-Dec-Meetup.pdf
