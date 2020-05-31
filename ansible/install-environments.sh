#!/bin/bash

export ANSIBLE_HOST_KEY_CHECKING=False
. ./openrc.sh; ansible-playbook --ask-become-pass install_environments.yaml -i inventory/hosts.ini