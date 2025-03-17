```
sudo apt install python3.12-venv
python3 -m venv test_env
source test_env/bin/activate
cd flask
pip3 install -r requirements.txt
```



```ssh
MW_API_KEY=xbqiunvwxdnksvtucxdywxehecupgqnawjxy MW_TARGET=https://dc47-103-156-143-126.ngrok-free.app:443 MW_VCS_COMMIT_SHA=a7ba8abeb9599b6acaab83d4e314108d1860d754 MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_SERVICE_NAME=test-16 middleware-run flask run
```