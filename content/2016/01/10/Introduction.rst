Docker VPS Setup
################

:Date: 2016-01-10
:Category: Docker
:Tags: VPS, Install

..  include::   ../../../../references.inc

Suppose you want to build a new application that lives on a server out there
"in the cloud". Your application needs some horsepower to run: a web server
like NGINX, a database engine like MySQL, and an application written in
something like Python. You want to use a continuous integration service like
TravisCI to run your tests as well. Finally, you need to be able to develop on
your local laptop, and keep all of your source code on GitHub. Sound familiar?

If not, you have some catching up to do, since this is a huge part of the
development landscape these days. Even desktop application developers tap into
setups like this so they can test their work using a continuous integration
service like Travis CI.

I want to build a new technology blog for my students, separate from the one I
use for my personal life. I use Pelican_, a nice blogging tool written in
Python, and I host my personal blog on one of my Rackspace VPS machines.

This time, I want to try Docker and another VPS provider: DigitalOcean_.

DigitalOcean Setup
******************

The starting point for this adventure invoves signing up on DigitalOcean_,
which is pretty simple. Like other VPS providers, you pay only for the servers
you create, and DigitalOcean's plans start off af $5.00/month for a 512MB RAM
server with 20GB of SSD disk, more than enough for my blog engine.

DigitalOcean_ calls their VPS machines "Droplets", so we will need a minimal
droplet. You can create one using their web controls, or you can do this using
an API they provide for those (like me) who like to script things so repeating
the process is well documented!

