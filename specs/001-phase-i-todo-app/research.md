# Implementation Research: Phase I Todo App

## Decisions

### 1. Unique ID Generation
- **Decision**: Use an auto-incrementing integer starting from 1.
- **Rationale**: Simple, human-readable for CLI input, and sufficient for in-memory session.
- **Alternatives**: UUID (rejected as too complex for console session interaction).

### 2. State Management
- **Decision**: Use a Python dictionary within the `TodoService` class where keys are IDs and values are `Task` objects.
- **Rationale**: Provides O(1) lookup, update, and deletion by ID.
- **Alternatives**: List of objects (rejected due to O(N) selection performance).

### 3. CLI Input Loop
- **Decision**: Implement a `while True` loop in `cli.py` that handles input parsing and dispatches to the service layer.
- **Rationale**: Standard pattern for console applications. Ensures application stays alive until "Exit" is chosen.

### 4. Input Validation
- **Decision**: Strict validation for empty strings and non-numeric lookup IDs.
- **Rationale**: Required by Success Criteria SC-003 to handle errors without crashing.

## Architecture Patterns

### Clean Architecture Layers
1. **Entities**: `Task` class (data structure).
2. **Use Cases**: `TodoService` class (adds logic like "mark complete", "update description").
3. **Interface Adapters**: `TodoCLI` class (translates user input into Service calls).
