# Nested Models

The automatic generation of mock data works for all types supported by pydantic, as well as nested classes that derive
from `BaseModel` (including for 3rd party libraries) and complex types. Let's look at another example:

```python
{!> ../docs_src/usage/nest-models/example1.py !}
```

This example will also work out of the box although no factory was defined for the Pet class, that's not a problem - a
factory will be dynamically generated for it on the fly.

The complex typing under the `assets` attribute is a bit more tricky, but the factory will generate a python object
fitting this signature, therefore passing validation.

**Please note**: the one thing factories cannot handle is self referencing models, because this can lead to recursion
errors. In this case you will need to handle the particular field by setting defaults for it.
