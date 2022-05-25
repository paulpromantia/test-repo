Install Python3 in the system
Install pip3 in the system

Install Virtual env using below commands
    pip3 install virtualenv
    virtualenv --python=python3 venv1  OR python3 -m venv .

Now go inside the newly created Folder i.e venv1
    cd venv1/
    source bin/activate

Install the dependencies by going into this folder i.e GetCricketer and running this command
    pip3 install -r requirements.txt

Once all the steps done is successful, please run the below command to start the application
    python3 GetCricketerDetail.py
