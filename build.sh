set -o errexit 

poetry install 

python manage.py collectstatic --no-input 
python manage.py migrate

pip install --upgrade pip
pip install --force-reinstall -U setuptools