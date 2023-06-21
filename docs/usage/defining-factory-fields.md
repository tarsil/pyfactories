# Defining Factory Fields

The factory api is designed to be as semantic and simple as possible, lets look at several examples that assume we have
the following models:

```python
{!> ../docs_src/usage/factory-fields/example1.py !}
```

In this case when we call `PersonFactory.build()` the result will be randomly generated, except the pets list, which
will be the hardcoded default we defined.

## Use

This though is often not desirable. We could instead, define a factory for `Pet` where we restrict the choices to a
range we like. For example:

```python
{!> ../docs_src/usage/factory-fields/example2.py !}
```

The signature for use is: `cb: Callable, *args, **defaults`, it can receive any sync callable. In the above example, we
used the `choice` function from the standard library's `random` package, and the batch method of `PetFactory`.

You do not need to use the `Use` field, **you can place callables (including classes) as values for a factory's
attribute** directly, and these will be invoked at build-time. Thus, you could for example re-write the
above `PetFactory` like so:

```python
{!> ../docs_src/usage/factory-fields/example3.py !}
```

`Use` is merely a semantic abstraction that makes the factory cleaner and simpler to understand.

## Global factory registration

Sometimes you want to alter how a model is built by default. It is especially useful for a model that is used a lot across the project. In this case updating attributes to reference specific factory everywhere can be quite cumbersome. Instead
you can rely on auto registering models by setting the `__auto_register__` attribute`.

```python
{!> ../docs_src/usage/factory-fields/example4.py !}
```

Here if we call `PersonFactory.build()` the result will be randomly generated except the pet list which will
contain a dog with the name `Ralph` or `Roxy`. Notice that in this case we didn't have to define the `pets`
attribute in the `PersonFactory` because we have registered `PetFactory` as the default factory for the `Pet`
model.

## PostGenerated

It allows for post generating fields based on already generated values of other (non post generated) fields. In most
cases this pattern is best avoided, but for the few valid cases the `PostGenerated` helper is provided. For example:

```python
{!> ../docs_src/usage/factory-fields/example5.py !}
```

The signature for use is: `cb: Callable, *args, **defaults`, it can receive any sync callable. The signature
for the callable should be: `name: str, values: dict[str, Any], *args, **defaults`. The already generated
values are mapped by name in the `values` dictionary.

## Ignore

`Ignore` is another field exported by this library, and its used - as its name implies - to designate a given attribute
as ignored:

```python
{!> ../docs_src/usage/factory-fields/example6.py !}
```

The above example is basically the extension included in `pyfactories` for the
library [ODMantic](https://github.com/art049/odmantic), which is a pydantic based mongo ODM.

For ODMantic models, the `id` attribute should not be set by the factory, but rather handled by the odmantic logic
itself. Thus, the `id` field is marked as ignored.

When you ignore an attribute using `Ignore`, it will be completely ignored by the factory - that is, it will not be set
as a kwarg passed to pydantic at all.

## Require

The `Require` field in turn specifies that a particular attribute is a **required kwarg**. That is, if a kwarg with a
value for this particular attribute is not passed when calling `factory.build()`, a `MissingBuildKwargError` will be
raised.

What is the use case for this? For example, lets say we have a document called `Article` which we store in some DB and
is represented using a non-pydantic model, say, an `elastic-dsl` document. We then need to store in our pydantic object
a reference to an id for this article. This value should not be some mock value, but must rather be an actual id passed
to the factory. Thus, we can define this attribute as required:

```python
{!> ../docs_src/usage/factory-fields/example7.py !}
```

If we call `factory.build()` without passing a value for article_id, an error will be raised.

## Fixture

The `Fixture` field is a special field meant to be used with factories that have been decorated using
[register_fixture](./pytest-fixtures.md). For example:

```python
{!> ../docs_src/usage/factory-fields/example8.py !}
```

If we tried to use `PersonFactory` now normally it wouldn't work because pytest fixtures can only be called by pytest.
Thus we can use `Fixture`. As you can see above, this field can accept kwargs that are passed to the factory's
underlying build or batch methods, and an optional `size` kwarg. If `size` is given, than a batch is returned, otherwise
the normal build method is used.
