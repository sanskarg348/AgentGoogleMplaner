# equipment_summary/sub_agents/sap_api/agent.py

# from google.adk.agents import FunctionAgent

from . import prompt

MODEL = "gemini-2.5-pro"

def call_sap_api_tool(endpoint: str, equipment_id: str, location):
    """
    Placeholder for interacting with SAP APIs.
    User will provide details for this later.
    """
    print(f"Calling SAP API endpoint: {endpoint} for equipment ID: {equipment_id}")
    # In a real implementation, this would make an actual API call
    # and return the response.
   
    return [
        {"order_id": "SO001", "description": "Routine maintenance", "status": "Completed", "customer": "ABC Corp", "location": "L01","locationdescr":"london"},
        {"order_id": "SO002", "description": "Component replacement", "status": "In Progress", "customer": "ABC Corp", "location": "L01","locationdescr":"Whitefield"},
        {"order_id": "SO003", "description": "Tower Maintenance", "status": "Open", "customer": "ABC Corp", "location": "L01", "locationdescr":"london"},
        {"order_id": "SO004", "description": "Tower Maintenance", "status": "Open", "customer": "ABC Corp", "location": "L02", "locationdescr":"JP Nagar"},
        {"order_id": "SO005", "description": "Tower Maintenance", "status": "Open", "customer": "ABC Corp", "location": "L01", "locationdescr":"london"},
        {"order_id": "SO006", "description": "Tower Maintenance", "status": "Open", "customer": "XYZ Corp", "location": "L03", "locationdescr":"Mysore"},
        {"order_id": "SO007", "description": "Tower Maintenance", "status": "Open", "customer": "XYZ Corp", "location": "L04", "locationdescr":"london"}
    ]
    # return {"data": "API response placeholder", "endpoint": endpoint, "equipment_id": equipment_id}


# sap_api_agent = FunctionAgent(
#     model=MODEL,
#     function=_call_sap_api_tool,
#     name="sap_api_agent",
#     instruction=prompt.SAP_API_PROMPT
# )