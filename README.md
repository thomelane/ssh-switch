# ssh-switch

Utility to switch Amazon EC2 instances on and off using SSH aliases.

## Install

`pip install .`

## Configure

Since switch on/off commands reference SSH aliases (e.g. `dev.com`), you must
provide a mapping between SSH aliases and InstanceId in the `~/.ssh/config`
file. Custom properties are not allowed so InstanceId is provided as a comment
in the relevant block. As example is shown below:

```bash
Host dev.com
    HostName 123.456.789
    User ec2-user
    IdentityFile ~/.ssh/keypair.pem
    # InstanceId i-123456fabcd1e1234
```

## Commands

* `ssh-switch on dev.com`
* `ssh-switch off dev.com`
