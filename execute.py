import github
import datetime
import requests
import json

def execute():
    config = json.loads(open('./config.json', 'r', encoding='utf-8').read())
    g = github.Github(login_or_token=config['token'])

    slugpath = config['slugpath']
    dog = json.loads(requests.get('https://dog.ceo/api/breeds/image/random').text)['message']
    sha = json.loads(requests.get(f'https://api.github.com/repos/{slugpath}/contents/README.md').text)['sha']

    readme = open('./README.md', 'r', encoding='utf-8').read()
    content = readme.replace('{{fact}}', f'[🐕 Random dog!]({dog})')

    repo = g.get_repo(slugpath, lazy=False)
    repo.delete_file(path='README.md', message=f'Auto-update README.md ({datetime.date.today().strftime("%B %d, %Y")})', branch='main', sha=sha)
    repo.create_file(path='README.md', message=f'Auto-update README.md ({datetime.date.today().strftime("%B %d, %Y")})', content=content, branch='main')

    print(f'Updated README.md ;) ({datetime.date.today().strftime("%B %d, %Y")})')