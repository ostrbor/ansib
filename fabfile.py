from fabric.api import task, local

CMD = 'ansible-playbook provision.yml '
CMD_SECURE = 'ansible-playbook provision-secure.yml --ask-vault-pass --ask-pass '
CHECK_PARAM = '--check '


@task
def user_proxy():
    local(CMD_SECURE + '--limit proxy')


@task
def up_proxy():
    local(CMD + '-u admin --limit proxy')


@task
def user_prod():
    local(CMD_SECURE + '--limit production')


@task
def up_prod():
    local(CMD + '--limit production')
