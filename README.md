# Genshin Impact Build Guide Creator

A web application where users can create and share character build guides for Genshin Impact. Users can post guides with images, and other users can view approved guides.

## Project Overview

This is a full-stack web application built for CWEB280. The app lets Genshin Impact players share their character builds, including artifacts, weapons, and strategies.

### Main Features
- Browse all 92 Genshin Impact characters
- Create build guides with images
- View approved guides from other users
- User authentication (login/logout)
- Server-side validation to prevent bad data
- Pagination for easier browsing

---

## Tech Stack

### Backend
- **Python 3.x** with FastAPI
- **SQLite** database (easy setup, no server needed)
- **SQLAlchemy** ORM for database operations
- **Pydantic** for data validation
- **JWT** for authentication
- **Python-Jose** for JWT tokens

### Frontend
- **Next.js 15** (React framework)
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **Axios** for API calls

### Testing
- **Cypress** for E2E testing

---

## Database Schema

We have 3 main tables:

**Characters** (seeded from API)
- Pre-loaded with all Genshin characters
- Used as reference data

**BuildGuides** (user created)
- username, title, description
- Links to a character
- Has "pending" or "approved" status
- Can have uploaded images

**Uploads** (optional, linked to guides)
- Image files with captions
- Multiple uploads per guide

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Navigate to backend folder:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Seed the database with characters:
```bash
python scripts/seed_characters.py
```
This fetches all 92 characters from the Genshin API and saves them to the database.

6. Run the backend server:
```bash
python run.py
```

Backend should be running on: `http://localhost:8000`

You can check the API docs at: `http://localhost:8000/docs`

---

### Frontend Setup

1. Navigate to frontend folder:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

4. Run the frontend:
```bash
npm run dev
```

Frontend should be running on: `http://localhost:3000`

---

## Running the Application

**You need both servers running at the same time!**

Terminal 1 (Backend):
```bash
cd backend
venv\Scripts\activate  # or source venv/bin/activate on Mac
python run.py
```

Terminal 2 (Frontend):
```bash
cd frontend
npm run dev
```

Then open your browser to: `http://localhost:3000`

---

## Test Credentials

For testing the login:
- **Email:** test@t.ca
- **Password:** 123456Pw

---

## Features Explained

### 1. Home Page
Shows 4 characters at a time in a grid. You can click through pages to see all 92 characters. Click on a character to see their details.

### 2. Guides Page
This is where users can:
- Create new build guides (must fill out form)
- View all approved guides
- See guides with pagination (4 per page)

### 3. Login System
- JWT-based authentication
- Token stored in localStorage
- Protected routes require login

### 4. Server-Side Validation
We validate ALL data on the server so users can't bypass frontend validation:
- Username: 4-20 characters, alphanumeric only
- Title: 4-30 characters
- Description: 10-350 characters
- Images: JPG/PNG only, max 2MB, no WebP

---

## API Endpoints

### Characters
- `GET /api/characters/` - Get all characters
- `GET /api/characters/{id}` - Get specific character

### Authentication
- `POST /api/auth/login` - Login with email/password

### Build Guides
- `GET /api/guides/` - Get all approved guides
- `POST /api/guides/` - Create new guide (validated)
- `GET /api/guides/{id}` - Get specific guide
- `GET /api/guides/pending` - Get pending guides (admin)

---

## Testing

We used Cypress for end-to-end testing.

### Running Tests

**Make sure both backend and frontend are running first!**

Then in a third terminal:
```bash
cd frontend
npx cypress open
```

Click "E2E Testing" → Choose Chrome → Click on test files to run them

### Test Files

1. **01-login.cy.js** - Tests login with wrong password first, then correct password
2. **02-home.cy.js** - Tests character display and pagination
3. **03-guides.cy.js** - Tests creating guides with invalid inputs first, then valid inputs

The tests check:
- Login with invalid credentials shows errors
- Login with valid credentials works
- Form validation (empty fields, too short text)
- Creating a guide with valid data
- Guide appears in the list after creation
- Navigation and pagination work

**Important:** Tests will FAIL if the backend API is not running (as required by the assignment).

---

## Project Structure
```
genshin-build-guide/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── routes/          # API endpoints
│   │   ├── schemas/         # Pydantic validation
│   │   ├── middleware/      # Auth middleware
│   │   ├── database.py      # DB setup
│   │   ├── config.py        # Settings
│   │   └── main.py          # FastAPI app
│   ├── scripts/
│   │   └── seed_characters.py
│   ├── static/              # Uploaded images
│   ├── requirements.txt
│   └── run.py
│
├── frontend/
│   ├── src/
│   │   ├── app/            # Next.js pages
│   │   ├── components/     # React components
│   │   ├── lib/           # API client, auth
│   │   └── types/         # TypeScript types
│   ├── cypress/
│   │   └── e2e/           # Test files
│   ├── package.json
│   └── .env.local
│
└── README.md
```

---

## Known Issues / Future Improvements

- [ ] No admin panel yet (guides are auto-approved)
- [ ] Could add edit/delete functionality
- [ ] Could add user registration
- [ ] Image preview before upload would be nice
- [ ] Search functionality for guides

---

## Resources Used

- Genshin Impact Character API: https://genshin.jmp.blue/
- FastAPI Documentation: https://fastapi.tiangolo.com/
- Next.js Documentation: https://nextjs.org/docs
- Cypress Documentation: https://docs.cypress.io/
- Tailwind CSS: https://tailwindcss.com/

---

## Notes

- Character data is fetched from a public API and seeded into the database
- All uploaded images are stored in `backend/app/static/build_pics/`
- The database file is `backend/genshin_builds.db`
- JWTs expire after 24 hours
- Guides are set to "pending" status when created (for future admin approval feature)

---

## Troubleshooting

**Backend won't start:**
- Make sure virtual environment is activated
- Try: `pip install -r requirements.txt` again

**Frontend won't start:**
- Delete `.next` folder and `node_modules`
- Run `npm install` again

**Tests failing:**
- Make sure BOTH backend and frontend are running
- Clear browser cache
- Try: `localStorage.clear()` in browser console

**Can't login:**
- Check backend terminal for errors
- Make sure you're using: test@t.ca / 123456Pw

**Database errors:**
- Delete `genshin_builds.db` and run seed script again

---
