---
description: "Task list for Phase I: In-Memory console Todo App"
---

# Tasks: Phase I In-Memory Console Todo App

**Input**: Design documents from `/specs/001-phase-i-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: US1 (Create), US2 (View), US3 (Complete), US4 (Update), US5 (Delete)

## Phase 1: Setup

- [X] T001 Initialize Python project structure (src/todo/, tests/)
- [X] T002 [P] Configure pytest for unit testing
- [X] T003 [P] Add .gitignore for Python

## Phase 2: Foundational

- [X] T004 Implement Task model in src/todo/models.py (id, description, is_completed)
- [X] T005 Implement base TodoService class with in-memory storage in src/todo/service.py
- [X] T006 [P] Create test fixtures for TodoService in tests/conftest.py

---

## Phase 3: User Story 1 - Task Creation (Priority: P1) 🎯 MVP

- [X] T007 [P] [US1] Unit test for add_task in tests/unit/test_service.py
- [X] T008 [US1] Implement add_task in src/todo/service.py (Depends on T005)

**Checkpoint**: Users can add tasks to the in-memory store.

---

## Phase 4: User Story 2 - Viewing Tasks (Priority: P1)

- [X] T009 [P] [US2] Unit test for list_tasks in tests/unit/test_service.py
- [X] T010 [US2] Implement list_tasks in src/todo/service.py

**Checkpoint**: Users can retrieve the list of added tasks.

---

## Phase 5: User Story 3 - Marking Completion (Priority: P1)

- [X] T011 [P] [US3] Unit test for complete_task in tests/unit/test_service.py
- [X] T012 [US3] Implement complete_task in src/todo/service.py

**Checkpoint**: Task status can be toggled to completed.

---

## Phase 6: User Story 4 - Updating Tasks (Priority: P2)

- [X] T013 [P] [US4] Unit test for update_task in tests/unit/test_service.py
- [X] T014 [US4] Implement update_task in src/todo/service.py

---

## Phase 7: User Story 5 - Deleting Tasks (Priority: P2)

- [X] T015 [P] [US5] Unit test for delete_task in tests/unit/test_service.py
- [X] T016 [US5] Implement delete_task in src/todo/service.py

---

## Phase 8: CLI Interface (US1-US5 Interaction)

- [X] T017 Implement TodoCLI control loop in src/todo/cli.py
- [X] T018 Connect CLI to TodoService methods
- [X] T019 Create src/main.py entry point
- [X] T020 [P] Implement input validation for empty descriptions and invalid IDs

---

## Phase 9: Polish

- [X] T021 Manual verification of all CRUD operations via console
- [X] T022 [P] Verify SC-004: Clean application exit
- [X] T023 Final code cleanup and documentation update in quickstart.md
