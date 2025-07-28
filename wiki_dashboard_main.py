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
from wiki_engine.card_components import WikiCard, RoadmapCard, StatsCard, render_dashboard_header

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
    🔧 Initialize our wiki engine components
    """
    if 'wiki_parser' not in st.session_state:
        st.session_state.wiki_parser = WikiParser("clients-hub-wiki")
    
    if 'git_sync' not in st.session_state:
        st.session_state.git_sync = GitSyncEngine("clients-hub-wiki")
    
    if 'feed_generator' not in st.session_state:
        st.session_state.feed_generator = FeedGenerator(st.session_state.wiki_parser)
    
    return st.session_state.wiki_parser, st.session_state.git_sync, st.session_state.feed_generator

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
    
    # Roadmap cards
    st.markdown("## 🗺️ Project Roadmap")
    roadmap_data = feed_generator.generate_roadmap_cards()
    
    cols = st.columns(len(roadmap_data))
    for i, phase_data in enumerate(roadmap_data):
        with cols[i]:
            roadmap_card = RoadmapCard(phase_data)
            roadmap_card.render()

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

def render_sidebar():
    """
    📋 Render the sidebar with additional controls and info
    """
    with st.sidebar:
        st.markdown("# 🎪 Monday Madness Control Panel")
        
        # Wiki status
        st.markdown("## 📊 Wiki Status")
        
        if hasattr(st.session_state, 'wiki_parser'):
            wiki_files = st.session_state.wiki_parser.get_all_wiki_files()
            st.metric("📚 Wiki Files", len(list(wiki_files)))
        
        if hasattr(st.session_state, 'feed_generator'):
            cache_size = len(st.session_state.feed_generator.feed_cache)
            st.metric("💾 Cached Cards", cache_size)
        
        st.markdown("---")
        
        # Dashboard controls
        st.markdown("## ⚙️ Dashboard Controls")
        
        if st.button("🧹 Clear Cache"):
            if hasattr(st.session_state, 'feed_generator'):
                st.session_state.feed_generator.feed_cache.clear()
                st.success("✅ Cache cleared!")
        
        if st.button("🔄 Force Refresh"):
            # Clear all session state and reload
            for key in list(st.session_state.keys()):
                if key.startswith(('wiki_', 'git_', 'feed_')):
                    del st.session_state[key]
            st.success("✅ Dashboard refreshed!")
            st.rerun()
        
        st.markdown("---")
        st.caption("🎨 Built with Monday Madness energy by SuperApp Team")

def main():
    """
    🎬 Main dashboard application
    """
    # Page config
    st.set_page_config(
        page_title="SuperApp Wiki Dashboard",
        page_icon="🚀",
        layout="wide",
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