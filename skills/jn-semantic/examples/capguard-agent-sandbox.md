# Example: Extracting Semantics from Agent Sandbox

## 1. First-Principles Goal

Agent sandbox exists to preserve useful task capability while reducing dangerous OS-visible effects.

```text
Useful capability: search repo, install dependencies, run tests, patch code.
Dangerous effects: read secrets, exfiltrate data, write outside workspace, access docker.sock.
```

## 2. Primitive Operations

| Operation | Meaning |
|---|---|
| read | agent reads files or env |
| write | agent modifies files |
| execute | agent runs commands |
| network | agent connects to external endpoints |
| rollback | system restores previous state |
| learn | system learns policy from trace |
| verify | system checks trace against policy/intent |

## 3. Objects

| Object | Semantic meaning |
|---|---|
| repo source | usually legitimate |
| `.env` | secret exposure risk |
| `~/.ssh` | default deny |
| package registry | install-stage capability |
| unknown endpoint | exfiltration risk |
| docker.sock | host-control capability |

## 4. States / Stages

| Stage | Network semantics |
|---|---|
| install | registry allowlist may be allowed |
| test | network usually denied unless integration test |
| patch | network usually denied |
| summarize | execution/network should be denied |

## 5. Observable Effects

| Effect | Example |
|---|---|
| files_read | `src/foo.py`, `.env` |
| files_written | `src/foo.py`, `/etc/hosts` |
| network_connect | `pypi.org`, unknown IP |
| permission_denied | deny reason |
| rollback_result | restored / partial / failed |

## 6. Rules

| Condition | Operation | Expected behavior |
|---|---|---|
| stage=test | network unknown host | deny |
| stage=install | network pypi.org | allow if allowlisted |
| any stage | read `~/.ssh/id_rsa` | deny |
| stage=patch | write repo source | allow + diff-track |
| after rollback | external HTTP POST | must not claim recovered |

## 7. Research Gap

Rollback semantics are unclear unless we distinguish local rollbackable effects from external non-rollbackable effects.

Minimal experiment:

```text
checkpoint → modify file → HTTP POST → rollback
```

Expected result:

```text
file can be restored;
external HTTP side effect cannot be restored.
```
