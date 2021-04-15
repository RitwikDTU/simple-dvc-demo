1.Create environment -- conda create -n my_env python=3.8 -y
2.activate env -- conda activate my_env
3.Create a requirements.txt file
4.Install the requirements.txt file -- pip install -r requirements.txt
5.create a readme.md file
6.a)create a template.py in which different empty folders and files that we will need are made -- see template.py file
  b)run template.py -- python template.py
7.create a data_given folder too and place the data file in this folder.
8.Initialize our git -- git init
9.Initialize our dvc -- dvc init
10.add data to dvc -- dvc add data_given/winequality.csv
11.add current version/any changes of data present -- git add .
12.finally commit to save all things -- git commit -m "first commit"
13.Create github repository to push all prev stuff
14.make the project remote   -- a)git remote add origin https://github.com/RitwikDTU/simple-dvc-demo.git
                                b)git branch -M main        
15.push to repository -- git push origin main
16. to add content changes to repository -- a) git add . && git commit -m "Update Readme.md"
                                            b) git push origin main
17.To run the full thing -- dvc repro
18.To check for parameters used and scores -- dvc metrics show
19.To check differences from past model parameters & scores -- dvc metrics diff
20.To go to a previous version, go to github repository and then in the commits tab and click on the copy sign beside the 
   commit version you want to switch to and in the cmd write -- git checkout [paste the copied code from github without 
   square brackets]
21.Install pytest and tox and make the required files -- a)tests folder
							 b)tests/test_config.py, tests/conftest.py, tests/__init__.py
							 c)tox.ini file
22.To run the test -- pytest -v
23.To run same test using tox -- tox      ##it will create a virtual environment to run the tests.
24.To reload the tox environment use -- tox -r
25.To check which packages install in the environment -- pip freeze
26.Setup commands:
		a)pip install -e .
27.Build your own package commands:
				  a)python setup.py sdist bdist wheel
28.For linting purpose, pip install flake8 and see the code in tox.ini file