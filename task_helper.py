# Task Addition Module Helper for US-0002
# Ensuring task addition logic is fully robust and encapsulated.

def validate_task_description(desc: str) -> bool:
    return bool(desc and desc.strip())
