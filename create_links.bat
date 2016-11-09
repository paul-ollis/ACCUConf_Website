pushd . && cd flask_application_part\accuconf && mklink /D static ..\..\static_nikola_part\output && popd
pushd . && cd flask_application_part\accuconf\proposals\templates && mklink accuconf.html ..\..\..\..\static_nikola_part\themes\accuconf\templates\accuconf.tmpl && popd
