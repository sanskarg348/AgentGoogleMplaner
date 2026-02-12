# equipment_summary/agent.py

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .prompt import PROMPT

from .sub_agents.sap_api import call_sap_api_tool
from .sub_agents.weather import get_current_weather_tool
from .sub_agents.get_technitian import get_available_technicians_tool

MODEL = "gemini-2.5-pro"

equipment_summary_coordinator = LlmAgent(
    name="equipment_summary_coordinator",
    model=MODEL,
    description=(
        "An agent that analyzes equipment-related data from SAP, "
        "provides weather information, finds available technicians, "
        "and generates comprehensive summaries based on the collected information."
    ),
    instruction=(
        "You are an expert in summarizing equipment information, weather, and technician availability. "
        "Your task is to gather relevant data using the 'sap_api_agent' (for service orders/confirmations), "
        "'weather_agent' (for current weather), and 'get_technitian_agent' (for technician details). "
        "The user will provide an equipment ID and may specify a location or skill for technicians. "
        "Use the appropriate agents to fetch the necessary data. "
        "Once all relevant data is retrieved, synthesize this information into a comprehensive summary. "
        "This summary should include details from service orders and confirmations, "
        "current weather conditions for the equipment's location (if available), "
        "and details of available technicians (if requested). "
        "Finally, present the combined summary as your output."
    ),
    output_key="equipment_summary",
    tools=[
        call_sap_api_tool,
        get_available_technicians_tool,
        get_current_weather_tool
    ]
)

root_agent = equipment_summary_coordinator
