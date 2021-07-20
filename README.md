# randomdog

![img](https://raw.githubusercontent.com/ajskateboarder/stuff/main/Screenshot%202021-07-23%20075316.png)

randomdog can edit a `README.md` file daily to display, of course, a random dog image link!
The link is displayed where there is the text: `{{fact}}`. 
You can use `{{fact}}` in multiple places but it will show the same image.

### Can it show anything else?

Of course it can! But you will need to do this on your own.

### How do I use this?

Usage of this program is not too hard. Just go into the settings page of your Github account.
Then go to Developer settings, and create a personal access token.

In addition to your token, you need an existing repo with a `README.md` file in it.
Use the slugpath (ex: torvalds/linux)

And throw both of these things into the `config.json` file. After that, open up a console window and type `python auto.py`
