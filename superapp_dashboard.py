#!/usr/bin/env python3
"""
🚀 SuperApp Wiki-Powered Dashboard - THE CLIMAX!
Monday Madness Ultimate Implementation!

Where Git Wiki documentation becomes a BEAUTIFUL dashboard experience!
"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime

# Add our wiki engine to the path
sys.path.append(str(Path(__file__).parent))

from wiki_engine import WikiParser, GitSyncEngine, FeedGenerator
from wiki_engine.card_components import WikiCard, RoadmapCard, StatsCard, TimelineRoadmap, render_dashboard_header

def load_custom_css():
    """
    🎨 Load our beautiful custom CSS styling
    """
    css_file = Path("dashboard_assets/styles.css")
    if css_file.exists():
        with open(css_file, 'r') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ CSS file not found - dashboard will use default styling")

def initialize_wiki_engine():
    """
    🔧 Initialize our wiki engine components with demo mode fallback
    """
    try:
        # Try to initialize with real wiki
        wiki_dir = Path("clients-hub-wiki")
        if not wiki_dir.exists():
            st.info("📡 Running in DEMO mode - showing sample content")
            return initialize_demo_mode()
        
        if 'wiki_parser' not in st.session_state:
            st.session_state.wiki_parser = WikiParser("clients-hub-wiki")
        
        if 'git_sync' not in st.session_state:
            st.session_state.git_sync = GitSyncEngine("clients-hub-wiki")
        
        if 'feed_generator' not in st.session_state:
            st.session_state.feed_generator = FeedGenerator(st.session_state.wiki_parser)
        
        return st.session_state.wiki_parser, st.session_state.git_sync, st.session_state.feed_generator
    
    except Exception as e:
        st.warning(f"📡 Wiki unavailable, running in DEMO mode: {str(e)[:100]}")
        return initialize_demo_mode()

def initialize_demo_mode():
    """
    🎭 Initialize demo mode with sample wiki content for Streamlit Cloud
    """
    class MockWikiParser:
        def __init__(self):
            self.wiki_dir = Path("demo")
        def get_all_wiki_files(self):
            return ["Home.md", "Account-Management.md", "User.md"]
    
    class MockGitSync:
        def __init__(self):
            self.last_sync = datetime.now()
        def pull_wiki_updates(self):
            return {"status": "demo", "message": "Demo mode - no sync available"}
    
    class MockFeedGenerator:
        def __init__(self, parser):
            self.parser = parser
            self.feed_cache = {}
        
        def generate_activity_timeline(self):
            return [
                {
                    "id": "demo_home",
                    "title": "SuperApp Documentation Home",
                    "summary": "Welcome to the SuperApp platform! This demo shows how your team's wiki documentation would be beautifully displayed as cards.",
                    "content": "# SuperApp Documentation\n\nThis is a demo of how your wiki content would appear. The real dashboard will sync with your Git repository to show live documentation.\n\n## Features\n- Real-time Git sync\n- Beautiful card display\n- Timeline roadmap\n- Engagement scoring",
                    "type": "overview",
                    "priority": "high",
                    "engagement_score": 95,
                    "features": ["Git Integration", "Beautiful UI", "Real-time Updates"],
                    "content_stats": {
                        "read_time": "3 min read",
                        "complexity": "Medium",
                        "feature_count": 3,
                        "word_count": 150
                    }
                },
                {
                    "id": "demo_account",
                    "title": "Account Management System",
                    "summary": "Complete user account management with invitations, permissions, and role-based access control.",
                    "content": "# Account Management\n\n## Features\n- User registration and login\n- Account invitations with 7-day expiry\n- Role-based permissions (Owner, Admin, Manager, Staff)\n- Multi-tenant architecture\n\n## Implementation Status\n✅ User Registration\n✅ Account Invitations\n🔄 Permission System (In Progress)",
                    "type": "feature",
                    "priority": "high",
                    "engagement_score": 88,
                    "features": ["User Registration", "Invitations", "Permissions", "Multi-tenant"],
                    "content_stats": {
                        "read_time": "5 min read",
                        "complexity": "High",
                        "feature_count": 4,
                        "word_count": 200
                    }
                },
                {
                    "id": "demo_integration",
                    "title": "Email Integration Research",
                    "summary": "Research and implementation of Brevo email service for Laravel-based transactional emails.",
                    "content": "# Email Integration\n\n## Brevo Integration\nResearching the best approach to integrate Brevo with Laravel while maintaining native mailing functionality.\n\n## Requirements\n- Native Laravel mail support\n- Template management\n- Delivery tracking\n- Cost-effective solution",
                    "type": "research",
                    "priority": "medium",
                    "engagement_score": 72,
                    "features": ["Laravel Integration", "Email Templates", "Delivery Tracking"],
                    "content_stats": {
                        "read_time": "2 min read",
                        "complexity": "Medium",
                        "feature_count": 3,
                        "word_count": 100
                    }
                }
            ]
        
        def generate_roadmap_cards(self):
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
        
        def create_stats_summary(self):
            return {
                "total_pages": 3,
                "total_features": 10,
                "last_updated": "Today",
                "status": "DEMO MODE"
            }
    
    # Create and store mock instances
    mock_parser = MockWikiParser()
    mock_git = MockGitSync()
    mock_feed = MockFeedGenerator(mock_parser)
    
    st.session_state.wiki_parser = mock_parser
    st.session_state.git_sync = mock_git
    st.session_state.feed_generator = mock_feed
    
    return mock_parser, mock_git, mock_feed

def sync_wiki_updates(git_sync):
    """
    🔄 Check for and pull wiki updates
    """
    with st.spinner("🔄 Checking for wiki updates..."):
        sync_result = git_sync.pull_wiki_updates()
        
        if sync_result["status"] == "success":
            if sync_result["changes_detected"]:
                st.success(f"✅ Wiki updated! {len(sync_result['files_updated'])} files changed")
                # Clear cache to reload fresh data
                if 'feed_generator' in st.session_state:
                    st.session_state.feed_generator.feed_cache.clear()
            else:
                st.info("📄 Wiki is up to date")
        else:
            st.error(f"❌ Sync failed: {sync_result.get('error', 'Unknown error')}")
    
    return sync_result

def render_dashboard_header_section(feed_generator):
    """
    🔝 Render the beautiful dashboard header with roadmap and stats
    """
    st.markdown("# SuperApp Documentation Dashboard")
    st.markdown("*Where wiki documentation becomes engaging and beautiful*")
    
    # Dashboard sync status
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown("**Live Wiki Dashboard** - Powered by Git Repository")
    
    with col2:
        if st.button("Sync Wiki", help="Pull latest updates from Git"):
            sync_wiki_updates(st.session_state.git_sync)
            st.rerun()
    
    with col3:
        last_sync = getattr(st.session_state.git_sync, 'last_sync', None)
        if last_sync:
            st.caption(f"Last sync: {last_sync.strftime('%H:%M')}")
        else:
            st.caption("Never synced")
    
    st.markdown("---")
    
    # Stats overview
    stats_data = feed_generator.create_stats_summary()
    stats_card = StatsCard(stats_data)
    stats_card.render()
    


def render_wiki_feed(feed_generator):
    """
    🎴 Render the main wiki documentation feed
    """
    # Check if we're viewing a specific card in detail
    viewing_card = None
    for key in st.session_state.keys():
        if key.startswith('viewing_card_') and st.session_state[key]:
            viewing_card = key.replace('viewing_card_', '')
            break
    
    if viewing_card:
        # Show detailed view for the selected card
        timeline = feed_generator.generate_activity_timeline()
        selected_card = next((card for card in timeline if card.get('id') == viewing_card), None)
        
        if selected_card:
            wiki_card = WikiCard(selected_card)
            wiki_card._show_full_content()
        return
    
    # Normal feed view
    st.markdown("## Documentation Feed")
    st.markdown("*Your team's wiki content, beautifully displayed*")
    
    # Generate the timeline of cards
    timeline = feed_generator.generate_activity_timeline()
    
    if not timeline:
        st.warning("📄 No wiki content found. Make sure the wiki repository is cloned and contains markdown files.")
        return
    
    # Display cards in full-width rows with proper card styling
    for i, card_data in enumerate(timeline):
        with st.container():
            wiki_card = WikiCard(card_data)
            wiki_card.render()
            
            # Add some spacing between cards
            if i < len(timeline) - 1:
                st.markdown("<br>", unsafe_allow_html=True)

def render_timeline_roadmap(feed_generator):
    """
    🗺️ Render the beautiful timeline-style roadmap
    """
    roadmap_data = feed_generator.generate_roadmap_cards()
    timeline_roadmap = TimelineRoadmap(roadmap_data)
    timeline_roadmap.render()

def render_sidebar():
    """
    📋 Render the sidebar with additional controls and info
    """
    with st.sidebar:
        st.markdown("# Control Panel")
        
        # Wiki status
        st.markdown("## Wiki Status")
        
        if hasattr(st.session_state, 'wiki_parser'):
            wiki_files = st.session_state.wiki_parser.get_all_wiki_files()
            st.metric("Wiki Files", len(list(wiki_files)))
        
        if hasattr(st.session_state, 'feed_generator'):
            cache_size = len(st.session_state.feed_generator.feed_cache)
            st.metric("Cached Cards", cache_size)
        
        st.markdown("---")
        
        # Dashboard controls
        st.markdown("## Dashboard Controls")
        
        if st.button("Clear Cache"):
            if hasattr(st.session_state, 'feed_generator'):
                st.session_state.feed_generator.feed_cache.clear()
                st.success("Cache cleared!")
        
        if st.button("Force Refresh"):
            # Clear all session state and reload
            for key in list(st.session_state.keys()):
                if key.startswith(('wiki_', 'git_', 'feed_')):
                    del st.session_state[key]
            st.success("Dashboard refreshed!")
            st.rerun()
        
        st.markdown("---")
        st.caption("Built with Monday Madness energy by SuperApp Team")

def main():
    """
    🎬 Main dashboard application
    """
    # Page config
    st.set_page_config(
        page_title="SuperApp Wiki Dashboard",
        page_icon="🚀",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    
    # Load custom styling
    load_custom_css()
    
    # Initialize components
    try:
        wiki_parser, git_sync, feed_generator = initialize_wiki_engine()
    except Exception as e:
        st.error(f"❌ Failed to initialize wiki engine: {e}")
        st.info("💡 Make sure the 'clients-hub-wiki' directory exists and contains wiki content")
        return
    
    # Render sidebar
    render_sidebar()
    
    # Main content area
    try:
        # Header section
        render_dashboard_header_section(feed_generator)
        
        # Wiki feed section
        render_wiki_feed(feed_generator)
        
        # Timeline roadmap section
        st.markdown("---")
        render_timeline_roadmap(feed_generator)
        
        # Footer
        st.markdown("---")
        st.markdown("### 🎉 Dashboard Complete!")
        st.markdown("*This dashboard automatically syncs with your Git Wiki for real-time documentation display*")
        
        # Success celebration
        col1, col2, col3 = st.columns(3)
        with col2:
            st.balloons()
        
    except Exception as e:
        st.error(f"❌ Dashboard error: {e}")
        st.info("🔧 Check the sidebar for refresh options")

if __name__ == "__main__":
    main() 