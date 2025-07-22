# 🎭 SUPERAPP USER ROLES PLAN

## 📋 OVERVIEW
This document defines the comprehensive role structure for SuperApp, covering both Account-level (business users) and Platform-level (admin) roles with their respective permissions and implementation strategy.

---

## 🏢 ACCOUNT ROLES (Business-Side Users)

### **TIER 1: CORE MANAGEMENT**
| Role | Description | Key Permissions |
|------|-------------|----------------|
| **Owner** | Business owner, full control | Account deletion, billing changes, all permissions |
| **Admin** | Senior management, nearly full access | All except billing/deletion, can manage users |
| **Manager** | Department/location oversight | Staff management, operational controls |

### **TIER 2: OPERATIONAL STAFF**
| Role | Description | Key Permissions |
|------|-------------|----------------|
| **Staff/Employee** | Basic operational access | Daily operations, can't manage others |
| **Shift Leader** | Limited management during shifts | Shift oversight, basic staff coordination |
| **Cashier/Front Desk** | Customer interaction focus | Order processing, customer service |

### **TIER 3: SPECIALIZED ROLES**
| Role | Description | Business Type | Key Permissions |
|------|-------------|---------------|----------------|
| **Chef/Kitchen Manager** | Menu & kitchen operations | Food Service | Menu management, inventory, kitchen staff |
| **Therapist/Practitioner** | Service provider | Spa/Wellness | Booking management, client notes, schedules |
| **Personal Trainer** | Fitness instruction | Gym/Fitness | Class management, member tracking, equipment |
| **Delivery Driver** | Order fulfillment | Food Service | Order status, delivery tracking, customer contact |

### **TIER 4: EXTERNAL ENTITIES** 
| Role | Description | Key Permissions |
|------|-------------|----------------|
| **Partner** | Affiliated businesses | Cross-referrals, shared promotions, data exchange |

> **NOTE**: Customers are now a **separate entity** outside the Account-User role structure. They interact with businesses but don't have Account roles.

---

## 🛠️ PLATFORM ROLES (SuperApp Admin)

### **TIER 1: PLATFORM MANAGEMENT**
| Role | Description | Key Permissions |
|------|-------------|----------------|
| **Super Admin** | Full platform control | All system access, user management, billing |
| **Platform Manager** | Operational oversight | Account management, feature rollouts, policies |
| **Developer** | Technical management | Code access, debugging, system maintenance |

### **TIER 2: SUPPORT & OPERATIONS**
| Role | Description | Key Permissions |
|------|-------------|----------------|
| **Support Manager** | Customer support lead | Account issues, escalations, refunds |
| **Support Agent** | Front-line support | Basic troubleshooting, ticket management |
| **Business Analyst** | Data & insights | Reports, analytics, business intelligence |
| **Financial Controller** | Money management | Commission tracking, payouts, financial reports |

### **TIER 3: SPECIALIZED FUNCTIONS**
| Role | Description | Key Permissions |
|------|-------------|----------------|
| **Content Moderator** | Quality control | Review content, handle complaints, enforce policies |
| **Marketing Manager** | Growth & campaigns | Platform marketing, feature announcements |
| **Integration Specialist** | Third-party systems | API management, partner integrations |

---

## 📊 PERMISSIONS MATRIX

### **ACCOUNT PERMISSIONS CATEGORIES**

#### 🏢 **ACCOUNT MANAGEMENT**
| Permission | Owner | Admin | Manager | Staff |
|------------|-------|-------|---------|-------|
| Delete Account | ✅ | ❌ | ❌ | ❌ |
| Change Billing Info | ✅ | ❌ | ❌ | ❌ |
| Modify Business Profile | ✅ | ✅ | Limited | ❌ |
| View Account Analytics | ✅ | ✅ | Limited | ❌ |

#### 👥 **USER MANAGEMENT**
| Permission | Owner | Admin | Manager | Staff |
|------------|-------|-------|---------|-------|
| Invite New Users | ✅ | ✅ | Limited | ❌ |
| Assign/Change Roles | ✅ | ✅ | Staff Only | ❌ |
| Remove Users | ✅ | ✅ | Staff Only | ❌ |
| View User Activity | ✅ | ✅ | Team Only | ❌ |

