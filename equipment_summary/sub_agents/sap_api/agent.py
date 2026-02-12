# equipment_summary/sub_agents/sap_api/agent.py

# from google.adk.agents import FunctionAgent

from . import prompt

MODEL = "gemini-2.5-pro"

def call_sap_api_tool():
    """
    Placeholder for interacting with SAP APIs.
    User will provide details for this later.
    """
    # print(f"Calling SAP API endpoint: {endpoint} for equipment ID: {equipment_id}")
    # In a real implementation, this would make an actual API call
    # and return the response.
   
    return [
        {"order_id": "SO001", "description": "Routine maintenance", "status": "Completed", "customer": "ABC Corp", "location": "L01","locationName":"london", "requieredweather": "sunny","priority": "low", "skillsneeded": "electrials", "requestedStartDate": "07.02.2026"},
        {"order_id": "SO002", "description": "Component replacement", "status": "In Progress", "customer": "ABC Corp", "location": "L01","locationName":"paris", "requieredweather": "sunny","priority": "high", "skillsneeded": "electrials", "requestedStartDate": "10.02.2026"},
        {"order_id": "SO003", "description": "Tower Maintenance", "status": "Open", "customer": "ABC Corp", "location": "L01", "locationName":"london", "requieredweather": "sunny","priority": "very high", "skillsneeded": "mechanicals", "requestedStartDate": "19.02.2026"},
        {"order_id": "SO004", "description": "Tower Maintenance", "status": "Open", "customer": "ABC Corp", "location": "L02", "locationName":"paris", "requieredweather": "windy","priority": "high", "skillsneeded": "electrials", "requestedStartDate": "17.02.2026"},
        {"order_id": "SO005", "description": "Tower Maintenance", "status": "Open", "customer": "ABC Corp", "location": "L01", "locationName":"london", "requieredweather": "sunny","priority": "medium", "skillsneeded": "instrumentation", "requestedStartDate": "17.02.2026"},
        {"order_id": "SO006", "description": "Tower Maintenance", "status": "Open", "customer": "XYZ Corp", "location": "L03", "locationName":"tokyo", "requieredweather": "rainy","priority": "low", "skillsneeded": "IT", "requestedStartDate": "15.02.2026"},
        {"order_id": "SO007", "description": "Tower Maintenance", "status": "Open", "customer": "XYZ Corp", "location": "L04", "locationName":"london", "requieredweather": "sunny", "priority": "high", "skillsneeded": "intrumentation", "requestedStartDate": "13.02.2026"},
    ]
    # return {"data": "API response placeholder", "endpoint": endpoint, "equipment_id": equipment_id}


# sap_api_agent = FunctionAgent(
#     model=MODEL,
#     function=_call_sap_api_tool,
#     name="sap_api_agent",
#     instruction=prompt.SAP_API_PROMPT
# )