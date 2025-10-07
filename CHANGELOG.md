# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup with OpenAPI 3.0.0 specification
- Auto-generated Python client using openapi-python-client
- Support for synchronous and asynchronous API calls
- Bearer token and HTTP Basic authentication
- Comprehensive models for Tickets, Messages, Customers, Contacts, Attachments, and Users
- Project documentation (README.md, CLAUDE.md, CONTRIBUTING.md)
- MIT License
- GitHub Actions for OpenAPI spec validation
- Scripts for client regeneration

## [1.0.0] - 2025-10-06

### Added
- Initial release of enchant-python-client
- Full support for Enchant REST API v1
- Ticket management (create, list, get, update, add/remove labels)
- Message operations (create notes, inbound/outbound replies)
- Customer management (create, list, get, update)
- Contact management (create, delete)
- Attachment handling (upload, retrieve)
- User listing
- Context manager support for proper resource cleanup
- Type hints and attrs-based models
- Python 3.9+ compatibility
- uv package manager support

[Unreleased]: https://github.com/0x0a1f-stacc/enchant-python-client/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/0x0a1f-stacc/enchant-python-client/releases/tag/v1.0.0