#### 🍕 **BUSINESS OPERATIONS**
| Permission | Owner | Admin | Manager | Staff |
|------------|-------|-------|---------|-------|
| Manage Menu/Services | ✅ | ✅ | ✅ | View Only |
| Process Orders | ✅ | ✅ | ✅ | ✅ |
| Handle Refunds | ✅ | ✅ | ✅ | Limited |
| Manage Inventory | ✅ | ✅ | ✅ | View Only |

> **NOTE**: Customer interactions (placing orders, requesting refunds) handled through separate customer-facing interfaces

#### 💰 **FINANCIAL ACCESS**
| Permission | Owner | Admin | Manager | Staff |
|------------|-------|-------|---------|-------|
| View Revenue Reports | ✅ | ✅ | Limited | ❌ |
| Manage Pricing | ✅ | ✅ | Limited | ❌ |
| Process Payouts | ✅ | ✅ | ❌ | ❌ |
| View Commission Data | ✅ | ✅ | ❌ | ❌ |

#### 👤 **CUSTOMER MANAGEMENT**
| Permission | Owner | Admin | Manager | Staff |
|------------|-------|-------|---------|-------|
| View Customer Data | ✅ | ✅ | ✅ | Limited |
| Send Marketing Messages | ✅ | ✅ | ✅ | ❌ |
| Handle Customer Support | ✅ | ✅ | ✅ | ✅ |
| Export Customer Lists | ✅ | ✅ | ❌ | ❌ |

> **NOTE**: Customers interact through separate customer management system, not role-based permissions

---

## 🎯 IMPLEMENTATION STRATEGY

### **PHASE 1: CORE ROLES (MVP)**
- Owner, Admin, Manager, Staff, Customer
- Basic permission structure
- Simple role assignment interface

### **PHASE 2: SPECIALIZED ROLES**
- Business-specific roles (Chef, Therapist, Trainer)
- Advanced permission granularity
- Role-based dashboard customization

### **PHASE 3: ADVANCED FEATURES**
- Time-based permissions (shift-based access)
- Location-based roles (multi-location businesses)
- Custom role creation for enterprise clients

---

## 🔧 TECHNICAL CONSIDERATIONS

### **DATABASE STRUCTURE**
```sql
-- Core tables needed
users           -- Account team members (Owner, Admin, Manager, Staff)
roles           -- Role definitions
permissions     -- Permission definitions  
role_permissions -- Role-to-permission mapping
user_roles      -- User-to-role assignments
accounts        -- Business accounts (our clients)
businesses      -- Business information linked to accounts
customers       -- SEPARATE: End users who interact with businesses
orders          -- Customer orders linked to businesses
```

### **PERMISSION NAMING CONVENTION**
- Format: `{category}.{action}.{scope}`
- Examples: 
  - `account.delete.own`
  - `users.manage.team`
  - `orders.process.all`
  - `reports.view.limited`

### **ROLE INHERITANCE**
- Higher roles inherit lower role permissions
- Custom permissions can be added/removed per user
- Override system for special cases

---

## 📋 BUSINESS TYPE VARIATIONS

### **FOOD SERVICE SPECIFIC**
- Kitchen Manager, Delivery Driver, Server
- Permissions: Menu management, order routing, delivery tracking

### **SPA/WELLNESS SPECIFIC**
- Therapist, Receptionist, Wellness Coach
- Permissions: Appointment booking, client notes, treatment plans

### **GYM/FITNESS SPECIFIC**
- Personal Trainer, Membership Coordinator, Maintenance
- Permissions: Class scheduling, member management, equipment tracking

### **TRADE BUSINESS SPECIFIC**
- Lead Technician, Apprentice, Dispatcher
- Permissions: Job scheduling, inventory management, quote creation

---

## 🚨 SECURITY CONSIDERATIONS

### **ROLE ASSIGNMENT RULES**
1. Only Owner can assign Owner role
2. Admin cannot assign roles equal to or higher than their own
3. Manager can only assign Staff and Customer roles
4. Self-role elevation prevention

