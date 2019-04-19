import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/testfile.txt')
    assert f.exists
    # Secrets owned by company
    assert f.contains('fe6e74aa-a099-4cc1-ae8e-aa3000d02c14::acme_login1_password')
    assert f.contains('fe6e74aa-a099-4cc1-ae8e-aa3000d02c14::name::acme login 1')
    assert f.contains('fe6e74aa-a099-4cc1-ae8e-aa3000d02c14::username::acme_login1')
    assert f.contains('fe6e74aa-a099-4cc1-ae8e-aa3000d02c14::passwword::acme_login1_password')
    assert f.contains('fe6e74aa-a099-4cc1-ae8e-aa3000d02c14::uri::acme_login1_url1')
    assert f.contains('fe6e74aa-a099-4cc1-ae8e-aa3000d02c14::notes::acme_login1_note')


    #Secrets owned by organization
    assert f.contains('fd8870cc-3659-40aa-9492-aa3000cedbb3::login_p_password')
    assert f.contains('fd8870cc-3659-40aa-9492-aa3000cedbb3::name::login personnal')
    assert f.contains('fd8870cc-3659-40aa-9492-aa3000cedbb3::username::login_p_username')
    assert f.contains('fd8870cc-3659-40aa-9492-aa3000cedbb3::passwword::login_p_password')
    assert f.contains('fd8870cc-3659-40aa-9492-aa3000cedbb3::uri::login_p_uri1')
    assert f.contains('fd8870cc-3659-40aa-9492-aa3000cedbb3::notes::login_p_notes')

