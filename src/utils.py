
import json
def parse_json_safely(payload: str) -> dict:
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        return {}

