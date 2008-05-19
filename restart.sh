rm db
python tennis/manage.py syncdb --noinput
python tennis/manage.py shell < populate.py
python tennis/manage.py runserver
