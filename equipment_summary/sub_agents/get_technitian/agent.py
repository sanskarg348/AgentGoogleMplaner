# equipment_summary/sub_agents/get_technitian/agent.py

from google.adk.agents import LlmAgent

from . import prompt

MODEL = "gemini-2.5-pro"

def get_available_technicians_tool(skill: str = None, location: str = None):
    """
    Placeholder for fetching available technicians based on skill or location.
    In a real implementation, this would query a technician database or service.
    """
    print(f"Fetching technicians with skill: {skill} in location: {location}")
    # Simulate technician data
    technicians = {
        "electrical": [
            {"name": "Alice Smith", "id": "T001", "location": "London", "availability": "Mon-Fri"},
            {"name": "Bob Johnson", "id": "T002", "location": "Paris", "availability": "Tue-Sat"}
        ],
        "mechanical": [
            {"name": "Charlie Brown", "id": "T003", "location": "tokyo", "availability": "Wed-Sun"},
            {"name": "Diana Prince", "id": "T004", "location": "London", "availability": "Mon-Thu"}
        ],
        "instrumentation": [
            {"name": "Sanskar Gupta", "id": "T007", "location": "London", "availability": "Mon-Thu"},
            {"name": "Vishal Kumar", "id": "T005", "location": "Tokyo", "availability": "Mon-Thu"},
            
        ],"IT": [
            {"name": "Mahina Sultana", "id": "T006", "location": "London", "availability": "Mon-Thu"}
        ],
    }

    results = []
    if skill:
        results.extend(technicians.get(skill.lower(), []))
    if location:
        results.extend(technicians.get(location.lower(), []))
    
    if not skill and not location:
        # Return all for demonstration if no specific criteria
        for tech_list in technicians.values():
            results.extend(tech_list)
        # Remove duplicates
        results = [dict(t) for t in {tuple(d.items()) for d in results}]


    return results if results else {"message": "No technicians found for the given criteria."}