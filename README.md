# CrackMapExec-PingCastle
CrackMapExec module that execute PingCastle on a remote machine.

## Install

```shell
cd /path/to/crackmapexec/modules/
wget https://raw.githubusercontent.com/TRIKKSS/CrackMapExec-PingCastle/main/pingcastle.py
```

## Usage

```shell
cme smb 172.16.13.35 -u Administrateur -H aad3b435b51404eeaad3b435b51404ee:a5d91b2f7f87d36e43c35b010bc943a5 -M pingcastle -o PINGC_PATH=/path/to/PingCastle.exe PINGC_CONF=/path/to/PingCastle.exe.config PINGC_FLAG='--no-enum-limit,--healthcheck'
```