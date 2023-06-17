# Checkmk extension for Dell MD Storage Server

![build](https://github.com/jiuka/checkmk_dell_mdss/workflows/build/badge.svg)
![flake8](https://github.com/jiuka/checkmk_dell_mdss/workflows/Lint/badge.svg)
![pytest](https://github.com/jiuka/checkmk_dell_mdss/workflows/pytest/badge.svg)

This check monitors the Dell MD Storage Server Needs Attention flag by SNMP.

> :warning: I do **NOT** have access to the hardware to test this any more.

Is known to work with:

 * MD34xx
 * MD3860

# Example Output
## OK
```
MD MD-SAN0 - DELL MD34xx 2701 (WWID: 0123456789abcdef0123456789abcdef)
```
## Warning
```
MD MD-SAN0 - DELL MD34xx 2701 (WWID: 0123456789abcdef0123456789abcdef), Needs Attention
```

## Development

For the best development experience use [VSCode](https://code.visualstudio.com/) with the [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension. This maps your workspace into a checkmk docker container giving you access to the python environment and libraries the installed extension has.

## Directories

The following directories in this repo are getting mapped into the Checkmk site.

* `agents`, `checkman`, `checks`, `doc`, `inventory`, `notifications`, `pnp-templates`, `web` are mapped into `local/share/check_mk/`
* `agent_based` is mapped to `local/lib/check_mk/base/plugins/agent_based`
* `nagios_plugins` is mapped to `local/lib/nagios/plugins`

## Continuous integration
### Local

To build the package hit `Crtl`+`Shift`+`B` to execute the build task in VSCode.

`pytest` can be executed from the terminal or the test ui.

### Github Workflow

The provided Github Workflows run `pytest` and `flake8` in the same checkmk docker conatiner as vscode