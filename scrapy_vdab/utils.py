import logging
import requests
import json
import os
import uuid
from datetime import datetime
from typing import Optional, Dict, Any
from collections import defaultdict


# Global counter for Slack notifications to prevent spam
_slack_notification_counts = defaultdict(int)
_max_slack_notifications_per_spider = 10  # Default maximum notifications per spider run


def _safe_extract_dict(obj, name: str) -> Dict[str, Any]:
    """
    Safely extracts dictionary data from Scrapy objects, handling non-serializable values.
    """
    if not hasattr(obj, name):
        return {}
        
    try:
        attr = getattr(obj, name)
        if not attr:
            return {}
            
        result = {}
        for key, value in dict(attr).items():
            try:
                # Convert bytes to string for headers
                if isinstance(value, bytes):
                    result[str(key)] = value.decode('utf-8', errors='replace')
                elif isinstance(value, list):
                    result[str(key)] = [str(item) for item in value]
                else:
                    result[str(key)] = str(value)
            except Exception:
                result[str(key)] = str(value)
        return result
    except Exception as e:
        return {"extraction_error": str(e)}


def _safe_extract_value(obj, attr_name: str, default=None):
    """
    Safely extracts an attribute value, converting to string if not JSON serializable.
    
    Args:
        obj: The object to extract from
        attr_name: The attribute name
        default: Default value if attribute doesn't exist
        
    Returns:
        JSON-serializable value
    """
    try:
        value = getattr(obj, attr_name, default)
        if value is None:
            return None
        # Test JSON serializability
        json.dumps(value, default=str)
        return value
    except (TypeError, ValueError):
        return str(value) if value is not None else default
    except Exception:
        return str(default) if default is not None else None


def dump_failure_data(failure_path: str, request_data: Optional[Dict[str, Any]] = None, 
                     response_data: Optional[Dict[str, Any]] = None, 
                     error_data: Optional[Dict[str, Any]] = None,
                     logger: logging.Logger = None) -> str:
    """
    Dumps complete failure data (request, response, error) to a JSON file.
    
    Args:
        failure_path: Base path for the failures directory
        request_data: Complete request information
        response_data: Complete response information  
        error_data: Complete error/exception information
        logger: Logger instance for logging
        
    Returns:
        str: Path to the created failure file
    """
    try:
        # Ensure failures directory exists
        os.makedirs(failure_path, exist_ok=True)
        
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"failure_{timestamp}_{uuid.uuid4().hex[:8]}.json"
        filepath = os.path.join(failure_path, filename)
        
        # Compile all failure data
        failure_dump = {
            "timestamp": datetime.now().isoformat(),
            "request": request_data,
            "response": response_data,
            "error": error_data
        }
        
        # Write to file with pretty formatting and robust error handling
        with open(filepath, 'w', encoding='utf-8') as f:
            try:
                json.dump(failure_dump, f, indent=2, ensure_ascii=False, default=str)
            except Exception as json_error:
                # If JSON serialization fails, create a fallback
                if logger:
                    logger.warning(f"JSON serialization failed: {json_error}, creating fallback dump")
                
                # Create a safer version of the data
                safe_dump = {
                    "timestamp": datetime.now().isoformat(),
                    "serialization_error": str(json_error),
                    "request": str(request_data) if request_data else None,
                    "response": str(response_data) if response_data else None,
                    "error": str(error_data) if error_data else None
                }
                json.dump(safe_dump, f, indent=2, ensure_ascii=False)
            
        if logger:
            logger.info(f"Failure data dumped to: {filepath}")
            
        return filepath
        
    except Exception as e:
        if logger:
            logger.error(f"Failed to dump failure data: {e}")
        return None


def extract_request_data(request) -> Dict[str, Any]:
    """
    Extracts complete request information for failure dumping.
    
    Args:
        request: Scrapy Request object
        
    Returns:
        Dict containing complete request data
    """
    if not request:
        return None
        
    try:
        return {
            "url": getattr(request, 'url', None),
            "method": getattr(request, 'method', 'GET'),
            "headers": _safe_extract_dict(request, 'headers'),
            "body": getattr(request, 'body', b'').decode('utf-8', errors='replace') if hasattr(request, 'body') and request.body else None,
            "meta": _safe_extract_dict(request, 'meta'),
            "cookies": _safe_extract_dict(request, 'cookies'),
            "priority": getattr(request, 'priority', None),
            "dont_filter": getattr(request, 'dont_filter', None),
            "callback": getattr(request, 'callback', None).__name__ if getattr(request, 'callback', None) else None,
            "errback": getattr(request, 'errback', None).__name__ if getattr(request, 'errback', None) else None
        }
    except Exception as e:
        return {
            "extraction_error": str(e),
            "url": str(getattr(request, 'url', 'unknown')),
            "method": str(getattr(request, 'method', 'unknown'))
        }


