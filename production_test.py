#!/usr/bin/env python3
"""
Comprehensive Production Readiness Test Suite
Tests all aspects of the MCP Taste Recommendation Server
"""

import sys
import os
import json
import time
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all critical imports"""
    try:
        from taste_engine import MasterTasteInterpreter, EnhancedTasteProfile, EnhancedRecommendation
        from mcp_starter import (
            execute_validate, execute_get_taste_recommendations, 
            execute_extract_taste_profile, execute_handle_contextual_request,
            handle_initialize, handle_tools_list, handle_tools_call
        )
        return True, "All imports successful"
    except Exception as e:
        return False, f"Import failed: {e}"

def test_taste_engine_comprehensive():
    """Comprehensive taste engine testing"""
    from taste_engine import MasterTasteInterpreter
    
    interpreter = MasterTasteInterpreter()
    
    # Test different input scenarios
    test_scenarios = [
        {"input": "Something like The Office but not a sitcom", "expected_elements": ["workplace", "character"]},
        {"input": "I want something cozy and comforting for evening", "expected_elements": ["cozy", "comfort"]},
        {"input": "Give me something with smart dialogue and character development", "expected_elements": ["intellectual", "character"]},
        {"input": "Something mysterious but not violent or scary", "expected_elements": ["mystery"], "anti_patterns": ["violence"]},
        {"input": "A podcast with two hosts having casual conversations", "expected_elements": ["conversational", "duo"]},
        {"input": "Something that makes me think but isn't too heavy", "expected_elements": ["intellectual"]},
    ]
    
    results = []
    for i, scenario in enumerate(test_scenarios, 1):
        try:
            profile = interpreter.extract_taste_profile(scenario["input"])
            recommendations = interpreter.generate_recommendations(profile)
            formatted = interpreter.format_recommendations_for_whatsapp(recommendations, profile)
            
            results.append({
                "test": i,
                "input": scenario["input"][:50] + "...",
                "profile_elements": len(profile.narrative_dna.story_structure) + len(profile.emotional_texture.primary_mood),
                "recommendations": len(recommendations),
                "formatted_length": len(formatted),
                "success": True
            })
        except Exception as e:
            results.append({
                "test": i,
                "input": scenario["input"][:50] + "...",
                "error": str(e),
                "success": False
            })
    
    return results

def test_mcp_protocol_compliance():
    """Test MCP protocol compliance"""
    from mcp_starter import handle_initialize, handle_tools_list, handle_tools_call
    
    tests = []
    
    # Test initialize
    try:
        init_result = handle_initialize("2025-06-18")
        assert "protocolVersion" in init_result
        assert "serverInfo" in init_result
        assert "capabilities" in init_result
        tests.append({"test": "initialize", "success": True})
    except Exception as e:
        tests.append({"test": "initialize", "success": False, "error": str(e)})
    
    # Test tools/list
    try:
        tools_result = handle_tools_list()
        assert "tools" in tools_result
        assert len(tools_result["tools"]) == 4  # validate, get_taste_recommendations, extract_taste_profile, handle_contextual_request
        tests.append({"test": "tools/list", "success": True, "tools_count": len(tools_result["tools"])})
    except Exception as e:
        tests.append({"test": "tools/list", "success": False, "error": str(e)})
    
    # Test tools/call
    tool_tests = [
        {"tool": "validate", "args": {}},
        {"tool": "get_taste_recommendations", "args": {"user_input": "Something like The Office"}},
        {"tool": "extract_taste_profile", "args": {"user_input": "Something cozy"}},
        {"tool": "handle_contextual_request", "args": {"user_input": "Something like X but not Y", "request_type": "something_like_but_not"}}
    ]
    
    for tool_test in tool_tests:
        try:
            result = handle_tools_call(tool_test["tool"], tool_test["args"])
            if "error" not in result:
                tests.append({"test": f"tools/call/{tool_test['tool']}", "success": True})
            else:
                tests.append({"test": f"tools/call/{tool_test['tool']}", "success": False, "error": result["error"]})
        except Exception as e:
            tests.append({"test": f"tools/call/{tool_test['tool']}", "success": False, "error": str(e)})
    
    return tests

def test_recommendation_quality():
    """Test recommendation quality and formatting"""
    from mcp_starter import execute_get_taste_recommendations
    
    quality_tests = []
    
    test_inputs = [
        "Something like The Office but not a sitcom",
        "I want something cozy for a rainy evening",
        "Give me a smart podcast with good conversations",
        "Something mysterious but not too dark"
    ]
    
    for i, test_input in enumerate(test_inputs, 1):
        try:
            result = execute_get_taste_recommendations(test_input, "mixed")
            
            # Quality checks
            checks = {
                "success": result.get("success", False),
                "has_recommendations": len(result.get("recommendations", [])) > 0,
                "has_formatted_response": len(result.get("formatted_response", "")) > 100,
                "has_taste_profile": result.get("taste_profile") is not None,
                "response_has_confidence": any(emoji in result.get("formatted_response", "") for emoji in ["🔥", "✨", "🎲"])
            }
            
            quality_score = sum(checks.values()) / len(checks) * 100
            
            quality_tests.append({
                "test": f"quality_{i}",
                "input": test_input[:30] + "...",
                "quality_score": quality_score,
                "checks": checks,
                "success": quality_score >= 80
            })
            
        except Exception as e:
            quality_tests.append({
                "test": f"quality_{i}",
                "input": test_input[:30] + "...",
                "error": str(e),
                "success": False
            })
    
    return quality_tests

def test_edge_cases():
    """Test edge cases and error handling"""
    from mcp_starter import execute_get_taste_recommendations, execute_extract_taste_profile
    
    edge_tests = []
    
    edge_cases = [
        {"input": "", "description": "empty_input"},
        {"input": "a", "description": "single_character"},
        {"input": "x" * 1000, "description": "very_long_input"},
        {"input": "🎬🎭🎪🎨🎵", "description": "emoji_only"},
        {"input": "1234567890", "description": "numbers_only"},
    ]
    
    for case in edge_cases:
        try:
            result = execute_get_taste_recommendations(case["input"], "mixed")
            # Should handle gracefully, not crash
            edge_tests.append({
                "test": case["description"],
                "success": True,
                "handled_gracefully": result.get("success", False) or "error" in result
            })
        except Exception as e:
            edge_tests.append({
                "test": case["description"],
                "success": False,
                "error": str(e)
            })
    
    return edge_tests

def test_performance():
    """Test performance benchmarks"""
    from mcp_starter import execute_get_taste_recommendations
    
    performance_tests = []
    
    # Test response times
    test_input = "Something like The Office but not a sitcom"
    
    for i in range(3):
        start_time = time.time()
        try:
            result = execute_get_taste_recommendations(test_input, "tv")
            end_time = time.time()
            response_time = end_time - start_time
            
            performance_tests.append({
                "test": f"performance_{i+1}",
                "response_time_seconds": round(response_time, 3),
                "success": result.get("success", False),
                "meets_target": response_time < 5.0  # Target: under 5 seconds
            })
        except Exception as e:
            performance_tests.append({
                "test": f"performance_{i+1}",
                "error": str(e),
                "success": False
            })
    
    return performance_tests

def main():
    """Run comprehensive production readiness tests"""
    print("🧪 COMPREHENSIVE PRODUCTION READINESS TEST SUITE")
    print("=" * 70)
    print(f"📅 Test Date: {datetime.now().isoformat()}")
    print()
    
    all_results = {}
    overall_success = True
    
    # Test 1: Imports
    print("1. 📦 Testing Imports...")
    success, message = test_imports()
    all_results["imports"] = {"success": success, "message": message}
    if success:
        print(f"   ✅ {message}")
    else:
        print(f"   ❌ {message}")
        overall_success = False
    
    # Test 2: Taste Engine
    print("\n2. 🧠 Testing Taste Engine...")
    taste_results = test_taste_engine_comprehensive()
    successful_taste_tests = sum(1 for r in taste_results if r["success"])
    all_results["taste_engine"] = taste_results
    print(f"   ✅ {successful_taste_tests}/{len(taste_results)} taste engine tests passed")
    if successful_taste_tests < len(taste_results):
        overall_success = False
    
    # Test 3: MCP Protocol
    print("\n3. 🚀 Testing MCP Protocol Compliance...")
    mcp_results = test_mcp_protocol_compliance()
    successful_mcp_tests = sum(1 for r in mcp_results if r["success"])
    all_results["mcp_protocol"] = mcp_results
    print(f"   ✅ {successful_mcp_tests}/{len(mcp_results)} MCP protocol tests passed")
    if successful_mcp_tests < len(mcp_results):
        overall_success = False
    
    # Test 4: Recommendation Quality
    print("\n4. 🎯 Testing Recommendation Quality...")
    quality_results = test_recommendation_quality()
    successful_quality_tests = sum(1 for r in quality_results if r["success"])
    all_results["recommendation_quality"] = quality_results
    print(f"   ✅ {successful_quality_tests}/{len(quality_results)} quality tests passed")
    avg_quality = sum(r.get("quality_score", 0) for r in quality_results if "quality_score" in r) / len(quality_results)
    print(f"   📊 Average quality score: {avg_quality:.1f}%")
    if successful_quality_tests < len(quality_results) or avg_quality < 80:
        overall_success = False
    
    # Test 5: Edge Cases
    print("\n5. ⚠️  Testing Edge Cases...")
    edge_results = test_edge_cases()
    successful_edge_tests = sum(1 for r in edge_results if r["success"])
    all_results["edge_cases"] = edge_results
    print(f"   ✅ {successful_edge_tests}/{len(edge_results)} edge case tests passed")
    if successful_edge_tests < len(edge_results):
        overall_success = False
    
    # Test 6: Performance
    print("\n6. ⚡ Testing Performance...")
    perf_results = test_performance()
    successful_perf_tests = sum(1 for r in perf_results if r.get("meets_target", False))
    all_results["performance"] = perf_results
    avg_response_time = sum(r.get("response_time_seconds", 0) for r in perf_results if "response_time_seconds" in r) / len(perf_results)
    print(f"   ✅ {successful_perf_tests}/{len(perf_results)} performance tests passed")
    print(f"   📊 Average response time: {avg_response_time:.2f}s")
    if successful_perf_tests < len(perf_results):
        overall_success = False
    
    # Summary
    print("\n" + "=" * 70)
    if overall_success:
        print("🎉 PRODUCTION READINESS: ✅ PASSED")
        print()
        print("🚀 Your MCP Taste Recommendation Server is PRODUCTION READY!")
        print("   • All critical tests passed")
        print("   • MCP protocol compliance verified")
        print("   • Recommendation quality meets standards")
        print("   • Performance targets achieved")
        print("   • Edge cases handled gracefully")
        print()
        print("🏆 Ready for Pooch AI Hackathon deployment!")
    else:
        print("❌ PRODUCTION READINESS: FAILED")
        print()
        print("⚠️  Some tests failed. Review the results above.")
        print("   Fix any issues before production deployment.")
    
    # Save detailed results
    with open("production_test_results.json", "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n📊 Detailed results saved to: production_test_results.json")
    
    return 0 if overall_success else 1

if __name__ == "__main__":
    sys.exit(main())
