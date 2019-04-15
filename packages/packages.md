# packages info

- why package
To organise the hierarchy architecture of your program.

- what is package
a filter which including modules and a `__init__.py` file. And this file tells python interpreter all modules this package has.

example:

```bash
- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
    - africa/
        - __init__.py
        - madagascar/
            - __init__.py
            - bar.py
```