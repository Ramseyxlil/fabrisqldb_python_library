# FabricEase 🚀

**A Simple Python Library for Microsoft Fabric SQL Database Connections**

*By Abdulrafiu Izuafa*

FabricEase solves the industry-wide problem of connecting to Microsoft Fabric SQL Database from Python. No more complex token encoding, authentication headaches, or cryptic ODBC errors!

## ✨ Features

- **🔐 Simple Authentication** - Just provide your Azure credentials
- **📦 Easy Installation** - One pip install command
- **🎯 Intuitive API** - Database operations that just make sense
- **🛡️ Error Handling** - Clear error messages and helpful guidance
- **📊 CRUD Operations** - Insert, query, update, delete made simple
- **🔧 Context Managers** - Automatic connection management
- **⚡ Production Ready** - Built on proven token-based authentication

## 🚀 Quick Start

### Installation

```bash
pip install fabricease
```

### Setup Credentials

Create a `.env` file with your Azure credentials:

```bash
# Generate template
python -c "from fabricease.utils import create_env_template; create_env_template()"
```

Edit `.env` with your actual values:

```env
FABRIC_SERVER=your-server.database.fabric.microsoft.com
FABRIC_DATABASE=your-database-name
AZURE_CLIENT_ID=your-application-client-id
AZURE_CLIENT_SECRET=your-client-secret-value
AZURE_TENANT_ID=your-directory-tenant-id
```

### Basic Usage

```python
from fabricease import FabricDatabase

# Connect using environment variables
db = FabricDatabase.from_env()

# Test connection
result = db.test_connection()
print(f"Connected: {result['connected']}")

# Query data
employees = db.query("SELECT * FROM employees")
print(f"Found {len(employees)} employees")

# Insert data
db.insert('employees', {
    'name': 'John Doe',
    'email': 'john@company.com',
    'salary': 75000.00
})

# Update data
db.update('employees', 
    data={'salary': 80000.00},
    where='name = ?', 
    params=('John Doe',)
)
```

## 📖 Examples

### Context Manager (Recommended)

```python
with FabricDatabase.from_env() as db:
    employees = db.query("SELECT * FROM employees WHERE salary > ?", (50000,))
    for emp in employees:
        print(f"{emp['name']}: ${emp['salary']:,.2f}")
# Connection automatically closed
```

### Bulk Operations

```python
# Insert multiple records
employees = [
    {'name': 'Alice', 'email': 'alice@company.com', 'salary': 65000},
    {'name': 'Bob', 'email': 'bob@company.com', 'salary': 70000},
    {'name': 'Carol', 'email': 'carol@company.com', 'salary': 68000}
]

rows_inserted = db.insert_many('employees', employees)
print(f"Inserted {rows_inserted} employees")
```

### Direct Credentials (Alternative)

```python
db = FabricDatabase(
    server="your-server.database.fabric.microsoft.com",
    database="your-database",
    client_id="your-client-id",
    client_secret="your-client-secret",
    tenant_id="your-tenant-id"
)
```

## 🔧 Setup Azure Service Principal

1. **Create App Registration**:
   - Go to Azure Portal → Microsoft Entra ID → App registrations
   - Click "New registration"
   - Note the **Application (client) ID** and **Directory (tenant) ID**

2. **Create Client Secret**:
   - Go to "Certificates & secrets" → "New client secret"
   - Copy the **secret value** (you won't see it again!)

3. **Grant Fabric Access**:
   - Go to your Fabric workspace → "Manage access"
   - Add your service principal with appropriate permissions

## 🛡️ Error Handling

```python
from fabricease import FabricDatabase, FabricConnectionError

try:
    db = FabricDatabase.from_env()
    result = db.query("SELECT * FROM employees")
except FabricConnectionError as e:
    print(f"Connection failed: {e}")
    print("Check your credentials and network connectivity")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 🔍 Troubleshooting

```python
from fabricease.utils import validate_environment, print_connection_help

# Check environment configuration
validation = validate_environment()
if not validation['valid']:
    print("Missing variables:", validation['missing'])

# Get detailed help
print_connection_help()
```

## 🎯 Why FabricEase?

Connecting to Microsoft Fabric SQL Database has been a major pain point:

- ❌ Complex token encoding requirements
- ❌ Confusing authentication methods  
- ❌ Poor documentation and examples
- ❌ Network configuration challenges
- ❌ Cryptic error messages

FabricEase solves all of these problems with a simple, intuitive API that handles the complexity for you.

## 📚 API Reference

### FabricDatabase

#### Methods

- `from_env()` - Create instance from environment variables
- `connect()` - Establish database connection
- `disconnect()` - Close database connection
- `query(sql, params=None)` - Execute SELECT query
- `execute(sql, params=None)` - Execute INSERT/UPDATE/DELETE
- `insert(table, data)` - Insert single record
- `insert_many(table, data_list)` - Insert multiple records
- `update(table, data, where, params=None)` - Update records
- `delete(table, where, params=None)` - Delete records
- `get_tables()` - List all tables
- `table_exists(table_name)` - Check if table exists
- `test_connection()` - Test connection and get server info

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see LICENSE file for details.

## 👨‍💻 Author

**Abdulrafiu Izuafa**
- Email: your.email@example.com
- GitHub: [@your-username](https://github.com/your-username)

## 🙏 Acknowledgments

- Built to solve real industry connection problems
- Inspired by the community's need for simpler Fabric SQL access
- Thanks to everyone who struggled with Fabric connections before this! 

---

*Making Fabric SQL Database connections as easy as they should be!* ✨