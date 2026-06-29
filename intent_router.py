import os
from typing import List, Dict, Any, Optional

class IntentRouterClient:
    """
    Production-grade routing classifier that maps natural queries to specific API endpoints.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ROUTER_API_KEY")

    def route_query(self, user_query: str, registry: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Classifies query based on keyword overlap ratio and targets dispatch endpoints.
        """
        if not user_query.strip():
            return {
                "matched_intent": "fallback",
                "confidence_score": 0.0,
                "dispatch_url": "https://api.genpark.ai/v1/fallback"
            }

        query_clean = user_query.lower()
        best_intent = "fallback"
        best_url = "https://api.genpark.ai/v1/fallback"
        max_score = 0.0

        for target in registry:
            intent = target.get("intent")
            endpoint = target.get("target_endpoint")
            keywords = target.get("keywords", [])

            # Compute match count
            matches = sum(1 for kw in keywords if kw.lower() in query_clean)
            
            # Normalize score relative to keyword length
            score = round(matches / len(keywords), 2) if keywords else 0.0
            
            if score > max_score:
                max_score = score
                best_intent = intent
                best_url = endpoint

        # Standard safety check fallback
        if max_score < 0.2:
            best_intent = "fallback"
            best_url = "https://api.genpark.ai/v1/fallback"
            max_score = 0.0

        return {
            "matched_intent": best_intent,
            "confidence_score": max_score,
            "dispatch_url": best_url
        }
