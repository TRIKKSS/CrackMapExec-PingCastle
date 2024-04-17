# PingCastle CME NXC

CrackMapExec / NetExec module that execute PingCastle on a remote machine.

## Install

### Manual

```bash
# CrackMapExec
wget https://raw.githubusercontent.com/TRIKKSS/CrackMapExec-PingCastle/main/pingcastle.py -O /path/to/crackmapexec/modules/pingcastle.py
# NetExec
wget https://raw.githubusercontent.com/TRIKKSS/CrackMapExec-PingCastle/main/pingcastle-nxc.py -O /path/to/netexec/modules/pingcastle.py
```

### BlackArch

```bash
# CrackMapExec
pacman -S crackmapexec-pingcastle
# NetExec
pacman -S netexec-pingcastle
```

Ref. [PKGBUILD](https://github.com/BlackArch/blackarch/tree/master/packages/pingcastle-cme-nxc/PKGBUILD)

## Usage

```bash
# CrackMapExec
cme smb $DC_HOST -d $DOMAIN -u $USER -p $PASSWORD -M pingcastle -o <options>
# NetExec
nxc smb $DC_HOST -d $DOMAIN -u $USER -p $PASSWORD -M pingcastle -o <options>
```

#### Options

```bash
# CrackMapExec
cme smb -M pingcastle --options
# NetExec
nxc smb -M pingcastle --options
# Output
            PINGC_PATH    path to the PingCastle executable
            PINGC_CONF    path to the PingCastle config file (optional)
            PINGC_FLAG    flags for the PingCastle executable (optional)
```

#### EXAMPLE

```bash
nxc smb 172.16.13.35 -u Administrateur -H 552902031BEDE9EFAAD3B435B51404EE:878D8014606CDA29677A44EFA1353FC7 -M pingcastle -o PINGC_PATH=/path/to/PingCastle.exe PINGC_CONF=/path/to/PingCastle.exe.config PINGC_FLAG='--no-enum-limit,--healthcheck'
```
