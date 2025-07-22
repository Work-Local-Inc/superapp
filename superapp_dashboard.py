#!/usr/bin/env python3
"""
🚀 SuperApp Command Center Dashboard
AI-powered project management and team coordination
NO DRAMA - Just pure collaboration and progress tracking!
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import os
from pathlib import Path
import time

import sys

# AI Integration - Dynamic imports for Streamlit Cloud
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
    print("✅ Anthropic imported successfully")
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("🔧 Anthropic not available - using fallback responses")

try:
    import openai  
    OPENAI_AVAILABLE = True
    print("✅ OpenAI imported successfully")
except ImportError:
    OPENAI_AVAILABLE = False
    print("🔧 OpenAI not available - using fallback responses")

# Muscle Memory available for development workflows (not dashboard UI)

# Configure the page
st.set_page_config(
    page_title="SuperApp Command Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

    # Enhanced CSS for better UI/UX and mobile responsiveness
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        .stColumns > div {
            margin-bottom: 1rem;
        }
    }
    .metric-card {
        background-color: #F0F2F6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #FF6B6B;
        margin-bottom: 1rem;
    }
    .achievement-badge {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 15px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
    }

    .nav-section {
        background-color: #F8F9FA;
        padding: 0.5rem;
        border-radius: 0.3rem;
        margin: 0.5rem 0;
    }
    .quick-action-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        margin: 0.5rem 0;
    }
    .section-divider {
        border-top: 2px solid #E1E5E9;
        margin: 2rem 0 1rem 0;
    }
    /* Better spacing and readability */
    .stMetric {
        background-color: #FFFFFF;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #E1E5E9;
    }
    /* Sidebar improvements */
    .css-1d391kg {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def load_project_data():
    """Load current project data from files and git"""
    data = {
        "current_phase": "initialization",
        "active_vertical": "food",
        "team_members": ["James Walker", "Nick Denysov", "Pavel", "Brian"],
        "completed_features": [
            "Dashboard creation and deployment",
            "Role system architecture design", 
            "Project documentation",
            "AI assistant integration",
            "Muscle Memory setup"
        ],
        "active_todos": [
            "Laravel backend initialization",
            "Food vertical API development",
            "Database schema implementation",
            "Payment integration planning",
            "Role permissions coding"
        ],
        "role_progress": {
            "food": 85,
            "spa": 20,
            "gym": 10,
            "trade": 5
        }
    }
    
    # Try to load real data
    
    # Load TODOs if available
    todos_file = Path("todos.json")
    if todos_file.exists():
        try:
            with open(todos_file, 'r') as f:
                todo_data = json.load(f)
                data["active_todos"] = [t["content"] for t in todo_data.get("todos", []) 
                                      if t["status"] != "completed"]
                data["completed_features"] = [t["content"] for t in todo_data.get("todos", []) 
                                             if t["status"] == "completed"]
        except:
            pass
    
    return data

def render_sidebar():
    """Render the navigation sidebar"""
    st.sidebar.markdown("# SuperApp Command")
    
    # Navigation first - most important
    st.sidebar.markdown("### **NAVIGATION**")
    all_pages = {
        "Project Overview": "overview",
        "Project Roadmap": "roadmap", 
        "AI Assistant": "ai_assistant",
        "Role System": "roles",
        "Business Verticals": "verticals",
        "Performance": "optimization"
    }
    
    # Simple, clear navigation - no confusing separators
    page_options = list(all_pages.keys())
    
    # Check if a page was selected via button (session state)
    if "selected_page" in st.session_state:
        selected_page = st.session_state.selected_page
        # Find the display name for this page
        selected_display = None
        for display, page_value in all_pages.items():
            if page_value == selected_page:
                selected_display = display
                break
        if selected_display is None:
            selected_display = "Project Overview"
    else:
        selected_display = "Project Overview"
    
    # Use radio buttons instead of dropdown for better UX
    selected_display = st.sidebar.radio("", page_options, 
                                       index=page_options.index(selected_display) if selected_display in page_options else 0)
    
    selected_page = all_pages.get(selected_display, "overview")
    
    # Update session state to match selectbox
    st.session_state.selected_page = selected_page
    
    # Quick Status section - after navigation
    data = load_project_data()
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Quick Status")
    st.sidebar.success(f"Phase: {data['current_phase'].title()}")
    st.sidebar.info(f"Focus: {data['active_vertical'].title()} Vertical")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Quick Stats")
    st.sidebar.metric("Active TODOs", len(data["active_todos"]))
    st.sidebar.metric("Completed Features", len(data["completed_features"]))
    
    return selected_page

def render_overview_page():
    """Render the main project overview page"""
    st.markdown('<h1 class="main-header">SuperApp Command Center</h1>', unsafe_allow_html=True)
    
    # Quick navigation cards at the top
    st.markdown("### Quick Access")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("View Full Roadmap", use_container_width=True):
            st.session_state.selected_page = "roadmap"
            st.rerun()
    
    with col2:
        if st.button("Ask AI Assistant", use_container_width=True):
            st.session_state.selected_page = "ai_assistant"
            st.rerun()
    
    with col3:
        if st.button("Check Progress", use_container_width=True):
            st.session_state.selected_page = "verticals"
            st.rerun()
    
    st.markdown("---")
    
    data = load_project_data()
    
    # Main metrics row - with better visual hierarchy
    st.markdown("### Project Status")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Phase", data["current_phase"].title(), "Active")
    
    with col2:
        st.metric("Active Vertical", data["active_vertical"].title(), "Focus")
    
    with col3:
        st.metric("Team Members", len(data["team_members"]), "Collaborating")
    
    # Progress visualization with better layout
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Tabbed interface for better organization
    tab1, tab2, tab3 = st.tabs(["Progress", "Achievements", "Current Work"])
    
    with tab1:
        st.markdown("#### Business Vertical Progress")
        
        # Create progress chart with better styling
        verticals = list(data["role_progress"].keys())
        progress = list(data["role_progress"].values())
        
        fig = go.Figure(data=[
            go.Bar(x=verticals, y=progress, 
                  marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],
                  text=[f"{p}%" for p in progress],
                  textposition='auto')
        ])
        
        fig.update_layout(
            title="Business Vertical Implementation",
            yaxis_title="Completion %",
            xaxis_title="Business Type",
            showlegend=False,
            height=400,
            margin=dict(t=50, b=50, l=50, r=50)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("#### Team Achievements")
        
        # Team achievements
        achievements = [
            "Role System Architecture Complete",
            "Comprehensive Documentation Created", 
            "Muscle Memory Integration Active",
            "Git Repository Successfully Initialized",
            "Development Framework Established",
            "Project Roadmap Visualization Added"
        ]
        
        # Display in a more organized way
        for i, achievement in enumerate(achievements):
            if i % 2 == 0:
                col1, col2 = st.columns(2)
                with col1:
                    st.success(f"• {achievement}")
            else:
                with col2:
                    st.success(f"• {achievement}")
    
    with tab3:
        st.markdown("#### Current Focus Areas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Completed Features**")
            completed = data["completed_features"] or ["Dashboard creation", "Role system design", "Project planning"]
            for feature in completed:
                st.success(f"• {feature}")
        
        with col2:
            st.markdown("**Active TODOs**") 
            active = data["active_todos"] or ["Laravel backend implementation", "Food vertical development", "API endpoint creation"]
            for todo in active:
                st.info(f"• {todo}")
    
    # Clean end of overview page

def render_ai_assistant_page():
    """Render the AI assistant page"""
    st.markdown("# SuperApp AI Assistant")
    
    # Check AI availability (silent)
    anthropic_key = os.getenv("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY", "")
    openai_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
    
    # Quick Questions at the top
    st.markdown("### Quick Questions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Status Report", use_container_width=True):
            report = generate_status_report()
            st.text_area("Status Report", report, height=200)
    
    with col2:
        if st.button("Next Tasks", use_container_width=True):
            tasks = suggest_next_tasks()
            st.markdown("#### Suggested Next Tasks:")
            for task in tasks:
                st.info(f"• {task}")
    
    with col3:
        if st.button("Find Issues", use_container_width=True):
            opportunities = identify_optimizations()
            st.markdown("#### Optimization Opportunities:")
            for opp in opportunities:
                st.warning(f"• {opp}")
    
    # Chat interface
    st.markdown("---")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm your SuperApp AI assistant. I know everything about your project - roles, architecture, progress, and goals. How can I help the team today?"}
        ]
    
    # Display chat messages in a container
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about the project, team, progress, or get recommendations..."):
        # Add user message to session
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Generate and add AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_ai_response(prompt)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to show the new messages in the chat history
        st.rerun()
    
    # Clean end of chat interface

def get_project_context():
    """Get comprehensive project context for AI"""
    data = load_project_data()
    
    # Read key project files for context
    context_parts = []
    
    # Project overview
    context_parts.append(f"""
