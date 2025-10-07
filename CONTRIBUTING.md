# Contributing to enchant-python-client

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Important Disclaimer

This is an **unofficial** Python client for the Enchant.com API. It is:
- **Not affiliated with** Senvee Inc or Enchant.com
- **Not endorsed by** Senvee Inc or Enchant.com
- **Not maintained by** Senvee Inc or Enchant.com

This client was created based on publicly available API documentation and is provided as-is under the MIT License.

## How to Contribute

### Reporting Bugs

Before creating a bug report:
1. Check the [existing issues](https://github.com/0x0a1f-stacc/enchant-python-client/issues)
2. Verify you're using the latest version
3. Test with the official Enchant API documentation at https://dev.enchant.com/api/v1

When creating a bug report, include:
- Python version
- Client version
- Minimal code to reproduce the issue
- Expected vs actual behavior
- Error messages and stack traces

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
1. Check existing issues and pull requests first
2. Provide a clear use case
3. Explain how it aligns with the Enchant API
4. Include code examples if applicable

### Pull Requests

1. **Fork the repository** and create a branch from `main`

2. **Install development dependencies**:
   ```bash
   uv sync
   ```

3. **Make your changes**:
   - If modifying the OpenAPI spec (`openapi.yaml`), regenerate the client:
     ```bash
     ./scripts/regenerate.sh
     ```
   - Follow the existing code style (Ruff configuration in `pyproject.toml`)
   - Add or update tests if applicable

4. **Run code quality checks**:
   ```bash
   uv run ruff check enchant_python_client/
   uv run ruff format enchant_python_client/
   ```

5. **Update documentation**:
   - Update `CHANGELOG.md` with your changes under `[Unreleased]`
   - Update `README.md` if you've added new features
   - Update `CLAUDE.md` if you've changed architecture

6. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Reference issue numbers if applicable (e.g., "Fix #123: ...")

7. **Submit a pull request**:
   - Provide a clear description of the changes
   - Link to related issues
   - Explain the motivation and impact

## Development Workflow

### Project Structure

```
enchant-python-client/
├── enchant_python_client/  # Generated client code
│   ├── api/               # API endpoint functions
│   ├── models/            # Data models
│   ├── client.py          # Client classes
│   ├── errors.py          # Exception classes
│   └── types.py           # Type utilities
├── scripts/               # Utility scripts
├── openapi.yaml           # Source of truth (OpenAPI spec)
├── pyproject.toml         # Project metadata
└── README.md             # User documentation
```

### Regenerating the Client

The client code in `enchant_python_client/` is **auto-generated** from `openapi.yaml`:

```bash
./scripts/regenerate.sh
```

**Important**:
- Do not manually edit files in `enchant_python_client/api/` or `enchant_python_client/models/`
- These will be overwritten when regenerating
- Custom logic should go in separate wrapper classes

### Code Style

- Line length: 120 characters
- Linting: Ruff (F, I, UP rules)
- Type hints: Encouraged but not required (attrs handles models)
- Docstrings: Follow existing patterns in generated code

### Testing

While this project doesn't currently have a comprehensive test suite, contributions adding tests are welcome:

```bash
# Run tests (when implemented)
pytest
```

## OpenAPI Specification Changes

When updating `openapi.yaml`:

1. **Verify against Enchant's official docs**: https://dev.enchant.com/api/v1
2. **Validate the spec**: GitHub Actions will automatically validate on PR
3. **Regenerate the client**: Use `./scripts/regenerate.sh`
4. **Test the changes**: Ensure the generated code works as expected
5. **Update CHANGELOG.md**: Document what API changes were reflected

## Release Process

(For maintainers)

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`:
   - Move `[Unreleased]` changes to new version section
   - Add release date
3. Create a git tag: `git tag -a vX.Y.Z -m "Version X.Y.Z"`
4. Push tag: `git push origin vX.Y.Z`
5. Build and publish:
   ```bash
   uv build
   uv publish
   ```

## Questions?

- Check the [README.md](README.md) for usage documentation
- Check the [official Enchant API docs](https://dev.enchant.com/api/v1)
- Open an [issue](https://github.com/0x0a1f-stacc/enchant-python-client/issues) for questions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
