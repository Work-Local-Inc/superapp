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
        # Create the main card container
        with st.container():
            # Apply custom CSS styling
            st.markdown(f"""
            <div class="{self.data.get('style_class', 'wiki-card')}">
                <div class="card-header">
                    <div class="card-title">
                        <span class="card-icon">{self.data.get('icon', '📄')}</span>
                        <h3>{self.data.get('title', 'Untitled')}</h3>
                    </div>
                    <div class="card-meta">
                        <span class="card-type">{self.data.get('type', 'documentation')}</span>
                        <span class="card-priority priority-{self.data.get('priority', 'low')}">{self.data.get('priority', 'low')}</span>
                    </div>
                </div>
                <div class="card-content">
                    <p class="card-summary">{self.data.get('summary', 'No summary available')}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Content stats row
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("📚 Features", len(self.data.get('features', [])))
            
            with col2:
                read_time = self.data.get('content_stats', {}).get('read_time', 'Unknown')
                st.metric("⏱️ Read Time", read_time)
            
            with col3:
                engagement = self.data.get('engagement_score', 0)
                st.metric("⚡ Score", f"{engagement}/100")
            
            with col4:
                word_count = self.data.get('content_stats', {}).get('word_count', 0)
                st.metric("📝 Words", word_count)
            
            # Action buttons
            actions = self.data.get('actions', [])
            if actions:
                cols = st.columns(len(actions))
                for i, action in enumerate(actions):
                    with cols[i]:
                        if st.button(f"{action.get('icon', '🔗')} {action.get('label', 'Action')}", 
                                   key=f"{self.data.get('id', 'card')}_{action.get('action', 'btn')}"):
                            st.info(f"Action: {action.get('action', 'Unknown')}")
            
            # Expandable content
            if self.data.get('expandable', False):
                with st.expander("📖 View Full Content"):
                    content = self.data.get('content', '')
                    if content:
                        st.markdown(content)
                    else:
                        st.info("No detailed content available")
                    
                    # Show features if available
                    features = self.data.get('features', [])
                    if features:
                        st.markdown("### ✨ Key Features:")
                        for feature in features:
                            st.markdown(f"- {feature}")
            
            # Monday Madness energy indicator
            energy_level = self.data.get('monday_madness_level', 'Building up...')
            st.caption(f"🎪 Energy Level: {energy_level}")

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
        with st.container():
            # Header row
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### 🗺️ {self.phase}")
                
            with col2:
                st.metric("Progress", f"{self.progress}%")
            
            # Progress bar with color based on status
            if self.status == "complete":
                st.success(f"✅ Complete")
            elif self.status == "in_progress":
                st.info(f"🔄 In Progress")
            else:
                st.warning(f"📅 Pending")
                
            st.progress(self.progress / 100)
            
            # Features list
            if self.features:
                st.markdown("**Key Deliverables:**")
                for feature in self.features:
                    feature_status = "✅" if self.status == "complete" else "🔄" if self.status == "in_progress" else "📋"
                    st.markdown(f"- {feature_status} {feature}")
            
            st.markdown("---")

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
        st.markdown("### 📊 Project Dashboard Stats")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📚 Wiki Pages", self.stats.get("total_pages", 0))
            
        with col2:
            st.metric("⭐ Features", self.stats.get("total_features", 0))
            
        with col3:
            last_updated = self.stats.get("last_updated", "Unknown")
            if isinstance(last_updated, str):
                st.metric("🕐 Last Updated", "Today")
            else:
                st.metric("🕐 Last Updated", last_updated.strftime("%m/%d"))
            
        with col4:
            status = self.stats.get("status", "🔥 ALIVE!")
            st.metric("💪 Status", status)
        
        st.markdown("---")

def render_dashboard_header():
    """
    🔝 Render the dashboard header with roadmap and stats
    """
    st.markdown("# 🚀 SuperApp Documentation Dashboard")
    st.markdown("*Where documentation becomes engaging and beautiful!*")
    
    # TODO: Full header implementation with roadmap and stats cards