SUPERAPP PROJECT OVERVIEW:
- Current Phase: {data['current_phase']}
- Active Vertical: {data['active_vertical']} 
- Team: {', '.join(data['team_members'])}
- Active TODOs: {len(data['active_todos'])}
- Completed Features: {len(data['completed_features'])}
""")
    
    # Try to read context files
    try:
        if Path("SUPERAPP_CONTEXT.md").exists():
            with open("SUPERAPP_CONTEXT.md", 'r') as f:
                context_parts.append(f"PROJECT CONTEXT:\n{f.read()[:2000]}")
    except:
        pass
    
    try:
        if Path("user_roles_plan.md").exists():
            with open("user_roles_plan.md", 'r') as f:
                context_parts.append(f"ROLE SYSTEM:\n{f.read()[:2000]}")
    except:
        pass
    
    return "\n\n".join(context_parts)

def generate_ai_response(prompt):
    """Generate AI response using real LLM"""
    
    # Get API keys from environment or Streamlit secrets
    anthropic_key = os.getenv("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY", "")
    openai_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
    
    project_context = get_project_context()
    
    system_prompt = f"""You are the SuperApp AI Assistant, an expert on this specific project. You have complete context about:

{project_context}

GUIDELINES:
- Be helpful, specific, and actionable
- Reference actual project details when relevant
- Support the ENTIRE team's success (no individual competition)
- Suggest concrete next steps when appropriate
- Use emojis and formatting to be engaging
- Keep responses concise but informative
- Be helpful and actionable for the team"""

    # Try Anthropic Claude first
    if ANTHROPIC_AVAILABLE and anthropic_key:
        try:
            client = anthropic.Anthropic(api_key=anthropic_key)
            
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=500,
                system=system_prompt,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text
            
        except Exception as e:
            st.error(f"Claude API error: {str(e)[:100]}")
    
    # Try OpenAI as fallback
    if OPENAI_AVAILABLE and openai_key:
        try:
            client = openai.OpenAI(api_key=openai_key)
            
            response = client.chat.completions.create(
                model="gpt-4",
                max_tokens=500,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            st.error(f"OpenAI API error: {str(e)[:100]}")
    
    # Fallback to simulated responses
    return generate_fallback_response(prompt)

def generate_fallback_response(prompt):
    """Fallback responses when no AI available"""
    prompt_lower = prompt.lower()
    
    if "status" in prompt_lower or "progress" in prompt_lower:
        return """**Project Status Update**:

