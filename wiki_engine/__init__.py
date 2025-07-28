"""
🚀 SuperApp Wiki Engine
The heart of our wiki-powered social feed dashboard

Monday Madness Implementation - Making Documentation ALIVE!
"""

from .wiki_parser import WikiParser
from .git_sync import GitSyncEngine
from .feed_generator import FeedGenerator
from .card_components import WikiCard, ExpandableCard, ActionButton

__version__ = "1.0.0"
__author__ = "SuperApp Team - Monday Madness Session"

# Core engine components
__all__ = [
    "WikiParser",
    "GitSyncEngine", 
    "FeedGenerator",
    "WikiCard",
    "ExpandableCard",
    "ActionButton"
]

# Engine status for dashboard
ENGINE_STATUS = {
    "initialized": True,
    "version": __version__,
    "components_loaded": len(__all__),
    "monday_madness_level": "MAXIMUM! 🚀"
} 