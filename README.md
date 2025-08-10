# 🎯 MCP Taste Recommendation Server

> **Advanced taste-based content recommendation engine for Pooch AI Hackathon**  
> *Implementing comprehensive prompt engineering framework for sophisticated taste interpretation*

[![MCP Protocol](https://img.shields.io/badge/MCP-2025--06--18-blue)](https://modelcontextprotocol.io)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-red)](https://fastapi.tiangolo.com)
[![Built for Pooch](https://img.shields.io/badge/Built%20for-Pooch%20AI-purple)](#)

## 🚀 **Revolutionary Approach**

This MCP server **revolutionizes content recommendations** by analyzing **WHY** users like content, not just WHAT they like. Instead of traditional genre-based matching, it extracts sophisticated taste elements:

- **🧬 Narrative DNA**: Story structure, pacing, conflict styles
- **💫 Emotional Texture**: Mood delivery, character relationships, intensity preferences  
- **🎨 Stylistic Signatures**: Visual/audio preferences, production values
- **⚡ Anti-Pattern Detection**: What to avoid based on user preferences
- **🎯 Context Awareness**: Current mood, time, viewing situation

## 🏗️ **Architecture**

### **Master Taste Interpreter**
Acts as a **cultural curator** and **conversation connoisseur** who understands:
- **Visual Content**: Cinematic language, narrative structure, visual storytelling
- **Audio Content**: Dialogue dynamics, information delivery, audio intimacy
- **All Content**: Eliminates decision paralysis with hyper-targeted recommendations

### **6-Factor Evaluation Matrix**
1. **Taste Match Strength** (1-10): How well content delivers extracted elements
2. **Anti-Pattern Avoidance** (1-10): How well it avoids stated dislikes  
3. **Context Fit** (1-10): Matches current mood/energy/time available
4. **Discovery Value** (1-10): Introduces something new within taste profile
5. **Source Validation** (1-10): Quality of discovery source (creator rec > algorithm)
6. **Craft Quality** (1-10): Evidence of intentional creative choices

## 🎮 **Quick Start**

### **1. Setup**
```bash
# Clone repository
git clone <repository-url>
cd mcp-taste-server

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### **2. Configuration**
```bash
# Copy environment template
cp env_example.txt .env

# Edit .env with your values:
AUTH_TOKEN=your_secret_token_here
MY_NUMBER=919876543210  # Format: {country_code}{number}
PORT=8086
MCP_PROTOCOL_VERSION=2025-06-18
```

### **3. Run Server**
```bash
python mcp_starter.py
# 🚀 Server starts on http://0.0.0.0:8086
```

### **4. Expose via ngrok**
```bash
ngrok http 8086
# Copy the HTTPS URL
```

### **5. Connect to Pooch AI**
```
/mcp connect https://your-ngrok-url.ngrok-free.app/mcp your_secret_token
```

## 🛠️ **MCP Tools**

### **`validate`**
Returns server owner's phone number for Pooch validation.

**Parameters:** None  
**Returns:** `{"phone_number": "919876543210", "status": "validated"}`

### **`get_taste_recommendations`** 
Main recommendation engine implementing the comprehensive framework.

**Parameters:**
- `user_input` (required): User's description or reference content
- `content_type` (optional): "tv", "movie", "podcast", "mixed" 
- `current_mood` (optional): Current mood/energy level
- `time_available` (optional): Available time for content
- `viewing_situation` (optional): Social context

**Returns:** Structured recommendations with detailed explanations

### **`extract_taste_profile`**
Analyzes user input to extract comprehensive taste elements.

**Parameters:**
- `user_input` (required): Content to analyze
- `content_type` (optional): Type of content analysis

### **`handle_contextual_request`**
Handles special request types with contextual adaptation.

**Parameters:**
- `user_input` (required): User's contextual request
- `request_type` (required): Type of request ("something_like_but_not", "dont_know", "surprise_me")

## 🎭 **Example Interaction**

### **Input:** 
```
"Something like The Office but not a sitcom"
```

### **Advanced Analysis:**
```
🧬 Narrative DNA:
- Workplace authenticity without forced structure
- Character growth through mundane situations  
- Episodic but character-driven

💫 Emotional Texture:
- Cozy comfort without saccharine moments
- Dry humor without laugh track dependency
- Protective relationship with characters

⚡ Anti-Patterns:
- Traditional sitcom format
- Forced comedy structures
```

### **Output:**
```
🎯 Your Personalized Recommendations

🔥 **Shrinking** - Apple TV+/2023

**Why it matches your taste:** Workplace therapy practice with authentic 
relationship dynamics, character development through daily interactions 
rather than episode plots, dry humor emerging from real situations

**What to expect:** Jason Segel as therapist breaking conventional boundaries, 
similar warmth to The Office but in dramatic format with genuine stakes

**Perfect for:** When you want Office-style character moments with more 
emotional depth

**Avoid if:** You're looking for pure comedy without heavier themes

*Quality indicators: Creator Driven, Film Director Involvement*

---

✨ **Atlanta** - FX/Hulu/2016

**Why it matches your taste:** Authentic slice-of-life following aspiring 
rapper and cousin, dry observational humor without traditional comedy structure

**What to expect:** Surreal moments mixed with realistic character interactions, 
unpredictable episode formats

**Perfect for:** Viewers who appreciate subtle humor and authentic character moments

**Avoid if:** You prefer structured plots and clear episode objectives

*Quality indicators: Creator Driven, Auteur Vision*
```

## 🧠 **Framework Features**

### **Narrative DNA Extraction**
- **Story Structure**: Episodic vs serialized, character vs plot-driven
- **Pacing**: Slow burn, quick cuts, deliberate builds
- **Conflict Style**: Internal growth, external obstacles, interpersonal
- **Resolution**: Ambiguous endings, clear closure, ongoing mysteries

### **Emotional Texture Mapping**
- **Primary Mood**: Cozy comfort, intellectual stimulation, cathartic release
- **Journey Type**: Steady state, emotional rollercoaster, gradual build
- **Intensity**: Background viewing vs full attention required
- **Character Bonds**: Aspirational, relatable, observational, protective

### **Medium-Specific Analysis**

**Visual Content:**
- Visual preferences (naturalistic vs stylized)
- Performance energy (understated vs theatrical)
- Technical craft appreciation

**Audio Content:**
- Host dynamics (solo vs conversational vs panel)
- Delivery style (structured vs meandering vs interview)
- Intimacy level (personal vs professional vs friendly)
- Production values (highly produced vs raw conversation)

### **Quality Indicators**
- **Film Director Involvement** (+2 points)
- **Book Adaptation** (+2 points)  
- **Creator-Driven Vision** (+1 point)
- **Limited Series Format** (+1 point)
- **Award Recognition** (Emmy, Oscar, Peabody)
- **Critical Acclaim** (Professional validation)

## 🔧 **Technical Architecture**

### **MCP Protocol 2025-06-18 Compliance**
- ✅ Protocol version enforcement via headers
- ✅ No JSON-RPC batching (removed in latest spec)
- ✅ Bearer token authentication
- ✅ Origin header validation (DNS rebinding protection)
- ✅ HTTPS required (via ngrok for development)
- ✅ Proper error handling with JSON-RPC 2.0 format

### **Content Database Structure**
```python
{
    "title": "Content Title",
    "platform": "Streaming Service", 
    "quality_indicators": ["creator_driven", "film_director"],
    "source_validation": ["critic_acclaim", "award_winner"],
    "narrative_dna": {
        "story_structure": ["character_driven"],
        "conflict_style": ["internal_growth"]
    },
    "emotional_texture": {
        "primary_mood": ["cozy_comfort"],
        "character_relationship": ["relatable"]
    },
    "craft_elements": ["authentic_workplace", "character_development"]
}
```

### **Evaluation Pipeline**
1. **Extract** comprehensive taste profile
2. **Score** content using 6-factor matrix
3. **Rank** by total evaluation score
4. **Select** top 2-3 recommendations
5. **Format** with explanations and confidence levels

## 🎯 **Confidence Indicators**

- **🔥 Perfect Match** (90%+ taste alignment)
- **✨ Strong Match** (75-89% taste alignment)  
- **🎲 Interesting Gamble** (60-74% taste alignment, high discovery value)

## 🔐 **Security Features**

- **Bearer Token Authentication**: Secure API access
- **Origin Header Validation**: DNS rebinding protection
- **Protocol Version Enforcement**: MCP spec compliance
- **Input Validation**: Comprehensive parameter checking
- **Error Sanitization**: Secure error responses

## 🧪 **Development & Testing**

### **Local Testing**
```bash
# Test health endpoint
curl http://localhost:8086/health

# Test MCP endpoint (requires auth)
curl -X POST http://localhost:8086/mcp \
  -H "Authorization: Bearer your_token" \
  -H "Content-Type: application/json" \
  -H "MCP-Protocol-Version: 2025-06-18" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":"1"}'
```

### **Development Endpoints** (DEBUG=true only)
- `/test-taste-extraction?user_input=...` - Test taste analysis
- `/test-recommendations?user_input=...` - Test recommendation generation
- `/docs` - FastAPI documentation
- `/redoc` - Alternative API docs

### **Extending Content Database**
```python
# Add new content to taste_engine.py
"new_content": {
    "title": "New Show",
    "platform": "Netflix",
    "quality_indicators": ["creator_driven"],
    "narrative_dna": {...},
    "emotional_texture": {...},
    "why_template": "Explanation of why it matches taste",
    "what_to_expect": "What user should expect",
    "perfect_for": "Ideal viewing context", 
    "avoid_if": "When to skip this content"
}
```

## 📊 **Performance Metrics**

- **Response Time**: < 2 seconds for recommendation generation
- **Content Database**: 10+ curated high-quality entries
- **Taste Elements**: 50+ narrative/emotional/style patterns
- **Evaluation Factors**: 6-dimensional scoring matrix
- **Protocol Compliance**: MCP 2025-06-18 specification

## 🏆 **Hackathon Features**

### **✅ MCP Protocol Compliance**
- Follows latest 2025-06-18 specification exactly
- Implements required `validate` tool
- Uses Bearer token authentication  
- Returns proper JSON-RPC 2.0 responses
- Serves over HTTPS (ngrok)

### **✅ Advanced Taste Engine**
- Extracts WHY users like content, not just WHAT
- Searches by taste elements, not genres
- Provides detailed explanations for recommendations
- Handles different content types (TV, movies, podcasts)
- Eliminates decision paralysis with 2-3 curated options

### **✅ Pooch AI Integration**
- Works seamlessly with WhatsApp bot
- Handles user input via MCP tools
- Returns formatted recommendations for chat
- Provides meaningful taste analysis
- Supports contextual adaptation

### **✅ Quality Indicators**
- Source validation (awards, critical acclaim)
- Craft quality assessment
- Discovery value calculation
- Anti-pattern avoidance
- Context-aware recommendations

## 🎨 **Built for Pooch AI Hackathon**

This server represents the **next evolution** of content recommendation systems:

- **🧠 Intelligence**: Advanced prompt engineering framework
- **🎯 Precision**: 6-factor evaluation matrix
- **⚡ Speed**: 2-3 curated options, no decision paralysis  
- **🔍 Depth**: Analyzes taste at narrative and emotional levels
- **🌟 Quality**: Prioritizes craft and artistic merit
- **📱 Integration**: Seamless WhatsApp experience via Pooch

**#BuildWithPouch** 🚀

---

## 📞 **Support**

For issues, questions, or contributions:
- 📧 Email: samay@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/samaysalunke/mcp-taste-server/issues)
- 📚 Docs: This README + inline code documentation

**Built with ❤️ for the Pooch AI Hackathon**
