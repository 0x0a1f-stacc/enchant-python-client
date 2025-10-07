---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

## Description
A clear and concise description of what the bug is.

## To Reproduce
Steps to reproduce the behavior:
1. Initialize client with '...'
2. Call method '...'
3. See error

**Code example:**
```python
from enchant_python_client import AuthenticatedClient
from enchant_python_client.api.tickets import get_ticket

client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-token"
)

# Code that produces the error
```

## Expected Behavior
A clear and concise description of what you expected to happen.

## Actual Behavior
What actually happened, including error messages and stack traces.

```
Paste error messages here
```

## Environment
- Python version: [e.g., 3.9.5]
- enchant-python-client version: [e.g., 1.0.0]
- Operating System: [e.g., Ubuntu 22.04, macOS 13.0, Windows 11]
- Installation method: [pip, uv, etc.]

## Additional Context
Add any other context about the problem here, such as:
- Does this work with the official Enchant API documentation?
- Have you tested with different API endpoints?
- Any relevant Enchant API documentation links
