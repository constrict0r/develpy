import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
    'curl',
    'emacs'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


def test_home_file(host):
    f = host.file('/home/mary')

    assert f.exists
    assert f.user == 'mary'


@pytest.mark.parametrize('file, content', [
  ('/home/mary/.vimrc',
   'syntax on')
])
def test_vim_file(host, file, content):
    f = host.file(file)

    assert f.exists
    assert f.contains(content)
    assert f.user == 'mary'


@pytest.mark.parametrize('file, content', [
  ('/home/mary/.emacs.d/init.el',
   'package-initialize')
])
def test_emacs_file(host, file, content):
    f = host.file(file)

    assert f.exists
    assert f.contains(content)
    assert f.user == 'mary'
