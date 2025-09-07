from fastmcp import FastMCP
import httpx
import logging
from typing import Optional, Dict, Any, List

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP("Productboard API Server")

# API configuration
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJraWQiOiJlYWQ0MWY3NmE1M2E5OGNmOGIxZjI2NTA5Mzg2ZThmNGM1OWYzMzg5ZTljMDQ0YjQ2NjRkYThjYzY5NjdkY2Q2IiwiYWxnIjoiUlM1MTIifQ.eyJpYXQiOjE3NTU2MTM3ODEsImlzcyI6IjY5N2FiYTc4LWM5MjAtNGNiNS1hNTNjLWZhM2QxN2QxMTA4MyIsInN1YiI6IjE1MjExMzUiLCJyb2xlIjoiYWRtaW4iLCJhdWQiOiJodHRwczovL2FwaS5wcm9kdWN0Ym9hcmQuY29tIiwidXNlcl9pZCI6MTUyMTEzNSwic3BhY2VfaWQiOiIzNDk0NDIifQ.mIu-C_SV2FOpeSPgrUa3yJHc2SU3MssXIdrZJbHb0mCnKfzhggiRqCkW1d2pp48Aaf6cPmKZ0i54Sxms5KHt52Ik7IincSiHTvQbHxMRXb5gYp-1hKI3BxhzYn-BrLAnZdf4GbYmKdlKsr13u5M5i4ak9w6cNbX4fUejVZ2L1NRfPjDzGE3yb1hlyub9dy0X7XN_6ShML4ImzJSRns33aaZZ6I7Fw5VXw2uRrSPcXGSlLExUpCrR1GM9EPn34aXqriyF4mMrKa71UqNY3NLcjYzPUTeFP708ByE26HMi3fY6lepr8sDzK8WnRVwSWfA4fd4A_AkVFrLJmvQ9OUXSBg",
BASE_URL = "https://api.productboard.com"


