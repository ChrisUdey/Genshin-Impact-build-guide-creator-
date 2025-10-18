# Genshin Impact Build Guide Creator

A web application that allows players to create and share character build guides for Genshin Impact. Users can browse 30 playable characters, create comprehensive build guides with multiple image uploads, and share strategies with the community.

## 🎮 About

This project was created as part of the CWEB280 course to demonstrate full-stack web development skills using modern frameworks and best practices.

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Python-Jose** - JWT token generation and validation
- **Pydantic** - Data validation using Python type hints
- **SQLite** - Lightweight database

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API calls

### Testing
- **Cypress** - End-to-end testing framework

## ✨ Features

- 📋 Browse 30 Genshin Impact characters with detailed information
- 🔐 JWT-based authentication
- ✍️ Create comprehensive build guides
- 📸 Upload multiple showcase images per guide with captions
- ✅ Client-side and server-side validation
- 🔒 Protected routes requiring authentication
- 📱 Responsive design with Tailwind CSS

## 📁 Project Structure
```
genshin-build-guide/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── models/         # SQLAlchemy database models
│   │   ├── routes/         # API route handlers
│   │   ├── middleware/     # Authentication middleware
│   │   ├── schemas/        # Pydantic validation schemas
│   │   ├── controllers/    # Business logic
│   │   ├── main.py         # FastAPI application
│   │   ├── database.py     # Database configuration
│   │   └── config.py       # App configuration
│   ├── uploads/            # User-uploaded files
│   ├── requirements.txt    # Python dependencies
│   └── run.py             # Development server
│
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js pages (App Router)
│   │   ├── components/    # React components
│   │   ├── lib/          # Utilities and API client
│   │   └── types/        # TypeScript type definitions
│   └── package.json      # Node dependencies
│
└── cypress/               # E2E tests
    └── e2e/
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- pip (Python package manager)
- npm or yarn (Node package manager)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with configuration:
```env
SECRET_KEY=your-secret-key-change-this
DATABASE_URL=sqlite:///./genshin_builds.db
FRONTEND_URL=http://localhost:3000
```

5. Run the development server:
```bash
python run.py
```

Backend will be available at: http://localhost:8000

API Documentation: http://localhost:8000/docs

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env.local` file:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

4. Run the development server:
```bash
npm run dev
```

Frontend will be available at: http://localhost:3000

## 🔑 Authentication

**Test Credentials:**
- Email: `test@t.ca`
- Password: `123456Pw`

## 📡 API Endpoints

### Public Endpoints
- `GET /api/characters/` - Get all characters
- `GET /api/characters/{id}` - Get character by ID
- `GET /api/guides/` - Get all build guides
- `GET /api/guides/{id}` - Get guide by ID
- `POST /api/auth/login` - User login

### Protected Endpoints (Require JWT)
- `POST /api/guides/` - Create new build guide
- `POST /api/guides/{id}/upload` - Upload image to guide

## 🧪 Testing

Run Cypress E2E tests:
```bash
npm run cypress:open
```

**Note:** Both backend and frontend servers must be running for tests to pass.

## 📊 Database Models

### Characters (Seeded)
- 30 playable characters from Genshin Impact
- Includes: name, vision, weapon, nation, rarity, description

### BuildGuides (User-created)
- Character builds created by authenticated users
- Fields: title, description, character reference

### Uploads (User-created)
- Multiple images per build guide
- Fields: image path, caption, timestamp

## 🎯 Project Requirements Met

✅ **Two entities with Create/List/Display**: BuildGuides & Uploads  
✅ **File upload with validation**: Image uploads with size/type checking  
✅ **Client & server validation**: Inline error messages  
✅ **Authentication**: JWT-based auth on protected routes  
✅ **Invalid file deletion**: Automatically removes invalid uploads  
✅ **E2E testing**: Cypress tests for complete user flows  

## 🤝 Contributing

This is a student project. For questions or issues, contact the development team.

## 👥 Team

- Chris Udey
- Jorge Martinez

## 📝 License

This project is created for educational purposes as part of CWEB280 coursework.

## 🙏 Acknowledgments

- Character data sourced from Genshin Impact
- Course materials from CWEB280
- Saskatchewan Polytechnic

---

**Last Updated:** [Current Date]
