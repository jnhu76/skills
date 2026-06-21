# Boundary Test Suggestions

Use these as templates, not checklists. Adapt to the specific project.

## Generic boundary tests

1. duplicate resource name
2. missing required config
3. invalid schema/frontmatter/metadata
4. broken dependency reference
5. source/resource deleted after previous sync
6. target already has local edits
7. permission denied
8. partial operation failure
9. config conflicts between project and global
10. unsupported OS/path/runtime behavior
11. repeated operation idempotency
12. rollback after failed operation
13. concurrent operation on same resource
14. stale cache or lock
15. dependency unavailable at startup
16. dependency unavailable during operation
17. timeout during external call
18. cancellation during long-running operation
19. malformed external response
20. version mismatch between components

## For skill/sync projects

1. duplicate skill name
2. missing SKILL.md
3. invalid frontmatter
4. broken symlink
5. source deleted after previous sync
6. target already has local edits
7. audit failure
8. partial sync failure
9. project/global config conflict
10. unsupported OS/path
11. repeated sync idempotency
12. rollback after failed sync

## For agent/executor/sandbox projects

1. executor unavailable
2. sandbox startup failure
3. sandbox timeout
4. sandbox cancellation
5. workspace missing
6. workspace permission denied
7. callback lost
8. streaming disconnect
9. duplicate task message
10. concurrent task execution
11. stale distributed lock
12. dependency restart during execution
13. rate limiter backend unavailable
14. token expired during operation
15. malformed tool call result
16. model API timeout
17. event ordering mismatch
18. task recovery after process restart
