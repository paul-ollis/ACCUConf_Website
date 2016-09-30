[![Build Status](https://travis-ci.org/ACCUConf/ACCUConf_Website.svg?branch=master)](https://travis-ci.org/ACCUConf/ACCUConf_Website)

Static page content: ![Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)

Flask application code: [![Licence](https://img.shields.io/badge/license-GPL_3-green.svg)](https://www.gnu.org/licenses/gpl-3.0.txt)


# ACCU Conference Website

## Introduction

This repository contains the framework for the [ACCU Conference website](http://conference.accu.org)
(http://conference.accu.org). The driver and manager of the dynamic content is a Flask application, the
static content is managed as a Nikola website. It is assumed that Python 3 is used for both Flask and
Nikola.

## The Toolchain

Git, obviously, but also [Nikola](https://getnikola.com/) and [Flask](http://flask.pocoo.org/).

Many operating system distributions package Nikola and Flask (some only the Python 2 version though :-( If
there is not a suitable package then creating a virtualenv and installing Nikola and Flask from PyPI using
pip works well – Python 3 being the most senble choice of Python obviously.

## The Licence

All text material in the Nikola managed part of this repository is licenced
under
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nd-nc/4.0/). The
code of the Flask application is licenced under
the [GNU Public Licence version 3](https://www.gnu.org/licenses/gpl-3.0.en.html) (GPLv3).
