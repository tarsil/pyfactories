# Persistence

`ModelFactory` has four persistence methods:

- `.create_sync(**kwargs)` - builds and persists a single instance of the factory's model synchronously
- `.create_batch_sync(size: int, **kwargs)` - builds and persists a list of size n instances synchronously
- `.create_async(**kwargs)` - builds and persists a single instance of the factory's model asynchronously
- `.create_batch_async(size: int, **kwargs)` - builds and persists a list of size n instances asynchronously

To use these methods, you must first specify a sync and/or async persistence handlers for the factory:

```python
{!> ../docs_src/usage/persistence/example1.py !}
```

Or create your own base factory and reuse it in your various factories:

```python
{!> ../docs_src/usage/persistence/example2.py !}
```

With the persistence handlers in place, you can now use all persistence methods. Please note - you do not need to define
any or both persistence handlers. If you will only use sync or async persistence, you only need to define the respective
handler to use these methods.

## Create Factory Method

If you prefer to create a factory imperatively, you can do so using the `ModelFactory.create_factory` method. This method receives the following arguments:

- model - the model for the factory.
- base - an optional base factory class. Defaults to the factory class on which the method is called.
- kwargs - a dictionary of arguments correlating to the class vars accepted by ModelFactory, e.g. **faker**.

You could also override the child factory's `__model__` attribute to specify the model to use and the default kwargs as shown as the BuildPet class as shown below:

```python
{!> ../docs_src/usage/persistence/example3.py !}
```
