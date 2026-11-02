import pytest
from agents.scrum_team.tools.github import _develop_branch_name

def test_develop_branch_name():
    branch = _develop_branch_name()
    assert branch is not None
    assert isinstance(branch, str)
