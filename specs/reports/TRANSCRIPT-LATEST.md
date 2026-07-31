# Conversation Transcript

## ScrumOrchestrator
- 🔧 `init_scrum_state()`
- 🔧 `create_litellm_virtual_key(max_budget, agent_name)`
- 🔧 `create_litellm_virtual_key(max_budget, agent_name)`
- 🔧 `create_litellm_virtual_key(max_budget, agent_name)`
- 🔧 `create_litellm_virtual_key(agent_name, max_budget)`
- 🔧 `create_litellm_virtual_key(max_budget, agent_name)`
- 🔧 `create_litellm_virtual_key(max_budget, agent_name)`
- 🔧 `transfer_to_agent(agent_name)`

## ProductOwner
- 🔧 `list_docs()`
- 🔧 `upsert_prd(filename, content)`
- 🔧 `update_roadmap(version, stories, goals)`
- 🔧 `upsert_epic(epic)`
- 🔧 `upsert_story(story)`
- 🔧 `upsert_story(story)`
- 🔧 `advance_story_stage(stage, title_or_id)`
- 🔧 `advance_story_stage(title_or_id, stage)`
- 🔧 `transfer_to_agent(agent_name)`

## DevTeam
- 🔧 `list_docs()`
- 🔧 `read_doc(path)`
- 🔧 `read_doc(path)`
- 🔧 `read_doc(path)`
- 🔧 `upsert_adr(status, title, context, decision, consequences)`
- 🔧 `plan_sprint_backlog_item(plan, title_or_id)`
- 🔧 `plan_sprint_backlog_item(plan, title_or_id)`
- 🔧 `start_feature_branch(slug, story_id)`
- 🔧 `write_file(content, path, overwrite)`
- 🔧 `write_file(overwrite, content, path)`
- 🔧 `write_file(overwrite, content, path)`
- 🔧 `write_file(overwrite, path, content)`
- 🔧 `write_file(content, overwrite, path)`
- 🔧 `git_push(commit_message, branch)`
- 🔧 `log_story_tokens(title_or_id, actual_tokens)`
- 🔧 `advance_story_stage(title_or_id, stage)`
- 🔧 `git_push(commit_message, branch)`
- 🔧 `gh_pr_checks(watch)`
- 🔧 `mark_pr_ready_for_review(pr_id)`
- 🔧 `transfer_to_agent(agent_name)`

## Architect
- 🔧 `gh_pr_review(event, body, pr_id)`
- 🔧 `gh_pr_comment(body, pr_id)`
- 🔧 `advance_story_stage(stage, title_or_id)`
- 🔧 `transfer_to_agent(agent_name)`

## QA
- 🔧 `check_build()`
- 🔧 `gh_pr_comment(body, pr_id)`
- 🔧 `advance_story_stage(stage, title_or_id)`
- 🔧 `transfer_to_agent(agent_name)`

## DevTeam
- 🔧 `write_file(path, content, overwrite)`
- 🔧 `git_push(commit_message, branch)`
- 🔧 `transfer_to_agent(agent_name)`

## QA
- 🔧 `check_build()`
- 🔧 `gh_pr_comment(body, pr_id)`
- 🔧 `advance_story_stage(stage, title_or_id)`
- 🔧 `transfer_to_agent(agent_name)`

## DevTeam
- 🔧 `write_file(path, content, overwrite)`
- 🔧 `git_push(branch, commit_message)`
- 🔧 `transfer_to_agent(agent_name)`

## QA
- 🔧 `check_build()`
- 🔧 `gh_pr_comment(pr_id, body)`
- 🔧 `advance_story_stage(title_or_id, stage)`
- 🔧 `transfer_to_agent(agent_name)`

## DevTeam
- 🔧 `write_file(path, overwrite, content)`
- 🔧 `git_push(branch, commit_message)`
- 🔧 `transfer_to_agent(agent_name)`

## QA
- 🔧 `check_build()`
- 🔧 `gh_pr_comment(pr_id, body)`
- 🔧 `advance_story_stage(stage, title_or_id)`
- 🔧 `transfer_to_agent(agent_name)`

## ScrumMaster
- 🔧 `add_impediment(owner, description)`
- 🔧 `add_retro_action(action, owner, success_metric)`
- 🔧 `transfer_to_agent(agent_name)`

## DevTeam
- 🔧 `transfer_to_agent(agent_name)`

## QualityGuardian
- 🔧 `calculate_kpis()`
- 🔧 `update_sprint_report(kpis)`
- 🔧 `upsert_issue(issue)`
- 🔧 `transfer_to_agent(agent_name)`

## ScrumOrchestrator
- 🔧 `transfer_to_agent(agent_name)`

## ProductOwner
- 🔧 `transfer_to_agent(agent_name)`

## ScrumMaster
- 🔧 `generate_workflow_diagram()`
- 🔧 `gather_workflow_improvement_proposals()`
- 🔧 `calculate_cost_breakdown()`
- 🔧 `recommend_sprint_budget()`
- 🔧 `transfer_to_agent(agent_name)`

## ScrumOrchestrator
- 🔧 `transfer_to_agent(agent_name)`

## ProductOwner
- 🔧 `create_sprint_report(summary, accomplishments)`
