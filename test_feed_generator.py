#!/usr/bin/env python3
"""
🧪 Test our FeedGenerator - Social Media Magic for Wiki Content!
Monday Madness Feed Generation Quality Assurance! 
"""

from wiki_engine.feed_generator import FeedGenerator
from wiki_engine.wiki_parser import WikiParser
import json
from datetime import datetime

def test_feed_generator():
    """
    🚀 Test the FeedGenerator with our actual wiki content
    """
    print("🧪 Testing FeedGenerator with Monday Madness energy!")
    print("=" * 70)
    
    # Initialize the feed generator
    parser = WikiParser("clients-hub-wiki")
    feed_gen = FeedGenerator(parser)
    
    # Test 1: Create Individual Wiki Cards
    print("\n🎴 Testing Individual Wiki Card Creation...")
    print("-" * 50)
    
    wiki_files = ["Home.md", "Account-Management.md", "Account-Member-Permissions.md", "User.md"]
    
    for wiki_file in wiki_files:
        print(f"\n📄 Creating card for {wiki_file}...")
        
        card = feed_gen.create_wiki_card(wiki_file)
        
        print(f"✅ Card ID: {card['id']}")
        print(f"🏷️  Title: {card['title']}")
        print(f"🎯 Type: {card['type']} ({card['icon']})")
        print(f"📊 Priority: {card['priority']}")
        print(f"⚡ Engagement: {card['engagement_score']}/100")
        print(f"🎪 Energy Level: {card['monday_madness_level']}")
        print(f"📚 Features: {len(card['features'])}")
        print(f"⏱️  Read Time: {card['social_stats']['read_time']}")
        print(f"🎨 Style Class: {card['style_class']}")
        
        if card['features']:
            print(f"🌟 Top Features: {', '.join(card['features'][:3])}")
    
    # Test 2: Generate Complete Activity Timeline
    print("\n\n📅 Testing Activity Timeline Generation...")
    print("-" * 50)
    
    timeline = feed_gen.generate_activity_timeline()
    
    print(f"📊 Generated {len(timeline)} cards in timeline")
    print("\n🏆 Timeline Order (by engagement & priority):")
    
    for i, card in enumerate(timeline, 1):
        priority_emoji = {"high": "🔥", "medium": "⚡", "low": "📄"}.get(card['priority'], "📄")
        print(f"   {i}. {card['icon']} {card['title']} {priority_emoji}")
        print(f"      📊 Score: {card['engagement_score']} | Type: {card['type']}")
    
    # Test 3: Test Roadmap Generation
    print("\n\n🗺️  Testing Roadmap Generation...")
    print("-" * 50)
    
    roadmap_cards = feed_gen.generate_roadmap_cards()
    
    for phase in roadmap_cards:
        status_emoji = "✅" if phase['status'] == 'complete' else "🔄" if phase['status'] == 'in_progress' else "📅"
        print(f"{status_emoji} {phase['phase']}: {phase['progress']}% complete")
        print(f"   Features: {', '.join(phase['features'])}")
    
    # Test 4: Test Stats Summary
    print("\n\n📈 Testing Stats Summary...")
    print("-" * 50)
    
    stats = feed_gen.create_stats_summary()
    
    print(f"📊 Project Stats:")
    print(f"   📚 Total Pages: {stats['total_pages']}")
    print(f"   ⭐ Total Features: {stats['total_features']}")
    print(f"   🕐 Last Updated: {stats['last_updated']}")
    print(f"   💪 Status: {stats['status']}")
    
    # Test 5: Test Action Buttons
    print("\n\n🔘 Testing Action Button Generation...")
    print("-" * 50)
    
    for card_type in ["permissions_matrix", "account_management", "user_system"]:
        actions = feed_gen.generate_action_buttons(card_type)
        print(f"\n{card_type}:")
        for action in actions:
            print(f"   {action['icon']} {action['label']} ({action['action']})")
    
    # Test 6: Show Cache Performance
    print("\n\n⚡ Testing Feed Cache...")
    print("-" * 50)
    
    print(f"📦 Cached cards: {len(feed_gen.feed_cache)}")
    for cached_file in feed_gen.feed_cache.keys():
        print(f"   💾 {cached_file}")
    
    print("\n" + "=" * 70)
    print("🎉 FeedGenerator Test Complete! SOCIAL FEED MAGIC ACTIVATED! 🎪✨")
    
    # Show the best card
    if timeline:
        best_card = timeline[0]
        print(f"\n🏆 BEST CARD: {best_card['icon']} {best_card['title']}")
        print(f"🎯 Why it's #1: {best_card['engagement_score']} engagement + {best_card['priority']} priority")
        print(f"🚀 Summary: {best_card['summary']}")

if __name__ == "__main__":
    test_feed_generator() 