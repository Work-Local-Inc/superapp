#!/usr/bin/env python3
"""
🧪 Test our WikiParser with real wiki content
Monday Madness Quality Assurance! 
"""

from wiki_engine.wiki_parser import WikiParser
import json
from pathlib import Path

def test_wiki_parser():
    """
    🚀 Test the WikiParser with our actual wiki files
    """
    print("🧪 Testing WikiParser with Monday Madness energy!")
    print("=" * 60)
    
    parser = WikiParser("clients-hub-wiki")
    
    # Test with each wiki file
    wiki_files = ["Home.md", "Account-Management.md", "Account-Member-Permissions.md", "User.md"]
    
    for wiki_file in wiki_files:
        print(f"\n📄 Testing {wiki_file}...")
        print("-" * 40)
        
        card_data = parser.parse_markdown_to_card(wiki_file)
        
        if card_data["status"] == "success":
            print(f"✅ SUCCESS!")
            print(f"🏷️  Title: {card_data['title']}")
            print(f"📝 Summary: {card_data['summary']}")
            print(f"🎯 Type: {card_data['type']}")
            print(f"📊 Metrics:")
            metrics = card_data['metadata']['metrics']
            print(f"   📖 Words: {metrics['word_count']}")
            print(f"   ⭐ Features: {metrics['feature_count']}")
            print(f"   📋 Tables: {metrics['table_count']}")
            print(f"   🎪 Engagement: {metrics['engagement_potential']}")
            print(f"   ✅ Monday Madness Approved: {metrics['monday_madness_approved']}")
            
            print(f"\n🎯 Features Found:")
            for i, feature in enumerate(card_data['metadata']['features'][:5], 1):
                print(f"   {i}. {feature}")
                
        else:
            print(f"❌ ERROR: {card_data['summary']}")
    
    print("\n" + "=" * 60)
    print("🎉 WikiParser Test Complete! Monday Madness VERIFIED! 🚀")

if __name__ == "__main__":
    test_wiki_parser() 