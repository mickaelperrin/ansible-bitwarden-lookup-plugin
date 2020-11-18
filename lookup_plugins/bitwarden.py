# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from bitwarden_simple_cli.Bitwarden import Bitwarden
__metaclass__ = type

DOCUMENTATION = """
lookup: bitwarden
author: Mickaël Perrin <contact@mickaelperrin.fr>
version_added: "1.0"
short_description: fast lookup of secrets stored in bitwarden
description:
  - This plugin uses the bitwarden-simple-cli python module that implements a faster way to retrieve
    secrets from a bitwarden vault.
requirements:
  - pip module bitwarden-simple-cli
  - BW_SESSION environment variable retrieven through the `bw unlock` command.
options:
  _uuid:
    description: uuid of the cipher to retrieve
    required: True
  field:
    description: the name of the field to be retrieven
      (name, username, password, notes, uri or any custom field)
    default: password
    required: False
"""

EXAMPLES = """
- name: get 'password'
  debug:
    msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c1' }}"
- name: get 'password'
  debug:
    msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c1', field='password' }}"
- name: get 'username'
  debug:
    msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c1', field='username' }}"
- name: get 'custom_field'
  debug:
    msg: "{{ lookup('bitwarden', 'fe6e74aa-a099-4cc1-ae8e-aa3000d02c1', field='custom_field' }}"
"""

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def run(self, uuids, **kwargs):
        ret = []
        field = kwargs.get('field', 'password')
        for uuid in uuids:
            display.debug("Bitwarden lookup field: %s of uuid: %s" % (field, uuid))
            try:
                app = Bitwarden()
                result = app.get(uuid, field)
                if result is not None:
                    ret.append(result.rstrip().decode('utf-8'))
                else:
                    raise AnsibleError("could not find field: %s" % field)
            except SystemExit as e:
                raise AnsibleError(e.code)
            except AnsibleParserError:
                raise AnsibleError("could not locate uuid: %s" % uuid)
        return ret
