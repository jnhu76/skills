# Review Checklists

## Security Checklist

- What secrets are reachable by default?
- Can the agent read home directories, SSH keys, cloud credentials, browser profiles, env vars, or package manager tokens?
- Can the agent write outside the workspace?
- Can it access Docker socket, host PID namespace, privileged devices, or mounted host paths?
- Can it reach arbitrary internet, private networks, metadata IPs, DNS, proxies, or local services?
- Are package install scripts isolated from later test/patch phases?
- Are denied actions logged with enough detail to explain the decision?

## Performance Checklist

- Is the claimed latency cold, warm, pooled, or snapshot restore?
- Are P50, P95, P99 reported?
- Is concurrency measured?
- Is the workload only create/delete, or full agent task execution?
- Is storage backend fixed?
- Is cache state controlled?
- Are network and package install costs included?

## Runtime + Storage Co-design Checklist

- Does the system rely on CoW snapshots?
- Which filesystem is required?
- What happens on ext4, XFS reflink, overlayfs, loopback, remote disk, or slow block storage?
- How large is the writable layer?
- Does snapshot clone remain fast under many small files?
- Does rollback include disk, memory, process, network, and external effects?

## Lifecycle Checklist

- Are create, pause, resume, checkpoint, rollback, clone, delete, and GC modeled as a state machine?
- Are operations idempotent?
- What happens when control-plane components crash?
- What happens when shim/hypervisor/guest agent becomes unknown?
- Are timeout and retry semantics explicit?
- Can concurrent operations leave leaked resources?
