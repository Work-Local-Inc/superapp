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
            
            # Clean, simple approach using Streamlit's built-in expander
            priority = self.data.get('priority', 'low').title()
            title = self.data.get('title', 'Untitled')
            
            # Use minimal expander label and add proper header inside
            with st.expander("View Details", expanded=True):
                
                # Proper card header inside the expander
                if priority == "High":
                    st.markdown(f"### {title}")
                    st.markdown("*High Priority*")
                else:
                    st.markdown(f"### {title}")
                
                st.markdown("---")
                
                # Card summary
                summary = self.data.get('summary', 'No summary available')
                st.markdown(summary)
                
                # Stats in columns - clean metrics without emoji spam
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Features", features_count)
                with col2:
                    st.metric("Score", f"{self.data.get('engagement_score', 0)}/100")
                with col3:
                    st.metric("Read Time", read_time)
                
                # Action buttons - clean labels
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("View Details", 
                               key=f"view_{self.data.get('id', 'card')}", 
                               use_container_width=True):
                        self._show_full_content()
                
                with col2:
                    if st.button("Wiki Link", 
                               key=f"wiki_{self.data.get('id', 'card')}", 
                               use_container_width=True):
                        st.info("Opens wiki page in new tab")
    
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

class TimelineRoadmap:
    """
    🗺️ Beautiful timeline-style roadmap component
    Displays project phases in a horizontal timeline with progress indicators
    """
    
    def __init__(self, roadmap_data: List[Dict]):
        self.roadmap_data = roadmap_data
    
    def render(self) -> None:
        """
        🎨 Render the timeline roadmap with beautiful styling
        """
        st.markdown("### Project Roadmap")
        st.markdown("*Our journey to building the SuperApp platform*")
        
        # Custom CSS for timeline styling
        st.markdown("""
        <style>
        .timeline-container {
            position: relative;
            margin: 2rem 0;
            padding: 1rem 0;
        }
        
        .timeline-line {
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #4CAF50 0%, #2196F3 50%, #FF9800 100%);
            border-radius: 2px;
            z-index: 1;
        }
        
        .timeline-items {
            display: flex;
            justify-content: space-between;
            position: relative;
            z-index: 2;
        }
        
        .timeline-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            background: white;
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border: 2px solid #e1e5e9;
            min-width: 200px;
            position: relative;
        }
        
        .timeline-item.completed {
            border-color: #4CAF50;
            background: linear-gradient(135deg, #f8fff8, #ffffff);
        }
        
        .timeline-item.in-progress, .timeline-item.in_progress {
            border-color: #2196F3;
            background: linear-gradient(135deg, #f0f8ff, #ffffff);
        }
        
        .timeline-item.pending {
            border-color: #FF9800;
            background: linear-gradient(135deg, #fff8f0, #ffffff);
        }
        
        .timeline-dot {
            width: 16px;
            height: 16px;
            border-radius: 50%;
            position: absolute;
            top: -8px;
            left: 50%;
            transform: translateX(-50%);
            border: 3px solid white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }
        
        .timeline-dot.completed { background: #4CAF50; }
        .timeline-dot.in-progress, .timeline-dot.in_progress { background: #2196F3; }
        .timeline-dot.pending { background: #FF9800; }
        
        .phase-title {
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            text-align: center;
            color: #2c3e50;
        }
        
        .phase-progress {
            width: 100%;
            height: 8px;
            background: #e1e5e9;
            border-radius: 4px;
            margin: 0.5rem 0;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s ease;
        }
        
        .progress-fill.completed { background: #4CAF50; }
        .progress-fill.in-progress, .progress-fill.in_progress { background: #2196F3; }
        .progress-fill.pending { background: #FF9800; }
        
        .phase-features {
            font-size: 0.85rem;
            color: #6c757d;
            text-align: center;
            margin-top: 0.5rem;
        }
        
        .phase-status {
            font-size: 0.75rem;
            font-weight: 500;
            text-transform: uppercase;
            padding: 0.25rem 0.5rem;
            border-radius: 12px;
            margin-top: 0.5rem;
        }
        
        .phase-status.completed {
            background: #4CAF50;
            color: white;
        }
        
        .phase-status.in-progress, .phase-status.in_progress {
            background: #2196F3;
            color: white;
        }
        
        .phase-status.pending {
            background: #FF9800;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Build timeline HTML
        timeline_html = '<div class="timeline-container">'
        timeline_html += '<div class="timeline-line"></div>'
        timeline_html += '<div class="timeline-items">'
        
        for phase in self.roadmap_data:
            status = phase.get('status', 'pending')
            progress = phase.get('progress', 0)
            features = phase.get('features', [])
            
            timeline_html += f'''
            <div class="timeline-item {status}">
                <div class="timeline-dot {status}"></div>
                <div class="phase-title">{phase.get('phase', 'Unknown Phase')}</div>
                <div class="phase-progress">
                    <div class="progress-fill {status}" style="width: {progress}%"></div>
                </div>
                <div class="phase-status {status}">{status.replace('-', ' ').replace('_', ' ')}</div>
                <div class="phase-features">
                    {len(features)} key features
                </div>
            </div>
            '''
        
        timeline_html += '</div></div>'
        
        # Render the timeline
        st.markdown(timeline_html, unsafe_allow_html=True)
        
        # Feature details below timeline
        with st.expander("View Detailed Features"):
            cols = st.columns(len(self.roadmap_data))
            
            for i, phase in enumerate(self.roadmap_data):
                with cols[i]:
                    st.markdown(f"**{phase.get('phase', 'Unknown')}**")
                    st.progress(phase.get('progress', 0) / 100)
                    st.caption(f"{phase.get('progress', 0)}% Complete")
                    
                    features = phase.get('features', [])
                    if features:
                        for feature in features:
                            st.markdown(f"• {feature}")
                    else:
                        st.markdown("*No features defined*")


class RoadmapCard:
    """
    🗺️ Legacy roadmap card - keeping for compatibility
    """
    
    def __init__(self, roadmap_data: List[Dict]):
        self.roadmap_data = roadmap_data
    
    def render(self) -> None:
        """
        📊 Render roadmap using the new timeline style
        """
        timeline = TimelineRoadmap(self.roadmap_data)
        timeline.render()


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
        st.markdown("### Project Dashboard Stats")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Wiki Pages", self.stats.get("total_pages", 0))
            
        with col2:
            st.metric("Features", self.stats.get("total_features", 0))
            
        with col3:
            last_updated = self.stats.get("last_updated", "Unknown")
            if isinstance(last_updated, str):
                st.metric("Last Updated", "Today")
            else:
                st.metric("Last Updated", last_updated.strftime("%m/%d"))
            
        with col4:
            status = self.stats.get("status", "ALIVE!")
            st.metric("Status", status)
        
        st.markdown("---")

def render_dashboard_header():
    """
    🔝 Render the dashboard header with roadmap and stats
    """
    st.markdown("# 🚀 SuperApp Documentation Dashboard")
    st.markdown("*Where documentation becomes engaging and beautiful!*")
    
    # TODO: Full header implementation with roadmap and stats cards