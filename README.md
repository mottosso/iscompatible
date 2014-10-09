### Python versioning with requirements.txt syntax

iscompatible gives you the power of the [pip requirements.txt][req]
syntax for everyday python packages, modules, classes or arbitrary
functions.

[req]: https://pip.readthedocs.org/en/1.1/requirements.html

The requirements.txt syntax allows you to specify inexact matches
between a set of requirements and a version. For example, let's
assume that the single package foo-5.6.1 exists on disk. The
following requirements are all compatible with foo-5.6.1.

- [Documentation][]
- [Issue tracker][]
- [Wiki][]

[Wiki]: https://github.com/mottosso/iscompatible/wiki
[Issue tracker]: https://github.com/mottosso/iscompatible/issues
[Documentation]: http://iscompatible.readthedocs.org

#### Example

Let's assume that the single package foo-5.6.1 exists on disk.
The following requirements are all compatible with foo-5.6.1.

|Requirement | Description
|------------|--------------------------------------------------
|foo         |any version of foo
|foo>=5      |any version of foo, above or equal to 5
|foo>=5.6    |any version of foo, above or equal to 5.6
|foo==5.6.1  |exact match
|foo>5       |foo-5 or greater, including minor and patch
|foo>5, <5.7 |foo-5 or greater, but less than foo-5.7
|foo>0, <5.7 |any foo version less than foo-5.7

#### Usage

```python
>>> iscompatible("foo>=5", (5, 6, 1))
True
>>> iscompatible("foo>=5.6.1, <5.7", (5, 0, 0))
False
>>> MyPlugin = type("MyPlugin", (), {'version': (5, 6, 1)})
>>> iscompatible("foo==5.6.1", MyPlugin.version)
True
```
