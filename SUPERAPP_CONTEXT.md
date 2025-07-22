# 🚀 SUPERAPP - ADHD-Friendly Context & Memory Bank

## 🎯 THE BIG PICTURE
- **What**: AI-powered "WeChat for local communities" - unified platform for towns/cities
- **Who**: James Walker (lead), Nick Denysov (backend), Pavel (dev), Brian (optimization)
- **Where**: Starting local (Kemptville, Carleton Place), scaling globally
- **When**: Currently in initialization phase, building MVP

## 🏗️ CORE ARCHITECTURE
### Tech Stack
- **Backend**: Laravel API (Nick's expertise)
- **AI**: Grok 4 (primary) + Claude + Gemini + OpenAI
- **Infrastructure**: Google Cloud (full access to Cursor)
- **Development**: Cursor with Background Agents
- **Payments**: Stripe (gateway model)
- **Security**: Google Secret Manager for API keys

### Data Structure (CRITICAL)
```
ACCOUNT (our client) 
  ├── BUSINESS(ES) (their actual business info)
  └── USERS (people with roles)
```
- **Account**: Payment entity, client communication hub
- **Business**: Actual business data (Joe's Pizza info)
- **Users**: People with roles (Owner/Admin/Manager/Employee/Customer)
- **Community**: Organized by location/address

## 💰 REVENUE MODEL
- **Commission-based**: Take % of transactions, pay business remainder
- **NO upfront fees**: No subscription initially
- **Stripe integration**: Users → Stripe → back to platform
- **Example**: Restaurant order → we process → keep commission → pay restaurant

## 🎯 PRIORITY FEATURES (Phase 1)
### Admin Hub (CRM)
- [ ] Admin roles & permissions (coded, not dashboard)
- [ ] Account creation & management
- [ ] Business onboarding
- [ ] User role assignments

### Client Hub (CMS)
- [ ] Business dashboard
- [ ] User management within account
- [ ] Basic business tools

### First Vertical: FOOD SERVICES
- [ ] Online ordering system
- [ ] Menu management
- [ ] Order processing & notifications
- [ ] Payment integration

## 🔥 CURRENT STATUS
- ✅ Google Cloud account established
- ✅ Cursor Teams plan active
- ✅ Repository structure planned
- 🔄 Laravel backend initialization (Nick leading)
- 🔄 Entity structure design
- ❌ GitHub repo creation pending
- ❌ OpenWebUI custom model setup pending

## 🎲 DEVELOPMENT APPROACH
- **AI-First**: Heavy use of AI for development acceleration
- **Modular**: Build in components, not monolith
- **Iterative**: One vertical at a time (food first)
- **50/50 coding**: Human + AI collaboration
- **Background Agents**: Use Cursor's async processing for large tasks

## 🚨 KEY DECISIONS MADE
1. **Start fresh** (not building on menu.ca)
2. **Laravel backend** (team expertise)
3. **Commission model** (not subscription)
4. **Roles in code** (not dashboard-configurable)
5. **Admin-created accounts** initially (not self-signup)
6. **Community-based organization** by geography

## 🔄 NEXT IMMEDIATE STEPS
1. Finalize entity structure (Account/Business/User)
2. Implement basic admin roles/permissions
3. Create account onboarding flow
4. Set up GitHub repository
5. Begin food ordering system design

## 📊 BUSINESS TYPES (Future Modules)
- 🍕 **Food**: Ordering, reservations, menu management
- 💆 **Spas**: Booking, scheduling, service management
- 🏋️ **Gyms**: Memberships, class booking, trainer scheduling
- 🔧 **Trade**: Quotes, scheduling, inventory management
- 🏪 **Retail**: Inventory, sales, customer management

## 🎯 SUCCESS METRICS
- Speed of development (AI acceleration)
- Modular reusability across business types
- Commission revenue generation
- Community adoption rates
- Platform scalability

---
**Last Updated**: [DATE]
**Project Phase**: Initialization
**Focus**: Backend architecture & food vertical MVP 