# Brent Oil Price Dashboard

An interactive dashboard application for analyzing Brent oil price trends and their correlation with various events. Built with Flask (backend) and React (frontend).

## Features

### Backend (Flask)
- **RESTful APIs** for serving oil price data and analysis results
- **Data generation** with realistic oil price patterns and event impacts
- **Statistical analysis** including moving averages, volatility, and trend analysis
- **Forecasting capabilities** with confidence intervals
- **Event impact analysis** showing how different events affect oil prices

### Frontend (React)
- **Interactive price charts** with event markers and tooltips
- **Real-time statistics** displaying key metrics and price changes
- **Events timeline** with filtering by event type
- **Volatility analysis** with moving averages visualization
- **Price forecasting** with confidence intervals
- **Date range filtering** for custom time periods
- **Responsive design** for desktop, tablet, and mobile devices

## Key Components

### Dashboard Sections
1. **Main Price Chart** - Interactive line chart showing Brent oil prices with event markers
2. **Statistics Card** - Key metrics including current price, averages, and price changes
3. **Events Timeline** - Chronological list of events with impact analysis
4. **Volatility Chart** - Moving averages and volatility trends
5. **Forecast Chart** - 30-day price predictions with confidence intervals

### Event Types
- **Crisis Events** (COVID-19, Oil Price War) - Red markers
- **Conflict Events** (Russia-Ukraine War, Israel-Hamas) - Orange markers
- **Economic Events** (OPEC+ cuts, Production changes) - Blue markers
- **Political Events** (Elections, Policy changes) - Purple markers
- **Logistics Events** (Shipping crises, Supply disruptions) - Green markers

## Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```

5. **Run Flask server:**
   ```bash
   python app.py
   ```

The backend will start on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start React development server:**
   ```bash
   npm start
   ```

The frontend will start on `http://localhost:3000`

## API Endpoints

### Data Endpoints
- `GET /api/health` - Health check
- `GET /api/data` - Oil price data (supports date filtering)
- `GET /api/events` - Events data with impacts
- `GET /api/statistics` - Statistical summary
- `GET /api/analysis` - Analysis results (moving averages, volatility)
- `GET /api/forecast` - 30-day price forecast

### Query Parameters
- `start_date` - Filter data from this date (YYYY-MM-DD)
- `end_date` - Filter data to this date (YYYY-MM-DD)

## Usage

### Dashboard Features

1. **Date Filtering**
   - Use the date picker in the header to select custom date ranges
   - Quick filter buttons for common periods (7D, 30D, 3M, 6M, 1Y, All)

2. **Interactive Charts**
   - Hover over data points to see detailed information
   - Click on event markers to highlight specific events
   - Zoom and pan on charts for detailed analysis

3. **Event Analysis**
   - Filter events by type using the timeline filters
   - View impact percentages and price changes
   - Compare different event types and their effects

4. **Statistical Insights**
   - Monitor current price and historical trends
   - Track volatility and moving averages
   - Analyze price changes over different time periods

### Sample Events Included
- COVID-19 Pandemic (2020-03-15) - Crisis event
- Oil Price War (2020-04-20) - Crisis event
- Biden Inauguration (2021-01-20) - Political event
- Russia-Ukraine War (2022-02-24) - Conflict event
- OPEC+ Production Cut (2022-10-05) - Economic event
- Saudi Arabia Production Cut (2023-04-02) - Economic event
- Israel-Hamas Conflict (2023-10-07) - Conflict event
- Red Sea Shipping Crisis (2024-01-15) - Logistics event

## Technology Stack

### Backend
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning for forecasting

### Frontend
- **React** - UI framework
- **Recharts** - Chart library
- **Styled-components** - CSS-in-JS styling
- **Axios** - HTTP client
- **React DatePicker** - Date selection component
- **Framer Motion** - Animations
- **React Icons** - Icon library

## Project Structure

```
├── backend/
│   └── app.py                 # Flask application
├── frontend/
│   ├── public/
│   │   └── index.html         # HTML template
│   ├── src/
│   │   ├── components/        # React components
│   │   │   ├── PriceChart.js
│   │   │   ├── StatisticsCard.js
│   │   │   ├── EventsTimeline.js
│   │   │   ├── ForecastChart.js
│   │   │   ├── VolatilityChart.js
│   │   │   └── DateFilter.js
│   │   ├── App.js            # Main React component
│   │   ├── index.js          # React entry point
│   │   └── index.css         # Global styles
│   └── package.json          # Frontend dependencies
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## Development

### Adding New Events
To add new events, modify the `events` dictionary in `backend/app.py`:

```python
events = {
    '2024-06-15': {
        'name': 'New Event Name',
        'impact': 10,  # Percentage impact
        'type': 'economic'  # Event type
    }
}
```

### Customizing Charts
Modify the chart components in `frontend/src/components/` to:
- Change colors and styling
- Add new chart types
- Customize tooltips and interactions

### Extending Analysis
Add new analysis endpoints in `backend/app.py`:
- Additional statistical measures
- New forecasting models
- Custom event impact calculations

## Deployment

### Backend Deployment
1. Install production dependencies: `pip install gunicorn`
2. Run with Gunicorn: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`

### Frontend Deployment
1. Build for production: `npm run build`
2. Serve static files with a web server (nginx, Apache)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and demonstration purposes.

## Support

For issues or questions, please create an issue in the repository. 