@mcp.tool()
def create_note(title: str, content: str) -> Dict[str, Any]:
    """Create a new note in Productboard.

    Parameters:
      title (str): Title of the note.
      content (str): Content of the note.
    """
    logger.info(f"create_note called with title: {title}")
    url = f"{BASE_URL}/notes"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1",
        "Content-Type": "application/json"
    }
    payload = {"title": title, "content": content}
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed create_note")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in create_note: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def list_notes(limit: Optional[int] = 10, offset: Optional[int] = 0) -> Dict[str, Any]:
    """Retrieve a list of all notes.

    Parameters:
      limit (int, optional): Limit of notes to retrieve. Default is 10.
      offset (int, optional): Offset for pagination. Default is 0.
    """
    logger.info(f"list_notes called with limit: {limit}, offset: {offset}")
    url = f"{BASE_URL}/notes"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    params = {"limit": limit, "offset": offset}
    try:
        response = httpx.get(url, headers=headers, params=params, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed list_notes")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in list_notes: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def get_note(id: str) -> Dict[str, Any]:
    """Retrieve a specific note by ID.

    Parameters:
      id (str): The unique identifier of the note.
    """
    logger.info(f"get_note called with id: {id}")
    url = f"{BASE_URL}/notes/{id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    try:
        response = httpx.get(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed get_note")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in get_note: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def delete_note(id: str) -> Dict[str, Any]:
    """Delete a specific note by ID.

    Parameters:
      id (str): The unique identifier of the note to delete.
    """
    logger.info(f"delete_note called with id: {id}")
    url = f"{BASE_URL}/notes/{id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    try:
        response = httpx.delete(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed delete_note")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in delete_note: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def create_company(name: str, domain: str, description: str) -> Dict[str, Any]:
    """Create a new company.

    Parameters:
      name (str): Name of the company.
      domain (str): Domain of the company.
      description (str): Description of the company.
    """
    logger.info(f"create_company called with name: {name}")
    url = f"{BASE_URL}/companies"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1",
        "Content-Type": "application/json"
    }
    payload = {"name": name, "domain": domain, "description": description}
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed create_company")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in create_company: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def list_companies(limit: Optional[int] = 20, offset: Optional[int] = 0) -> Dict[str, Any]:
    """Retrieve a list of all companies.

    Parameters:
      limit (int, optional): Limit of companies to retrieve. Default is 20.
      offset (int, optional): Offset for pagination. Default is 0.
    """
    logger.info(f"list_companies called with limit: {limit}, offset: {offset}")
    url = f"{BASE_URL}/companies"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    params = {"limit": limit, "offset": offset}
    try:
        response = httpx.get(url, headers=headers, params=params, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed list_companies")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in list_companies: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def create_feature(name: str, description: str) -> Dict[str, Any]:
    """Create a new feature.

    Parameters:
      name (str): Name of the feature.
      description (str): Description of the feature.
    """
    logger.info(f"create_feature called with name: {name}")
    url = f"{BASE_URL}/features"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1",
        "Content-Type": "application/json"
    }
    payload = {"name": name, "description": description}
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed create_feature")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in create_feature: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def list_features(limit: Optional[int] = 50, offset: Optional[int] = 0) -> Dict[str, Any]:
    """Retrieve a list of all features.

    Parameters:
      limit (int, optional): Limit of features to retrieve. Default is 50.
      offset (int, optional): Offset for pagination. Default is 0.
    """
    logger.info(f"list_features called with limit: {limit}, offset: {offset}")
    url = f"{BASE_URL}/features"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    params = {"limit": limit, "offset": offset}
    try:
        response = httpx.get(url, headers=headers, params=params, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed list_features")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in list_features: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def create_release_group(name: str, description: str) -> Dict[str, Any]:
    """Create a new release group.

    Parameters:
      name (str): Name of the release group.
      description (str): Description of the release group.
    """
    logger.info(f"create_release_group called with name: {name}")
    url = f"{BASE_URL}/release-groups"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1",
        "Content-Type": "application/json"
    }
    payload = {"name": name, "description": description}
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed create_release_group")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in create_release_group: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def list_release_groups(limit: Optional[int] = 20, offset: Optional[int] = 0) -> Dict[str, Any]:
    """Retrieve a list of all release groups.

    Parameters:
      limit (int, optional): Limit of release groups to retrieve. Default is 20.
      offset (int, optional): Offset for pagination. Default is 0.
    """
    logger.info(f"list_release_groups called with limit: {limit}, offset: {offset}")
    url = f"{BASE_URL}/release-groups"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    params = {"limit": limit, "offset": offset}
    try:
        response = httpx.get(url, headers=headers, params=params, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed list_release_groups")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in list_release_groups: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def create_webhook(url_param: str, event_types: List[str]) -> Dict[str, Any]:
    """Create a new webhook subscription.

    Parameters:
      url_param (str): The webhook URL.
      event_types (List[str]): List of event types for the webhook.
    """
    logger.info(f"create_webhook called with url: {url_param}")
    url = f"{BASE_URL}/webhooks"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1",
        "Content-Type": "application/json"
    }
    payload = {"url": url_param, "eventTypes": event_types}
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed create_webhook")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in create_webhook: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def list_webhooks(limit: Optional[int] = 10, offset: Optional[int] = 0) -> Dict[str, Any]:
    """Retrieve a list of all webhook subscriptions.

    Parameters:
      limit (int, optional): Limit of webhooks to retrieve. Default is 10.
      offset (int, optional): Offset for pagination. Default is 0.
    """
    logger.info(f"list_webhooks called with limit: {limit}, offset: {offset}")
    url = f"{BASE_URL}/webhooks"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    params = {"limit": limit, "offset": offset}
    try:
        response = httpx.get(url, headers=headers, params=params, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed list_webhooks")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in list_webhooks: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def list_custom_fields(limit: Optional[int] = 100, offset: Optional[int] = 0) -> Dict[str, Any]:
    """Retrieve list of all company custom fields.

    Parameters:
      limit (int, optional): Limit of custom fields to retrieve. Default is 100.
      offset (int, optional): Offset for pagination. Default is 0.
    """
    logger.info(f"list_custom_fields called with limit: {limit}, offset: {offset}")
    url = f"{BASE_URL}/companies/custom-fields"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    params = {"limit": limit, "offset": offset}
    try:
        response = httpx.get(url, headers=headers, params=params, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed list_custom_fields")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in list_custom_fields: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def set_company_field_value(company_id: str, company_custom_field_id: str, value: Any) -> Dict[str, Any]:
    """Set value of a company custom field.

    Parameters:
      company_id (str): The ID of the company.
      company_custom_field_id (str): The ID of the custom field.
      value (str or int): The value to set.
    """
    logger.info(f"set_company_field_value called with company_id: {company_id}, field_id: {company_custom_field_id}")
    url = f"{BASE_URL}/companies/{company_id}/custom-fields/{company_custom_field_id}/value"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1",
        "Content-Type": "application/json"
    }
    payload = {"value": value}
    try:
        response = httpx.put(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        logger.info("Successfully executed set_company_field_value")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in set_company_field_value: {str(e)}")
        return {"status": "error", "message": str(e)}


@mcp.tool()
def health_check() -> Dict[str, Any]:
    """Health check endpoint for the Productboard MCP Server."""
    logger.info("health_check called")
    url = f"{BASE_URL}/health"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1"
    }
    try:
        response = httpx.get(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        health_status = "healthy" if response.status_code == 200 else "unhealthy"
        logger.info("Successfully executed health_check")
        return {
            "status": health_status,
            "server": "Productboard MCP Server",
            "tools": [
                "create_note",
                "list_notes",
                "get_note",
                "delete_note",
                "create_company",
                "list_companies",
                "create_feature",
                "list_features",
                "create_release_group",
                "list_release_groups",
                "create_webhook",
                "list_webhooks",
                "list_custom_fields",
                "set_company_field_value"
            ]
        }
    except Exception as e:
        logger.error(f"Error in health_check: {str(e)}")
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    logger.info("Starting Productboard FastMCP server...")
    mcp.run(transport="http", port=8080, host="0.0.0.0")
