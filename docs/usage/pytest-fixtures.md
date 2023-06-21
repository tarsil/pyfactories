# Using Factories as Fixtures

Any class from `ModelFactory` can use the decorator to register as a fixture easily.

The model factory will be registered as a fixture with the name in snake case.

e.g. `PersonFactory` -> `person_factory`

The decorator also provides some pytest-like arguments to define the fixture. (`scope`, `autouse`, `name`)

```python
{!> ../docs_src/usage/fixtures/example.py !}
```

Use `pytest --fixtures` will show output along these lines:

```sh
------------- fixtures defined from pyfactories.plugins.pytest_plugin -------------
cool_guy_factory [session scope] -- pyfactories/plugins/pytest_plugin.py:48
    A cool guy factory

person_factory -- pyfactories/plugins/pytest_plugin.py:48
    A person factory

```
