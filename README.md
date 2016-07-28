# ACCU Conference Website

## Introduction

This repository contains the general framework for the Nikola managed content of the ACCU Conference website
(http://conference.accu.org). The driver and manager of the dynamic content is the
[ACCUConfWebsite_Flask](https://github.com/ACCUConf/ACCUConfWebsite_Flask) repository, this
ACCUConfWebsite_Static repository is for the static content and the blog.

## The Branches

The master branch contains the generic common material, the year specific branches contain the material for
that year's conference. Only one year specific branch is ever active. Pull requests for generic stuff should
be made to master for merging into the year specific branch. Year specific material must be  in pull
requests for the year specific branch. Obvious but worth being explicit about.

## The Toolchain

Git, obviously, but also [Nikola](https://getnikola.com/).

Many operating system distributions package Nikola (some only the Python 2 version though :-( If there is
not a suitable package then creating a virtualenv and installing Nikola from PyPI using pip works well –
Python 3 being the most senble choice of Python obviously.

## The Licence

![Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)

All material in this repository is licenced under
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nd-nc/4.0/)
