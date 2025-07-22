# Megistus Backend

A Django REST API backend for the Megistus application.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed
- Virtual environment activated

### Installation

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Activate virtual environment**
   ```bash
   # Windows
   .\venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver 8000
   ```
6. **Quick little oneliner hehe**
   ```bash
   source venv_wsl/bin/activate && python3 manage.py runserver 8000
   ```
## 📚 API Endpoints

The API is available at `http://localhost:8000/`

### Available Endpoints

- **Root**: `GET /` - API information
- **Health Check**: `GET /api/health/` - Server health status  
- **API Info**: `GET /api/info/` - API metadata
- **Example**: `GET|POST /api/example/` - Example endpoint

### Example API Calls

```bash
# Health check
curl http://localhost:8000/api/health/

# Get example data
curl http://localhost:8000/api/example/

# Post example data
curl -X POST http://localhost:8000/api/example/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from frontend!"}'
```

## 🛠️ Development Scripts

Available npm scripts (run with `npm run <script>`):

- `dev` - Start development server on port 8000
- `migrate` - Run database migrations
- `makemigrations` - Create new migrations
- `createsuperuser` - Create Django admin user
- `shell` - Open Django shell
- `test` - Run tests

## 🌐 CORS Configuration

The backend is configured to accept requests from:
- `http://localhost:5173` (Vite frontend dev server)
- `http://127.0.0.1:5173`

## 🔧 Environment Variables

Create a `.env` file with:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 📁 Project Structure

```
backend/
├── api/                 # Main API app
│   ├── views.py        # API endpoints
│   ├── urls.py         # URL routing
│   └── ...
├── core/               # Django project settings
│   ├── settings.py     # Configuration
│   ├── urls.py         # Main URL config
│   └── ...
├── requirements.txt    # Python dependencies
├── manage.py          # Django management script
└── .env              # Environment variables
```

## 🗄️ Database

Currently using SQLite for development. Database file: `db.sqlite3`

## 🔑 Admin Interface

Create a superuser to access Django admin at `/admin/`:

```bash
python manage.py createsuperuser
```

## 📦 Technology Stack

- **Django 5.2+** - Web framework
- **Django REST Framework** - API framework  
- **django-cors-headers** - CORS handling
- **python-dotenv** - Environment variables
- **SQLite** - Database (development) 