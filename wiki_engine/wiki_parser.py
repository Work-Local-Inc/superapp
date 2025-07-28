"""
WikiParser - Transform Git Wiki Markdown into Social Feed Gold
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class WikiParser:
    """
    🔍 The brain that transforms boring markdown into engaging social cards
    
    Monday Madness Level: EXPERT! 🚀
    """
    
    def __init__(self, wiki_directory: str = "clients-hub-wiki"):
        self.wiki_dir = Path(wiki_directory)
        self.last_parsed = {}
        
    def parse_markdown_to_card(self, md_file: str) -> Dict:
        """
        🎯 Transform a markdown file into a social feed card
        
        Args:
            md_file: Path to markdown file
            
        Returns:
            Dict containing card data (title, summary, content, metadata)
        """
        file_path = self.wiki_dir / md_file
        
        if not file_path.exists():
            return {
                "title": "File Not Found",
                "summary": "Wiki file could not be located",
                "content": "",
                "metadata": {"error": "file_not_found"},
                "status": "error"
            }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title from first heading or filename
            title = self._extract_title(content, md_file)
            
            # Generate engaging summary
            summary = self.generate_summary(content)
            
            # Extract metadata
            metadata = self.extract_metadata(content)
            
            # Calculate metrics
            metrics = self.calculate_content_metrics(content)
            
            # Extract features
            features = self.extract_features_from_content(content)
            
            return {
                "id": f"wiki_{md_file.replace('.md', '').replace('-', '_')}",
                "title": title,
                "summary": summary,
                "content": content,
                "metadata": {
                    **metadata,
                    "file_name": md_file,
                    "file_path": str(file_path),
                    "features": features,
                    "metrics": metrics
                },
                "type": self._determine_card_type(title, content),
                "timestamp": datetime.fromtimestamp(file_path.stat().st_mtime),
                "status": "success",
                "monday_madness_level": "MAXIMUM! 🚀"
            }
            
        except Exception as e:
            return {
                "title": "Parse Error",
                "summary": f"Error parsing {md_file}",
                "content": "",
                "metadata": {"error": str(e)},
                "status": "error"
            }
    
    def extract_metadata(self, content: str) -> Dict:
        """
        📊 Extract juicy metadata from markdown content
        """
        metadata = {}
        
        # Extract headings for navigation
        headings = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
        metadata["headings"] = headings
        
        # Extract tables (for permissions matrix, etc.)
        table_matches = re.findall(r'\|.*\|', content)
        metadata["has_tables"] = len(table_matches) > 0
        metadata["table_count"] = len([line for line in content.split('\n') if '|' in line and line.strip().startswith('|')])
        
        # Extract code blocks
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        metadata["code_blocks"] = len(code_blocks)
        
        # Extract links
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        metadata["external_links"] = [{"text": text, "url": url} for text, url in links if url.startswith('http')]
        metadata["internal_links"] = [{"text": text, "url": url} for text, url in links if not url.startswith('http')]
        
        # Detect content type based on keywords
        content_lower = content.lower()
        if "permission" in content_lower and "|" in content:
            metadata["content_type"] = "permissions_matrix"
        elif "account" in content_lower and "management" in content_lower:
            metadata["content_type"] = "account_management"
        elif "user" in content_lower and ("registration" in content_lower or "profile" in content_lower):
            metadata["content_type"] = "user_system"
        else:
            metadata["content_type"] = "general_documentation"
            
        return metadata
    
    def generate_summary(self, full_content: str, max_length: int = 150) -> str:
        """
        📝 Create punchy summaries that make people want to expand
        """
        # Remove markdown formatting for clean summary
        clean_content = re.sub(r'#{1,6}\s+', '', full_content)  # Remove headers
        clean_content = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean_content)  # Remove bold
        clean_content = re.sub(r'\*([^*]+)\*', r'\1', clean_content)  # Remove italic
        clean_content = re.sub(r'`([^`]+)`', r'\1', clean_content)  # Remove code
        clean_content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean_content)  # Remove links, keep text
        clean_content = re.sub(r'\|.*\|', '', clean_content)  # Remove table rows
        
        # Split into sentences and find the most engaging ones
        sentences = [s.strip() for s in re.split(r'[.!?]+', clean_content) if s.strip()]
        
        # Prioritize sentences with action words and technical terms
        engaging_words = ['account', 'user', 'permission', 'invite', 'management', 'system', 'feature', 'implement', 'create']
        
        scored_sentences = []
        for sentence in sentences[:10]:  # Only check first 10 sentences
            if len(sentence) > 20 and len(sentence) < 200:  # Good length
                score = sum(1 for word in engaging_words if word.lower() in sentence.lower())
                scored_sentences.append((score, sentence))
        
        # Sort by score and length preference
        scored_sentences.sort(key=lambda x: (x[0], -abs(len(x[1]) - 100)), reverse=True)
        
        if scored_sentences:
            summary = scored_sentences[0][1]
        else:
            # Fallback to first meaningful sentence
            summary = next((s for s in sentences if len(s) > 20), "Comprehensive documentation available")
        
        # Truncate if needed
        if len(summary) > max_length:
            summary = summary[:max_length - 3] + "..."
            
        return summary
    
    def detect_changes(self, old_content: str, new_content: str) -> List[str]:
        """
        🔄 Detect what changed in wiki content for activity feed
        """
        # TODO: Diff analysis
        return []
    
    def get_all_wiki_files(self) -> List[Path]:
        """
        📂 Get all markdown files from wiki directory
        """
        if not self.wiki_dir.exists():
            return []
        
        return list(self.wiki_dir.glob("*.md"))
    
    def extract_features_from_content(self, content: str) -> List[str]:
        """
        ⭐ Extract feature bullets and lists from markdown
        """
        features = []
        
        # Extract bullet points
        bullet_pattern = r'^[\s]*[-*+]\s+(.+)$'
        bullets = re.findall(bullet_pattern, content, re.MULTILINE)
        features.extend([bullet.strip() for bullet in bullets if len(bullet.strip()) > 5])
        
        # Extract numbered lists
        numbered_pattern = r'^[\s]*\d+\.\s+(.+)$'
        numbered = re.findall(numbered_pattern, content, re.MULTILINE)
        features.extend([item.strip() for item in numbered if len(item.strip()) > 5])
        
        # Extract features from headings (likely features if they're action-oriented)
        headings = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
        for heading in headings:
            if any(word in heading.lower() for word in ['invite', 'remove', 'change', 'edit', 'manage', 'create']):
                features.append(heading.strip())
        
        # Remove duplicates while preserving order
        seen = set()
        unique_features = []
        for feature in features:
            if feature.lower() not in seen:
                seen.add(feature.lower())
                unique_features.append(feature)
        
        return unique_features[:10]  # Limit to top 10 features
    
    def calculate_content_metrics(self, content: str) -> Dict:
        """
        📈 Calculate engagement metrics for content
        """
        words = content.split()
        lines = content.split('\n')
        
        # Calculate complexity based on various factors
        complexity_factors = {
            "technical_terms": sum(1 for word in words if word.lower() in 
                                 ['api', 'authentication', 'permission', 'validation', 'migration', 'database']),
            "code_blocks": len(re.findall(r'```[\s\S]*?```', content)),
            "bullet_points": len(re.findall(r'^[\s]*[-*+]\s+', content, re.MULTILINE)),
            "headings": len(re.findall(r'^#{1,6}\s+', content, re.MULTILINE)),
            "tables": len([line for line in lines if '|' in line and line.strip()])
        }
        
        complexity_score = min(100, sum(complexity_factors.values()) * 5)
        
        # Calculate engagement potential
        engagement_indicators = {
            "action_words": sum(1 for word in words if word.lower() in 
                              ['create', 'build', 'implement', 'manage', 'invite', 'configure']),
            "has_examples": '```' in content,
            "has_lists": any(line.strip().startswith(('-', '*', '+')) for line in lines),
            "good_length": 100 < len(words) < 1000
        }
        
        engagement_score = sum(engagement_indicators.values()) * 25
        
        # Determine engagement level
        if engagement_score >= 75:
            engagement_level = "MAXIMUM MONDAY MADNESS! 🚀🔥"
        elif engagement_score >= 50:
            engagement_level = "HIGH ENERGY! ⚡"
        elif engagement_score >= 25:
            engagement_level = "SOLID! 💪"
        else:
            engagement_level = "Building up... 📈"
        
        return {
            "word_count": len(words),
            "line_count": len(lines),
            "character_count": len(content),
            "complexity_score": complexity_score,
            "engagement_score": engagement_score,
            "feature_count": len(self.extract_features_from_content(content)),
            "table_count": complexity_factors["tables"],
            "code_blocks": complexity_factors["code_blocks"],
            "headings": complexity_factors["headings"],
            "estimated_read_time": max(1, len(words) // 200),  # Assume 200 words per minute
            "engagement_potential": engagement_level,
            "complexity_factors": complexity_factors,
            "monday_madness_approved": engagement_score > 50
        }
    
    # Helper methods for WikiParser
    
    def _extract_title(self, content: str, filename: str) -> str:
        """
        🏷️ Extract title from content or generate from filename
        """
        # Try to find first heading
        heading_match = re.search(r'^#{1,3}\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            return heading_match.group(1).strip()
        
        # Fallback to filename without extension, formatted nicely
        title = filename.replace('.md', '').replace('-', ' ').replace('_', ' ')
        return ' '.join(word.capitalize() for word in title.split())
    
    def _determine_card_type(self, title: str, content: str) -> str:
        """
        🎯 Determine the type of card based on content analysis
        """
        title_lower = title.lower()
        content_lower = content.lower()
        
        if "permission" in title_lower and "|" in content:
            return "permissions_matrix"
        elif "account" in title_lower and "management" in title_lower:
            return "account_management"
        elif "user" in title_lower:
            return "user_system"
        elif title_lower == "home":
            return "welcome"
        elif "api" in content_lower or "endpoint" in content_lower:
            return "api_documentation"
        else:
            return "general_documentation"
    
    def get_all_wiki_files(self):
        """
        📁 Get all markdown files in the wiki directory
        """
        if not self.wiki_dir.exists():
            return []
        
        return list(self.wiki_dir.glob("*.md")) 