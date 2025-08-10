"""
MCP Taste Recommendation Server
Advanced taste-based content recommendation engine for Pooch AI Hackathon.

Implements MCP Protocol 2025-06-18 with comprehensive taste analysis framework.
Acts as a master taste interpreter for movies, TV shows, and podcasts.
"""

import os
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List, Optional, Union

from fastapi import FastAPI, Depends, Request, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import uvicorn
from dotenv import load_dotenv

from taste_engine import MasterTasteInterpreter, EnhancedTasteProfile, EnhancedRecommendation

# Load environment variables
load_dotenv()

# Configuration
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "pooch-taste-server-2024")
MY_NUMBER = os.getenv("MY_NUMBER", "919876543210")
PORT = int(os.getenv("PORT", 8086))
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# MCP Protocol Configuration
MCP_PROTOCOL_VERSION = "2025-06-18"
FALLBACK_VERSION = "2025-03-26"
SUPPORTED_VERSIONS = [MCP_PROTOCOL_VERSION, FALLBACK_VERSION]

# FastAPI app setup
app = FastAPI(
    title="MCP Taste Recommendation Server",
    description="Advanced taste-based content recommendation engine implementing sophisticated prompt engineering framework",
    version="2.0.0",
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None
)

# CORS middleware with security considerations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if DEBUG else ["http://localhost", "https://localhost"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

# Initialize the master taste interpreter
taste_interpreter = MasterTasteInterpreter()

# Pydantic models for MCP protocol 2025-06-18
class MCPRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: Optional[Dict[str, Any]] = None
    id: Optional[Union[str, int]] = None

class MCPResponse(BaseModel):
    jsonrpc: str = "2.0"
    result: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None
    id: Optional[Union[str, int]] = None

class MCPError(BaseModel):
    code: int
    message: str
    data: Optional[Any] = None

# MCP Tool definitions implementing the framework requirements
MCP_TOOLS = [
    {
        "name": "validate",
        "description": "Returns the server owner's phone number for Pooch AI validation",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_taste_recommendations", 
        "description": "Get personalized content recommendations using advanced taste analysis framework",
        "inputSchema": {
            "type": "object",
            "properties": {
                "user_input": {
                    "type": "string",
                    "description": "User's description of what they like, want, or reference content they enjoyed"
                },
                "content_type": {
                    "type": "string",
                    "enum": ["tv", "movie", "podcast", "mixed"],
                    "default": "mixed",
                    "description": "Type of content to recommend"
                },
                "current_mood": {
                    "type": "string",
                    "description": "User's current mood or energy level (optional)"
                },
                "time_available": {
                    "type": "string", 
                    "description": "Available time for consuming content (optional)"
                },
                "viewing_situation": {
                    "type": "string",
                    "description": "Viewing context: alone, with friends, family, etc. (optional)"
                }
            },
            "required": ["user_input"]
        }
    },
    {
        "name": "extract_taste_profile",
        "description": "Extract and analyze comprehensive taste profile from user input using the advanced framework",
        "inputSchema": {
            "type": "object",
            "properties": {
                "user_input": {
                    "type": "string",
                    "description": "User's description to analyze for taste elements"
                },
                "content_type": {
                    "type": "string",
                    "enum": ["tv", "movie", "podcast", "mixed"],
                    "default": "mixed"
                }
            },
            "required": ["user_input"]
        }
    },
    {
        "name": "handle_contextual_request",
        "description": "Handle special request types like 'something like X but not exactly', 'I don't know what I want', 'surprise me'",
        "inputSchema": {
            "type": "object",
            "properties": {
                "user_input": {
                    "type": "string",
                    "description": "User's contextual request"
                },
                "request_type": {
                    "type": "string",
                    "enum": ["something_like_but_not", "dont_know", "surprise_me", "general"],
                    "description": "Type of contextual request"
                }
            },
            "required": ["user_input", "request_type"]
        }
    }
]

