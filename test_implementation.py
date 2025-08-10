#!/usr/bin/env python3
"""
Test script for MCP Taste Recommendation Server
Validates the implementation without requiring external dependencies.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_taste_engine_import():
    """Test that taste engine imports correctly"""
    try:
        from taste_engine import MasterTasteInterpreter, EnhancedTasteProfile
        print("✅ Taste engine imports successfully")
        return True
    except Exception as e:
        print(f"❌ Taste engine import failed: {e}")
        return False

def test_taste_profile_creation():
    """Test taste profile creation"""
    try:
        from taste_engine import MasterTasteInterpreter
        
        interpreter = MasterTasteInterpreter()
        profile = interpreter.extract_taste_profile(
            "Something like The Office but not a sitcom", 
            "tv"
        )
        
        print("✅ Taste profile creation successful")
        print(f"   - Narrative elements found: {len(profile.narrative_dna.story_structure)}")
        print(f"   - Emotional elements found: {len(profile.emotional_texture.primary_mood)}")
        print(f"   - Anti-patterns detected: {len(profile.anti_patterns.deal_breakers)}")
        return True
    except Exception as e:
        print(f"❌ Taste profile creation failed: {e}")
        return False

def test_recommendation_generation():
    """Test recommendation generation"""
    try:
        from taste_engine import MasterTasteInterpreter
        
        interpreter = MasterTasteInterpreter()
        profile = interpreter.extract_taste_profile(
            "Something like The Office but not a sitcom", 
            "tv"
        )
        
        recommendations = interpreter.generate_recommendations(profile)
        
        print("✅ Recommendation generation successful")
        print(f"   - Recommendations generated: {len(recommendations)}")
        
        if recommendations:
            rec = recommendations[0]
            print(f"   - Top recommendation: {rec.title}")
            print(f"   - Match strength: {rec.match_strength}")
            print(f"   - Confidence: {rec.confidence_percentage:.1f}%")
        
        return True
    except Exception as e:
        print(f"❌ Recommendation generation failed: {e}")
        return False

def test_whatsapp_formatting():
    """Test WhatsApp formatting"""
    try:
        from taste_engine import MasterTasteInterpreter
        
        interpreter = MasterTasteInterpreter()
        profile = interpreter.extract_taste_profile(
            "Something like The Office but not a sitcom", 
            "tv"
        )
        
        recommendations = interpreter.generate_recommendations(profile)
        formatted = interpreter.format_recommendations_for_whatsapp(recommendations, profile)
        
        print("✅ WhatsApp formatting successful")
        print(f"   - Formatted response length: {len(formatted)} characters")
        print(f"   - Contains confidence indicators: {'🔥' in formatted or '✨' in formatted or '🎲' in formatted}")
        
        return True
    except Exception as e:
        print(f"❌ WhatsApp formatting failed: {e}")
        return False

def test_content_database():
    """Test content database initialization"""
    try:
        from taste_engine import MasterTasteInterpreter
        
        interpreter = MasterTasteInterpreter()
        db_size = len(interpreter.enhanced_content_db)
        
        print("✅ Content database initialization successful")
        print(f"   - Database size: {db_size} items")
        
        # Test a specific content item
        if "shrinking" in interpreter.enhanced_content_db:
            shrinking = interpreter.enhanced_content_db["shrinking"]
            print(f"   - Sample content: {shrinking['title']} ({shrinking['platform']})")
            print(f"   - Quality indicators: {shrinking.get('quality_indicators', [])}")
        
        return True
    except Exception as e:
        print(f"❌ Content database test failed: {e}")
        return False

def test_evaluation_matrix():
    """Test 6-factor evaluation matrix"""
    try:
        from taste_engine import MasterTasteInterpreter
        
        interpreter = MasterTasteInterpreter()
        profile = interpreter.extract_taste_profile(
            "Something like The Office but not a sitcom", 
            "tv"
        )
        
        # Test evaluation of a known content item
        if "shrinking" in interpreter.enhanced_content_db:
            content = interpreter.enhanced_content_db["shrinking"]
            evaluation = interpreter.evaluate_content(content, profile)
            
            print("✅ Evaluation matrix successful")
            print(f"   - Taste match strength: {evaluation.taste_match_strength:.1f}/10")
            print(f"   - Anti-pattern avoidance: {evaluation.anti_pattern_avoidance:.1f}/10")
            print(f"   - Context fit: {evaluation.context_fit:.1f}/10")
            print(f"   - Discovery value: {evaluation.discovery_value:.1f}/10")
            print(f"   - Source validation: {evaluation.source_validation:.1f}/10")
            print(f"   - Craft quality: {evaluation.craft_quality:.1f}/10")
            print(f"   - Total score: {evaluation.total_score:.1f}/60")
        
        return True
    except Exception as e:
        print(f"❌ Evaluation matrix test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing MCP Taste Recommendation Server Implementation")
    print("=" * 60)
    
    tests = [
        test_taste_engine_import,
        test_content_database,
        test_taste_profile_creation,
        test_evaluation_matrix,
        test_recommendation_generation,
        test_whatsapp_formatting
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        print()
        if test():
            passed += 1
        
    print()
    print("=" * 60)
    print(f"🎯 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Implementation is ready!")
        print()
        print("🚀 Next steps:")
        print("   1. Install dependencies: pip install -r requirements.txt")
        print("   2. Set up .env file with your credentials")
        print("   3. Run server: python mcp_starter.py")
        print("   4. Expose via ngrok: ngrok http 8086")
        print("   5. Connect to Pooch: /mcp connect <https-url> <token>")
    else:
        print("❌ Some tests failed. Check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
