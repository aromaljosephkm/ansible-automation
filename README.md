# Chronicle Server Configuration Automation - Ansible
Project for DevOps

## Ansible - an overview
> Ansible is an open sourceIT automation tool that automates provisioning, configuration management, application deployment, orchestration, and many other manual IT processes. Ansible users can use Ansible automation to install software, automate daily tasks, provision infrastructure, improve security and compliance, patch systems, and share automation across the entire organization.

## Ansible - Our Usecase
> Our plan is to edit the configuration of the chronicle servers together whenever it is needed. So we will be using ansible to ssh into the chronicle servers as root and then will have to change the contents of the configuration XML file.

## How it's done
- Created ansible.cfg file using ***ansible-config init --disabled > ansible.cfg***
- Updated the values of ***inventory, roles_path***
- Create the inventory file
- SSH Public Key sharing
    - Create a SSH Key ***ssh-keygen***
    - Copy the Public Key from ***~/.ssh/*** to the other system using the command ***cat id_rsa.pub | ssh username@ip_address "cat - >> ~/.ssh/authorized_keys"*** to the authorized keys.
- There are roles defined for each operation in the playbook. Uncomment the roles needed.

## Things to Do:
 >- Indentation must be considered on adding configurations
 >- Ansible vault passwords must be considered instead of plaintext passwords.





