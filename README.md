# Waste Management System - Database Module

A comprehensive database module for a Waste Management System with support for users, provinces, projects, datasets, complaints, resources, reports, and KPIs.

## 📋 Features

### 1. **Users, Roles & Permissions**
- User authentication and authorization
- Role-based access control (RBAC)
- Granular permission system
- User activity tracking

### 2. **Provinces (with Geo Reference)**
- CRUD operations for provinces
- Geographic coordinates (latitude/longitude)
- GeoJSON support
- Area and population data

### 3. **Projects**
- Project management with budget tracking
- Timeline management (start/end dates)
- Province linkage
- Budget history tracking
- Status and priority management

### 4. **Datasets**
- File upload support
- CSV/Excel import functionality
- Import status tracking
- Data validation
- Metadata storage

### 5. **Complaints (Public Form & Status Workflow)**
- Public complaint submission
- Status workflow tracking
- Assignment to users
- Location tracking
- Attachment support

### 6. **Resources (Publications & Downloads)**
- Publication management
- File downloads
- Download tracking
- Category organization
- Public/private resources

### 7. **Reports (Graphs, Summaries, Dashboard)**
- Report template system
- Report generation
- Dashboard widgets
- Customizable user dashboards
- Multiple export formats

### 8. **KPIs & Analytics**
- KPI definition and management
- Historical KPI tracking
- Analytics event tracking
- Threshold monitoring
- Multiple calculation methods

## 🚀 Quick Start

### Prerequisites
- MySQL 8.0 or higher
- MySQL client tools

### Installation

1. **Clone or download this repository**

2. **Run the setup script:**
   
   **Windows:**
   ```bash
   cd database/scripts
   setup_database.bat
   ```
   
   **Linux/Mac:**
   ```bash
   cd database/scripts
   chmod +x setup_database.sh
   ./setup_database.sh
   ```

3. **Or manually:**
   ```bash
   # Create database
   mysql -u root -p -e "CREATE DATABASE waste_management_db;"
   
   # Run schema
   mysql -u root -p waste_management_db < database/schema.sql
   
   # Run seeds
   mysql -u root -p waste_management_db < database/seeds/01_roles_permissions.sql
   mysql -u root -p waste_management_db < database/seeds/02_complaint_categories.sql
   mysql -u root -p waste_management_db < database/seeds/03_resource_categories.sql
   mysql -u root -p waste_management_db < database/seeds/04_system_settings.sql
   mysql -u root -p waste_management_db < database/seeds/05_sample_kpis.sql
   ```

4. **Create your first admin user:**
   ```bash
   # Edit database/scripts/create_admin_user.sql with your credentials
   mysql -u root -p waste_management_db < database/scripts/create_admin_user.sql
   ```

## 📁 Project Structure

```
Database_WasteManagement/
├── database/
│   ├── schema.sql                    # Main database schema
│   ├── migrations/                   # Migration scripts
│   ├── seeds/                        # Seed data files
│   ├── config/                       # Database configuration
│   │   ├── database.config.js       # Node.js config
│   │   └── database.config.py       # Python config
│   ├── scripts/                      # Utility scripts
│   │   ├── setup_database.sh        # Linux/Mac setup
│   │   ├── setup_database.bat       # Windows setup
│   │   └── create_admin_user.sql     # Admin user creation
│   ├── ER_DIAGRAM.md                # Entity relationship docs
│   └── README.md                     # Database documentation
├── .gitignore
└── README.md                         # This file
```

## 🔐 Default Roles

1. **Super Admin** - Full system access with all permissions
2. **Admin** - Administrative access to manage system operations
3. **Manager** - Management access to oversee projects and reports
4. **Officer** - Standard user with operational permissions
5. **Public User** - Limited access for public complaint submission

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=waste_management_db
DB_SSL=false
```

### Backend Integration

**Node.js/Express:**
```javascript
const dbConfig = require('./database/config/database.config.js');
const config = dbConfig[process.env.NODE_ENV || 'development'];
```

**Python/Django:**
```python
from database.config.database.config import DATABASE_CONFIG
config = DATABASE_CONFIG[os.getenv('ENVIRONMENT', 'development')]
```

**Python/FastAPI:**
```python
from database.config.database.config import SQLALCHEMY_DATABASE_URL
```

## 📊 Database Schema Overview

- **30+ tables** covering all system modules
- **Foreign key relationships** for data integrity
- **Indexes** for optimal query performance
- **Audit logging** for change tracking
- **Soft deletes** using `is_active` flags
- **JSON columns** for flexible metadata

## 📚 Documentation

- [Database README](database/README.md) - Detailed database documentation
- [ER Diagram](database/ER_DIAGRAM.md) - Entity relationship documentation
- [Migrations Guide](database/migrations/README.md) - Migration instructions

## 🛠️ Next Steps

1. **Create Admin User** - Set up your first administrator account
2. **Import Province Data** - Add your province/region data
3. **Configure Settings** - Update system settings for your environment
4. **Set Up File Storage** - Configure paths for file uploads
5. **Integrate Backend** - Connect your application to the database

## 🔄 Maintenance

### Backup
```bash
mysqldump -u root -p waste_management_db > backup_$(date +%Y%m%d).sql
```

### Restore
```bash
mysql -u root -p waste_management_db < backup_20240101.sql
```

## 📝 License

This database module is part of the Waste Management System project.

## 🤝 Contributing

When contributing to the database schema:
1. Never modify existing migration files
2. Create new migration files for schema changes
3. Update documentation for any schema changes
4. Test migrations on development database first

## 📞 Support

For issues or questions:
1. Check the [Database README](database/README.md)
2. Review the [ER Diagram](database/ER_DIAGRAM.md)
3. Check migration files for schema changes

---

**Built with MySQL 8.0+** | **Supports Node.js, Python, and other backends**