**Current Phase**: Initialization → MVP transition  
**Progress**: Role system architecture complete, dashboard deployed  
**Next Priority**: Laravel backend implementation

**Team Focus**:
- Nick/Pavel: Backend development with role system
- Brian: Optimization and performance tracking  
- James: Project coordination and stakeholder updates

The team is making excellent collaborative progress!"""
    
    elif "nick" in prompt_lower or "backend" in prompt_lower:
        return """🛠️ **Backend Development Guidance**:

**Priority Tasks for Nick/Pavel**:
1. Implement Laravel role system using our permissions matrix
2. Set up Account/Business/User entity relationships
3. Create API endpoints for food vertical
4. Database schema for multi-tenant architecture

**Suggestion**: Start with Phase 1 roles (Owner, Admin, Manager, Staff) and build incrementally! 💪"""
    
    elif "ai" in prompt_lower or "chat" in prompt_lower:
        return """🤖 **AI Assistant Setup**:

To activate full AI capabilities:
1. Set up API keys in Streamlit secrets or environment variables
2. Add `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`
3. Restart the dashboard

**Currently running in basic mode** with project-aware fallback responses! 🚀"""
    
    else:
        return f"""💡 **SuperApp AI Assistant**:

I can help with:
- Project status and progress updates
- Team task recommendations  
- Architecture and technical questions
- Role system implementation guidance
- Optimization opportunities