def extract_response_data(response) -> Dict[str, Any]:
    """
    Extracts complete response information for failure dumping.
    
    Args:
        response: Scrapy Response object
        
    Returns:
        Dict containing complete response data
    """
    if not response:
        return None
        
    try:
        return {
            "url": getattr(response, 'url', None),
            "status": getattr(response, 'status', None),
            "headers": _safe_extract_dict(response, 'headers'),
            "body": getattr(response, 'body', b'').decode('utf-8', errors='replace') if hasattr(response, 'body') and response.body else None,
            "text": getattr(response, 'text', None),
            "encoding": getattr(response, 'encoding', None),
            "request": extract_request_data(getattr(response, 'request', None)),
            "meta": _safe_extract_dict(response, 'meta'),
            "flags": [str(flag) for flag in getattr(response, 'flags', [])],
            "certificate": str(getattr(response, 'certificate', None)) if getattr(response, 'certificate', None) else None,
            "ip_address": getattr(response, 'ip_address', None)
        }
    except Exception as e:
        return {
            "extraction_error": str(e),
            "url": str(getattr(response, 'url', 'unknown')),
            "status": str(getattr(response, 'status', 'unknown'))
        }


def extract_error_data(failure) -> Dict[str, Any]:
    """
    Extracts complete error/failure information for dumping.
    
    Args:
        failure: Twisted Failure object or Exception
        
    Returns:
        Dict containing complete error data
    """
    if not failure:
        return None
        
    try:
        error_data = {
            "type": type(failure).__name__,
            "value": str(failure),
            "traceback": None,
            "request": None,
            "http_status": None,
            "server_message": None,
            "response_body": None
        }
        
        # Handle Twisted Failure objects
        if hasattr(failure, 'getTraceback'):
            try:
                error_data["traceback"] = failure.getTraceback()
            except Exception:
                error_data["traceback"] = "Failed to extract traceback"
            error_data["type"] = failure.type.__name__ if failure.type else "Unknown"
            error_data["value"] = str(failure.value) if failure.value else "Unknown"
            
            # Special handling for HttpError to extract response details
            if hasattr(failure, 'value') and hasattr(failure.value, 'response'):
                response = failure.value.response
                if response:
                    error_data["http_status"] = getattr(response, 'status', None)
                    error_data["server_message"] = f"HTTP {getattr(response, 'status', 'Unknown')} - {getattr(response, 'reason', 'Unknown reason')}"
                    
                    # Try to extract response body/text for server error messages
                    try:
                        if hasattr(response, 'text') and response.text:
                            error_data["response_body"] = response.text[:1000]  # Limit to first 1000 chars
                        elif hasattr(response, 'body') and response.body:
                            body_text = response.body.decode('utf-8', errors='replace')
                            error_data["response_body"] = body_text[:1000]  # Limit to first 1000 chars
                    except Exception:
                        error_data["response_body"] = "Failed to extract response body"
                    
                    # Enhanced error value with status code
                    error_data["value"] = f"HTTP {getattr(response, 'status', 'Unknown')} Error: {str(failure.value)}"
            
        # Extract request data if available
        if hasattr(failure, 'request'):
            error_data["request"] = extract_request_data(failure.request)
            
        return error_data
    except Exception as e:
        return {
            "extraction_error": str(e),
            "type": "ExtractionFailed",
            "value": str(failure) if failure else "Unknown failure"
        }


def can_send_slack_notification(spider_name: str, max_notifications: int = None) -> bool:
    """
    Checks if a Slack notification can be sent based on the current count.
    This prevents spam by limiting notifications per spider.
    
    Args:
        spider_name: Name of the spider
        max_notifications: Maximum allowed notifications (uses global default if None)
        
    Returns:
        bool: True if notification can be sent, False otherwise
    """
    current_count = _slack_notification_counts[spider_name]
    limit = max_notifications if max_notifications is not None else _max_slack_notifications_per_spider
    return current_count < limit


def send_slack_notification(logger: logging.Logger, slack_enabled: bool, slack_webhook_url: str, 
                          message: str, spider_name: str = "unknown", max_notifications: int = None) -> bool:
    """
    Sends a Slack notification with spam protection.
    
    Args:
        logger: Logger instance
        slack_enabled: Whether Slack notifications are enabled
        slack_webhook_url: Slack webhook URL
        message: Message to send
        spider_name: Name of the spider (for spam protection)
        max_notifications: Maximum allowed notifications (uses global default if None)
        
    Returns:
        bool: True if notification was sent, False otherwise
    """
    if not slack_enabled:
        return False
        
    if not slack_webhook_url or 'YOUR/WEBHOOK/URL' in slack_webhook_url:
        logger.warning("Slack notifications are enabled, but SLACK_WEBHOOK_URL is not configured properly.")
        return False
    
    # Check if we can send more notifications
    if not can_send_slack_notification(spider_name, max_notifications):
        limit = max_notifications if max_notifications is not None else _max_slack_notifications_per_spider
        logger.warning(f"Slack notification limit reached for spider '{spider_name}'. "
                      f"Suppressing further notifications. Current count: {_slack_notification_counts[spider_name]}/{limit}")
        return False
    
    payload = {"text": message}
    try:
        response = requests.post(slack_webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        
        # Increment counter only on successful send
        _slack_notification_counts[spider_name] += 1
        
        limit = max_notifications if max_notifications is not None else _max_slack_notifications_per_spider
        logger.info(f"Successfully sent Slack notification. Count: {_slack_notification_counts[spider_name]}/{limit}")
        return True
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send Slack notification: {e}")
        # Still increment counter to avoid repeated failed attempts
        _slack_notification_counts[spider_name] += 1
        return False


def reset_slack_notification_count(spider_name: str = None):
    """
    Resets the Slack notification count for a specific spider or all spiders.
    
    Args:
        spider_name: Name of the spider to reset, or None to reset all
    """
    if spider_name:
        _slack_notification_counts[spider_name] = 0
    else:
        _slack_notification_counts.clear()
