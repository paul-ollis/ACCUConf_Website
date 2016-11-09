#!/bin/bash
(cd flask_application_part/accuconf && ln -s -f ../../static_nikola_part/output static)
(cd static_nikola_part/themes/accuconf/templates && ln -s -f ../../../../flask_application_part/accuconf/proposals/templates/accuconf.html accuconf.tmpl)
