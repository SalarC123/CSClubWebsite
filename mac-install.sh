export FLASK_APP=routes.py 
cd src
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
flask run
