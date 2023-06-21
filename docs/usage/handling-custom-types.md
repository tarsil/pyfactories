# Handling Custom Types

If your model has an attribute that is not supported by `pyfactories` and
it depends on third party libraries, you can create your custom extension
subclassing the `ModelFactory`, and overriding the `get_mock_value` method to
add your logic.

```python
{!> ../docs_src/usage/custom-types/example1.py !}
```

Where `cls.get_faker()` is a `faker` instance that you can use to build your
returned value.
