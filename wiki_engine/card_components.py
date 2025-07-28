"""
Card Components - Beautiful UI Elements for Our Social Feed
"""

from typing import Dict, List, Optional

# Optional Streamlit import for testing
try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False
    # Mock streamlit for testing
    class MockStreamlit:
        def container(self): return self
        def markdown(self, text, **kwargs): pass
        def info(self, text): pass
        def json(self, data): pass
        def columns(self, cols): return [self] * (cols if isinstance(cols, int) else len(cols))
        def button(self, label, **kwargs): return False
        def progress(self, value): pass
        def metric(self, label, value): pass
        def __enter__(self): return self
        def __exit__(self, *args): pass
    
    st = MockStreamlit()

class WikiCard:
    """
    🎴 Base wiki card component for social feed display
    
    Monday Madness Level: STYLISH! ✨
    """
    
    def __init__(self, card_data: Dict):
        self.data = card_data
        self.expanded = False
        
    def render(self) -> None:
        """
        🎨 Render the card in Streamlit
        """
        # TODO: Implementation coming in Task 6!
        with st.container():
            st.markdown("### 🎴 Wiki Card Coming Soon!")
            st.info("Monday Madness implementation in progress...")
            st.json(self.data)

class ExpandableCard(WikiCard):
    """
    📖 Expandable card with smooth animations and rich content
    
    Monday Madness Level: INTERACTIVE! 🎪
    """
    
    def __init__(self, card_data: Dict, default_expanded: bool = False):
        super().__init__(card_data)
        self.expanded = default_expanded
        
    def render_collapsed(self) -> None:
        """
        📋 Render collapsed state with summary
        """
        # TODO: Beautiful collapsed view
        pass
        
    def render_expanded(self) -> None:
        """
        📖 Render full expanded content
        """
        # TODO: Rich expanded content
        pass
        
    def toggle_expansion(self) -> None:
        """
        🔄 Toggle between collapsed and expanded states
        """
        self.expanded = not self.expanded

class ActionButton:
    """
    🔘 Interactive action buttons for wiki cards
    
    Monday Madness Level: FUNCTIONAL! ⚡
    """
    
    def __init__(self, icon: str, label: str, action: str, style: str = "primary"):
        self.icon = icon
        self.label = label
        self.action = action
        self.style = style
        
    def render(self, key: str = None) -> bool:
        """
        🔘 Render button and return True if clicked
        """
        # TODO: Beautiful button implementation
        return st.button(f"{self.icon} {self.label}", key=key)
        
    def render_icon_only(self, key: str = None) -> bool:
        """
        🎯 Render icon-only version for compact display
        """
        return st.button(self.icon, key=key, help=self.label)

class RoadmapCard:
    """
    🗺️ Special card for roadmap display in header
    
    Monday Madness Level: STRATEGIC! 🎯
    """
    
    def __init__(self, phase_data: Dict):
        self.phase = phase_data["phase"]
        self.status = phase_data["status"]
        self.progress = phase_data["progress"]
        self.features = phase_data.get("features", [])
        
    def render(self) -> None:
        """
        🗺️ Render roadmap phase card
        """
        # TODO: Beautiful roadmap visualization
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{self.phase}**")
            st.progress(self.progress / 100)
            
        with col2:
            status_emoji = "✅" if self.status == "complete" else "🔄" if self.status == "in_progress" else "📅"
            st.markdown(f"{status_emoji} {self.status}")

class StatsCard:
    """
    📊 Statistics display card for dashboard header
    
    Monday Madness Level: INFORMATIVE! 📈
    """
    
    def __init__(self, stats_data: Dict):
        self.stats = stats_data
        
    def render(self) -> None:
        """
        📊 Render stats in a beautiful format
        """
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Wiki Pages", self.stats.get("total_pages", 0))
            
        with col2:
            st.metric("Features", self.stats.get("total_features", 0))
            
        with col3:
            st.metric("Status", "🔥 ALIVE!")

def render_social_feed_header():
    """
    🔝 Render the social feed header with roadmap and stats
    """
    st.markdown("# 🚀 SuperApp Wiki Social Feed")
    st.markdown("*Where documentation becomes engaging!*")
    
    # TODO: Implement full header with roadmap cards 