# CrackMapExec-PingCastle
CrackMapExec module that execute PingCastle on a remote machine.

## Install

```shell
cd /path/to/crackmapexec/modules/
wget https://raw.githubusercontent.com/TRIKKSS/CrackMapExec-PingCastle/main/pingcastle.py
```

## Usage

```shell
cme smb domain_controller -d domain.local -u someuser -p somepassword -M pingcastle -o options
```

#### OPTIONS

	- PINGC_PATH    path to the PingCastle executable
	- PINGC_CONF    path to the PingCastle config file (optional)
	- PINGC_FLAG    flags for the PingCastle executable (optional)

#### EXAMPLE

```shell
cme smb 172.16.13.35 -u Administrateur -H 552902031BEDE9EFAAD3B435B51404EE:878D8014606CDA29677A44EFA1353FC7 -M pingcastle -o PINGC_PATH=/path/to/PingCastle.exe PINGC_CONF=/path/to/PingCastle.exe.config PINGC_FLAG='--no-enum-limit,--healthcheck'
```