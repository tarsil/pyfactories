# PyFactories

<p align="center">
  <a href="https://esmerald.dymmond.com"><img src="https://res.cloudinary.com/tarsild/image/upload/v1687347327/packages/pyfactories/logo_lvtl5d.png" alt='Esmerald'></a>
</p>


<p align="center">
    <em>🚀 Mock data generation for pydantic and dataclasses. 🚀</em>
</p>

<p align="center">
<a href="https://github.com/tarsil/pyfactories/workflows/Test%20Suite/badge.svg?event=push&branch=main" target="_blank">
    <img src="https://github.com/tarsil/pyfactories/workflows/Test%20Suite/badge.svg?event=push&branch=main" alt="Test Suite">
</a>

<a href="https://pypi.org/project/pyfactories" target="_blank">
    <img src="https://img.shields.io/pypi/v/pyfactories?color=%2334D058&label=pypi%20package" alt="Package version">
</a>

<a href="https://pypi.org/project/pyfactories" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/pyfactories.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: [https://pyfactories.tarsild.io][docs] 📚

**Source Code**: [https://github.com/dymmond/esmerald][github]

---

## Motivation

[Pydantic Factories][pydantic_factories] was initially created and used by a lot of people and it
is an extremely powerful package that was heavily tested by the same authors of Starlite, now,
Litestar. During their own evolution and development they felt the need to add more support to the
package that was no longer only pydantic and therefore they created the [Polyfactory][polyfactory]
and archived the [Pydantic Factories][pydantic_factories].

PyFactories is a literal fork from the latest Pydantic Factories and aims to continue the same
work set by the previous creators with the difference that will be only maintaining the factories
for Pydantic and the upcoming Pydantic 2.0+.

The team behind Pydantic Factories did a fantastic job and the credit goes to them while
**PyFactories** continues its own fork path.

If you aim to use something more than just Pydantic, it is strongly recommended to visit
[Polyfactory][polyfactory] and migrate to it and of course, leave them a ⭐️.

In the meantime if you only want the Pydantic side of things, then you can use **PyFactories** in
the same fashion as its ancestor.

## Installation

```shell
pip install pyfactories
```

## Migrate from Pydantic Factories

It is actually straightforward, you simply need to replace `pydantic_factories` with `pyfactories`
in your imports and that is it.

## Example

```python
from datetime import date, datetime
from typing import List, Union

from pydantic import UUID4, BaseModel

from pyfactories import ModelFactory


class Person(BaseModel):
    id: UUID4
    name: str
    hobbies: List[str]
    age: Union[float, int]
    birthday: Union[datetime, date]


class PersonFactory(ModelFactory):
    __model__ = Person


result = PersonFactory.build()
```

And just its own ancestor, this is it. Almost no work, you are able to create mock data objects
that fits the `Person` Pydantic class model definition.

This is possible because of the typing information available on the pydantic model and model-fields,
which are used as a source of truth for data generation.

The factory parses the information stored in the pydantic model and generates a dictionary of kwargs
that are passed to the `Person` class' `init` method.

## Features

Being initially the fork of [Pydantic Factories][pydantic_factories], that also means:

- ✅ Supports both built-in and pydantic types
- ✅ Supports pydantic field constraints
- ✅ Supports complex field types
- ✅ Supports custom model fields
- ✅ Supports dataclasses
- ✅ Supports TypedDicts

## Why This Library

This library was widely used before because of its powerfull features and therefore with the
upcoming Pydantic 2.0, it will be even more robust with the core done in Rust.

- 💯 Powerful
- 💯 Extensible
- 💯 Simple
- 💯 Rigorously tested

## Contributing

This library is open to contributions. [Please see the contribution guide!][contributing]

## Star the initial authors

Although the intial [Pydantic Factories][pydantic_factories] is no longer maintained, there is
always the [Polyfactory][polyfactory] that deserves a ⭐️.

[docs]: https://pyfactories.tarsild.io
[github]: https://github.com/tarsil/pyfactories
[pydantic_factories]: https://github.com/litestar-org/pydantic-factories
[polyfactory]: https://pypi.org/project/polyfactory/
[contributing]: https://pyfactories.tarsild.io/contributing
