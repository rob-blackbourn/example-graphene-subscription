# Graphene Subscription Example

Note this **requires graphene v3** which at the time of writing (2020-05-20) is in pre-release.

## Usage

1. Create a virtual environment for Python 3.7 or later.
2. Activate the virtual environment,
3. Install the packages,
4. Run the example `subscribe.py`.

```bash
$ python3.7 -m venv .venv
$ . .venv/bin/activate
(.venv)$ python setup.py install
(.venv)$ python subscribe.py
```

## Notes

A graphene/graphql schema requires a query to be valid. In this example there
is no need for a query, but i must exist to make the schema valid.
