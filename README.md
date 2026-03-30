
# GreenGo 🌱

**GreenGo** is a community-driven web platform that combines AI, satellite imagery, and citizen science to map, 
track, and enhance local biodiversity. Users can visualize their neighborhood's flora and fauna, contribute 
observations, and engage in sustainable community projects.  
---

## 🌟 Features

- **Satellite Analysis**: Uses NDMI indices to track vegetation health via Google Earth Engine.
- **Community Contributions**: Upload images of plants and animals, automatically labeled using AI.
- **Interactive Maps**: Map-based visualization of community biodiversity (future version: pins for each observation).
- **Events & Engagement**: Participate in community sustainability events.
- **Optional TTS**: Text-to-speech integration for accessibility or audio summaries (Coqui TTS / Piper recommended).

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React + Vite |
| Backend | Django + Django REST Framework |
| Database | PostgreSQL / SQLite (dev) |
| Cloud / Storage | AWS S3 for images, AWS EC2 or RDS optional |
| AI / ML | Custom Computer Vision models, Coqui TTS or Piper for voice |
| Maps / Geospatial | Google Maps API (or Leaflet + OpenStreetMap for free) |
| APIs | Google Earth Engine, optional TTS API |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/greengo.git
cd greengo
````

### 2. Backend setup (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Mac/Linux
# or venv\Scripts\activate for Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # create admin
python manage.py runserver
```

### 3. Frontend setup (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser.

---

## ⚙ Configuration

### Environment Variables (`.env`)

```env
# Backend
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:pass@localhost:5432/dbname

# AWS
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name

# Google Maps
REACT_APP_GOOGLE_MAPS_API_KEY=your_api_key
```

---

## 🖼 Using AI for Plant Identification

1. Upload images of plants/animals via the frontend.
2. Django sends them to the AI model (local or cloud).
3. The model returns labels → stored in database and shown on maps.

> Recommended for MVP: **Coqui TTS / Piper for optional audio features**
> Paid alternatives: AWS Rekognition, Google Vision API.

---

## 🗺 Maps Integration

* **Google Maps API**: Freemium with $200 monthly credit
* **Leaflet + OpenStreetMap**: Free alternative

---

## 💡 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push branch: `git push origin feature-name`
5. Open a Pull Request

---

## 📝 Roadmap

* [ ] Map pins for uploaded flora/fauna
* [ ] Advanced AI recognition for rare species
* [ ] Community event participation module
* [ ] Text-to-speech voice summaries
* [ ] Mobile responsive design improvements

---

## 📖 References

* [Google Earth Engine](https://earthengine.google.com/)
* [Coqui TTS](https://tts.coqui.ai/)
* [Leaflet Maps](https://leafletjs.com/)
* [OpenStreetMap](https://www.openstreetmap.org/)
* [Google Maps Platform](https://developers.google.com/maps/documentation/javascript/overview)

---

## 📝 License

This project is licensed under the **MIT License**.

---
