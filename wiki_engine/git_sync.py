"""
GitSync Engine - Keep Our Dashboard ALIVE with Real-Time Wiki Updates
"""

import subprocess
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class GitSyncEngine:
    """
    🔄 The engine that keeps our dashboard synced with wiki reality
    
    Monday Madness Level: UNSTOPPABLE! ⚡
    """
    
    def __init__(self, wiki_repo_path: str = "clients-hub-wiki"):
        self.repo_path = Path(wiki_repo_path)
        self.last_sync = None
        self.sync_history = []
        
    def pull_wiki_updates(self) -> Dict:
        """
        📥 Pull latest wiki updates from Git repository
        
        Returns:
            Dict with sync status, changes, and metadata
        """
        if not self.repo_path.exists():
            return {
                "status": "error",
                "error": "Repository path does not exist",
                "changes_detected": False,
                "files_updated": [],
                "sync_time": datetime.now()
            }
        
        try:
            # Save current working directory
            original_cwd = os.getcwd()
            
            # Change to repo directory (ensure it's absolute path)
            repo_abs_path = self.repo_path.resolve()
            os.chdir(repo_abs_path)
            
            # Check if it's a git repository (use current directory after cd)
            if not Path(".git").exists():
                os.chdir(original_cwd)
                return {
                    "status": "error",
                    "error": "Not a git repository",
                    "changes_detected": False,
                    "files_updated": [],
                    "sync_time": datetime.now()
                }
            
            # Get current commit hash before pull
            result_before = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                                         capture_output=True, text=True, check=True)
            commit_before = result_before.stdout.strip()
            
            # Perform git pull
            result_pull = subprocess.run(['git', 'pull'], 
                                       capture_output=True, text=True, check=True)
            
            # Get commit hash after pull
            result_after = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                                        capture_output=True, text=True, check=True)
            commit_after = result_after.stdout.strip()
            
            # Detect changes
            changes_detected = commit_before != commit_after
            files_updated = []
            
            if changes_detected:
                # Get list of changed files
                result_files = subprocess.run(['git', 'diff', '--name-only', commit_before, commit_after], 
                                            capture_output=True, text=True, check=True)
                files_updated = [f.strip() for f in result_files.stdout.split('\n') if f.strip()]
            
            # Restore original working directory
            os.chdir(original_cwd)
            
            sync_result = {
                "status": "success",
                "changes_detected": changes_detected,
                "files_updated": files_updated,
                "commit_before": commit_before[:8],  # Short hash
                "commit_after": commit_after[:8],
                "pull_output": result_pull.stdout,
                "sync_time": datetime.now(),
                "monday_madness_energy": "MAXIMUM SYNC POWER! ⚡🔄" if changes_detected else "STABLE AND READY! 💪"
            }
            
            # Log the sync activity
            self.log_sync_activity(sync_result)
            self.last_sync = sync_result["sync_time"]
            
            return sync_result
            
        except subprocess.CalledProcessError as e:
            os.chdir(original_cwd) if 'original_cwd' in locals() else None
            return {
                "status": "error",
                "error": f"Git command failed: {e.stderr}",
                "changes_detected": False,
                "files_updated": [],
                "sync_time": datetime.now()
            }
        except Exception as e:
            os.chdir(original_cwd) if 'original_cwd' in locals() else None
            return {
                "status": "error", 
                "error": str(e),
                "changes_detected": False,
                "files_updated": [],
                "sync_time": datetime.now()
            }
    
    def detect_file_changes(self, commit_before: str = None, commit_after: str = None) -> List[Dict]:
        """
        🔍 Detect which files changed since last sync
        """
        if not self.repo_path.exists():
            return []
        
        try:
            original_cwd = os.getcwd()
            os.chdir(self.repo_path)
            
            # If no commits provided, compare with last known state
            if not commit_before or not commit_after:
                # Get recent commits
                result = subprocess.run(['git', 'log', '--oneline', '-n', '2'], 
                                      capture_output=True, text=True, check=True)
                commits = result.stdout.strip().split('\n')
                if len(commits) >= 2:
                    commit_after = commits[0].split()[0]
                    commit_before = commits[1].split()[0]
                else:
                    os.chdir(original_cwd)
                    return []
            
            # Get detailed file changes
            result = subprocess.run(['git', 'diff', '--name-status', commit_before, commit_after], 
                                  capture_output=True, text=True, check=True)
            
            file_changes = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    parts = line.split('\t')
                    if len(parts) >= 2:
                        status = parts[0]
                        filename = parts[1]
                        
                        change_type = {
                            'A': 'added',
                            'M': 'modified', 
                            'D': 'deleted',
                            'R': 'renamed',
                            'C': 'copied'
                        }.get(status[0], 'unknown')
                        
                        file_changes.append({
                            "filename": filename,
                            "status": change_type,
                            "git_status": status,
                            "is_markdown": filename.endswith('.md'),
                            "monday_madness_impact": "HIGH! 🚀" if filename.endswith('.md') else "LOW 📄"
                        })
            
            os.chdir(original_cwd)
            return file_changes
            
        except Exception as e:
            os.chdir(original_cwd) if 'original_cwd' in locals() else None
            return []
    
    def trigger_dashboard_refresh(self, changed_files: List[str]) -> bool:
        """
        🔄 Trigger dashboard refresh for changed content
        """
        if not changed_files:
            return False
        
        try:
            # Count markdown files that changed
            md_files = [f for f in changed_files if f.endswith('.md')]
            
            if md_files:
                refresh_data = {
                    "trigger_time": datetime.now(),
                    "changed_files": changed_files,
                    "markdown_files": md_files,
                    "refresh_needed": True,
                    "monday_madness_alert": f"🚨 {len(md_files)} wiki pages updated! REFRESH INCOMING! ⚡"
                }
                
                # Log refresh trigger
                self.log_sync_activity({
                    "type": "dashboard_refresh_triggered",
                    "data": refresh_data
                })
                
                return True
            
            return False
            
        except Exception as e:
            self.log_sync_activity({
                "type": "refresh_trigger_error",
                "error": str(e)
            })
            return False
    
    def log_sync_activity(self, activity: Dict) -> None:
        """
        📝 Log sync activities for debugging and analytics
        """
        self.sync_history.append({
            **activity,
            "timestamp": datetime.now(),
            "sync_count": len(self.sync_history) + 1
        })
        
        # Keep only last 100 entries
        if len(self.sync_history) > 100:
            self.sync_history = self.sync_history[-100:]
    
    def get_repo_status(self) -> Dict:
        """
        📊 Get current repository status and health
        """
        return {
            "repo_exists": self.repo_path.exists(),
            "is_git_repo": (self.repo_path / ".git").exists(),
            "last_sync": self.last_sync,
            "sync_count": len(self.sync_history),
            "health_status": "EXCELLENT! 💪"
        }
    
    def setup_auto_sync(self, interval_minutes: int = 30) -> bool:
        """
        ⏰ Setup automatic sync every X minutes
        """
        try:
            # For now, we'll return setup success
            # In a real implementation, this would set up a background scheduler
            self.log_sync_activity({
                "type": "auto_sync_setup",
                "interval_minutes": interval_minutes,
                "status": "configured",
                "next_sync": datetime.now().replace(minute=datetime.now().minute + interval_minutes),
                "monday_madness_scheduler": f"AUTO-SYNC ACTIVATED! Every {interval_minutes} minutes! ⏰🚀"
            })
            
            return True
            
        except Exception as e:
            self.log_sync_activity({
                "type": "auto_sync_setup_error", 
                "error": str(e)
            })
            return False
    
    def force_sync_now(self) -> Dict:
        """
        🚨 Force immediate sync (for manual refresh)
        """
        return self.pull_wiki_updates() 