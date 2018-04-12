# JTracker

NOTE: This software is under active development and may do nothing at all yet, or not work correctly.

A player for a JSON based variant of the MOD tracker format.

## Setup

```
$ git clone ...
$ cd jtracker
$ virtualenv -q -p $(which python3) --no-site-packages --distribute .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ pip install -e .
```

## Documentation

[.jt file format](docs/jt-format.md)

[.mod file format](docs/mod-format.md)

## Development

Before submitting a PR...

Verify style:

```
$ make style
```

Run unit tests:

```
$ make test
```