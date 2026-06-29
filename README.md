# GenPark Query Intent Router Skill

This repository contains the **GenPark Query Intent Router Skill** — an agent configuration skill config (`skill.json`), a production-ready Python SDK client (`intent_router.py`), and executable verification tests. It is designed to evaluate incoming user queries, classify intent categories based on keyword weighting models, and dispatch payloads to matched target endpoints.

---

## 🚀 Capabilities

* **Intent Match Scoring:** Computes confidence ratios for custom keyword matches.
* **Smart Endpoint Fallbacks:** Automatically routes unstructured queries to general fallback paths if confidence metrics fall below safety thresholds.
* **Registry Dispatching:** Integrates with complex API microservices architectures for multi-agent environments.

---

## 🛠️ Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 SDK Usage Reference

```python
from intent_router import IntentRouterClient

client = IntentRouterClient()

route = client.route_query(
    user_query="Can you find a cheap phone?",
    registry=[
        {"intent": "search", "target_endpoint": "https://api.genpark.ai/search", "keywords": ["find", "buy", "cheap"]}
    ]
)

print(f"Matched Intent: {route['matched_intent']}")
print(f"Dispatch URL: {route['dispatch_url']}")
```

---

## 📜 License
This project is licensed under the MIT License.
