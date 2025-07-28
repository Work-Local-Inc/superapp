"""
FeedGenerator - Transform Wiki Content into Dashboard Cards
"""

from datetime import datetime
from typing import Dict, List, Optional
from .wiki_parser import WikiParser

class FeedGenerator:
    """
    🎨 The artist that creates beautiful dashboard cards from wiki content
    
    Monday Madness Level: CREATIVE GENIUS! 🎪
    """
    
    def __init__(self, wiki_parser: Optional[WikiParser] = None):
        self.parser = wiki_parser or WikiParser()
        self.feed_cache = {}
        
    def create_wiki_card(self, wiki_page: str) -> Dict:
        """
        🎯 Create a stunning dashboard card from a wiki page
        
        Args:
            wiki_page: Path to wiki markdown file
            
        Returns:
            Dict containing card HTML, metadata, and actions
        """
        # Parse the wiki page using our WikiParser
        card_data = self.parser.parse_markdown_to_card(wiki_page)
        
        if card_data["status"] != "success":
            return self._create_error_card(wiki_page, card_data.get("error", "Unknown error"))
        
        # Generate engagement score based on content metrics
        metrics = card_data["metadata"]["metrics"]
        engagement_score = self._calculate_engagement_score(metrics)
        
        # Determine card priority and styling
        priority = self._determine_card_priority(card_data["type"], engagement_score)
        
        # Generate contextual action buttons
        actions = self.generate_action_buttons(card_data["type"])
        
        # Create the final dashboard card
        dashboard_card = {
            "id": f"wiki_card_{card_data['id']}",
            "title": card_data["title"],
            "summary": card_data["summary"],
            "content": card_data["content"],
            "content_preview": self._create_content_preview(card_data["content"]),
            "timestamp": card_data["timestamp"],
            "author": self._extract_author_from_git(wiki_page),
            "type": card_data["type"],
            "expandable": True,
            "expanded": False,
            "actions": actions,
            "engagement_score": engagement_score,
            "priority": priority,
            "features": card_data["metadata"]["features"],
            "metrics": metrics,
            "style_class": self._get_card_style_class(card_data["type"], priority),
            "icon": self._get_card_icon(card_data["type"]),
            "monday_madness_level": metrics["engagement_potential"],
            "content_stats": {
                "read_time": f"{metrics['estimated_read_time']} min read",
                "complexity": metrics["complexity_score"],
                "feature_count": metrics["feature_count"],
                "word_count": metrics["word_count"]
            }
        }
        
        # Cache the card for performance
        self.feed_cache[wiki_page] = dashboard_card
        
        return dashboard_card
    
    def generate_activity_timeline(self) -> List[Dict]:
        """
        📅 Generate chronological activity timeline from all wiki content
        """
        timeline = []
        
        # Get all wiki files
        wiki_files = self.parser.get_all_wiki_files()
        
        for wiki_file in wiki_files:
            filename = wiki_file.name
            
            # Create card for each wiki file
            card = self.create_wiki_card(filename)
            
            if card.get("engagement_score", 0) > 0:  # Only include valid cards
                timeline.append(card)
        
        # Sort by priority and recency
        sorted_timeline = self.sort_by_priority_and_recency(timeline)
        
        return sorted_timeline
    
    def sort_by_priority_and_recency(self, cards: List[Dict]) -> List[Dict]:
        """
        🎯 Smart sorting: most important and recent content first
        """
        def sort_key(card):
            # Multi-factor sorting algorithm
            engagement = card.get("engagement_score", 0)
            priority_weight = {"high": 3, "medium": 2, "low": 1}.get(card.get("priority", "low"), 1)
            
            # Timestamp recency (more recent = higher score)
            timestamp = card.get("timestamp", datetime.now())
            hours_old = (datetime.now() - timestamp).total_seconds() / 3600
            recency_score = max(0, 100 - hours_old)  # Decay over time
            
            # Type importance weights
            type_weights = {
                "permissions_matrix": 10,  # Always important
                "account_management": 8,   # Core functionality
                "user_system": 6,         # User-facing features
                "api_documentation": 4,    # Technical docs
                "welcome": 2,             # Nice to have
                "general_documentation": 3 # Default
            }
            type_weight = type_weights.get(card.get("type", "general_documentation"), 3)
            
            # Final score calculation
            total_score = (engagement * 0.4) + (recency_score * 0.3) + (priority_weight * type_weight * 0.3)
            
            return total_score
        
        # Sort in descending order (highest score first)
        return sorted(cards, key=sort_key, reverse=True)
    
    def create_expandable_content(self, full_markdown: str) -> Dict:
        """
        📖 Create expandable content sections with rich formatting
        """
        return {
            "preview": "Click to expand...",
            "full_content": full_markdown,
            "estimated_read_time": "2 min",
            "complexity": "medium"
        }
    
    def generate_roadmap_cards(self) -> List[Dict]:
        """
        🗺️ Generate Coles Notes roadmap from wiki content
        """
        # Real SuperApp project roadmap from your actual development
        return [
            {
                "phase": "Foundation & Backend",
                "status": "in_progress",
                "progress": 75,
                "features": ["Laravel Backend", "Database Schema", "Account Management", "User System"]
            },
            {
                "phase": "Food Vertical",
                "status": "pending",
                "progress": 15,
                "features": ["Restaurant Management", "Menu System", "Order Processing", "Payment Integration"]
            },
            {
                "phase": "Multi-Vertical Platform",
                "status": "pending", 
                "progress": 5,
                "features": ["Spa Booking", "Gym Memberships", "Trade Services", "Unified Dashboard"]
            }
        ]
    
    def create_stats_summary(self) -> Dict:
        """
        📊 Create quick stats for dashboard header
        """
        wiki_files = self.parser.get_all_wiki_files()
        
        return {
            "total_pages": len(wiki_files),
            "total_features": 0,  # TODO: Count features
            "last_updated": datetime.now(),
            "status": "ALIVE AND GROWING! 🌱"
        }
    
    def generate_action_buttons(self, card_type: str) -> List[Dict]:
        """
        🔘 Generate contextual action buttons for cards
        """
        base_actions = [
            {"icon": "🔗", "label": "View in Wiki", "action": "view_wiki"},
            {"icon": "⭐", "label": "Feature", "action": "mark_feature"}
        ]
        
        if card_type == "permissions":
            base_actions.append({"icon": "👥", "label": "Assign Roles", "action": "assign_roles"})
        
        return base_actions
    
    # Helper methods for FeedGenerator
    
    def _create_error_card(self, wiki_page: str, error: str) -> Dict:
        """
        ❌ Create error card for failed parsing
        """
        return {
            "id": f"error_card_{wiki_page}",
            "title": f"Error: {wiki_page}",
            "summary": f"Could not parse wiki page: {error}",
            "content": "",
            "timestamp": datetime.now(),
            "author": "System",
            "type": "error",
            "expandable": False,
            "actions": [],
            "engagement_score": 0,
            "priority": "low",
            "monday_madness_level": "ERROR STATE! 🚨"
        }
    
    def _calculate_engagement_score(self, metrics: Dict) -> int:
        """
        📊 Calculate engagement score from content metrics
        """
        base_score = metrics.get("engagement_score", 0)
        
        # Bonus points for Monday Madness approval
        if metrics.get("monday_madness_approved", False):
            base_score += 25
            
        # Bonus for feature richness
        feature_count = metrics.get("feature_count", 0)
        base_score += min(feature_count * 5, 25)  # Max 25 bonus points
        
        # Bonus for good complexity
        complexity = metrics.get("complexity_score", 0)
        if 20 <= complexity <= 80:  # Sweet spot
            base_score += 15
        
        return min(base_score, 100)  # Cap at 100
    
    def _determine_card_priority(self, card_type: str, engagement_score: int) -> str:
        """
        🎯 Determine card priority for sorting and styling
        """
        if card_type in ["permissions_matrix", "account_management"]:
            return "high"
        elif engagement_score >= 75:
            return "high"
        elif engagement_score >= 50:
            return "medium"
        else:
            return "low"
    
    def _create_content_preview(self, content: str, max_lines: int = 3) -> str:
        """
        👀 Create preview snippet of content for collapsed view
        """
        lines = content.split('\n')
        preview_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):  # Skip headers
                preview_lines.append(line)
                if len(preview_lines) >= max_lines:
                    break
        
        preview = '\n'.join(preview_lines)
        if len(preview) > 200:
            preview = preview[:197] + "..."
            
        return preview
    
    def _extract_author_from_git(self, wiki_page: str) -> str:
        """
        👤 Extract author from git history (fallback to team member)
        """
        # For now, return team member based on content type
        # In real implementation, could use git log to get actual author
        return "SuperApp Team"
    
    def _get_card_style_class(self, card_type: str, priority: str) -> str:
        """
        🎨 Get CSS class for card styling
        """
        base_class = "wiki-card"
        
        type_class = {
            "permissions_matrix": "permissions-card",
            "account_management": "management-card", 
            "user_system": "user-card",
            "welcome": "welcome-card",
            "api_documentation": "api-card",
            "general_documentation": "docs-card"
        }.get(card_type, "docs-card")
        
        priority_class = f"priority-{priority}"
        
        return f"{base_class} {type_class} {priority_class}"
    
    def _get_card_icon(self, card_type: str) -> str:
        """
        🎯 Get emoji icon for card type
        """
        icons = {
            "permissions_matrix": "🔐",
            "account_management": "👥", 
            "user_system": "👤",
            "welcome": "🏠",
            "api_documentation": "⚙️",
            "general_documentation": "📖"
        }
        
        return icons.get(card_type, "📄") 