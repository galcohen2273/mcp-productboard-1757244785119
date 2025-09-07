from fastmcp import FastMCP
import httpx
import logging

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP("Productboard API")

# API configuration
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJraWQiOiJlYWQ0MWY3NmE1M2E5OGNmOGIxZjI2NTA5Mzg2ZThmNGM1OWYzMzg5ZTljMDQ0YjQ2NjRkYThjYzY5NjdkY2Q2IiwiYWxnIjoiUlM1MTIifQ.eyJpYXQiOjE3NTU2MTM3ODEsImlzcyI6IjY5N2FiYTc4LWM5MjAtNGNiNS1hNTNjLWZhM2QxN2QxMTA4MyIsInN1YiI6IjE1MjExMzUiLCJyb2xlIjoiYWRtaW4iLCJhdWQiOiJodHRwczovL2FwaS5wcm9kdWN0Ym9hcmQuY29tIiwidXNlcl9pZCI6MTUyMTEzNSwic3BhY2VfaWQiOiIzNDk0NDIifQ.mIu-C_SV2FOpeSPgrUa3yJHc2SU3MssXIdrZJbHb0mCnKfzhggiRqCkW1d2pp48Aaf6cPmKZ0i54Sxms5KHt52Ik7IincSiHTvQbHxMRXb5gYp-1hKI3BxhzYn-BrLAnZdf4GbYmKdlKsr13u5M5i4ak9w6cNbX4fUejVZ2L1NRfPjDzGE3yb1hlyub9dy0X7XN_6ShML4ImzJSRns33aaZZ6I7Fw5VXw2uRrSPcXGSlLExUpCrR1GM9EPn34aXqriyF4mMrKa71UqNY3NLcjYzPUTeFP708ByE26HMi3fY6lepr8sDzK8WnRVwSWfA4fd4A_AkVFrLJmvQ9OUXSBg"
BASE_URL = "https://api.productboard.com"

@mcp.tool()
def list_features() -> dict:
    """List all features in Productboard."""
    logger.info("list_features tool called")
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    url = f"{BASE_URL}/features"
    
    try:
        response = httpx.get(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        logger.info(f"Successfully retrieved {len(response.json().get('data', []))} features")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in list_features: {str(e)}")
        return {"status": "error", "message": str(e)}

@mcp.tool()
def create_feature(name: str, description: str = "") -> dict:
    """Create a new feature in Productboard."""
    logger.info(f"create_feature tool called with name: {name}")
    headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/features"
    payload = {"name": name}
    
    if description:
        payload["description"] = description
        
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        logger.info(f"Successfully created feature: {name}")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in create_feature: {str(e)}")
        return {"status": "error", "message": str(e)}

@mcp.tool()
def get_feature(feature_id: str) -> dict:
    """Get details for a specific feature by ID."""
    logger.info(f"get_feature tool called with ID: {feature_id}")
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    url = f"{BASE_URL}/features/{feature_id}"
    
    try:
        response = httpx.get(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        logger.info(f"Successfully retrieved feature: {feature_id}")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in get_feature: {str(e)}")
        return {"status": "error", "message": str(e)}

@mcp.tool()
def update_feature(feature_id: str, name: str = None, description: str = None) -> dict:
    """Update an existing feature's name and/or description by ID."""
    logger.info(f"update_feature tool called with ID: {feature_id}")
    headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/features/{feature_id}"
    payload = {}
    
    if name:
        payload["name"] = name
    if description:
        payload["description"] = description
        
    if not payload:
        return {"status": "error", "message": "No update fields provided."}
    
    try:
        response = httpx.put(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        logger.info(f"Successfully updated feature: {feature_id}")
        return {"status": "success", "data": response.json()}
    except Exception as e:
        logger.error(f"Error in update_feature: {str(e)}")
        return {"status": "error", "message": str(e)}

@mcp.tool()
def delete_feature(feature_id: str) -> dict:
    """Delete a feature by ID (if endpoint available)."""
    logger.info(f"delete_feature tool called with ID: {feature_id}")
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    url = f"{BASE_URL}/features/{feature_id}"
    
    try:
        response = httpx.delete(url, headers=headers, timeout=30.0)
        if response.status_code in (200, 204):
            logger.info(f"Successfully deleted feature: {feature_id}")
            return {"status": "success", "data": "Feature deleted."}
        else:
            logger.error(f"Delete failed with status {response.status_code}: {response.text}")
            return {"status": "error", "message": str(response.text)}
    except Exception as e:
        logger.error(f"Error in delete_feature: {str(e)}")
        return {"status": "error", "message": str(e)}

# Simple health check tool
@mcp.tool()
def health_check() -> dict:
    """Simple health check that returns server status."""
    logger.info("health_check tool called")
    return {
        "status": "healthy",
        "server": "Productboard MCP Server",
        "tools": ["list_features", "create_feature", "get_feature", "update_feature", "delete_feature", "health_check"]
    }

if __name__ == "__main__":
    logger.info("Starting FastMCP server...")
    # Try with explicit configuration
    mcp.run(
        transport="http",
        port=8080,
        host="0.0.0.0"
    )
