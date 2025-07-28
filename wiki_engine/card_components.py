#!/usr/bin/env python3
"""
Card Components - Beautiful UI Elements for Our Documentation Dashboard

Monday Madness Implementation - Clean and Professional!
"""

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

from typing import Dict, List, Optional
from datetime import datetime

class WikiCard:
    """
    🎴 Base wiki card component for documentation display
    
    Monday Madness Level: BEAUTIFUL! 🎨
    """
    
    def __init__(self, card_data: Dict):
        self.data = card_data
        self.expanded = False
        
    def render(self) -> None:
        """
        🎨 Render the card in Streamlit with beautiful card styling
        """
        # Create the beautiful card container with CSS styling
        with st.container():
            # Get the data we need for inside the card
            features_count = len(self.data.get('features', []))
            engagement = self.data.get('engagement_score', 0)
            read_time = self.data.get('content_stats', {}).get('read_time', 'Unknown')
            
            # Use Streamlit container with proper styling
            with st.container():
                # Add CSS that will actually work
                st.markdown("""
                <style>
                .stContainer:has(.wiki-card-content) {
                    background: white !important;
                    border: 1px solid #e5e7eb !important;
                    border-radius: 16px !important;
                    padding: 1.5rem !important;
                    margin: 1rem 0 !important;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07) !important;
                }
                </style>
                """, unsafe_allow_html=True)
                
                # Mark this as a wiki card container
                st.markdown('<div class="wiki-card-content">', unsafe_allow_html=True)
                
                # Card header with icon, title, and priority
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"### {self.data.get('icon', '📄')} {self.data.get('title', 'Untitled')}")
                with col2:
                    priority = self.data.get('priority', 'low')
                    priority_emoji = {"high": "🔥", "medium": "⚡", "low": "📄"}.get(priority, "📄")
                    st.markdown(f"**{priority_emoji} {priority.title()}**")
                
                # Card summary
                summary = self.data.get('summary', 'No summary available')
                st.markdown(f"*{summary}*")
                
                # Divider
                st.markdown("---")
                
                # Stats row
                st.markdown(f"📚 **{features_count} features** • ⚡ **{engagement}/100** • ⏱️ **{read_time}**")
                
                # Action buttons
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("📖 View Details", 
                               key=f"view_{self.data.get('id', 'card')}", 
                               use_container_width=True):
                        self._show_full_content()
                
                with col2:
                    if st.button("🔗 Wiki Link", 
                               key=f"wiki_{self.data.get('id', 'card')}", 
                               use_container_width=True):
                        st.info("📝 Would open wiki page in new tab")
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    def _show_full_content(self):
        """
        📖 Show full content in a modal-like experience
        """
        # Use session state to track which card is being viewed
        card_id = self.data.get('id', 'unknown')
        st.session_state[f'viewing_card_{card_id}'] = True
        
        # Create a modal-like display
        with st.container():
            st.markdown("---")
            st.markdown(f"# 📖 {self.data.get('title', 'Content Details')}")
            
            # Card metadata
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("📚 Features", len(self.data.get('features', [])))
            
            with col2:
                engagement = self.data.get('engagement_score', 0)
                st.metric("⚡ Engagement", f"{engagement}/100")
            
            with col3:
                read_time = self.data.get('content_stats', {}).get('read_time', 'Unknown')
                st.metric("⏱️ Read Time", read_time)
            
            # Full content
            content = self.data.get('content', '')
            if content:
                st.markdown("## 📄 Full Documentation")
                st.markdown(content)
            else:
                st.info("No detailed content available")
            
            # Features list
            features = self.data.get('features', [])
            if features:
                st.markdown("## ✨ Key Features")
                for feature in features:
                    st.markdown(f"- {feature}")
            
            # Close button
            if st.button("← Back to Feed", key=f"close_{card_id}"):
                del st.session_state[f'viewing_card_{card_id}']
                st.rerun()
            
            st.markdown("---")

class ExpandableCard(WikiCard):
    """
    📖 Expandable card with smooth animations and rich content
    
    Monday Madness Level: INTERACTIVE! 🎪
    """
    
    def __init__(self, card_data: Dict, default_expanded: bool = False):
        super().__init__(card_data)
        self.expanded = default_expanded
        
    def toggle_expanded(self) -> None:
        """
        🔄 Toggle card expansion state
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