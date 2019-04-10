# UztozTopBot
## Telegram bot built with Django and Telebot
### live at https://t.me/ustoztopbot

<p align="center">
 <img src="https://raw.githubusercontent.com/azimjohn/ustoztop/master/screen.png" width="500">
</p>

### First get the repo on your machine:
```bash
$ git clone https://github.com/azimjohn/ustoztop.git
```


### Then install requirements:
```bash
$ pip install -r requirements.txt
```

### Make the migrations and apply them:
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### Export the bot token, replace `REPLACE_ME` with your bot's token
```bash
$ export BOT_TOKEN=REPLACE_ME
```

### Finally, run the server 🎉
```bash
$ python manage.py runserver
```

