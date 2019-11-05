Steps
1) create new virtual env 
2) python3 -m venv zomatoenv
3) source zomatoenv/bin/activate  #readme will also be moved to zomatoenv so refer zomatoenv/Readme.md
4) mv  -v submission/* zomatoenv/  
5) cd zomatoenv/rreview
6) pip3 install -r ../requirements.txt
7) python manage.py runserver
### DB used sqlite
