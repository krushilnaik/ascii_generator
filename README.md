# ASCII Generator

Final project for INF 360 - Programming with Python

# Setup

```
pip install -r requirements.txt
```

A SQLite database is included in `db.sqlite3`, but you can freshly seed it with:

```
python manage.py seed
```

You can also replace `management/commands/alphabet.txt` with your own alphabet, provided it's in a similar format to the provided one, i.e. a "header" line followed by the ASCII representation

```
63 '?'
.####.
#....#
....#.
...#..
......
...#..
......
```

# Start-up

```
python manage.py runserver [<PORT>]
```

Where `<PORT>` is optional (defaults to 8000)
