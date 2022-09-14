# insta-bot

### Set your environment
 - Create a virtual environment
```commandline
$ python -m venv {ABSOLUT_PATH_TO_YOUR_VENVS_FOLDER}\insta-bot
```
 - Install dependencies
```commandline
$ pip install -r requeriments.txt
```
 - Download a Selenium WebDriver (this project is using [Firefox WebDriver](https://github.com/mozilla/geckodriver/releases))
 - Add the Selenium WebDriver downloaded to the path
   - On Windows, create a new environment variable pointing to a folder and add this variable to the PATH variable
 - Install [Firefox Browser](https://www.mozilla.org/en-US/firefox/new/) (required because of the InstaPy lib) 
