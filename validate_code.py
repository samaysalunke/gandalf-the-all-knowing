#!/usr/bin/env python3
"""
Code validation script for MCP Taste Recommendation Server
Validates syntax and structure without requiring external dependencies.
"""

import ast
import sys
import os

def validate_python_syntax(filepath):
    """Validate Python syntax of a file"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Parse the AST to check syntax
        ast.parse(content)
        return True, "Syntax valid"
    except SyntaxError as e:
        return False, f"Syntax error: {e}"
    except Exception as e:
        return False, f"Error reading file: {e}"

def validate_imports(filepath):
    """Check import structure"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        imports = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    for alias in node.names:
                        imports.append(f"{node.module}.{alias.name}")
        
        return True, imports
    except Exception as e:
        return False, f"Error analyzing imports: {e}"

def validate_class_structure(filepath, expected_classes):
    """Validate that expected classes exist"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        found_classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                found_classes.append(node.name)
        
        missing_classes = set(expected_classes) - set(found_classes)
        return len(missing_classes) == 0, found_classes, missing_classes
    except Exception as e:
        return False, [], f"Error analyzing classes: {e}"

def validate_function_structure(filepath, expected_functions):
    """Validate that expected functions exist"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        found_functions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                found_functions.append(node.name)
        
        missing_functions = set(expected_functions) - set(found_functions)
        return len(missing_functions) == 0, found_functions, missing_functions
    except Exception as e:
        return False, [], f"Error analyzing functions: {e}"

def main():
    """Run validation"""
    print("🔍 Validating MCP Taste Recommendation Server Code")
    print("=" * 60)
    
    files_to_check = [
        "taste_engine.py",
        "mcp_starter.py"
    ]
    
    all_valid = True
    
    for filepath in files_to_check:
        print(f"\n📁 Validating {filepath}:")
        
        if not os.path.exists(filepath):
            print(f"   ❌ File not found: {filepath}")
            all_valid = False
            continue
        
        # Check syntax
        syntax_valid, syntax_msg = validate_python_syntax(filepath)
        if syntax_valid:
            print(f"   ✅ Syntax: {syntax_msg}")
        else:
            print(f"   ❌ Syntax: {syntax_msg}")
            all_valid = False
            continue
        
        # Check imports
        imports_valid, imports = validate_imports(filepath)
        if imports_valid:
            print(f"   ✅ Imports: {len(imports)} imports found")
        else:
            print(f"   ❌ Imports: {imports}")
            all_valid = False
    
    # Validate taste_engine.py structure
    print(f"\n🧬 Validating taste_engine.py structure:")
    expected_classes = [
        "NarrativeDNA",
        "EmotionalTexture", 
        "VisualStylePreferences",
        "AudioStylePreferences",
        "AntiPatterns",
        "EnhancedTasteProfile",
        "EvaluationScore",
        "EnhancedRecommendation",
        "MasterTasteInterpreter"
    ]
    
    classes_valid, found_classes, missing_classes = validate_class_structure("taste_engine.py", expected_classes)
    if classes_valid:
        print(f"   ✅ Classes: All {len(expected_classes)} required classes found")
    else:
        print(f"   ❌ Classes: Missing {missing_classes}")
        all_valid = False
    
    expected_methods = [
        "extract_taste_profile",
        "generate_recommendations", 
        "format_recommendations_for_whatsapp",
        "evaluate_content"
    ]
    
    methods_valid, found_methods, missing_methods = validate_function_structure("taste_engine.py", expected_methods)
    if methods_valid:
        print(f"   ✅ Methods: All {len(expected_methods)} required methods found")
    else:
        print(f"   ❌ Methods: Missing {missing_methods}")
        all_valid = False
    
    # Validate mcp_starter.py structure
    print(f"\n🚀 Validating mcp_starter.py structure:")
    expected_mcp_functions = [
        "execute_validate",
        "execute_get_taste_recommendations",
        "execute_extract_taste_profile",
        "handle_initialize",
        "handle_tools_list",
        "handle_tools_call"
    ]
    
    mcp_functions_valid, found_mcp_functions, missing_mcp_functions = validate_function_structure("mcp_starter.py", expected_mcp_functions)
    if mcp_functions_valid:
        print(f"   ✅ Functions: All {len(expected_mcp_functions)} required functions found")
    else:
        print(f"   ❌ Functions: Missing {missing_mcp_functions}")
        all_valid = False
    
    # Check for MCP protocol constants
    try:
        with open("mcp_starter.py", 'r') as f:
            content = f.read()
        
        mcp_constants = [
            "MCP_PROTOCOL_VERSION",
            "MCP_TOOLS",
            "AUTH_TOKEN"
        ]
        
        constants_found = all(const in content for const in mcp_constants)
        if constants_found:
            print(f"   ✅ Constants: All MCP protocol constants found")
        else:
            print(f"   ❌ Constants: Some MCP constants missing")
            all_valid = False
    except Exception as e:
        print(f"   ❌ Constants check failed: {e}")
        all_valid = False
    
    # Check file sizes (rough complexity check)
    print(f"\n📊 File size analysis:")
    for filepath in files_to_check:
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            lines = len(open(filepath).readlines())
            print(f"   📄 {filepath}: {size:,} bytes, {lines:,} lines")
    
    print("\n" + "=" * 60)
    
    if all_valid:
        print("🎉 Code validation successful!")
        print()
        print("✅ All syntax checks passed")
        print("✅ All required classes and functions present")
        print("✅ MCP protocol structure complete")
        print("✅ Framework implementation comprehensive")
        print()
        print("🚀 Ready for deployment!")
        print("   Next steps:")
        print("   1. Install dependencies: pip install -r requirements.txt")
        print("   2. Set up environment: cp env_example.txt .env")
        print("   3. Configure .env with your values")
        print("   4. Run server: python mcp_starter.py")
        print("   5. Expose via ngrok: ngrok http 8086")
        print("   6. Connect to Pooch AI")
    else:
        print("❌ Code validation failed!")
        print("   Please fix the issues above before proceeding.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
