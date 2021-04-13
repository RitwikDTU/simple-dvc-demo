1.Create environment -- conda create -n my_env python=3.8 -y
2.activate env -- conda activate my_env
3.Create a requirements.txt file
4.Install the requirements.txt file -- pip install -r requirements.txt
5.create a readme.md file
6.create a template.py in which different empty folders and files that we will need are made -- see template.py file
7.create a data_given folder too and place the data file in this folder.
8.Initialize our git -- git init
9.Initialize our dvc -- dvc init
10.add data to dvc -- dvc add data_given/winequality.csv
11.add current version/any changes of data present -- git add .
12.finally commit to save all things -- git commit -m "first commit"
13.Create github repository to push all prev stuff
14.make the project remote   -- a)git remote add origin https://github.com/RitwikDTU/simple-dvc-demo.git
                                b)git branch -M main        
15.push to repository -- git push -u origin main
16. to add content changes to repository -- a) git add . && git commit -m "Update Readme.md"
                                            b) git push origin main