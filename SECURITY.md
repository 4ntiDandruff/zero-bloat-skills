# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| 1.x     | Yes       |

## Reporting a Vulnerability

Megapass Intra Solusindo takes security, resource isolation, and OPSEC hygiene seriously across all 21 zero-bloat skills.

If you discover a security vulnerability (such as unintended remote code execution, token leakage, or unsafe shell expansion):

1. **Do not create a public GitHub issue.**
2. Report privately via email to: `inigue31@gmail.com` with the subject tag `[SECURITY: zero-bloat-skills]`.
3. Provide reproducible steps, proof-of-concept shell snippets, and the affected skill name.
4. We will acknowledge receipt within 48 hours and coordinate a coordinated disclosure patch.

## Operational Security (OPSEC) Standards

All skills strictly conform to zero-bloat safety directives:
* **Zero Credential Hardcoding**: API tokens and SSH keys must remain isolated in environment files (`.env`).
* **Resource Fuses**: Background daemons must implement circuit limits to avoid infinite retry loops or storage exhaustion.
* **Non-Destructive Defaults**: Automated operations cannot execute destructive actions without explicit interactive confirmation.
