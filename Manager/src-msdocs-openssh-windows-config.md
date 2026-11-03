---
tags: [manager-kb, source]
url: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-server-configuration
type: official-doc
author: Microsoft Learn
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (official doc, full page read)
---
# OpenSSH Server configuration for Windows
## Key claims
- Initial default shell for incoming SSH on Windows is cmd.exe. Set another shell by registry string `HKLM:\SOFTWARE\OpenSSH` value `DefaultShell` = full path (e.g. `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`); does not affect the OpenSSH client. (Changing it is a remote-access config change under our confirm-first list.)
- sshd config is `%programdata%\ssh\sshd_config`; changes need a service restart.
- For users in the Administrators group, keys are read from `%programdata%\ssh\administrators_authorized_keys`, not `~\.ssh\authorized_keys`; that file may only have ACEs for SYSTEM and BUILTIN\Administrators: `icacls.exe "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"`. Wrong ACLs make key auth silently fail.
- Only `password` and `publickey` auth methods exist; Entra account auth unsupported. Domain users must be written `domain\user` in AllowUsers/AllowGroups. `AuthorizedKeysCommand`, `AcceptEnv` etc. are NOT available on the Windows build. ChrootDirectory only for SFTP. `SyslogFacility LOCAL0` writes files under `%programdata%\ssh\logs`, otherwise logs go to ETW.
## Quotable
> The initial default in Windows is the Windows command prompt (cmd.exe).

## Used by
[[topic-cross-device-agent-control]]
