@echo off
python $$encrypt.py
cd EncryptedFiles
git init
git add -A **
git commit -a -m "auto commit"
git remote add origin https://github.com/AdaJass/EncryptedFiles.git
git push -u origin master
pause
 