### **AUDIT TRAIL**
- Log all role changes with timestamp and actor
- Track permission usage for security monitoring
- Regular role review and cleanup processes

### **FAIL-SAFE MECHANISMS**
- Always ensure at least one Owner per account
- Prevent role changes that would lock out management
- Emergency admin override capabilities

---

## 📈 FUTURE ENHANCEMENTS

### **ADVANCED FEATURES TO CONSIDER**
- **Temporary Roles**: Time-limited access (vacation coverage)
- **Conditional Permissions**: Location/time-based restrictions
- **Role Templates**: Pre-configured role sets by business type
- **Custom Role Builder**: Enterprise feature for large accounts
- **Multi-Account Roles**: Users spanning multiple businesses

### **INTEGRATION POSSIBILITIES**
- Single Sign-On (SSO) with external systems
- Role synchronization with existing business tools
- API access for third-party role management
- Mobile app role-specific interfaces

---

## 🎭 SAMPLE ROLES LIST

### **PHASE 1: MVP ROLES (Start Here)**
```javascript
// Core Account Roles (Business Team Members)
const ACCOUNT_ROLES = [
  'owner',           // Full control, billing access
  'admin',           // Nearly full access, no billing
  'manager',         // Department oversight
  'staff'            // Basic operations
];

// NOTE: Customers are separate entities, not account roles

// Basic Platform Roles
const PLATFORM_ROLES = [
  'super_admin',     // Full platform control
  'support_manager', // Customer support lead
  'support_agent',   // Front-line support
  'developer'        // Technical access
];
```

### **PHASE 2: SPECIALIZED ROLES (Business-Specific)**
```javascript
// Food Service Roles
const FOOD_ROLES = [
  'kitchen_manager', // Menu, inventory, kitchen staff
  'chef',           // Menu creation, kitchen operations
  'server',         // Order taking, customer service
  'delivery_driver', // Order delivery, status updates
  'hostess'         // Seating, reservations
];

// Spa/Wellness Roles
const SPA_ROLES = [
  'therapist',      // Service provider, bookings
  'receptionist',   // Front desk, scheduling
  'wellness_coach', // Programs, client guidance
  'spa_manager'     // Operations, staff oversight
];

// Gym/Fitness Roles
const GYM_ROLES = [
  'personal_trainer',    // Classes, member training
  'membership_coord',    // Member management, sales
  'maintenance_tech',    // Equipment, facility care
  'group_instructor'     // Class leadership
];

// Trade Business Roles
const TRADE_ROLES = [
  'lead_technician',  // Senior technical work
  'apprentice',       // Learning, basic tasks
  'dispatcher',       // Job scheduling, coordination
  'estimator'         // Quotes, project planning
];
```

### **PHASE 3: ADVANCED ROLES (Future)**
```javascript
// Time-Based Roles
const SHIFT_ROLES = [
  'day_manager',      // Daytime operations
  'night_manager',    // Evening/night shift
  'weekend_supervisor', // Weekend coverage
  'holiday_staff'     // Special event coverage
];

// Location-Based Roles
const LOCATION_ROLES = [
  'regional_manager',  // Multiple locations
  'site_manager',      // Single location
  'area_supervisor',   // Geographic area
  'mobile_worker'      // Works across locations
];

// Customer Tier Roles
const CUSTOMER_TIERS = [
  'guest_customer',    // One-time users
  'regular_customer',  // Standard members
  'vip_customer',      // Premium tier
  'corporate_customer', // Business accounts
  'partner_business'   // Affiliated companies
];
```

### **SAMPLE ROLE CONFIGURATIONS**

#### **🍕 PIZZA RESTAURANT SETUP**
```javascript
const PIZZA_SHOP_ROLES = {
  // Management
  owner: ['Joe Smith', 'Full business control'],
  manager: ['Sarah Johnson', 'Day operations'],
  
  // Kitchen
  kitchen_manager: ['Mike Chef', 'Menu and kitchen'],
  chef: ['Tony Kitchen', 'Food preparation'],
  
  // Front of House
  cashier: ['Lisa Front', 'Orders and payments'],
  server: ['Tom Waiter', 'Table service'],
  
  // Delivery
  delivery_driver: ['Bob Driver', 'Order delivery'],
  
  // Note: Customers are separate entities, not roles
};
```

