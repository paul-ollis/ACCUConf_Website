#!/bin/bash
pushd . && cd flask_application_part/accuconf && ln -s ../../static_nikola_part/output static && popd
pushd . && cd flask_application_part/accuconf/proposals/templates && ln -s ../../../../static_nikola_part/themes/accuconf/templates/accuconf.tmpl accuconf.html && popd