# Authentication and security functions
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify Bearer token authentication"""
    if credentials.credentials != AUTH_TOKEN:
        raise HTTPException(
            status_code=403, 
            detail="Invalid authentication token"
        )
    return credentials.credentials

def validate_mcp_protocol_version(mcp_protocol_version: Optional[str] = Header(None)):
    """Validate MCP-Protocol-Version header as required by 2025-06-18 spec"""
    if mcp_protocol_version is None:
        # Use fallback version if header missing
        return FALLBACK_VERSION
    
    if mcp_protocol_version not in SUPPORTED_VERSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported MCP protocol version: {mcp_protocol_version}. Supported versions: {', '.join(SUPPORTED_VERSIONS)}"
        )
    
    return mcp_protocol_version

def validate_origin(request: Request):
    """Validate Origin header for security (DNS rebinding protection)"""
    origin = request.headers.get("origin")
    if origin:
        # Allow localhost and development origins
        allowed_origins = [
            "http://localhost",
            "https://localhost", 
            "http://127.0.0.1",
            "https://127.0.0.1"
        ]
        
        # In production, add your actual domain
        if not DEBUG:
            # Add production origins here
            pass
        
        # For development, be more permissive
        if DEBUG or any(origin.startswith(allowed) for allowed in allowed_origins):
            return True
        
        raise HTTPException(
            status_code=403,
            detail="Invalid origin header"
        )
    
    return True

# Tool execution functions implementing the advanced framework
def execute_validate() -> Dict[str, Any]:
    """Execute the validate tool - returns phone number for Puch validation
    
    According to Puch AI docs (https://puch.ai/mcp), the validate tool must return 
    the phone number in {country_code}{number} format. The MCP protocol requires
    a content field with the phone number.
    """
    return {
        "content": [
            {
                "type": "text",
                "text": MY_NUMBER  # Phone number as text content
            }
        ],
        "isError": False
    }

def execute_get_taste_recommendations(
    user_input: str, 
    content_type: str = "mixed", 
    current_mood: Optional[str] = None, 
    time_available: Optional[str] = None,
    viewing_situation: Optional[str] = None
) -> Dict[str, Any]:
    """Execute taste recommendation generation using the comprehensive framework"""
    try:
        # Build context from optional parameters
        context = {}
        if current_mood:
            context["mood"] = current_mood
        if time_available:
            context["time"] = time_available
        if viewing_situation:
            context["social"] = viewing_situation
        
        # Extract comprehensive taste profile
        profile = taste_interpreter.extract_taste_profile(
            user_input=user_input, 
            content_type=content_type, 
            context=context
        )
        
        # Generate recommendations using 6-factor evaluation matrix
        recommendations = taste_interpreter.generate_recommendations(
            profile=profile, 
            context=context, 
            max_recommendations=3
        )
        
        # Format for WhatsApp using exact framework structure
        formatted_response = taste_interpreter.format_recommendations_for_whatsapp(
            recommendations=recommendations, 
            profile=profile
        )
        
        # Build comprehensive response
        result_data = {
            "success": True,
            "recommendations": [rec.dict() for rec in recommendations],
            "taste_profile": profile.dict(),
            "total_recommendations": len(recommendations),
            "analysis_timestamp": datetime.now().isoformat(),
            "framework_version": "2.0.0"
        }
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": formatted_response
                }
            ],
            "isError": False,
            "_meta": result_data
        }
        
    except Exception as e:
        error_msg = f"Failed to generate recommendations: {str(e)}"
        error_response = ("Sorry, I encountered an error while analyzing your taste preferences. "
                         "Could you try rephrasing your request or provide more details about what you're looking for?")
        
        return {
            "content": [
                {
                    "type": "text", 
                    "text": error_response
                }
            ],
            "isError": True,
            "_meta": {
                "success": False,
                "error": error_msg,
                "recommendations": [],
                "taste_profile": None
            }
        }

def execute_extract_taste_profile(user_input: str, content_type: str = "mixed") -> Dict[str, Any]:
    """Execute comprehensive taste profile extraction"""
    try:
        profile = taste_interpreter.extract_taste_profile(user_input, content_type)
        
        # Analyze profile richness
        analysis = {
            "narrative_elements_found": (
                len(profile.narrative_dna.story_structure) +
                len(profile.narrative_dna.pacing_preferences) +
                len(profile.narrative_dna.conflict_style) +
                len(profile.narrative_dna.resolution_patterns)
            ),
            "emotional_texture_found": (
                len(profile.emotional_texture.primary_mood) +
                len(profile.emotional_texture.emotional_journey) +
                len(profile.emotional_texture.intensity_comfort) +
                len(profile.emotional_texture.character_relationship)
            ),
            "style_preferences_found": 0,
            "anti_patterns_found": (
                len(profile.anti_patterns.deal_breakers) +
                len(profile.anti_patterns.tone_violations) +
                len(profile.anti_patterns.structural_issues) +
                len(profile.anti_patterns.context_mismatches)
            ),
            "context_clues_found": len(profile.context)
        }
        
        # Add style analysis
        if profile.visual_style:
            analysis["style_preferences_found"] += (
                len(profile.visual_style.visual_preferences) +
                len(profile.visual_style.performance_energy) +
                len(profile.visual_style.technical_craft)
            )
        
        if profile.audio_style:
            analysis["style_preferences_found"] += (
                len(profile.audio_style.host_dynamics) +
                len(profile.audio_style.delivery_style) +
                len(profile.audio_style.intimacy_level) +
                len(profile.audio_style.production_values)
            )
        
        result_data = {
            "success": True,
            "taste_profile": profile.dict(),
            "analysis": analysis,
            "extraction_quality": "rich" if sum(analysis.values()) > 5 else "moderate" if sum(analysis.values()) > 2 else "minimal",
            "timestamp": datetime.now().isoformat()
        }
        
        extraction_summary = f"Taste profile extracted successfully. Found {sum(analysis.values())} taste elements. Quality: {result_data['extraction_quality']}"
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": extraction_summary
                }
            ],
            "isError": False,
            "_meta": result_data
        }
        
    except Exception as e:
        error_msg = f"Failed to extract taste profile: {str(e)}"
        return {
            "content": [
                {
                    "type": "text",
                    "text": "Sorry, I couldn't analyze your taste profile. Please try again with more details."
                }
            ],
            "isError": True,
            "_meta": {
                "success": False,
                "error": error_msg,
                "taste_profile": None
            }
        }

def execute_handle_contextual_request(user_input: str, request_type: str) -> Dict[str, Any]:
    """Execute contextual request handling"""
    try:
        response = taste_interpreter.handle_contextual_requests(
            user_input=user_input,
            request_type=request_type
        )
        
        result_data = {
            "success": True,
            "request_type": request_type,
            "timestamp": datetime.now().isoformat()
        }
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": response
                }
            ],
            "isError": False,
            "_meta": result_data
        }
        
    except Exception as e:
        error_msg = f"Failed to handle contextual request: {str(e)}"
        fallback_response = "I can help you find content recommendations. Could you tell me more about what you're looking for?"
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": fallback_response
                }
            ],
            "isError": True,
            "_meta": {
                "success": False,
                "error": error_msg
            }
        }

# MCP Protocol handlers
def handle_initialize(protocol_version: str) -> Dict[str, Any]:
    """Handle MCP initialize method with protocol version support"""
    return {
        "protocolVersion": protocol_version,
        "serverInfo": {
            "name": "mcp-taste-server",
            "version": "2.0.0",
            "description": "Advanced taste-based content recommendation engine implementing comprehensive prompt engineering framework"
        },
        "capabilities": {
            "tools": {
                "list": True,
                "call": True
            },
            "resources": {
                "list": False,
                "read": False
            },
            "prompts": {
                "list": False,
                "get": False
            }
        }
    }

def handle_tools_list() -> Dict[str, Any]:
    """Handle MCP tools/list method"""
    return {
        "tools": MCP_TOOLS
    }

def handle_tools_call(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Handle MCP tools/call method with comprehensive error handling"""
    try:
        if tool_name == "validate":
            # Puch AI expects validate tool to return phone number  
            return execute_validate()
            
        elif tool_name == "get_taste_recommendations":
            user_input = arguments.get("user_input")
            if not user_input:
                raise ValueError("user_input is required")
                
            return execute_get_taste_recommendations(
                user_input=user_input,
                content_type=arguments.get("content_type", "mixed"),
                current_mood=arguments.get("current_mood"),
                time_available=arguments.get("time_available"),
                viewing_situation=arguments.get("viewing_situation")
            )
            
        elif tool_name == "extract_taste_profile":
            user_input = arguments.get("user_input")
            if not user_input:
                raise ValueError("user_input is required")
                
            return execute_extract_taste_profile(
                user_input=user_input,
                content_type=arguments.get("content_type", "mixed")
            )
            
        elif tool_name == "handle_contextual_request":
            user_input = arguments.get("user_input")
            request_type = arguments.get("request_type")
            
            if not user_input or not request_type:
                raise ValueError("user_input and request_type are required")
                
            return execute_handle_contextual_request(
                user_input=user_input,
                request_type=request_type
            )
            
        else:
            raise ValueError(f"Unknown tool: {tool_name}")
            
    except Exception as e:
        return {
            "success": False,
            "error": f"Tool execution failed: {str(e)}",
            "tool_name": tool_name,
            "timestamp": datetime.now().isoformat()
        }

# API Endpoints
@app.post("/mcp")
async def mcp_endpoint(
    request: Request,
    token: str = Depends(verify_token),
    protocol_version: str = Depends(validate_mcp_protocol_version)
) -> JSONResponse:
    """
    Main MCP endpoint implementing JSON-RPC 2.0 protocol with 2025-06-18 enhancements.
    
    Key features:
    - Protocol version enforcement
    - Origin header validation
    - No JSON-RPC batching (removed in 2025-06-18)
    - Bearer token authentication
    - Comprehensive error handling
    """
    
    # Validate origin for security
    validate_origin(request)
    
    try:
        # Parse JSON-RPC request
        request_data = await request.json()
        
        # Ensure it's NOT a batch request (removed in 2025-06-18)
        if isinstance(request_data, list):
            return JSONResponse(
                status_code=400,
                content={
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32600,
                        "message": "JSON-RPC batching not supported in MCP 2025-06-18"
                    },
                    "id": None
                },
                headers={"MCP-Protocol-Version": protocol_version}
            )
        
        mcp_request = MCPRequest(**request_data)
        
        # Handle different MCP methods
        if mcp_request.method == "initialize":
            result = handle_initialize(protocol_version)
            
        elif mcp_request.method == "tools/list":
            result = handle_tools_list()
            
        elif mcp_request.method == "tools/call":
            if not mcp_request.params:
                raise ValueError("Missing parameters for tools/call")
                
            tool_name = mcp_request.params.get("name")
            arguments = mcp_request.params.get("arguments", {})
            
            if not tool_name:
                raise ValueError("Missing tool name")
                
            result = handle_tools_call(tool_name, arguments)
            
        else:
            return JSONResponse(
                content=MCPResponse(
                    id=mcp_request.id,
                    error=MCPError(
                        code=-32601,
                        message=f"Method not found: {mcp_request.method}"
                    ).dict()
                ).dict(),
                headers={"MCP-Protocol-Version": protocol_version}
            )
        
        # Return successful response
        response = MCPResponse(
            id=mcp_request.id,
            result=result
        )
        
        return JSONResponse(
            content=response.dict(),
            headers={"MCP-Protocol-Version": protocol_version}
        )
        
    except ValidationError as e:
        return JSONResponse(
            content=MCPResponse(
                id=getattr(request_data, 'id', None) if 'request_data' in locals() else None,
                error=MCPError(
                    code=-32602,
                    message="Invalid params",
                    data=str(e)
                ).dict()
            ).dict(),
            headers={"MCP-Protocol-Version": protocol_version}
        )
        
    except json.JSONDecodeError:
        return JSONResponse(
            content=MCPResponse(
                error=MCPError(
                    code=-32700,
                    message="Parse error"
                ).dict()
            ).dict(),
            headers={"MCP-Protocol-Version": protocol_version}
        )
        
    except Exception as e:
        return JSONResponse(
            content=MCPResponse(
                id=getattr(request_data, 'id', None) if 'request_data' in locals() else None,
                error=MCPError(
                    code=-32603,
                    message="Internal error",
                    data=str(e) if DEBUG else "Internal server error"
                ).dict()
            ).dict(),
            headers={"MCP-Protocol-Version": protocol_version}
        )

