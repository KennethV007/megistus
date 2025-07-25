# 💸 Megistus — AI-Powered Personal Finance Tracker

**Megistus** is a full-stack web application that tracks and analyzes personal financial transactions using machine learning to predict and visualize future spending habits, helping users make informed financial decisions. Currently it is in a demo phase so it will only display **My** transactions that I have trained the model on. 

## 📊 Project Status

This project is currently under active development. Here's the current progress:

- ✅ **Boilerplate Setup**: Docker containerization, basic project structure, and development environment
- 🚧 **Core Dependencies**: Setting up PyTorch integration, database migrations, Plaid API framework, and essential backend services
- ⏳ **Frontend Development**: Building a polished, modern UI (not just MVP - aiming for production-quality design)
- ⏳ **System Integration**: Connecting frontend, backend, database, and ML components seamlessly
- ⏳ **ML Model Training**: Training and fine-tuning predictive models on financial data
- ⏳ **Final Polish**: Performance optimization, testing, documentation, and deployment preparation

## 🔍 Overview

Megistus serves as a comprehensive personal finance management platform that combines transaction tracking with predictive analytics. The application uses a machine learning "collar" model to forecast spending patterns and provide confidence intervals, enabling users to budget more effectively and avoid overspending.

## 🧠 Key Features

- ✅ **Transaction Management**: Log transactions with amount, category, merchant, date, and notes
- ✅ **Data Visualization**: Interactive charts and graphs showing spending trends and category breakdowns  
- ✅ **ML Forecasting**: Predict future spending patterns with confidence intervals using PyTorch models
- ✅ **Category Analysis**: Detailed spending analysis across different expense categories
- ✅ **Expandable Architecture**: Built to support future enhancements including:
  - Multi-user authentication and authorization
  - Bank integrations (Plaid API ready)
  - Advanced analytics and reporting
  - Mobile-responsive design

## 🏗️ Tech Stack

### Frontend
- **React 18** with **TypeScript** for type-safe development
- **Vite** for fast development and optimized builds
- **TailwindCSS** for modern, responsive styling

### Backend  
- **Django 4.x** with **Django REST Framework** for robust API development
- **PostgreSQL** for reliable data persistence
- **PyTorch** for machine learning model development and inference

### DevOps & Tools
- **Docker & Docker Compose** for containerized development
- **WSL2** for Windows development environment
- **DBeaver** for database management

## 📋 Prerequisites

### For All Platforms
- **Git** for version control
- **Docker Engine** (v20.10 or higher) OR **Docker Desktop**
- **Docker Compose** (v2.0 or higher)

### Platform-Specific Setup

#### 🐧 **Linux (Ubuntu/Debian)**
```bash
# Install Docker Engine
sudo apt update
sudo apt install docker.io docker-compose-plugin
sudo usermod -aG docker $USER
# Log out and back in for group changes to take effect

# Clone and run
git clone https://github.com/KennethV007/megistus.git
cd megistus
docker compose up --build
```

#### 🪟 **Windows**
**Option 1: WSL2 + Docker Engine (Recommended)**
```bash
# Install WSL2, then in WSL2:
sudo apt update && sudo apt install docker.io docker-compose-plugin
sudo service docker start

# Clone and run
git clone https://github.com/KennethV007/megistus.git
cd megistus
docker compose up --build
```

**Option 2: Docker Desktop**
- Install Docker Desktop for Windows
- Enable WSL2 integration
- Use PowerShell or WSL2 terminal to run commands

#### 🍎 **macOS**
```bash
# Install Docker using Homebrew
brew install docker docker-compose

# Or install Docker Desktop for Mac
# Then clone and run:
git clone https://github.com/KennethV007/megistus.git
cd megistus
docker compose up --build
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/KennethV007/megistus.git
cd megistus
```

### 2. Environment Setup

The application uses Docker Compose for easy development setup. All necessary environment variables are pre-configured in the `docker-compose.yml` file.

### 3. Build and Run

```bash
# Start all services (database, backend, frontend)
docker compose up --build

# Or run in detached mode
docker compose up -d --build
```

### 4. Access the Application

Once all containers are running:

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Database**: PostgreSQL on localhost:5433

### 5. Initial Setup

The application will automatically:
- Set up the PostgreSQL database
- Run Django migrations
- Start the development servers

## 📁 Project Structure

```
megistus/
├── frontend/                 # React TypeScript frontend
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Application pages/views
│   │   ├── services/       # API service layers
│   │   └── utils/          # Utility functions
│   ├── public/             # Static assets
│   └── package.json
├── backend/                  # Django REST API backend
│   ├── api/                # Main API application
│   │   ├── models.py      # Database models
│   │   ├── views.py       # API endpoints
│   │   ├── serializers.py # Data serialization
│   │   └── urls.py        # URL routing
│   ├── core/               # Django project settings
│   ├── ml/                 # Machine learning models
│   ├── requirements.txt    # Python dependencies
│   └── manage.py
├── docker-compose.yml        # Container orchestration
└── README.md
```

## 🔧 Development

### Running Individual Services

```bash
# Start only the database
docker compose up db

# Start backend only (requires database)
docker compose up db backend

# Start frontend only
docker compose up frontend
```

### Database Management

```bash
# Access the PostgreSQL database
docker compose exec db psql -U megistus_user -d megistus_db

# Run Django migrations
docker compose exec backend python manage.py migrate

# Create Django superuser
docker compose exec backend python manage.py createsuperuser
```

### Stopping Services

```bash
# Stop all services
docker compose down

# Stop and remove volumes (clears database)
docker compose down --volumes
```

## 🤖 Machine Learning Features

Megistus incorporates PyTorch-based machine learning models to:

- **Spending Prediction**: Forecast future expenses based on historical patterns
- **Category Classification**: Automatically categorize transactions
- **Anomaly Detection**: Identify unusual spending patterns
- **Confidence Intervals**: Provide "collar" predictions with uncertainty ranges

## 🔐 Security & Privacy

- All financial data is stored locally in your PostgreSQL database
- No data is transmitted to external services without explicit configuration
- Built with security best practices including CSRF protection and secure headers
- Ready for authentication and authorization implementation

## 🚧 Roadmap

- [ ] User authentication and multi-user support  
- [ ] Plaid API integration for automatic transaction import
- [ ] Advanced ML models for better predictions
- [ ] Mobile application development
- [ ] Export/import functionality
- [ ] Advanced reporting and analytics dashboard


