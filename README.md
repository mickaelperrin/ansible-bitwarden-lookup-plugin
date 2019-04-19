Bitwarden Lookup Plugin
=========

This is a simple lookup plugin that search for secrets in a Bitwarden vault. 
It uses the [bitwarden-simple-cli](https://github.com/mickaelperrin/bitwarden-decrypt-cli) python module that 
greatly improve performance.

Requirements
------------

You require:
- python 3.7
- bitwarden-simple-cli module

```
pip3 install bitwarden-simple-ci
```

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: mickaelperrin.ansible-bitwarden-lookup-plugin
      tasks
        - debug:
            msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c14', field='name') }}"
        - debug:
            msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c14', field='username') }}"
        - debug:
            msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c14', field='password') }}"
        - debug:
            msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c14', field='my_custom_field_name') }}"
        - debug:
            msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c14', field='uri') }}"
        - debug:
            msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c14', field='notes') }}"            

Tests
-----

Tests are managed by `pytest` for the python part and `molecule` for the ansible part with `docker` as driver.

```
mkvirtualenv3 ansible-bitwarden-lookup-plugin
pip install -r requirements.txt
```

### Pytest

```
pytest
``` 

### Molecule

Ensure that `docker` service is up and running

```
molecule test
``` 

License
-------

GPLv3

