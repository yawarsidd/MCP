## Creating an Environment
1. conda create -p venv python == 3.12
2. conda activate venv/
3. Everytime when we open the vs studio code after cancellation plz activate the conda

## How to deploy that in Github actions needed:

1. Create a file with name README.md and .gitignore in local.
2. Go and create a repo without readme.md file in github. (Which contains all the repo command instructions that can be used further)
3. First step to add the .env file or (venv/) to the .gitignore as the git doesn't track it and push to the github.
4. Second Step write (git init) in the terminal.
5. Third Step write (git add .)
6. Fourth Step write (git commit -m "first commit")
7. Fifth step write (git branch -M main)
8. Sixth step write (git remote add origin https://github.com/yawarsidd/MCP1.git)
9. Seventh step (git push -u origin main)

## To do commit again and again in local file and save changes to the github
1. First step (git add .)
2. second step (git commit -m "Second Commit")
3. Third step (git push origin main)

## To make Git stop tracking .DS_Store and ensure it’s ignored on GitHub, you need to:
1. Add .DS_Store to .gitignore

2. Remove any .DS_Store files that are already tracked using the command:
   
   ### Code
   git rm --cached .DS_Store

   ### Explaination of the above line
   git rm → remove a file from Git tracking.
   --cached → remove it only from Git’s index (staging area), not from your local filesystem.
   .DS_Store → the specific file you want to remove from tracking.

3. git add .gitignore
4. git commit -m "Ignore .DS_Store files"
5. git push origin main

## To delete the old env
rm -rf venv
(make sure you are inside the correct folder)

## ✅ Difference between name vs path
Name-based (most common):

1. conda create -n aienv python=3.10
2. conda activate aienv

Here aienv is just a name, not a folder in your project.

Path-based:

1. conda create -p venv python=3.7
2. conda activate venv/

Writing venv/ makes it clear to Conda that:
this is a path, not a name





