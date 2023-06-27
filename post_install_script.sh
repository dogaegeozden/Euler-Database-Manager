#!/bin/bash

username=${SUDO_USER:-${USER}}

chown -R $username:$username /opt/euler_database_manager/