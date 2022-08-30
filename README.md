# ansible-automation

## Commands executed

ssh-keygen
cd ~/.ssh/
cat id_rsa.pub | ssh altruist@192.168.18.13 "cat - >> ~/.ssh/authorized_keys"
ansible-config init --disabled > ansible.cfg
ansible-vault create passwd.yml
ansible-vault edit passwd.yml
ansible-playbook --ask-vault-pass --extra-vars '@passwd.yml' playbook.yml

TODO:
    ansible vault passwords must be considered instead of plaintext passwords





