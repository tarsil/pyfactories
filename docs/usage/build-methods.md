# Build Methods

The `ModelFactory` class exposes two build methods:

- `.build(**kwargs)` - builds a single instance of the factory's model
- `.batch(size: int, **kwargs)` - build a list of size n instances

```python
{!> ../docs_src/usage/build-methods/example1.py !}
```

Any `kwargs` you pass to `.build`, `.batch` or any of the [persistence methods](./persistence.md), will take precedence over
whatever defaults are defined on the factory class itself.

By default, when building a pydantic class, kwargs are validated, to avoid input validation you can use the `factory_use_construct` param.

```python
{!> ../docs_src/usage/build-methods/example2.py !}
```

## Partial Parameters

Factories can randomly generate missing parameters for child factories. For example:

```python
{!> ../docs_src/usage/build-methods/partial-params.py !}
```

When building a person without specifying the Person and pets ages, all these fields will be randomly generated:

```python
{!> ../docs_src/usage/build-methods/partial-params2.py !}
```

```json
{
  "name": "John",
  "pets": [
    {
      "name": "dog",
      "age": 9005
    },
    {
      "name": "cat",
      "age": 2455
    }
  ],
  "age": 975
}
```
