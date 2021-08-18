export FLASK_APP=routes.py 
cd src
py -3 -m venv venv
venv\Scripts\activate
pip3 install -r requirements.txt
flask run
