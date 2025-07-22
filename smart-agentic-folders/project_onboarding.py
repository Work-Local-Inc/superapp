#!/usr/bin/env python3
"""
🧠 Smart Agentic Project Folders™ - Onboarding Questionnaire
Generates custom project structure based on user answers
"""

import os
import json
from datetime import datetime
from pathlib import Path

class ProjectOnboarding:
    def __init__(self):
        self.answers = {}
        self.project_type_configs = {
            "software": {
                "dashboard_theme": "tech",
                "ai_personality": "technical_advisor",
                "focus_areas": ["code_quality", "performance", "scalability"],
                "default_phases": ["planning", "development", "testing", "deployment"]
            },
            "research": {
                "dashboard_theme": "research",
                "ai_personality": "data_analyst", 
                "focus_areas": ["literature_review", "hypothesis", "analysis", "publication"],
                "default_phases": ["research", "analysis", "documentation", "presentation"]
            },
            "business": {
                "dashboard_theme": "enterprise",
                "ai_personality": "startup_mentor",
                "focus_areas": ["market_analysis", "revenue", "growth", "optimization"],
                "default_phases": ["planning", "mvp", "launch", "scale"]
            },
            "creative": {
                "dashboard_theme": "creative",
                "ai_personality": "team_coach",
                "focus_areas": ["ideation", "creation", "feedback", "iteration"],
                "default_phases": ["concept", "creation", "review", "delivery"]
            },
            "consulting": {
                "dashboard_theme": "consulting",
                "ai_personality": "project_manager",
                "focus_areas": ["client_needs", "deliverables", "timeline", "satisfaction"],
                "default_phases": ["discovery", "proposal", "execution", "delivery"]
            }
        }

    def welcome(self):
        print("🧠 Welcome to Smart Agentic Project Folders™!")
        print("=" * 50)
        print("Let's create your custom AI-powered project command center!")
        print("This will take about 5 minutes and generate your entire project structure.\n")

    def ask_question(self, question, options=None, required=True):
        """Ask a question and get user input"""
        while True:
            if options:
                print(f"\n{question}")
                for i, option in enumerate(options, 1):
                    print(f"  {i}. {option}")
                try:
                    choice = int(input("Enter number: ")) - 1
                    if 0 <= choice < len(options):
                        return options[choice]
                    print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                answer = input(f"\n{question}: ").strip()
                if answer or not required:
                    return answer
                print("This field is required. Please provide an answer.")

    def run_questionnaire(self):
        """Run the complete onboarding questionnaire"""
        
        print("\n📋 PROJECT BASICS")
        print("-" * 30)
        
        self.answers["project_name"] = self.ask_question("What's your project called?")
        
        project_types = ["Software Development", "Research Project", "Business/Startup", 
                        "Creative Project", "Consulting Work", "Other"]
        self.answers["project_type"] = self.ask_question("What type of project is this?", project_types)
        
        timelines = ["1-2 weeks", "1 month", "3 months", "6 months", "1 year", "Ongoing"]
        self.answers["timeline"] = self.ask_question("What's your target timeline?", timelines)
        
        team_sizes = ["Just me", "2-3 people", "4-6 people", "7-10 people", "10+ people"]
        self.answers["team_size"] = self.ask_question("How big is your team?", team_sizes)

        print("\n🛠️ TECHNICAL STACK")
        print("-" * 30)
        
        technologies = ["Python", "JavaScript/Node.js", "Laravel/PHP", "React/Frontend", 
                       "Data Science/ML", "Mobile App", "WordPress", "Other"]
        self.answers["primary_tech"] = self.ask_question("Primary technology/platform?", technologies)
        
        infrastructure = ["Local Development", "Google Cloud", "AWS", "Heroku", "Vercel", 
                         "Self-hosted", "Not Sure Yet"]
        self.answers["infrastructure"] = self.ask_question("Infrastructure preference?", infrastructure)
        
        ai_providers = ["OpenAI (ChatGPT)", "Anthropic (Claude)", "Google (Gemini)", 
                       "Multiple Providers", "Not Using AI", "Undecided"]
        self.answers["ai_integration"] = self.ask_question("AI integration plans?", ai_providers)

        print("\n🎯 PROJECT GOALS")
        print("-" * 30)
        
        self.answers["primary_objective"] = self.ask_question("What's your main goal/objective?")
        
        success_metrics = ["Revenue/Sales", "User Adoption", "Technical Performance", 
                          "Research Publications", "Client Satisfaction", "Personal Learning"]
        self.answers["success_metrics"] = self.ask_question("How will you measure success?", success_metrics)
        
        self.answers["revenue_model"] = self.ask_question("Revenue model (if applicable)", required=False)

        print("\n👥 TEAM & COLLABORATION")
        print("-" * 30)
        
        self.answers["team_members"] = self.ask_question("Team member names and roles", required=False)
        
        communication = ["Slack", "Discord", "Microsoft Teams", "Email", "In-Person", "Mixed"]
        self.answers["communication"] = self.ask_question("Primary communication method?", communication)
        
        environments = ["Highly Collaborative", "Balanced", "Independent Work", "Structured/Formal"]
        self.answers["work_environment"] = self.ask_question("Preferred work environment?", environments)

        print("\n🎨 PREFERENCES & STYLE")
        print("-" * 30)
        
        org_styles = ["ADHD-Friendly (Visual, Quick)", "Detailed & Comprehensive", 
                     "Minimal & Clean", "Data-Heavy Analytics"]
        self.answers["organization_style"] = self.ask_question("Organization style preference?", org_styles)
        
        update_frequencies = ["Daily Check-ins", "Weekly Reviews", "Bi-weekly", "Monthly", "As Needed"]
        self.answers["update_frequency"] = self.ask_question("How often do you want progress updates?", update_frequencies)
        
        self.answers["biggest_challenge"] = self.ask_question("What's your biggest expected challenge?")
        
        print("\n✅ Questionnaire Complete!")
        return self.answers

    def generate_project_context(self):
        """Generate PROJECT_CONTEXT.md based on answers"""
        
        project_type_key = self.answers["project_type"].lower().split()[0]
        config = self.project_type_configs.get(project_type_key, self.project_type_configs["software"])
        
        context = f"""# 🚀 {self.answers['project_name'].upper()} - Project Context & Memory Bank

## 🎯 THE BIG PICTURE
- **What**: {self.answers['primary_objective']}
- **Type**: {self.answers['project_type']}
- **Timeline**: {self.answers['timeline']}
- **Team**: {self.answers['team_size']}
- **Success Metric**: {self.answers['success_metrics']}

## 🏗️ CORE ARCHITECTURE
### Tech Stack
- **Primary Technology**: {self.answers['primary_tech']}
- **Infrastructure**: {self.answers['infrastructure']}
- **AI Integration**: {self.answers['ai_integration']}
- **Communication**: {self.answers['communication']}

### Team Structure
{self.answers.get('team_members', 'Team details to be defined')}

## 💰 REVENUE MODEL
{self.answers.get('revenue_model', 'Revenue model to be determined')}

## 🎯 CURRENT STATUS
- ✅ Project initialized with Smart Agentic Folder structure
- ✅ Onboarding questionnaire completed
- 🔄 Ready for development kickoff
- ❌ Dashboard customization pending

## 🚨 KEY FOCUS AREAS
- **Biggest Challenge**: {self.answers['biggest_challenge']}
- **Organization Style**: {self.answers['organization_style']}
- **Update Frequency**: {self.answers['update_frequency']}
- **Work Environment**: {self.answers['work_environment']}

## 🔄 NEXT IMMEDIATE STEPS
1. Launch project dashboard: `streamlit run project_dashboard.py`
2. Set up AI assistant with API keys
3. Define initial project phases and milestones
4. Configure team collaboration tools
5. Begin primary development work

---
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Project Type**: {self.answers['project_type']}
**System**: Smart Agentic Project Folders™ v1.0
"""
        
        with open("PROJECT_CONTEXT.md", "w") as f:
            f.write(context)
        
        print(f"✅ Generated PROJECT_CONTEXT.md")

    def generate_dashboard(self):
        """Generate customized dashboard based on project type"""
        
        # Get the path to Smart Agentic Folders templates
        script_dir = Path(__file__).parent
        template_path = script_dir / "template_dashboard.py"
        
        if template_path.exists():
            with open(template_path, "r") as f:
                dashboard_content = f.read()
            
            # Customize for this project
            dashboard_content = dashboard_content.replace(
                "SuperApp Command Center", 
                f"{self.answers['project_name']} Command Center"
            )
            dashboard_content = dashboard_content.replace(
                "superapp", 
                self.answers['project_name'].lower().replace(" ", "_")
            )
            
            with open("project_dashboard.py", "w") as f:
                f.write(dashboard_content)
            
            print(f"✅ Generated project_dashboard.py")
        else:
            print("⚠️  Template dashboard not found - using basic template")

    def generate_requirements(self):
        """Generate requirements.txt based on tech stack"""
        
        base_requirements = [
            "streamlit>=1.47.0",
            "plotly>=5.17.0", 
            "pandas>=2.0.0",
            "muscle-mem>=0.1.0",
            "python-dotenv>=1.0.0",
            "requests>=2.31.0",
            "psutil>=5.9.0",
            "gitpython>=3.1.0"
        ]
        
        # Add AI provider dependencies
        if "OpenAI" in self.answers.get("ai_integration", ""):
            base_requirements.append("openai>=1.0.0")
        if "Anthropic" in self.answers.get("ai_integration", ""):
            base_requirements.append("anthropic>=0.8.0")
        if "Google" in self.answers.get("ai_integration", ""):
            base_requirements.append("google-generativeai>=0.3.0")
        
        # Add tech-specific requirements
        if "Laravel" in self.answers.get("primary_tech", ""):
            base_requirements.extend(["requests", "python-decouple"])
        if "Data Science" in self.answers.get("primary_tech", ""):
            base_requirements.extend(["numpy", "scipy", "scikit-learn", "jupyter"])
        if "WordPress" in self.answers.get("primary_tech", ""):
            base_requirements.extend(["wordpress-xmlrpc", "beautifulsoup4"])
        
        with open("requirements.txt", "w") as f:
            f.write("# " + self.answers['project_name'] + " Dependencies\n")
            f.write("# Generated by Smart Agentic Project Folders™\n\n")
            for req in base_requirements:
                f.write(req + "\n")
        
        print(f"✅ Generated requirements.txt")

    def generate_muscle_memory(self):
        """Generate customized muscle memory system"""
        
        script_dir = Path(__file__).parent
        template_path = script_dir / "template_muscle_memory.py"
        
        if template_path.exists():
            with open(template_path, "r") as f:
                muscle_content = f.read()
            
            # Customize for this project
            muscle_content = muscle_content.replace(
                "SuperApp", 
                self.answers['project_name']
            )
            muscle_content = muscle_content.replace(
                "superapp", 
                self.answers['project_name'].lower().replace(" ", "_")
            )
            
            with open("project_muscle_memory.py", "w") as f:
                f.write(muscle_content)
            
            print(f"✅ Generated project_muscle_memory.py")
        else:
            print("⚠️  Template muscle memory not found")

    def save_config(self):
        """Save configuration for future reference"""
        config = {
            "answers": self.answers,
            "generated_at": datetime.now().isoformat(),
            "version": "1.0"
        }
        
        with open(".project_config.json", "w") as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Saved project configuration")

    def generate_readme(self):
        """Generate project README with quick start instructions"""
        
        readme = f"""# 🚀 {self.answers['project_name']}

> **{self.answers['primary_objective']}**

## 🎯 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Launch command center
streamlit run project_dashboard.py
```

## 📊 Project Details

- **Type**: {self.answers['project_type']}
- **Timeline**: {self.answers['timeline']}
- **Team**: {self.answers['team_size']}
- **Tech Stack**: {self.answers['primary_tech']}

## 🤖 AI-Powered Features

- **Real-time Dashboard** - Project progress and team collaboration
- **AI Assistant** - Context-aware project guidance
- **Muscle Memory** - Workflow optimization and pattern learning
- **Visual Roadmap** - Phase tracking and milestone management

## 🔧 Configuration

This project uses **Smart Agentic Project Folders™** for AI-powered organization.

- Dashboard: `streamlit run project_dashboard.py`
- Context: See `PROJECT_CONTEXT.md`
- Config: `.project_config.json`

## 🎨 Customization

Generated for: **{self.answers['organization_style']}** style
Update frequency: **{self.answers['update_frequency']}**

---

*Powered by Smart Agentic Project Folders™*
"""
        
        with open("README.md", "w") as f:
            f.write(readme)
        
        print(f"✅ Generated README.md")

    def finalize(self):
        """Final setup and instructions"""
        print("\n🎉 PROJECT SETUP COMPLETE!")
        print("=" * 50)
        print(f"Your '{self.answers['project_name']}' Smart Agentic Project Folder is ready!")
        print("\n🚀 Next Steps:")
        print("1. Run: pip install -r requirements.txt")
        print("2. Launch: streamlit run project_dashboard.py")
        print("3. Configure AI: Add API keys to Streamlit secrets")
        print("4. Share with team: Send them the dashboard URL")
        print("\n💡 Pro Tip: Check PROJECT_CONTEXT.md for your complete project overview!")

def main():
    """Main onboarding flow"""
    onboarding = ProjectOnboarding()
    
    onboarding.welcome()
    answers = onboarding.run_questionnaire()
    
    print("\n🔧 Generating your Smart Agentic Project structure...")
    onboarding.generate_project_context()
    onboarding.generate_dashboard()
    onboarding.generate_muscle_memory()
    onboarding.generate_requirements()
    onboarding.generate_readme()
    onboarding.save_config()
    
    onboarding.finalize()

if __name__ == "__main__":
    main() 