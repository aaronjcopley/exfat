# exfat
Spec file for building the exfat project (https://github.com/relan/exfat) as 
the fuse-exfat and exfat-utils RPMs. 

This project can be built locally, but it is intended to be used by a COPR
repository.

See: https://copr.fedorainfracloud.org/coprs/aaronjcopley/exfat/

## Installation

    dnf copr enable aaronjcopley/exfat
    dnf install fuse-exfat exfat-utils

## Compatibility
This project is meant to provide a solution for EL8. RPM Fusion previously
provided these packages for EL7 and earlier, while exFAT is mainline in EL9.

Additionally, while EPEL ships exfatprogs for EL8, it is not able to mount
exFAT file systems. As such, this package conflicts with exfatprogs.