#### **💆 SPA BUSINESS SETUP**
```javascript
const SPA_BUSINESS_ROLES = {
  // Management
  owner: ['Emma Wellness', 'Business owner'],
  spa_manager: ['Rachel Mgr', 'Operations'],
  
  // Service Providers
  therapist: ['Dr. Massage', 'Treatments'],
  wellness_coach: ['Fit Guru', 'Programs'],
  
  // Support
  receptionist: ['Front Desk', 'Bookings'],
  
  // Note: Customers (including VIP) are separate entities
};
```

#### **🏋️ GYM SETUP**
```javascript
const GYM_ROLES = {
  // Management
  owner: ['Fit Owner', 'Gym business'],
  manager: ['Strong Manager', 'Daily ops'],
  
  // Trainers
  personal_trainer: ['PT Smith', 'One-on-one training'],
  group_instructor: ['Class Leader', 'Group fitness'],
  
  // Support
  membership_coord: ['Member Rep', 'Sales and service'],
  maintenance_tech: ['Fix Guy', 'Equipment care'],
  
  // Note: Members/customers are separate entities
};
```

### **ROLE ASSIGNMENT EXAMPLES**

#### **TYPICAL SMALL BUSINESS (5-10 EMPLOYEES)**
```javascript
const SMALL_BUSINESS_SETUP = {
  // Account Team Members
  owner: 1,          // Business owner
  manager: 1,        // Assistant manager
  staff: 6,          // General employees
  
  // Separate Customer Entity
  customers: 'unlimited' // Managed separately from roles
};
```

#### **MEDIUM BUSINESS (20-50 EMPLOYEES)**
```javascript
const MEDIUM_BUSINESS_SETUP = {
  // Account Team Members
  owner: 1,          // Business owner
  admin: 1,          // General manager
  manager: 3,        // Department heads
  shift_leader: 4,   // Shift supervisors
  staff: 35,         // General employees
  
  // Separate Customer Entity
  customers: 'unlimited' // Managed separately
};
```

#### **LARGE BUSINESS (50+ EMPLOYEES)**
```javascript
const LARGE_BUSINESS_SETUP = {
  // Account Team Members
  owner: 1,              // Business owner
  admin: 2,              // Senior management
  regional_manager: 1,   // Multi-location oversight
  site_manager: 5,       // Location managers
  manager: 10,           // Department heads
  shift_leader: 8,       // Shift supervisors
  specialized_roles: 15, // Chefs, trainers, etc.
  staff: 45,             // General employees
  
  // Separate Customer Entity
  customers: 'unlimited' // Managed separately
};
```

### **QUICK REFERENCE: ROLE CODES**

```javascript
// Role Code Format: {business_type}_{role_level}_{function}
ROLE_CODES = {
  // Universal Roles
  'UNI_OWN_FULL': 'owner',
  'UNI_ADM_MGMT': 'admin',
  'UNI_MGR_DEPT': 'manager',
  'UNI_STF_BASIC': 'staff',
  // Note: Customers are separate entities, not roles
  
  // Food Service
  'FOD_MGR_KTCH': 'kitchen_manager',
  'FOD_STF_CHEF': 'chef',
  'FOD_STF_SERV': 'server',
  'FOD_STF_DELV': 'delivery_driver',
  
  // Spa/Wellness
  'SPA_STF_THER': 'therapist',
  'SPA_STF_RECEP': 'receptionist',
  'SPA_STF_COACH': 'wellness_coach',
  
  // Gym/Fitness
  'GYM_STF_TRAIN': 'personal_trainer',
  'GYM_STF_INSTRU': 'group_instructor',
  'GYM_STF_MEMB': 'membership_coord'
};
```

---

**Last Updated**: January 2025  
**Status**: Planning Phase  
**Next Action**: Create permissions spreadsheet and implement core roles 