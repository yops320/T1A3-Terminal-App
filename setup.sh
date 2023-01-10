#! /bin/bash
echo "Welcome to recipe selector" 
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Oh no! 
     Python 3 is needed. Install here https://www.python.org/downloads/' >&2
  exit 1
fi
echo "Working"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Done"