@app.get("/health")
async def health_check():
    """Health check endpoint with comprehensive server status"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "2.0.0",
        "server": "mcp-taste-server",
        "mcp_protocol_version": MCP_PROTOCOL_VERSION,
        "supported_versions": SUPPORTED_VERSIONS,
        "framework": "advanced-taste-analysis",
        "tools_available": len(MCP_TOOLS),
        "content_database_size": len(taste_interpreter.enhanced_content_db)
    }

@app.get("/")
async def root():
    """Root endpoint with comprehensive server information"""
    return {
        "name": "MCP Taste Recommendation Server",
        "version": "2.0.0",
        "description": "Advanced taste-based content recommendation engine implementing comprehensive prompt engineering framework",
        "mcp_protocol_version": MCP_PROTOCOL_VERSION,
        "supported_versions": SUPPORTED_VERSIONS,
        "framework_features": [
            "Narrative DNA Extraction",
            "Emotional Texture Mapping", 
            "Stylistic Signature Detection",
            "Anti-Pattern Identification",
            "6-Factor Evaluation Matrix",
            "Contextual Adaptation",
            "Source Validation",
            "Craft Quality Assessment"
        ],
        "endpoints": {
            "mcp": "/mcp",
            "health": "/health",
            "docs": "/docs" if DEBUG else "disabled"
        },
        "tools": [tool["name"] for tool in MCP_TOOLS],
        "content_types": ["tv", "movie", "podcast", "mixed"],
        "built_for": "Pooch AI Hackathon - #BuildWithPouch"
    }

# Additional utility endpoints for development
if DEBUG:
    @app.get("/test-taste-extraction")
    async def test_taste_extraction(user_input: str = "Something like The Office but not a sitcom"):
        """Test endpoint for taste extraction (development only)"""
        profile = taste_interpreter.extract_taste_profile(user_input, "mixed")
        return {
            "input": user_input,
            "extracted_profile": profile.dict(),
            "timestamp": datetime.now().isoformat()
        }
    
    @app.get("/test-recommendations")
    async def test_recommendations(user_input: str = "Something like The Office but not a sitcom"):
        """Test endpoint for recommendations (development only)"""
        profile = taste_interpreter.extract_taste_profile(user_input, "mixed")
        recommendations = taste_interpreter.generate_recommendations(profile)
        formatted = taste_interpreter.format_recommendations_for_whatsapp(recommendations, profile)
        
        return {
            "input": user_input,
            "recommendations": [rec.dict() for rec in recommendations],
            "formatted_response": formatted,
            "timestamp": datetime.now().isoformat()
        }

# Server startup
if __name__ == "__main__":
    print("🚀 Starting MCP Taste Recommendation Server")
    print(f"📋 Version: 2.0.0")
    print(f"🔗 MCP Protocol: {MCP_PROTOCOL_VERSION}")
    print(f"🌐 Server URL: http://0.0.0.0:{PORT}")
    print(f"📱 Validate endpoint returns: {MY_NUMBER}")
    print(f"🔐 Authentication token: {AUTH_TOKEN[:8]}...")
    print(f"🎯 Framework: Advanced Taste Analysis Engine")
    print(f"📚 Content database: {len(taste_interpreter.enhanced_content_db)} items")
    print(f"🛠️  Tools available: {len(MCP_TOOLS)}")
    print("🎬 Ready for Pooch AI integration!")
    
    uvicorn.run(
        "mcp_starter:app",
        host="0.0.0.0",
        port=PORT,
        reload=DEBUG,
        log_level="info" if DEBUG else "warning"
    )
