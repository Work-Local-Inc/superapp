#!/usr/bin/env python3
"""
🚀 SuperApp Wiki Dashboard Launcher
Monday Madness Quick Launch Script!
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Launch the dashboard with proper error handling"""
    
    print("🚀 Launching SuperApp Wiki Dashboard...")
    print("🎪 Monday Madness Energy: MAXIMUM!")
    print("=" * 50)
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit found!")
    except ImportError:
        print("❌ Streamlit not installed!")
        print("💡 Install with: pip install streamlit")
        return
    
    # Check if wiki directory exists
    wiki_dir = Path("clients-hub-wiki")
    if not wiki_dir.exists():
        print("⚠️  Wiki directory not found!")
        print("💡 Make sure 'clients-hub-wiki' directory exists")
        print("💡 Clone with: git clone https://github.com/Shared-Concepts/clients-hub.wiki.git clients-hub-wiki")
    else:
        print("✅ Wiki directory found!")
    
    # Check wiki engine components
    try:
        from wiki_engine import WikiParser, GitSyncEngine, FeedGenerator
        print("✅ Wiki engine ready!")
    except ImportError as e:
        print(f"❌ Wiki engine error: {e}")
        return
    
    print("\n🎬 LAUNCHING DASHBOARD...")
    print("🌐 Dashboard will open in your browser automatically!")
    print("🎪 Enjoy the Monday Madness experience!")
    
    # Launch streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "wiki_dashboard_main.py",
            "--server.port", "8501",
            "--server.headless", "false",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Dashboard shutdown complete!")
    except Exception as e:
        print(f"❌ Launch error: {e}")

if __name__ == "__main__":
    main() 