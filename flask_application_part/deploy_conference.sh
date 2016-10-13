#!/bin/sh

chmod -R go+rX accuconf*

rsync -rav --delete  --exclude __pycache__/ --exclude accuconf/static accuconf accuconf_config.py accuconf.wsgi conference@dennis.accu.org:/srv/conference.accu.org/public/htdocs/
