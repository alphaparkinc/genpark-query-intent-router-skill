import sys
import json
from intent_router import IntentRouterClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== GenPark Intent Router Verification ===")
    client = IntentRouterClient()

    registry = [
        {
            "intent": "track_order",
            "target_endpoint": "https://api.genpark.ai/v1/orders/track",
            "keywords": ["track", "order", "where is", "delivery", "status"]
        },
        {
            "intent": "search_products",
            "target_endpoint": "https://api.genpark.ai/v1/products/search",
            "keywords": ["find", "buy", "search", "looking for", "cheap"]
        }
    ]

    # Test Query A: Match tracking intent
    query_a = "Where is my order? Can you track the delivery status?"
    print(f"\n[Test A] Routing Query: '{query_a}'")
    result_a = client.route_query(query_a, registry)
    print(json.dumps(result_a, indent=2))

    # Test Query B: Fallback matching
    query_b = "I want to apply for a job at your company"
    print(f"\n[Test B] Routing Query: '{query_b}'")
    result_b = client.route_query(query_b, registry)
    print(json.dumps(result_b, indent=2))

if __name__ == "__main__":
    main()
