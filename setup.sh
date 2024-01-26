echo "[ `date` ]": "START"
echo "[ `date` ]": "Creating env with python 3.9" 
python -m venv venv/
echo "[ `date` ]": "activate venv"
# for windows
# venv\Scripts\activate
source ./venv/bin/activate
echo "[ `date` ]": "installing the requirements" 
pip install -r requirements.txt
echo "[ `date` ]": "END" 