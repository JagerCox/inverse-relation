# Inverse Relation


## Model

![Model](doc-img/ER.png  "Model")

## Install and run Inverse Relation

Install "Inverse Relation" contact form.

```
./install.sh
```

First time and test.

```
./clean-run.sh
```

Use run.sh normally. Use it as debug mode

```
./run.sh
```

Use run.sh normally. Use it on your server with Nignx, Gunicorn and Supervisor.
Remember: You should change on settings_production.py your **ALLOWED_HOSTS**

```
./run-production.sh
```

Finally, try it...

```
http://127.0.0.1:8000/
```

## Screenshots

Screenshot 1
![Inverse relation](doc-img/1.png  "Capture 1")


Screenshot 2
![Inverse relation](doc-img/2.png  "Capture 2")