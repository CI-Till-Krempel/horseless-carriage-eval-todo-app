# Steering Proposals

## DevTeam
- Proposed By: ScrumMaster
- Pull Request: https://github.com/CI-Till-Krempel/horseless-carriage-eval-todo-app/pull/754

### Rationale
Recurring retrospective findings across sprints 2 and 3 highlighted the need for strict adherence to story workflow and stage transition rules, avoiding missing requirements like SQLAlchemy in dependencies.

### Proposed Content
```
# DevTeam Identity & Workflow Customization

- Always strictly follow the story workflow (Draft -> Ready -> Implemented -> Reviewed -> Tested -> Accepted).
- Never advance a story or skip stage transition gates without fulfilling all requirements (such as matching test suites and build requirements in `requirements.txt`).
- Ensure all dependency changes are validated locally via `check_build` before submitting for review.

```

## DevTeam
- Proposed By: ScrumMaster
- Pull Request: https://github.com/CI-Till-Krempel/horseless-carriage-eval-todo-app/pull/760

### Rationale
Addressing recurring technical process findings regarding workflow stage verification and strict adherence to story workflow rules (SPEC-ISSUE-0003 and SPEC-ISSUE-0004).

### Proposed Content
```
- DevTeam must strictly adhere to story workflow stages and verify schema/model compatibility before marking items Implemented.
```
