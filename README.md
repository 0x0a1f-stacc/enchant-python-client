# enchant-python-client

[![CI](https://github.com/0x0a1f-stacc/enchant-python-client/workflows/CI/badge.svg)](https://github.com/0x0a1f-stacc/enchant-python-client/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python client library for the [Enchant.com](https://www.enchant.com) REST API with support for both synchronous and asynchronous operations.

## ⚠️ Important Disclaimer

This is an **unofficial** Python client for the Enchant.com API.

- **Not affiliated with** Senvee Inc or Enchant.com
- **Not endorsed by** Senvee Inc or Enchant.com
- **Not maintained by** Senvee Inc or Enchant.com

This client was created based on publicly available [API documentation](https://dev.enchant.com/api/v1) and is provided as-is under the MIT License. Use at your own risk.

For official support, please contact Enchant at https://www.enchant.com

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Tickets](#tickets)
  - [Messages](#messages)
  - [Customers](#customers)
  - [Attachments](#attachments)
  - [Users](#users)
  - [Async Usage](#async-usage)
- [Advanced Usage](#advanced-usage)
- [API Coverage](#api-coverage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

- ✅ **Full API Coverage** - Supports all Enchant REST API v1 endpoints
- ✅ **Sync & Async** - Both synchronous and asynchronous request methods
- ✅ **Type Hints** - Full type annotations for better IDE support
- ✅ **Auto-generated** - Generated from OpenAPI 3.0 specification
- ✅ **Python 3.9+** - Modern Python support
- ✅ **Context Managers** - Proper resource cleanup with `with` statements
- ✅ **Flexible Auth** - Bearer token and HTTP Basic authentication
- ✅ **Customizable** - Built on httpx with extensive configuration options

## Installation

### Using pip

```bash
pip install enchant-python-client
```

### Using uv

```bash
uv add enchant-python-client
```

### From source

```bash
git clone https://github.com/0x0a1f-stacc/enchant-python-client.git
cd enchant-python-client
uv build --wheel
pip install dist/*.whl
```

## Quick Start

```python
from enchant_python_client import AuthenticatedClient
from enchant_python_client.api.tickets import list_tickets

# Create an authenticated client
client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-api-token"
)

# List all open tickets
with client as client:
    tickets = list_tickets.sync(client=client, state=["open"])
    for ticket in tickets:
        print(f"#{ticket.number}: {ticket.subject}")
```

## Usage

### Authentication

Get your API token from your Enchant account settings.

```python
from enchant_python_client import AuthenticatedClient

# Standard Bearer token authentication
client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-api-token"
)

# HTTP Basic Auth (token as username, any password)
client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-api-token",
    prefix="",  # Empty prefix for Basic Auth
)
```

### Tickets

```python
from enchant_python_client.api.tickets import (
    list_tickets,
    get_ticket,
    create_ticket,
    update_ticket,
    add_labels_to_ticket,
)
from enchant_python_client.models import TicketUpdate

with client as client:
    # List tickets with filters
    open_tickets = list_tickets.sync(
        client=client,
        state=["open"],
        per_page=50,
        page=1
    )

    # Get a specific ticket with embedded data
    ticket = get_ticket.sync(
        client=client,
        ticket_id="abc123",
        embed=["customer", "messages", "labels"]
    )

    # Create a new ticket
    new_ticket_data = {
        "type": "email",
        "subject": "Need help with billing",
        "customer_id": "customer123",
        "inbox_id": "inbox456",
        "user_id": "user789"
    }
    new_ticket = create_ticket.sync(client=client, body=new_ticket_data)

    # Update a ticket
    update = TicketUpdate(state="closed", user_id="user789")
    updated = update_ticket.sync(
        client=client,
        ticket_id="abc123",
        body=update
    )

    # Add labels
    add_labels_to_ticket.sync(
        client=client,
        ticket_id="abc123",
        label_ids=["label1", "label2"]
    )
```

### Messages

```python
from enchant_python_client.api.messages import create_message
from enchant_python_client.models import (
    MessageCreateNote,
    MessageCreateOutboundReply,
)

with client as client:
    # Create an internal note
    note = MessageCreateNote(
        type="note",
        user_id="user123",
        body="Customer called to follow up",
        htmlized=False
    )
    message = create_message.sync(
        client=client,
        ticket_id="ticket123",
        body=note
    )

    # Send an outbound reply
    reply = MessageCreateOutboundReply(
        type="reply",
        direction="out",
        user_id="user123",
        to="customer@example.com",
        body="Thanks for contacting us! Here's the solution...",
        htmlized=False
    )
    message = create_message.sync(
        client=client,
        ticket_id="ticket123",
        body=reply
    )
```

### Customers

```python
from enchant_python_client.api.customers import (
    list_customers,
    get_customer,
    create_customer,
    update_customer,
)
from enchant_python_client.models import CustomerInput, ContactInput

with client as client:
    # List customers
    customers = list_customers.sync(client=client, per_page=100)

    # Get a specific customer
    customer = get_customer.sync(client=client, customer_id="cust123")

    # Create a customer
    new_customer = CustomerInput(
        first_name="John",
        last_name="Doe",
        contacts=[
            ContactInput(type="email", value="john@example.com"),
            ContactInput(type="phone", value="+1234567890")
        ]
    )
    customer = create_customer.sync(client=client, body=new_customer)

    # Update a customer
    update = CustomerInput(
        first_name="Jane",
        last_name="Doe"
    )
    updated = update_customer.sync(
        client=client,
        customer_id="cust123",
        body=update
    )
```

### Attachments

```python
from enchant_python_client.api.attachments import create_attachment, get_attachment
from enchant_python_client.models import AttachmentCreate
import base64

with client as client:
    # Upload an attachment
    with open("document.pdf", "rb") as f:
        file_data = base64.b64encode(f.read()).decode("utf-8")

    attachment = AttachmentCreate(
        name="document.pdf",
        type="application/pdf",
        data=file_data
    )
    created = create_attachment.sync(client=client, body=attachment)

    # Get attachment metadata
    attachment_info = get_attachment.sync(
        client=client,
        attachment_id=created.id
    )

    # Use attachment in a message
    note = MessageCreateNote(
        type="note",
        user_id="user123",
        body="Attached the requested document",
        htmlized=False,
        attachment_ids=[created.id]
    )
```

### Users

```python
from enchant_python_client.api.users import list_users

with client as client:
    # List all users in your help desk
    users = list_users.sync(client=client)
    for user in users:
        print(f"{user.first_name} {user.last_name} ({user.email})")
```

### Async Usage

All API methods have async equivalents:

```python
import asyncio
from enchant_python_client import AuthenticatedClient
from enchant_python_client.api.tickets import list_tickets, get_ticket

async def main():
    client = AuthenticatedClient(
        base_url="https://yoursite.enchant.com/api/v1",
        token="your-api-token"
    )

    async with client as client:
        # List tickets asynchronously
        tickets = await list_tickets.asyncio(
            client=client,
            state=["open"]
        )

        # Get detailed response with status code
        response = await get_ticket.asyncio_detailed(
            client=client,
            ticket_id="abc123"
        )
        print(f"Status: {response.status_code}")
        print(f"Ticket: {response.parsed}")

asyncio.run(main())
```

## Advanced Usage

### Custom HTTP Client Configuration

```python
from enchant_python_client import AuthenticatedClient

# Custom timeout
client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-api-token",
    timeout=30.0  # 30 seconds
)

# Custom SSL verification
client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-api-token",
    verify_ssl="/path/to/certificate.pem"
)

# Disable SSL verification (not recommended for production)
client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-api-token",
    verify_ssl=False
)
```

### Request/Response Hooks

```python
from enchant_python_client import AuthenticatedClient

def log_request(request):
    print(f"→ {request.method} {request.url}")

def log_response(response):
    print(f"← {response.status_code}")

client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-api-token",
    httpx_args={
        "event_hooks": {
            "request": [log_request],
            "response": [log_response]
        }
    }
)
```

### Pagination

```python
from enchant_python_client.api.tickets import list_tickets

with client as client:
    page = 1
    per_page = 100

    while True:
        tickets = list_tickets.sync(
            client=client,
            state=["open"],
            page=page,
            per_page=per_page
        )

        if not tickets:
            break

        for ticket in tickets:
            print(f"#{ticket.number}: {ticket.subject}")

        page += 1
```

### Error Handling

```python
from enchant_python_client import AuthenticatedClient
from enchant_python_client.api.tickets import get_ticket
from enchant_python_client.models import Error
import httpx

client = AuthenticatedClient(
    base_url="https://yoursite.enchant.com/api/v1",
    token="your-api-token",
    raise_on_unexpected_status=True
)

try:
    with client as client:
        response = get_ticket.sync_detailed(
            client=client,
            ticket_id="invalid-id"
        )

        if isinstance(response.parsed, Error):
            print(f"API Error: {response.parsed.message}")
        else:
            print(f"Ticket: {response.parsed.subject}")

except httpx.TimeoutException:
    print("Request timed out")
except Exception as e:
    print(f"Error: {e}")
```

## API Coverage

This client supports all Enchant REST API v1 endpoints:

| Resource | Endpoints |
|----------|-----------|
| **Tickets** | List, Get, Create, Update, Add Labels, Remove Labels |
| **Messages** | Create (Notes, Inbound Replies, Outbound Replies) |
| **Customers** | List, Get, Create, Update |
| **Contacts** | Create, Delete |
| **Attachments** | Create (Upload), Get |
| **Users** | List |

For detailed API documentation, see: https://dev.enchant.com/api/v1

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repository
git clone https://github.com/0x0a1f-stacc/enchant-python-client.git
cd enchant-python-client

# Install dependencies
uv sync

# Run linting
uv run ruff check enchant_python_client/
uv run ruff format enchant_python_client/

# Build distribution
uv build

# Regenerate client from OpenAPI spec
./scripts/regenerate.sh
```

### Project Structure

- `openapi.yaml` - OpenAPI 3.0 specification (source of truth)
- `enchant_python_client/` - Auto-generated client code
- `scripts/regenerate.sh` - Regenerate client from spec
- `CLAUDE.md` - AI coding assistant guidance
- `CONTRIBUTING.md` - Contribution guidelines

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Reporting Issues

- [Bug Reports](.github/ISSUE_TEMPLATE/bug_report.md)
- [Feature Requests](.github/ISSUE_TEMPLATE/feature_request.md)

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run linting: `uv run ruff check && uv run ruff format`
5. Update `CHANGELOG.md`
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Alfredo Ruiz

## Acknowledgments

- Generated using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
- Built with [httpx](https://www.python-encode.io/httpx/) and [attrs](https://www.attrs.org/)
- OpenAPI specification based on [Enchant API documentation](https://dev.enchant.com/api/v1)

## Links

- **Official Enchant Website**: https://www.enchant.com
- **Enchant API Documentation**: https://dev.enchant.com/api/v1
- **GitHub Repository**: https://github.com/0x0a1f-stacc/enchant-python-client
- **Issue Tracker**: https://github.com/0x0a1f-stacc/enchant-python-client/issues
