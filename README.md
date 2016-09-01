## Dev environment
### Front-end

```
cd price/static/js
npm install
webpack
```

### Back-end

dependencies

```
mkvirtualenv book
pip install -r requirements.txt
```

run

```
python manage.py server
```

db

```
createuser username -P
createdb dbname -O username -E UTF8 -e
```

migrate

```
python manage.py db upgrade
```
