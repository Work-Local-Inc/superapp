#!/usr/bin/env python3
"""
🧪 Test our GitSync Engine
Monday Madness Git Sync Quality Assurance! 
"""

from wiki_engine.git_sync import GitSyncEngine
import json
from datetime import datetime

def test_git_sync():
    """
    🚀 Test the GitSync engine with our actual wiki repository
    """
    print("🧪 Testing GitSync Engine with Monday Madness energy!")
    print("=" * 60)
    
    sync_engine = GitSyncEngine("clients-hub-wiki")
    
    # Test 1: Repository Status
    print("\n📊 Testing Repository Status...")
    print("-" * 40)
    
    status = sync_engine.get_repo_status()
    print(f"✅ Repository exists: {status['repo_exists']}")
    print(f"✅ Is Git repo: {status['is_git_repo']}")
    print(f"✅ Health status: {status['health_status']}")
    print(f"✅ Sync count: {status['sync_count']}")
    
    # Test 2: Pull Wiki Updates
    print("\n📥 Testing Wiki Sync...")
    print("-" * 40)
    
    sync_result = sync_engine.pull_wiki_updates()
    print(f"📊 Sync Status: {sync_result['status']}")
    print(f"🔄 Changes Detected: {sync_result['changes_detected']}")
    print(f"📂 Files Updated: {len(sync_result.get('files_updated', []))}")
    
    if sync_result['status'] == 'success':
        print(f"⚡ Energy Level: {sync_result['monday_madness_energy']}")
        if 'commit_before' in sync_result:
            print(f"📍 Commit Before: {sync_result['commit_before']}")
            print(f"📍 Commit After: {sync_result['commit_after']}")
        if 'pull_output' in sync_result:
            print(f"📤 Git Output: {sync_result['pull_output'].strip()}")
    elif sync_result['status'] == 'error':
        print(f"❌ Error: {sync_result.get('error', 'Unknown error')}")
        print("🔧 Debugging: This might be normal if repo is up-to-date")
    
    # Test 3: File Change Detection
    print("\n🔍 Testing File Change Detection...")
    print("-" * 40)
    
    file_changes = sync_engine.detect_file_changes()
    if file_changes:
        print(f"📋 {len(file_changes)} changes detected:")
        for change in file_changes[:5]:  # Show first 5
            print(f"   {change['status'].upper()}: {change['filename']} {change['monday_madness_impact']}")
    else:
        print("📝 No recent changes detected")
    
    # Test 4: Auto-sync Setup
    print("\n⏰ Testing Auto-sync Setup...")
    print("-" * 40)
    
    auto_setup = sync_engine.setup_auto_sync(30)
    print(f"🚀 Auto-sync configured: {auto_setup}")
    
    # Test 5: Sync History
    print("\n📚 Testing Sync History...")
    print("-" * 40)
    
    history = sync_engine.sync_history
    print(f"📈 Total sync activities: {len(history)}")
    
    if history:
        latest = history[-1]
        print(f"🕐 Latest activity: {latest.get('type', 'sync')} at {latest['timestamp']}")
    
    # Test 6: Force Sync
    print("\n🚨 Testing Force Sync...")
    print("-" * 40)
    
    force_result = sync_engine.force_sync_now()
    print(f"⚡ Force sync result: {force_result['status']}")
    
    print("\n" + "=" * 60)
    print("🎉 GitSync Engine Test Complete! ROLLIN' AND SYNC-IN'! 🚀🔄")
    
    # Show final stats
    final_status = sync_engine.get_repo_status()
    print(f"\n📊 Final Stats:")
    print(f"   🔄 Total syncs performed: {final_status['sync_count']}")
    print(f"   ⏰ Last sync: {final_status['last_sync']}")
    print(f"   💪 Overall health: {final_status['health_status']}")

if __name__ == "__main__":
    test_git_sync() 