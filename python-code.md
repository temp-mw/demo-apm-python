```
sudo apt install python3.12-venv
python3 -m venv test_env
source test_env/bin/activate
cd flask
pip3 install -r requirements.txt
```



```ssh
MW_API_KEY=xbqiunvwxdnksvtucxdywxehecupgqnawjxy MW_TARGET=https://7f5e-103-156-143-126.ngrok-free.app:443 MW_GIT_COMMIT_SHA=7b53fa6773fb83ebe6df92e33aa02267f00546db MW_GIT_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python middleware-run python app.py
```