import pytest
from os import path
from lookup_plugins.bitwarden import LookupModule
from ansible.errors import AnsibleError

def common_data(item):
    return dict(
        BW_SESSION='Tyy0rDgzvA/jgHsqUtKIgNnAWaRtHKZoSs6pa10qWQf0QmFtd2/xn8TNJy8Fu2nPRNVDpn3k7tu49W1pQVU8Zg==',
        nl='\n',
        organization_id='1ff51ccd-0a25-46a2-a3cd-aa3000cfa874',
        protected_key='ArxoewBOPtCYZKqn34f8CoMQVUrNZnrhGU9OYuJu8UpB7DngEwf/TEHjbxPJJhUDG+DnPQR76J9d12/4tnGT5C6ZaLxxInRooT4AuX2ljIrSppCee1AvzIMu7ljGhR++ng==',
        protected_key_decoded=b'/lCGAMDGAq+mjRP3FJv+VNDDnbrYcVGnsiPeXTm4NfU=',
        test_database_filename='data.json',
        user_email='dev+bitwarden@mickaelperrin.fr',
        user_id='03780246-7f1d-4221-8615-aa3000cd8123',
        uuid_login_organization='fe6e74aa-a099-4cc1-ae8e-aa3000d02c14',
        uuid_login_personal='fd8870cc-3659-40aa-9492-aa3000cedbb3',
        uuid_note_personal='450cbad2-580b-4523-bce8-aa3000cf641a'
    ).get(item)


@pytest.fixture
def bw_session(monkeypatch):
    monkeypatch.setenv('BW_SESSION', common_data('BW_SESSION'))
    monkeypatch.setenv('BITWARDENCLI_APPDATA_DIR', path.join(path.dirname(__file__), '..', 'molecule', 'default', 'tests'))


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_password(capsys):
    LookupModule().run([common_data('uuid_login_organization')], field='password')
    std = capsys.readouterr()
    assert std.out == 'acme_login1_password'


@pytest.mark.usefixtures("bw_session")
def test_get_login_organization_password(capsys):
    with pytest.raises(AnsibleError) as e:
        LookupModule().run(['missing-uuid'], field='password')
    assert e.type == AnsibleError
    assert e.value.message == 'Unable to find entry with id: missing-uuid'
