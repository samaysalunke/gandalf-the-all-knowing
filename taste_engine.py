"""
Enhanced Taste Recommendation Engine
Implements comprehensive taste analysis framework for content recommendations.
Based on advanced prompt engineering for sophisticated taste interpretation.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Literal, Union, Any
from enum import Enum
import re
import json
from datetime import datetime
import logging

# Enhanced Data Models implementing the full framework

class NarrativeDNA(BaseModel):
    """Narrative structure preferences"""
    story_structure: List[str] = Field(default_factory=list, description="episodic, serialized, character_driven, plot_driven")
    pacing_preferences: List[str] = Field(default_factory=list, description="slow_burn, quick_cuts, deliberate_builds")
    conflict_style: List[str] = Field(default_factory=list, description="internal_growth, external_obstacles, interpersonal")
    resolution_patterns: List[str] = Field(default_factory=list, description="ambiguous, clear_closure, ongoing_mysteries")

class EmotionalTexture(BaseModel):
    """Emotional experience preferences"""
    primary_mood: List[str] = Field(default_factory=list, description="cozy_comfort, intellectual_stimulation, cathartic_release, escapist_fantasy")
    emotional_journey: List[str] = Field(default_factory=list, description="steady_state, emotional_rollercoaster, gradual_build, surprising_shifts")
    intensity_comfort: List[str] = Field(default_factory=list, description="background_viewing, full_attention_required")
    character_relationship: List[str] = Field(default_factory=list, description="aspirational, relatable, observational, protective")

class VisualStylePreferences(BaseModel):
    """Visual content style preferences"""
    visual_preferences: List[str] = Field(default_factory=list, description="naturalistic, stylized, minimal, rich_production")
    performance_energy: List[str] = Field(default_factory=list, description="understated, theatrical, naturalistic, heightened")
    technical_craft: List[str] = Field(default_factory=list, description="cinematography_conscious, story_focused")

class AudioStylePreferences(BaseModel):
    """Podcast/audio content style preferences"""
    host_dynamics: List[str] = Field(default_factory=list, description="solo_expertise, conversational_duos, panel_discussions")
    delivery_style: List[str] = Field(default_factory=list, description="structured_lessons, meandering_conversations, interview_format")
    intimacy_level: List[str] = Field(default_factory=list, description="personal_confessions, professional_distance, friend_like_chat")
    production_values: List[str] = Field(default_factory=list, description="highly_produced, raw_conversation, sound_design")

class AntiPatterns(BaseModel):
    """Content elements to avoid"""
    deal_breakers: List[str] = Field(default_factory=list, description="forced_laugh_tracks, excessive_violence, slow_pacing")
    tone_violations: List[str] = Field(default_factory=list, description="cringe_humor, melodrama")
    structural_issues: List[str] = Field(default_factory=list, description="rushed_endings, too_many_subplots, predictable_arcs")
    context_mismatches: List[str] = Field(default_factory=list, description="requires_too_much_attention")

class EnhancedTasteProfile(BaseModel):
    """Comprehensive taste profile using the advanced framework"""
    narrative_dna: NarrativeDNA = Field(default_factory=NarrativeDNA)
    emotional_texture: EmotionalTexture = Field(default_factory=EmotionalTexture)
    visual_style: Optional[VisualStylePreferences] = None
    audio_style: Optional[AudioStylePreferences] = None
    anti_patterns: AntiPatterns = Field(default_factory=AntiPatterns)
    context: Dict[str, str] = Field(default_factory=dict)
    content_type: str = "mixed"
    extraction_timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

class EvaluationScore(BaseModel):
    """6-factor evaluation matrix from the framework"""
    taste_match_strength: float = Field(ge=1.0, le=10.0, description="How well it delivers extracted elements")
    anti_pattern_avoidance: float = Field(ge=1.0, le=10.0, description="How well it avoids stated dislikes")
    context_fit: float = Field(ge=1.0, le=10.0, description="Matches current mood/energy/time")
    discovery_value: float = Field(ge=1.0, le=10.0, description="Introduces something new within taste profile")
    source_validation: float = Field(ge=1.0, le=10.0, description="Quality of discovery source")
    craft_quality: float = Field(ge=1.0, le=10.0, description="Evidence of intentional creative choices")
    total_score: float = Field(ge=6.0, le=60.0)

class EnhancedRecommendation(BaseModel):
    """Enhanced recommendation with full evaluation"""
    title: str
    platform: str
    year: Optional[str] = None
    content_type: Literal["movie", "tv_show", "podcast", "documentary", "limited_series"]
    match_strength: Literal["🔥", "✨", "🎲"]
    
    # Framework requirements
    why_matches: str = Field(description="2-3 specific taste elements that align")
    what_to_expect: str = Field(description="Experiential qualities, not plot")
    perfect_for: str = Field(description="Current context/mood/viewing situation")
    avoid_if: str = Field(description="Clear warning about what might not work")
    
    # Quality indicators
    quality_indicators: List[str] = Field(default_factory=list, description="film_director, book_adaptation, etc.")
    source_validation: List[str] = Field(default_factory=list, description="awards, critical_acclaim, etc.")
    craft_elements: List[str] = Field(default_factory=list, description="Specific craft qualities")
    
    # Evaluation scores
    evaluation: EvaluationScore
    confidence_percentage: float = Field(ge=0.0, le=100.0)

class MasterTasteInterpreter:
    """
    Master taste interpreter implementing the comprehensive framework.
    Acts as a cultural curator and conversation connoisseur.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._initialize_pattern_databases()
        self._initialize_content_database()
    
    def _initialize_pattern_databases(self):
        """Initialize comprehensive pattern matching databases"""
        
        # Narrative DNA patterns
        self.narrative_patterns = {
            # Story Structure
            "episodic": [
                "standalone episodes", "case by case", "procedural", "episodic", 
                "monster of the week", "self contained", "individual stories",
                "each episode different", "no continuing story"
            ],
            "serialized": [
                "ongoing story", "continuous narrative", "serialized", "long arc", 
                "season-long", "continuing plot", "story develops", "builds over time",
                "connected episodes", "overarching narrative"
            ],
            "character_driven": [
                "character development", "character focus", "personal growth", 
                "character study", "character arc", "character centered", 
                "about the people", "character relationships", "internal journey"
            ],
            "plot_driven": [
                "plot focused", "action driven", "event focused", "plot heavy",
                "story driven", "what happens", "events", "action packed"
            ],
            
            # Pacing preferences
            "slow_burn": [
                "slow burn", "gradual", "patient storytelling", "deliberate pace", 
                "takes time", "builds slowly", "patient", "unhurried", "meditative pace"
            ],
            "quick_cuts": [
                "fast paced", "quick", "rapid", "snappy", "energetic pace",
                "quick editing", "fast cuts", "rapid fire", "high energy"
            ],
            "deliberate_builds": [
                "building tension", "careful construction", "measured pace",
                "thoughtful pacing", "intentional build", "structured progression"
            ],
            
            # Conflict style
            "internal_growth": [
                "character growth", "internal conflict", "personal development", 
                "self discovery", "inner journey", "psychological", "introspective",
                "self reflection", "personal change"
            ],
            "external_obstacles": [
                "external challenges", "outside forces", "environmental conflict",
                "external pressure", "obstacles", "challenges from outside"
            ],
            "interpersonal": [
                "relationship dynamics", "interpersonal conflict", "social dynamics",
                "between people", "relationship tension", "social conflict",
                "people problems", "relationship drama"
            ],
            
            # Resolution patterns
            "ambiguous": [
                "open ended", "ambiguous", "unclear resolution", "open to interpretation",
                "no clear answer", "mysterious ending", "you decide"
            ],
            "clear_closure": [
                "clear ending", "resolution", "tied up", "conclusive",
                "everything resolved", "clear answers", "satisfying ending"
            ],
            "ongoing_mysteries": [
                "ongoing mystery", "continuing questions", "unresolved elements",
                "more to explore", "questions remain", "ongoing intrigue"
            ]
        }
        
        # Emotional texture patterns
        self.emotional_patterns = {
            # Primary mood
            "cozy_comfort": [
                "cozy", "comfort", "warm", "comforting", "safe", "familiar",
                "feel good", "heartwarming", "soothing", "gentle", "peaceful"
            ],
            "intellectual_stimulation": [
                "smart", "intellectual", "thought provoking", "clever", "cerebral",
                "makes you think", "complex", "sophisticated", "challenging ideas"
            ],
            "cathartic_release": [
                "cathartic", "emotional release", "purging", "therapeutic",
                "emotional", "crying", "moving", "powerful emotions"
            ],
            "escapist_fantasy": [
                "escapist", "fantasy", "otherworldly", "immersive", "escape",
                "different world", "magical", "fantastical", "not real world"
            ],
            
            # Emotional journey
            "steady_state": [
                "consistent tone", "steady", "even keel", "stable mood",
                "doesn't vary much", "consistent feeling", "steady emotional tone"
            ],
            "emotional_rollercoaster": [
                "emotional ups and downs", "rollercoaster", "intense emotions",
                "emotional swings", "high highs low lows", "emotional ride"
            ],
            "gradual_build": [
                "building emotion", "gradual", "slow emotional build",
                "emotions build", "growing feelings", "escalating emotion"
            ],
            "surprising_shifts": [
                "surprising turns", "unexpected emotions", "tonal shifts",
                "emotional surprises", "mood changes", "unexpected feelings"
            ],
            
            # Intensity comfort
            "background_viewing": [
                "background", "easy watching", "casual viewing", "not demanding",
                "while doing other things", "casual", "light", "easy to follow"
            ],
            "full_attention": [
                "requires attention", "demanding", "complex", "needs focus",
                "pay attention", "concentrate", "full focus", "can't multitask"
            ],
            
            # Character relationship
            "aspirational": [
                "aspirational", "look up to", "inspiring characters",
                "want to be like", "admirable", "inspiring", "role model"
            ],
            "relatable": [
                "relatable", "like me", "familiar", "recognizable",
                "see myself", "similar to me", "understand them"
            ],
            "observational": [
                "watching", "observing", "anthropological", "documentary style",
                "study people", "watch from distance", "observer"
            ],
            "protective": [
                "protective", "care about", "worried for", "emotional investment",
                "want to help", "feel for them", "concerned about"
            ]
        }
        
        # Visual style patterns
        self.visual_patterns = {
            "naturalistic": [
                "realistic", "natural", "authentic", "real looking", "documentary style",
                "handheld", "natural lighting", "realistic look"
            ],
            "stylized": [
                "stylized", "artistic", "visual flair", "distinctive look",
                "unique visual style", "artistic direction", "visually striking"
            ],
            "minimal": [
                "minimal", "simple", "clean", "understated", "subtle",
                "not flashy", "simple production", "basic"
            ],
            "rich_production": [
                "high production", "expensive looking", "rich visuals", "elaborate",
                "high budget", "lavish", "beautiful production", "cinematic"
            ],
            "understated": [
                "understated", "subtle", "quiet", "restrained", "low key",
                "not over the top", "controlled"
            ],
            "theatrical": [
                "theatrical", "dramatic", "big", "over the top", "heightened",
                "dramatic style", "theatrical performance"
            ]
        }
        
        # Audio/podcast patterns
        self.audio_patterns = {
            "solo_expertise": [
                "solo host", "one person", "expert", "authority", "single voice",
                "solo show", "individual host", "one expert"
            ],
            "conversational_duos": [
                "two hosts", "conversation", "duo", "back and forth",
                "chat between two", "conversational", "dialogue"
            ],
            "panel_discussions": [
                "panel", "multiple people", "group discussion", "round table",
                "several hosts", "group conversation"
            ],
            "structured_lessons": [
                "educational", "lessons", "structured", "teaching", "learning",
                "instructional", "step by step", "educational format"
            ],
            "meandering_conversations": [
                "meandering", "casual chat", "wandering conversation", "free flowing",
                "stream of consciousness", "goes wherever", "natural conversation"
            ],
            "interview_format": [
                "interview", "guest", "Q&A", "asking questions", "interviewing",
                "guest format", "question and answer"
            ]
        }
        
        # Anti-pattern detection
        self.anti_pattern_indicators = {
            "forced_laugh_tracks": [
                "laugh track", "canned laughter", "fake laughs", "forced humor"
            ],
            "excessive_violence": [
                "too violent", "graphic", "brutal", "excessive violence", "too much violence"
            ],
            "slow_pacing": [
                "too slow", "boring", "drags", "nothing happens", "slow pace"
            ],
            "cringe_humor": [
                "cringe", "cringey", "awkward humor", "uncomfortable comedy"
            ],
            "melodrama": [
                "melodramatic", "over dramatic", "too dramatic", "soap opera"
            ],
            "traditional_sitcom_format": [
                "sitcom", "traditional comedy", "typical sitcom", "standard sitcom format"
            ]
        }
    
    def _initialize_content_database(self):
        """Initialize comprehensive content database with quality indicators"""
        
        self.enhanced_content_db = {
            "shrinking": {
                "title": "Shrinking",
                "platform": "Apple TV+",
                "year": "2023",
                "content_type": "tv_show",
                "quality_indicators": ["creator_driven", "film_director_involvement"],
                "source_validation": ["critic_acclaim", "industry_recognition", "audience_praise"],
                "craft_elements": ["authentic_workplace_dynamics", "therapy_setting_authenticity", "character_development"],
                "narrative_dna": {
                    "story_structure": ["character_driven", "episodic"],
                    "conflict_style": ["internal_growth", "interpersonal"],
                    "pacing_preferences": ["deliberate_builds"]
                },
                "emotional_texture": {
                    "primary_mood": ["cozy_comfort", "intellectual_stimulation"],
                    "character_relationship": ["relatable", "protective"],
                    "emotional_journey": ["gradual_build"]
                },
                "visual_style": {
                    "performance_energy": ["naturalistic"],
                    "technical_craft": ["story_focused"],
                    "visual_preferences": ["naturalistic"]
                },
                "why_template": "Workplace therapy practice with authentic relationship dynamics, character development through daily interactions rather than episode plots",
                "what_to_expect": "Jason Segel as therapist breaking conventional boundaries, similar warmth to The Office but in dramatic format with genuine stakes",
                "perfect_for": "When you want Office-style character moments with more emotional depth",
                "avoid_if": "You're looking for pure comedy without heavier themes"
            },
            
            "atlanta": {
                "title": "Atlanta",
                "platform": "FX/Hulu",
                "year": "2016",
                "content_type": "tv_show",
                "quality_indicators": ["creator_driven", "auteur_vision"],
                "source_validation": ["emmy_winner", "critic_acclaim", "cultural_impact"],
                "craft_elements": ["authentic_cultural_representation", "surreal_realism", "observational_comedy"],
                "narrative_dna": {
                    "story_structure": ["character_driven", "episodic"],
                    "conflict_style": ["interpersonal", "external_obstacles"],
                    "pacing_preferences": ["deliberate_builds"]
                },
                "emotional_texture": {
                    "primary_mood": ["intellectual_stimulation"],
                    "character_relationship": ["observational", "relatable"],
                    "intensity_comfort": ["full_attention"]
                },
                "visual_style": {
                    "performance_energy": ["naturalistic"],
                    "visual_preferences": ["naturalistic", "stylized"],
                    "technical_craft": ["cinematography_conscious"]
                },
                "why_template": "Authentic slice-of-life following aspiring rapper and cousin, dry observational humor without traditional comedy structure",
                "what_to_expect": "Surreal moments mixed with realistic character interactions, unpredictable episode formats",
                "perfect_for": "Viewers who appreciate subtle humor and authentic character moments",
                "avoid_if": "You prefer structured plots and clear episode objectives"
            },
            
            "reservation_dogs": {
                "title": "Reservation Dogs",
                "platform": "FX/Hulu",
                "year": "2021",
                "content_type": "tv_show",
                "quality_indicators": ["authentic_representation", "creator_driven"],
                "source_validation": ["critic_acclaim", "cultural_significance", "peabody_award"],
                "craft_elements": ["indigenous_authenticity", "coming_of_age", "community_focus"],
                "narrative_dna": {
                    "story_structure": ["character_driven", "episodic"],
                    "conflict_style": ["internal_growth", "interpersonal"],
                    "pacing_preferences": ["deliberate_builds"]
                },
                "emotional_texture": {
                    "primary_mood": ["cozy_comfort"],
                    "character_relationship": ["protective", "relatable"],
                    "emotional_journey": ["gradual_build"]
                },
                "visual_style": {
                    "performance_energy": ["naturalistic"],
                    "visual_preferences": ["naturalistic"],
                    "technical_craft": ["story_focused"]
                },
                "why_template": "Indigenous teens in rural Oklahoma, authentic community dynamics with heart and humor",
                "what_to_expect": "Coming-of-age story with cultural authenticity and gentle humor about friendship",
                "perfect_for": "Those seeking authentic character relationships and cultural representation",
                "avoid_if": "You need fast-paced plots or urban settings"
            },
            
            "severance": {
                "title": "Severance",
                "platform": "Apple TV+",
                "year": "2022",
                "content_type": "tv_show",
                "quality_indicators": ["creator_driven", "high_concept"],
                "source_validation": ["critic_acclaim", "award_nominations", "audience_praise"],
                "craft_elements": ["psychological_thriller", "workplace_satire", "production_design"],
                "narrative_dna": {
                    "story_structure": ["serialized", "plot_driven"],
                    "conflict_style": ["internal_growth", "external_obstacles"],
                    "pacing_preferences": ["deliberate_builds"],
                    "resolution_patterns": ["ongoing_mysteries"]
                },
                "emotional_texture": {
                    "primary_mood": ["intellectual_stimulation"],
                    "intensity_comfort": ["full_attention"],
                    "emotional_journey": ["gradual_build"]
                },
                "visual_style": {
                    "visual_preferences": ["stylized", "rich_production"],
                    "technical_craft": ["cinematography_conscious"],
                    "performance_energy": ["understated"]
                },
                "why_template": "Workplace psychological thriller with authentic office dynamics in surreal setting",
                "what_to_expect": "Mind-bending premise with realistic character interactions and workplace politics",
                "perfect_for": "Fans of workplace dynamics with sci-fi psychological elements",
                "avoid_if": "You prefer light, easy viewing or dislike workplace settings"
            },
            
            "the_bear": {
                "title": "The Bear",
                "platform": "FX/Hulu",
                "year": "2022",
                "content_type": "tv_show",
                "quality_indicators": ["authentic_workplace", "creator_driven"],
                "source_validation": ["emmy_winner", "critic_acclaim", "industry_praise"],
                "craft_elements": ["kitchen_authenticity", "working_class_representation", "stress_dynamics"],
                "narrative_dna": {
                    "story_structure": ["character_driven", "episodic"],
                    "conflict_style": ["interpersonal", "internal_growth"],
                    "pacing_preferences": ["quick_cuts"]
                },
                "emotional_texture": {
                    "primary_mood": ["cathartic_release"],
                    "intensity_comfort": ["full_attention"],
                    "character_relationship": ["protective", "relatable"],
                    "emotional_journey": ["emotional_rollercoaster"]
                },
                "visual_style": {
                    "performance_energy": ["naturalistic"],
                    "visual_preferences": ["naturalistic"],
                    "technical_craft": ["story_focused"]
                },
                "why_template": "Authentic kitchen culture with intense workplace dynamics and character growth through stress",
                "what_to_expect": "High-stress restaurant environment with realistic working-class characters and emotional depth",
                "perfect_for": "Those who appreciate authentic workplace stress and character development",
                "avoid_if": "You're stressed and need comfort viewing"
            },
            
            "ted_lasso": {
                "title": "Ted Lasso",
                "platform": "Apple TV+",
                "year": "2020",
                "content_type": "tv_show",
                "quality_indicators": ["character_driven", "feel_good"],
                "source_validation": ["emmy_winner", "audience_favorite", "cultural_phenomenon"],
                "craft_elements": ["optimism", "emotional_intelligence", "sports_backdrop"],
                "narrative_dna": {
                    "story_structure": ["character_driven", "episodic"],
                    "conflict_style": ["internal_growth", "interpersonal"],
                    "pacing_preferences": ["deliberate_builds"]
                },
                "emotional_texture": {
                    "primary_mood": ["cozy_comfort"],
                    "character_relationship": ["aspirational", "protective"],
                    "emotional_journey": ["gradual_build"]
                },
                "visual_style": {
                    "performance_energy": ["naturalistic"],
                    "visual_preferences": ["rich_production"],
                    "technical_craft": ["story_focused"]
                },
                "why_template": "Optimistic coach bringing emotional intelligence to cynical environment, character growth through kindness",
                "what_to_expect": "Feel-good sports backdrop with focus on personal relationships and emotional healing",
                "perfect_for": "When you need hope and want to believe in people's potential for growth",
                "avoid_if": "You find excessive optimism unrealistic or annoying"
            },
            
            # Podcast examples
            "radiolab": {
                "title": "Radiolab",
                "platform": "WNYC/NPR",
                "year": "2002",
                "content_type": "podcast",
                "quality_indicators": ["innovative_format", "sound_design"],
                "source_validation": ["peabody_award", "podcast_pioneer", "critical_acclaim"],
                "craft_elements": ["scientific_storytelling", "sound_design", "philosophical_questions"],
                "narrative_dna": {
                    "story_structure": ["episodic"],
                    "pacing_preferences": ["deliberate_builds"]
                },
                "emotional_texture": {
                    "primary_mood": ["intellectual_stimulation"],
                    "intensity_comfort": ["full_attention"]
                },
                "audio_style": {
                    "host_dynamics": ["conversational_duos"],
                    "delivery_style": ["structured_lessons"],
                    "production_values": ["highly_produced"]
                },
                "why_template": "Science and philosophy exploration with innovative sound design and deep curiosity",
                "what_to_expect": "Complex topics made accessible through storytelling and immersive audio experience",
                "perfect_for": "Curious minds who enjoy scientific thinking and audio craftsmanship",
                "avoid_if": "You prefer simple, straightforward information delivery"
            },
            
            "conan_obrien_needs_a_friend": {
                "title": "Conan O'Brien Needs a Friend",
                "platform": "Team Coco",
                "year": "2018",
                "content_type": "podcast",
                "quality_indicators": ["celebrity_host", "consistent_quality"],
                "source_validation": ["audience_favorite", "comedy_legend"],
                "craft_elements": ["improvisational_comedy", "genuine_conversation", "self_deprecating"],
                "narrative_dna": {
                    "story_structure": ["episodic"],
                    "conflict_style": ["interpersonal"]
                },
                "emotional_texture": {
                    "primary_mood": ["cozy_comfort"],
                    "character_relationship": ["observational"],
                    "intensity_comfort": ["background_viewing"]
                },
                "audio_style": {
                    "host_dynamics": ["conversational_duos"],
                    "delivery_style": ["meandering_conversations"],
                    "intimacy_level": ["friend_like_chat"],
                    "production_values": ["raw_conversation"]
                },
                "why_template": "Established comedian having genuine conversations with guests, improvisational humor emerging naturally",
                "what_to_expect": "Unscripted comedy through real relationship building and spontaneous interactions",
                "perfect_for": "Background listening when you want gentle humor and authentic conversation",
                "avoid_if": "You prefer structured interviews or dislike rambling conversations"
            }
        }
    
    def extract_taste_profile(self, user_input: str, content_type: str = "mixed", context: Dict[str, str] = None) -> EnhancedTasteProfile:
        """
        Extract comprehensive taste profile using the advanced framework.
        
        Acts as master taste interpreter, analyzing WHY users like content,
        not just WHAT they like.
        """
        profile = EnhancedTasteProfile(content_type=content_type)
        if context:
            profile.context.update(context)
        
        user_lower = user_input.lower()
        
        # Extract Narrative DNA
        self._extract_narrative_dna(user_input, profile)
        
        # Extract Emotional Texture
        self._extract_emotional_texture(user_input, profile)
        
        # Medium-specific style extraction
        if content_type in ["tv", "movie", "mixed"]:
            profile.visual_style = VisualStylePreferences()
            self._extract_visual_style(user_input, profile.visual_style)
            
        if content_type in ["podcast", "mixed"]:
            profile.audio_style = AudioStylePreferences()
            self._extract_audio_style(user_input, profile.audio_style)
        
        # Extract anti-patterns with sophisticated negation detection
        self._extract_anti_patterns(user_input, profile)
        
        # Context extraction
        self._extract_context_clues(user_input, profile)
        
        return profile
    
    def _extract_narrative_dna(self, user_input: str, profile: EnhancedTasteProfile):
        """Extract narrative structure preferences"""
        user_lower = user_input.lower()
        
        for element, patterns in self.narrative_patterns.items():
            if any(pattern in user_lower for pattern in patterns):
                if element in ["episodic", "serialized", "character_driven", "plot_driven"]:
                    profile.narrative_dna.story_structure.append(element)
                elif element in ["slow_burn", "quick_cuts", "deliberate_builds"]:
                    profile.narrative_dna.pacing_preferences.append(element)
                elif element in ["internal_growth", "external_obstacles", "interpersonal"]:
                    profile.narrative_dna.conflict_style.append(element)
                elif element in ["ambiguous", "clear_closure", "ongoing_mysteries"]:
                    profile.narrative_dna.resolution_patterns.append(element)
    
    def _extract_emotional_texture(self, user_input: str, profile: EnhancedTasteProfile):
        """Extract emotional experience preferences"""
        user_lower = user_input.lower()
        
        for emotion, patterns in self.emotional_patterns.items():
            if any(pattern in user_lower for pattern in patterns):
                if emotion in ["cozy_comfort", "intellectual_stimulation", "cathartic_release", "escapist_fantasy"]:
                    profile.emotional_texture.primary_mood.append(emotion)
                elif emotion in ["steady_state", "emotional_rollercoaster", "gradual_build", "surprising_shifts"]:
                    profile.emotional_texture.emotional_journey.append(emotion)
                elif emotion in ["background_viewing", "full_attention"]:
                    profile.emotional_texture.intensity_comfort.append(emotion)
                elif emotion in ["aspirational", "relatable", "observational", "protective"]:
                    profile.emotional_texture.character_relationship.append(emotion)
    
    def _extract_visual_style(self, user_input: str, visual_style: VisualStylePreferences):
        """Extract visual content style preferences"""
        user_lower = user_input.lower()
        
        for style, patterns in self.visual_patterns.items():
            if any(pattern in user_lower for pattern in patterns):
                if style in ["naturalistic", "stylized", "minimal", "rich_production"]:
                    visual_style.visual_preferences.append(style)
                elif style in ["understated", "theatrical"]:
                    visual_style.performance_energy.append(style)
    
    def _extract_audio_style(self, user_input: str, audio_style: AudioStylePreferences):
        """Extract podcast/audio style preferences"""
        user_lower = user_input.lower()
        
        for style, patterns in self.audio_patterns.items():
            if any(pattern in user_lower for pattern in patterns):
                if style in ["solo_expertise", "conversational_duos", "panel_discussions"]:
                    audio_style.host_dynamics.append(style)
                elif style in ["structured_lessons", "meandering_conversations", "interview_format"]:
                    audio_style.delivery_style.append(style)
    
    def _extract_anti_patterns(self, user_input: str, profile: EnhancedTasteProfile):
        """Extract what to avoid using sophisticated negation detection"""
        negation_words = ["not", "avoid", "hate", "dislike", "without", "no", "don't want", "can't stand", "never"]
        user_lower = user_input.lower()
        
        for negation in negation_words:
            if negation in user_lower:
                # Find context after negation word
                parts = user_lower.split(negation)
                if len(parts) > 1:
                    negative_context = parts[1][:150]  # Next 150 chars
                    
                    # Pattern matching for anti-patterns
                    for anti_pattern, patterns in self.anti_pattern_indicators.items():
                        if any(pattern in negative_context for pattern in patterns):
                            if anti_pattern not in profile.anti_patterns.deal_breakers:
                                profile.anti_patterns.deal_breakers.append(anti_pattern)
    
    def _extract_context_clues(self, user_input: str, profile: EnhancedTasteProfile):
        """Extract contextual information"""
        user_lower = user_input.lower()
        
        # Time context
        time_patterns = {
            "morning": ["morning", "wake up", "breakfast"],
            "evening": ["evening", "night", "before bed", "end of day"],
            "weekend": ["weekend", "saturday", "sunday", "free time"]
        }
        
        # Mood context
        mood_patterns = {
            "stressed": ["stressed", "overwhelmed", "busy", "tired"],
            "energetic": ["energetic", "pumped", "ready", "motivated"],
            "relaxed": ["relaxed", "chill", "calm", "peaceful"]
        }
        
        # Social context
        social_patterns = {
            "alone": ["alone", "by myself", "solo viewing"],
            "with_friends": ["with friends", "group", "together"],
            "family": ["family", "kids", "parents", "family friendly"]
        }
        
        for context_type, patterns_dict in [("time", time_patterns), ("mood", mood_patterns), ("social", social_patterns)]:
            for context_value, patterns in patterns_dict.items():
                if any(pattern in user_lower for pattern in patterns):
                    profile.context[context_type] = context_value
    
    def evaluate_content(self, content: Dict[str, Any], profile: EnhancedTasteProfile, context: Dict[str, str] = None) -> EvaluationScore:
        """
        Evaluate content using 6-factor matrix from the framework
        """
        # Initialize scores
        scores = EvaluationScore(
            taste_match_strength=1.0,
            anti_pattern_avoidance=10.0,  # Start high, deduct for violations
            context_fit=5.0,  # Neutral start
            discovery_value=5.0,  # Neutral start
            source_validation=1.0,
            craft_quality=1.0,
            total_score=23.0
        )
        
        # 1. Taste Match Strength (1-10)
        narrative_score = self._calculate_narrative_match(content, profile)
        emotional_score = self._calculate_emotional_match(content, profile)
        style_score = self._calculate_style_match(content, profile)
        
        # Weight the scores: narrative (40%), emotional (40%), style (20%)
        scores.taste_match_strength = min(10.0, max(1.0, 
            (narrative_score * 0.4 + emotional_score * 0.4 + style_score * 0.2) * 10
        ))
        
        # 2. Anti-Pattern Avoidance (1-10)
        scores.anti_pattern_avoidance = self._calculate_anti_pattern_avoidance(content, profile)
        
        # 3. Context Fit (1-10)
        scores.context_fit = self._calculate_context_fit(content, profile, context or {})
        
        # 4. Discovery Value (1-10)
        scores.discovery_value = self._calculate_discovery_value(content, profile)
        
        # 5. Source Validation (1-10)
        scores.source_validation = self._calculate_source_validation(content)
        
        # 6. Craft Quality (1-10)
        scores.craft_quality = self._calculate_craft_quality(content)
        
        # Calculate total
        scores.total_score = (
            scores.taste_match_strength + scores.anti_pattern_avoidance + 
            scores.context_fit + scores.discovery_value + 
            scores.source_validation + scores.craft_quality
        )
        
        return scores
    
    def _calculate_narrative_match(self, content: Dict[str, Any], profile: EnhancedTasteProfile) -> float:
        """Calculate narrative DNA match score (0.0-1.0)"""
        content_narrative = content.get("narrative_dna", {})
        profile_narrative = profile.narrative_dna
        
        total_matches = 0
        total_elements = 0
        
        # Story structure matches
        if profile_narrative.story_structure:
            content_structure = content_narrative.get("story_structure", [])
            matches = len(set(profile_narrative.story_structure) & set(content_structure))
            total_matches += matches
            total_elements += len(profile_narrative.story_structure)
        
        # Pacing matches
        if profile_narrative.pacing_preferences:
            content_pacing = content_narrative.get("pacing_preferences", [])
            matches = len(set(profile_narrative.pacing_preferences) & set(content_pacing))
            total_matches += matches
            total_elements += len(profile_narrative.pacing_preferences)
        
        # Conflict style matches
        if profile_narrative.conflict_style:
            content_conflict = content_narrative.get("conflict_style", [])
            matches = len(set(profile_narrative.conflict_style) & set(content_conflict))
            total_matches += matches
            total_elements += len(profile_narrative.conflict_style)
        
        return total_matches / max(total_elements, 1)
    
    def _calculate_emotional_match(self, content: Dict[str, Any], profile: EnhancedTasteProfile) -> float:
        """Calculate emotional texture match score (0.0-1.0)"""
        content_emotional = content.get("emotional_texture", {})
        profile_emotional = profile.emotional_texture
        
        total_matches = 0
        total_elements = 0
        
        # Primary mood matches
        if profile_emotional.primary_mood:
            content_mood = content_emotional.get("primary_mood", [])
            matches = len(set(profile_emotional.primary_mood) & set(content_mood))
            total_matches += matches * 2  # Weight mood highly
            total_elements += len(profile_emotional.primary_mood) * 2
        
        # Character relationship matches
        if profile_emotional.character_relationship:
            content_relationship = content_emotional.get("character_relationship", [])
            matches = len(set(profile_emotional.character_relationship) & set(content_relationship))
            total_matches += matches
            total_elements += len(profile_emotional.character_relationship)
        
        return total_matches / max(total_elements, 1)
    
    def _calculate_style_match(self, content: Dict[str, Any], profile: EnhancedTasteProfile) -> float:
        """Calculate style match score (0.0-1.0)"""
        total_matches = 0
        total_elements = 0
        
        # Visual style matching
        if profile.visual_style and content.get("visual_style"):
            content_visual = content["visual_style"]
            
            if profile.visual_style.visual_preferences:
                content_prefs = content_visual.get("visual_preferences", [])
                matches = len(set(profile.visual_style.visual_preferences) & set(content_prefs))
                total_matches += matches
                total_elements += len(profile.visual_style.visual_preferences)
        
        # Audio style matching
        if profile.audio_style and content.get("audio_style"):
            content_audio = content["audio_style"]
            
            if profile.audio_style.host_dynamics:
                content_dynamics = content_audio.get("host_dynamics", [])
                matches = len(set(profile.audio_style.host_dynamics) & set(content_dynamics))
                total_matches += matches
                total_elements += len(profile.audio_style.host_dynamics)
        
        return total_matches / max(total_elements, 1) if total_elements > 0 else 0.5
    
    def _calculate_anti_pattern_avoidance(self, content: Dict[str, Any], profile: EnhancedTasteProfile) -> float:
        """Calculate anti-pattern avoidance score (1-10)"""
        score = 10.0  # Start with perfect score
        
        # Check if content has any elements user wants to avoid
        content_elements = []
        
        # Collect all content characteristics
        if "visual_style" in content:
            content_elements.extend(content["visual_style"].get("performance_energy", []))
        
        # Deduct points for each anti-pattern violation
        for deal_breaker in profile.anti_patterns.deal_breakers:
            if deal_breaker == "traditional_sitcom_format":
                # Check if content avoids sitcom format
                if "sitcom" in content.get("craft_elements", []):
                    score -= 3.0
                elif "no_laugh_track" in content_elements:
                    score += 1.0  # Bonus for explicitly avoiding
            
            elif deal_breaker == "excessive_violence":
                if "violence" in content.get("craft_elements", []):
                    score -= 4.0
        
        return max(1.0, min(10.0, score))
    
    def _calculate_context_fit(self, content: Dict[str, Any], profile: EnhancedTasteProfile, context: Dict[str, str]) -> float:
        """Calculate context fit score (1-10)"""
        score = 5.0  # Neutral start
        
        # Time context
        if "time" in profile.context or "time" in context:
            time_context = profile.context.get("time", context.get("time"))
            if time_context == "morning" and "cozy_comfort" in content.get("emotional_texture", {}).get("primary_mood", []):
                score += 2.0
            elif time_context == "evening" and "cathartic_release" in content.get("emotional_texture", {}).get("primary_mood", []):
                score += 1.5
        
        # Mood context
        if "mood" in profile.context or "mood" in context:
            mood_context = profile.context.get("mood", context.get("mood"))
            if mood_context == "stressed" and "cozy_comfort" in content.get("emotional_texture", {}).get("primary_mood", []):
                score += 2.0
            elif mood_context == "energetic" and "full_attention" in content.get("emotional_texture", {}).get("intensity_comfort", []):
                score += 1.5
        
        # Attention level
        if "background_viewing" in profile.emotional_texture.intensity_comfort:
            if content.get("emotional_texture", {}).get("intensity_comfort") == ["background_viewing"]:
                score += 2.0
            elif "full_attention" in content.get("emotional_texture", {}).get("intensity_comfort", []):
                score -= 2.0
        
        return max(1.0, min(10.0, score))
    
    def _calculate_discovery_value(self, content: Dict[str, Any], profile: EnhancedTasteProfile) -> float:
        """Calculate discovery value score (1-10)"""
        score = 5.0  # Neutral start
        
        # Award points for introducing adjacent taste territories
        content_elements = set()
        if "narrative_dna" in content:
            for key, values in content["narrative_dna"].items():
                content_elements.update(values)
        
        profile_elements = set()
        for attr in ["story_structure", "pacing_preferences", "conflict_style"]:
            profile_elements.update(getattr(profile.narrative_dna, attr, []))
        
        # Calculate overlap and adjacent elements
        overlap = len(content_elements & profile_elements)
        total_content = len(content_elements)
        
        if total_content > 0:
            overlap_ratio = overlap / total_content
            # Sweet spot: some overlap but introduces new elements
            if 0.3 <= overlap_ratio <= 0.7:
                score += 3.0
            elif overlap_ratio < 0.3:
                score += 1.0  # Might be too different
            else:
                score -= 1.0  # Too similar, low discovery value
        
        # Bonus for quality indicators
        if "innovative_format" in content.get("quality_indicators", []):
            score += 1.0
        
        return max(1.0, min(10.0, score))
    
    def _calculate_source_validation(self, content: Dict[str, Any]) -> float:
        """Calculate source validation score (1-10)"""
        score = 1.0
        source_validation = content.get("source_validation", [])
        
        # Award points based on validation sources
        validation_scores = {
            "critic_acclaim": 2.0,
            "industry_recognition": 2.0,
            "emmy_winner": 3.0,
            "peabody_award": 3.0,
            "audience_favorite": 1.5,
            "cultural_phenomenon": 2.0,
            "award_nominations": 1.5
        }
        
        for validation in source_validation:
            score += validation_scores.get(validation, 0.5)
        
        return min(10.0, score)
    
    def _calculate_craft_quality(self, content: Dict[str, Any]) -> float:
        """Calculate craft quality score (1-10) with specific quality indicators"""
        score = 1.0
        quality_indicators = content.get("quality_indicators", [])
        
        # Quality indicator points (from framework)
        quality_scores = {
            "film_director_involvement": 2.0,
            "book_adaptation": 2.0,
            "creator_driven": 1.0,
            "limited_series": 1.0,
            "authentic_representation": 1.5,
            "innovative_format": 1.5,
            "high_concept": 1.0
        }
        
        for indicator in quality_indicators:
            score += quality_scores.get(indicator, 0.5)
        
        # Bonus for craft elements
        craft_elements = content.get("craft_elements", [])
        score += len(craft_elements) * 0.3  # Small bonus for each craft element
        
        return min(10.0, score)
    
    def generate_recommendations(self, profile: EnhancedTasteProfile, context: Dict[str, str] = None, max_recommendations: int = 3) -> List[EnhancedRecommendation]:
        """
        Generate curated recommendations using the evaluation framework.
        Implements the 'Speed Over Perfection' principle: 2-3 options quickly.
        """
        recommendations = []
        
        # Filter content by type if specified
        relevant_content = {}
        for content_id, content in self.enhanced_content_db.items():
            if profile.content_type == "mixed":
                relevant_content[content_id] = content
            elif profile.content_type == "tv" and content["content_type"] == "tv_show":
                relevant_content[content_id] = content
            elif profile.content_type == content["content_type"]:
                relevant_content[content_id] = content
            elif profile.content_type == "podcast" and content["content_type"] == "podcast":
                relevant_content[content_id] = content
        
        if not relevant_content:
            # Fallback to mixed content if no specific matches
            relevant_content = self.enhanced_content_db
        
        # Evaluate all relevant content
        scored_content = []
        for content_id, content in relevant_content.items():
            evaluation = self.evaluate_content(content, profile, context)
            
            # Only include content with decent scores (threshold: 30/60)
            if evaluation.total_score >= 30.0:
                scored_content.append((content_id, content, evaluation))
        
        # Sort by total score and take top recommendations
        scored_content.sort(key=lambda x: x[2].total_score, reverse=True)
        top_content = scored_content[:max_recommendations]
        
        # Generate enhanced recommendations
        for content_id, content, evaluation in top_content:
            recommendation = self._create_recommendation(content, evaluation, profile, context)
            recommendations.append(recommendation)
        
        return recommendations
    
    def _create_recommendation(self, content: Dict[str, Any], evaluation: EvaluationScore, 
                             profile: EnhancedTasteProfile, context: Dict[str, str] = None) -> EnhancedRecommendation:
        """Create enhanced recommendation with full framework compliance"""
        
        # Calculate confidence percentage
        confidence_percentage = (evaluation.total_score / 60.0) * 100
        
        # Determine match strength based on framework thresholds
        if confidence_percentage >= 90:
            match_strength = "🔥"  # Perfect match
        elif confidence_percentage >= 75:
            match_strength = "✨"  # Strong match
        else:
            match_strength = "🎲"  # Interesting gamble
        
        # Generate recommendation text using content templates
        why_matches = self._generate_why_matches(content, profile)
        what_to_expect = content.get("what_to_expect", "Engaging content that matches your taste profile")
        perfect_for = self._generate_perfect_for(content, profile, context)
        avoid_if = content.get("avoid_if", "You're looking for something completely different")
        
        return EnhancedRecommendation(
            title=content["title"],
            platform=content["platform"],
            year=content.get("year"),
            content_type=content["content_type"],
            match_strength=match_strength,
            why_matches=why_matches,
            what_to_expect=what_to_expect,
            perfect_for=perfect_for,
            avoid_if=avoid_if,
            quality_indicators=content.get("quality_indicators", []),
            source_validation=content.get("source_validation", []),
            craft_elements=content.get("craft_elements", []),
            evaluation=evaluation,
            confidence_percentage=confidence_percentage
        )
    
    def _generate_why_matches(self, content: Dict[str, Any], profile: EnhancedTasteProfile) -> str:
        """Generate personalized explanation of why content matches user's taste"""
        matches = []
        
        # Check narrative matches
        content_narrative = content.get("narrative_dna", {})
        if profile.narrative_dna.story_structure:
            content_structure = content_narrative.get("story_structure", [])
            common_structure = set(profile.narrative_dna.story_structure) & set(content_structure)
            if common_structure:
                structure_text = ", ".join(common_structure).replace("_", " ")
                matches.append(f"{structure_text} storytelling")
        
        # Check emotional matches
        content_emotional = content.get("emotional_texture", {})
        if profile.emotional_texture.primary_mood:
            content_mood = content_emotional.get("primary_mood", [])
            common_mood = set(profile.emotional_texture.primary_mood) & set(content_mood)
            if common_mood:
                mood_text = ", ".join(common_mood).replace("_", " ")
                matches.append(f"provides {mood_text}")
        
        # Use template if available, otherwise construct from matches
        if content.get("why_template"):
            return content["why_template"]
        elif matches:
            return f"Features {', '.join(matches[:2])}"  # Limit to 2-3 elements as per framework
        else:
            return "Aligns with your taste preferences"
    
    def _generate_perfect_for(self, content: Dict[str, Any], profile: EnhancedTasteProfile, context: Dict[str, str] = None) -> str:
        """Generate context-appropriate 'perfect for' statement"""
        if content.get("perfect_for"):
            return content["perfect_for"]
        
        context_perfect = []
        
        # Check mood context
        if profile.context.get("mood") == "stressed" and "cozy_comfort" in content.get("emotional_texture", {}).get("primary_mood", []):
            context_perfect.append("when you need comfort and stress relief")
        elif profile.context.get("mood") == "energetic" and "intellectual_stimulation" in content.get("emotional_texture", {}).get("primary_mood", []):
            context_perfect.append("when you want mental engagement")
        
        # Check attention level
        if "background_viewing" in profile.emotional_texture.intensity_comfort:
            context_perfect.append("casual viewing while multitasking")
        elif "full_attention" in profile.emotional_texture.intensity_comfort:
            context_perfect.append("focused viewing sessions")
        
        if context_perfect:
            return context_perfect[0].capitalize()
        else:
            return "Viewers who appreciate thoughtful content"
    
    def format_recommendations_for_whatsapp(self, recommendations: List[EnhancedRecommendation], profile: EnhancedTasteProfile = None) -> str:
        """
        Format recommendations using the exact output structure from framework.
        Implements anti-browsing principle: eliminate decision paralysis.
        """
        if not recommendations:
            return self._generate_no_recommendations_response(profile)
        
        response_text = "🎯 **Your Personalized Recommendations**\n\n"
        
        for i, rec in enumerate(recommendations, 1):
            # Title and platform
            response_text += f"{rec.match_strength} **{rec.title}** - {rec.platform}"
            if rec.year:
                response_text += f"/{rec.year}"
            response_text += "\n\n"
            
            # Framework-required sections
            response_text += f"**Why it matches your taste:** {rec.why_matches}\n\n"
            response_text += f"**What to expect:** {rec.what_to_expect}\n\n"
            response_text += f"**Perfect for:** {rec.perfect_for}\n\n"
            response_text += f"**Avoid if:** {rec.avoid_if}\n\n"
            
            # Quality indicators (if present)
            if rec.quality_indicators:
                indicators = ", ".join(rec.quality_indicators).replace("_", " ").title()
                response_text += f"*Quality indicators: {indicators}*\n\n"
            
            # Separator between recommendations
            if i < len(recommendations):
                response_text += "---\n\n"
        
        # Footer with confidence explanation
        response_text += "\n💡 *Confidence levels: 🔥 Perfect match (90%+), ✨ Strong match (75-89%), 🎲 Interesting gamble (60-74%)*\n\n"
        response_text += "*Want more recommendations? Tell me what you think of these or describe another show/movie you enjoyed!*"
        
        return response_text
    
    def _generate_no_recommendations_response(self, profile: EnhancedTasteProfile = None) -> str:
        """Generate helpful response when no recommendations found"""
        if profile and (profile.narrative_dna.story_structure or profile.emotional_texture.primary_mood):
            return ("🤔 I extracted some taste elements but couldn't find strong matches in my current database. "
                   "Could you tell me about a specific show, movie, or podcast you recently enjoyed and what you liked about it? "
                   "This will help me better understand your preferences.")
        else:
            return ("🤔 I need more information to understand your taste profile. "
                   "Could you describe something you recently watched or listened to that you really enjoyed? "
                   "What specifically did you like about it - the characters, the mood, the style?")
    
    def handle_contextual_requests(self, user_input: str, request_type: str, profile: EnhancedTasteProfile = None) -> str:
        """
        Handle different request types as specified in the framework:
        - "Something like [X] but not exactly"
        - "I don't know what I want"  
        - "Surprise me"
        """
        if request_type == "something_like_but_not":
            return self._handle_something_like_request(user_input, profile)
        elif request_type == "dont_know":
            return self._handle_dont_know_request(user_input, profile)
        elif request_type == "surprise_me":
            return self._handle_surprise_request(user_input, profile)
        else:
            return "I can help you find content recommendations. Could you tell me more about what you're looking for?"
    
    def _handle_something_like_request(self, user_input: str, profile: EnhancedTasteProfile = None) -> str:
        """Handle 'Something like [X] but not exactly' requests"""
        # Extract what made [X] special beyond surface genre
        # Find content that delivers those elements through different vehicles
        return "Let me analyze what made that content special and find something that captures those elements in a different way..."
    
    def _handle_dont_know_request(self, user_input: str, profile: EnhancedTasteProfile = None) -> str:
        """Handle 'I don't know what I want' requests with quick context assessment"""
        context_questions = [
            "What's your energy level right now? (drained/neutral/energized)",
            "How much attention can you give? (background/partial/full focus)",
            "What do you need emotionally? (comfort/stimulation/distraction/inspiration)",
            "How much time do you have and where are you watching?"
        ]
        
        return ("Let's figure this out together! " + 
                "Quick context check: " + context_questions[0] + 
                " This will help me suggest something perfect for your current state.")
    
    def _handle_surprise_request(self, user_input: str, profile: EnhancedTasteProfile = None) -> str:
        """Handle 'Surprise me' requests by analyzing taste patterns"""
        # Analyze past mentions for taste patterns they might not be aware of
        # Find adjacent areas they haven't explored
        # Suggest elevated versions of things they casually enjoyed
        return "Let me surprise you with something that matches taste patterns you might not even realize you have..."

# Factory function for easy import
def create_taste_interpreter() -> MasterTasteInterpreter:
    """Factory function to create a master taste interpreter instance"""
    return MasterTasteInterpreter()
