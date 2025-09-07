from fastmcp import FastMCP
import requests

# API configuration
API_TOKEN = "YOUR_API_TOKEN"  # Replace with your actual API token
BASE_URL = "https://api.productboard.com"


def get_headers(content_type: str = "application/json") -> dict:
    """Generate the standard headers including authorization and versioning."""
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "X-Version": "1",
        "Content-Type": content_type
    }

# Initialize FastMCP server
mcp = FastMCP("Productboard API")


@mcp.tool

def create_note(title: str, content: str) -> dict:
    """Create a new note in Productboard."""
    try:
        url = BASE_URL + "/notes"
        payload = {"title": title, "content": content}
        response = requests.post(url, json=payload, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def list_notes(limit: int = 10, offset: int = 0) -> dict:
    """Retrieve a list of all notes."""
    try:
        url = BASE_URL + "/notes"
        params = {"limit": limit, "offset": offset}
        response = requests.get(url, params=params, headers=get_headers("application/json"))
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def get_note(note_id: str) -> dict:
    """Retrieve a specific note by ID."""
    try:
        url = BASE_URL + f"/notes/{note_id}"
        response = requests.get(url, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def delete_note(note_id: str) -> dict:
    """Delete a specific note by ID."""
    try:
        url = BASE_URL + f"/notes/{note_id}"
        response = requests.delete(url, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def create_company(name: str, domain: str, description: str) -> dict:
    """Create a new company in Productboard."""
    try:
        url = BASE_URL + "/companies"
        payload = {"name": name, "domain": domain, "description": description}
        response = requests.post(url, json=payload, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def list_companies(limit: int = 20, offset: int = 0) -> dict:
    """Retrieve a list of all companies."""
    try:
        url = BASE_URL + "/companies"
        params = {"limit": limit, "offset": offset}
        response = requests.get(url, params=params, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def create_feature(name: str, description: str) -> dict:
    """Create a new feature."""
    try:
        url = BASE_URL + "/features"
        payload = {"name": name, "description": description}
        response = requests.post(url, json=payload, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def list_features(limit: int = 50, offset: int = 0) -> dict:
    """Retrieve a list of all features."""
    try:
        url = BASE_URL + "/features"
        params = {"limit": limit, "offset": offset}
        response = requests.get(url, params=params, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def create_release_group(name: str, description: str) -> dict:
    """Create a new release group."""
    try:
        url = BASE_URL + "/release-groups"
        payload = {"name": name, "description": description}
        response = requests.post(url, json=payload, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def list_release_groups(limit: int = 20, offset: int = 0) -> dict:
    """Retrieve a list of all release groups."""
    try:
        url = BASE_URL + "/release-groups"
        params = {"limit": limit, "offset": offset}
        response = requests.get(url, params=params, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def create_webhook(url_webhook: str, eventTypes: list) -> dict:
    """Create a new webhook subscription."""
    try:
        url = BASE_URL + "/webhooks"
        payload = {"url": url_webhook, "eventTypes": eventTypes}
        response = requests.post(url, json=payload, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def list_webhooks(limit: int = 10, offset: int = 0) -> dict:
    """Retrieve a list of all webhook subscriptions."""
    try:
        url = BASE_URL + "/webhooks"
        params = {"limit": limit, "offset": offset}
        response = requests.get(url, params=params, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def list_custom_fields(limit: int = 100, offset: int = 0) -> dict:
    """Retrieve list of all company custom fields."""
    try:
        url = BASE_URL + "/companies/custom-fields"
        params = {"limit": limit, "offset": offset}
        response = requests.get(url, params=params, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def set_company_field_value(companyId: str, companyCustomFieldId: str, value) -> dict:
    """Set value of a company custom field."""
    try:
        url = BASE_URL + f"/companies/{companyId}/custom-fields/{companyCustomFieldId}/value"
        payload = {"value": value}
        response = requests.put(url, json=payload, headers=get_headers())
        return response.json()
    except Exception as e:
        return {"error": True, "message": str(e)}


@mcp.tool

def health_check() -> dict:
    """Perform a health check on the Productboard API."""
    try:
        url = BASE_URL + "/health"
        response = requests.get(url, headers=get_headers())
        if response.status_code == 200:
            return {"status": "healthy"}
        else:
            return {"status": "unhealthy", "code": response.status_code}
    except Exception as e:
        return {"error": True, "message": str(e)}


if __name__ == "__main__":
    # Start the FastMCP server with HTTP transport
    mcp.run(transport="http", port=8081, host="0.0.0.0")
