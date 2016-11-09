pushd . && cd flask_application_part\accuconf && mklink /D static ..\..\static_nikola_part\output && popd
pushd . && cd static_nikola_part\themes\accuconf\templates && mklink accuconf.tmpl ..\..\..\..\flask_application_part\accuconf\proposals\templates\accuconf.html && popd
