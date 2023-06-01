# Site_Portfolio

The project for study Django.

#Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.


  1.Firstly, create and activate a new virtual environment:

    python3.9 -m venv ../venv
    source ../venv/bin/activate

  2.Install packages:

    pip install --upgrade pip
    pip install -r requirements.txt

  3.Run project dependencies, migrations, fill the
  
    ./manage.py migrate
    ./manage.py runserver 