**Pro tip**: For full AI capabilities, configure API keys in the dashboard settings!

Ask me anything about the SuperApp project! 🎯"""

def generate_status_report():
    """Generate a status report"""
    data = load_project_data()
    
    report = f"""SuperApp Development Status Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

OVERVIEW:
- Phase: {data['current_phase'].title()}
- Active Vertical: {data['active_vertical'].title()}
- Team Members: {len(data['team_members'])}

PROGRESS:
- Food Vertical: 85% complete
- Role System: Architecture complete, implementation in progress
- Muscle Memory: Successfully integrated
- Documentation: Comprehensive and up-to-date

NEXT PRIORITIES:
1. Laravel backend implementation (Nick/Pavel)
2. API endpoint development for food vertical
3. Role system database implementation
4. Payment integration planning

TEAM STATUS:
All team members actively contributing with clear responsibilities."""
    
    return report

def suggest_next_tasks():
    """Suggest next tasks for the team"""
    return [
        "Implement Laravel role system database schema",
        "Create API endpoints for food vertical",
        "Set up development environment for backend team",
        "Begin food service order processing workflow",
        "Plan spa vertical role specializations",
        "Update Muscle Memory with backend patterns"
    ]

def identify_optimizations():
    """Identify optimization opportunities"""
    return [
        "Cache frequently used role permission checks",
        "Optimize database queries for multi-tenant architecture", 
        "Implement automated testing for role system",
        "Set up CI/CD pipeline for faster deployments",
        "Create reusable components for business verticals",
        "Establish coding standards for team consistency"
    ]

def render_role_tracker_page():
    """Render the role system tracking page"""
    st.markdown("# Role System Tracker")
    
    data = load_project_data()
    
    # Phase progress
    phases = {
        "Phase 1: Core Roles": {"status": "✅ Complete", "progress": 100},
        "Phase 2: Specialized Roles": {"status": "🔄 In Progress", "progress": 60},
        "Phase 3: Advanced Features": {"status": "⏳ Planned", "progress": 0}
    }
    
    for phase, info in phases.items():
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.markdown(f"### {phase}")
        with col2:
            st.progress(info["progress"] / 100)
        with col3:
            st.markdown(info["status"])
    
    # Business type progress
    st.markdown("---")
    st.markdown("### Business Type Implementation")
    
    for business, progress in data["role_progress"].items():
        st.markdown(f"#### {business.title()} Business")
        st.progress(progress / 100)
        st.caption(f"{progress}% complete")


def render_verticals_page():
    """Render business verticals progress"""
    st.markdown("# Business Vertical Development")
    
    data = load_project_data()
    
    verticals = {
        "Food Service": {
            "progress": 85,
            "features": ["Menu Management", "Order Processing", "Payment Integration"],
            "next": "Complete order workflow and commission tracking"
        },
        "Spa/Wellness": {
            "progress": 20,
            "features": ["Booking System", "Service Management", "Client Tracking"],
            "next": "Plan booking system architecture"
        },
        "Gym/Fitness": {
            "progress": 10,
            "features": ["Membership Management", "Class Booking", "Equipment Tracking"],
            "next": "Define membership tier structure"
        },
        "Trade Business": {
            "progress": 5,
            "features": ["Quote Management", "Job Scheduling", "Inventory Tracking"],
            "next": "Research trade business workflows"
        }
    }
    
    for vertical, info in verticals.items():
        with st.expander(f"{vertical} - {info['progress']}% Complete"):
            st.progress(info['progress'] / 100)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Features:**")
                for feature in info['features']:
                    st.markdown(f"• {feature}")
            
            with col2:
                st.markdown("**Next Priority:**")
                st.info(info['next'])

def render_roadmap_page():
    """Render the project roadmap from SUPERAPP_CONTEXT.md"""
    st.markdown("# SuperApp Project Roadmap")
    st.markdown("### Strategic development timeline and priorities")
    
    # Read current status from context file
    current_phase = "Initialization"
    try:
        if Path("SUPERAPP_CONTEXT.md").exists():
            with open("SUPERAPP_CONTEXT.md", 'r') as f:
                content = f.read()
                if "initialization" in content.lower():
                    current_phase = "Initialization"
                elif "mvp" in content.lower():
                    current_phase = "MVP Development"
    except:
        pass
    
    st.info(f"**Current Phase**: {current_phase}")
    
    # Phase timeline
    phases = [
        {
            "phase": "Phase 1: Foundation",
            "status": "Complete",
            "duration": "Week 1-2",
            "progress": 100,
            "items": [
                "Project architecture defined",
                "Role system designed", 
                "Entity structure (Account/Business/User)",
                "Tech stack confirmed (Laravel + AI)",
                "Documentation & memory bank created"
            ]
        },
        {
            "phase": "Phase 2: Backend Core",
            "status": "In Progress",
            "duration": "Week 3-6", 
            "progress": 45,
            "items": [
                "Laravel backend initialization",
                "Role system implementation",
                "Database schema & migrations",
                "API endpoints for core functions",
                "Authentication & authorization"
            ]
        },
        {
            "phase": "Phase 3: Food Vertical MVP",
            "status": "Planned",
            "duration": "Week 7-10",
            "progress": 0,
            "items": [
                "Menu management system",
                "Order processing workflow",
                "Payment integration (Stripe)",
                "Commission tracking",
                "Basic admin dashboard"
            ]
        },
        {
            "phase": "Phase 4: Multi-Tenant Scale",
            "status": "Future",
            "duration": "Week 11-14",
            "progress": 0,
            "items": [
                "Multiple business support",
                "Community organization features", 
                "Advanced role permissions",
                "Performance optimization",
                "Mobile app foundation"
            ]
        }
    ]
    
    # Render each phase
    for phase in phases:
        with st.expander(f"{phase['phase']} - {phase['status']} ({phase['duration']})"):
            # Progress bar
            st.progress(phase['progress'] / 100)
            st.caption(f"{phase['progress']}% Complete")
            
            # Items
            for item in phase['items']:
                if phase['status'] == "Complete":
                    st.success(f"✅ {item}")
                elif phase['status'] == "In Progress":
                    st.info(f"🔄 {item}")
                else:
                    st.warning(f"⏳ {item}")
    
    # Business verticals roadmap
    st.markdown("---")
    st.markdown("### Business Verticals Roadmap")
    
    verticals_timeline = {
        "Food Services": {
            "launch": "Q1 2024",
            "status": "MVP Development",
            "features": ["Online ordering", "Menu management", "Payment processing"],
            "revenue_target": "$10k/month by month 3"
        },
        "Spa/Wellness": {
            "launch": "Q2 2024", 
            "status": "Planned",
            "features": ["Booking system", "Service management", "Client profiles"],
            "revenue_target": "$15k/month by month 6"
        },
        "Fitness/Gym": {
            "launch": "Q3 2024",
            "status": "Research",
            "features": ["Membership management", "Class booking", "Trainer scheduling"],
            "revenue_target": "$20k/month by month 9"
        },
        "Trade Services": {
            "launch": "Q4 2024",
            "status": "Concept",
            "features": ["Quote management", "Job scheduling", "Inventory tracking"],
            "revenue_target": "$25k/month by month 12"
        }
    }
    
    for vertical, info in verticals_timeline.items():
        col1, col2, col3 = st.columns([2, 1, 2])
        
        with col1:
            st.markdown(f"### {vertical}")
            st.markdown(f"**Status**: {info['status']}")
            st.markdown(f"**Launch**: {info['launch']}")
        
        with col2:
            # Status indicator
            if "Development" in info['status']:
                st.success("🚀 Active")
            elif "Planned" in info['status']:
                st.info("📋 Ready")
            elif "Research" in info['status']:
                st.warning("🔍 Research")
            else:
                st.error("💡 Concept")
        
        with col3:
            st.markdown("**Key Features**:")
            for feature in info['features']:
                st.markdown(f"• {feature}")
            st.markdown(f"**Target**: {info['revenue_target']}")
    
    # Critical path & dependencies
    st.markdown("---")
    st.markdown("### Critical Path & Dependencies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Blockers & Dependencies")
        blockers = [
            "Laravel backend completion → Food vertical development",
            "Role system implementation → Multi-tenant features",
            "Payment integration → Commission tracking",
            "Mobile app foundation → iOS/Android deployment"
        ]
        
        for blocker in blockers:
            st.warning(f"• {blocker}")
    
    with col2:
        st.markdown("#### Success Milestones")
        milestones = [
            "First food order processed (Week 8)",
            "10 businesses onboarded (Week 12)",
            "Break-even revenue achieved (Week 16)",
            "Multi-vertical platform ready (Week 20)"
        ]
        
        for milestone in milestones:
            st.info(f"• {milestone}")
    


def render_optimization_page():
    """Render optimization tracking"""
    st.markdown("# Optimization Dashboard")
    
    # Development velocity simulation
    dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
    velocity = [2, 3, 5, 4, 6, 8, 7, 9, 11, 10, 12, 15, 14, 16, 18, 17, 19, 22, 21, 24, 26, 25, 28, 30, 29, 32, 35, 34, 37, 40]
    
    df = pd.DataFrame({
        'Date': dates,
        'Velocity': velocity
    })
    
    fig = px.line(df, x='Date', y='Velocity', title='Development Velocity (Story Points/Week)')
    st.plotly_chart(fig, use_container_width=True)
    
    # Optimization goals
    st.markdown("---")
    st.markdown("### Current Optimization Goals")
    
    goals = [
        {"goal": "Reduce Laravel API response time", "target": "<200ms", "current": "350ms", "status": "In Progress"},
        {"goal": "Increase role system reusability", "target": "90%", "current": "75%", "status": "In Progress"},
        {"goal": "Improve documentation coverage", "target": "95%", "current": "88%", "status": "In Progress"}
    ]
    
    for goal in goals:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"**{goal['goal']}**")
        with col2:
            st.markdown(f"Target: {goal['target']}")
        with col3:
            st.markdown(f"Current: {goal['current']}")
        with col4:
            st.markdown(goal['status'])

def main():
    """Main dashboard application"""
    
    # Render sidebar and get selected page
    selected_page = render_sidebar()
    
    # Render the selected page
    if selected_page == "overview":
        render_overview_page()
    elif selected_page == "roadmap":
        render_roadmap_page()
    elif selected_page == "ai_assistant":
        render_ai_assistant_page()
    elif selected_page == "roles":
        render_role_tracker_page()

    elif selected_page == "verticals":
        render_verticals_page()
    elif selected_page == "optimization":
        render_optimization_page()
    
    # Clean footer - no clutter needed

if __name__ == "__main__":
    main() 