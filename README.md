# Recipe Preparation Agent

An AI-powered Node.js web application that transforms your available ingredients into complete, detailed recipes using IBM Granite LLM.

## Features

- **Smart Recipe Generation**: Input any combination of ingredients and get a complete recipe
- **Detailed Instructions**: Step-by-step cooking instructions that are easy to follow
- **Ingredient Substitutions**: Smart suggestions for alternative ingredients
- **Cooking Tips**: Expert tips to improve your cooking
- **Nutritional Information**: Basic nutritional highlights for your recipes
- **Modern UI**: Clean, responsive interface built with Tailwind CSS
- **Copy Functionality**: Easy recipe copying for saving or sharing

## Technology Stack

- **Backend**: Node.js with Express
- **AI Model**: IBM Granite LLM via Watson Machine Learning
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **Styling**: Tailwind CSS with custom components

## Setup Instructions

### Prerequisites

1. Node.js 16 or higher
2. IBM Cloud account with Watson Machine Learning service
3. IBM Watson Machine Learning API credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd recipe-preparation-agent
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Fill in your IBM Watson Machine Learning credentials:
     ```
     IBM_WATSON_ML_API_KEY=your_api_key_here
     IBM_WATSON_ML_URL=https://us-south.ml.cloud.ibm.com
     IBM_WATSON_ML_PROJECT_ID=your_project_id_here
     ```

4. **Run the application**
   ```bash
   npm start
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`

## How to Get IBM Watson ML Credentials

1. **Create IBM Cloud Account**
   - Go to [IBM Cloud](https://cloud.ibm.com/)
   - Sign up for a free account

2. **Create Watson Machine Learning Service**
   - In IBM Cloud dashboard, click "Create resource"
   - Search for "Watson Machine Learning"
   - Create a Lite (free) plan instance

3. **Get API Key**
   - Go to your Watson ML service instance
   - Click on "Service credentials"
   - Create new credentials if none exist
   - Copy the `apikey` value

4. **Get Project ID**
   - Go to [Watson Studio](https://dataplatform.cloud.ibm.com/)
   - Create a new project
   - In project settings, copy the Project ID

## Usage

1. **Enter Ingredients**: Type your available ingredients in the text area (e.g., "tomato, onion, rice, chicken")

2. **Generate Recipe**: Click the "Generate Recipe" button

3. **View Results**: The AI will provide:
   - Complete recipe with measurements
   - Step-by-step cooking instructions
   - Cooking tips and tricks
   - Ingredient substitutions
   - Nutritional highlights

4. **Copy Recipe**: Use the copy button to save the recipe for later use

## Example Inputs

- `"tomato, onion, rice"` → Tomato Rice Pilaf
- `"chicken, garlic, lemon, herbs"` → Herb-Crusted Lemon Chicken
- `"pasta, mushrooms, cream, parmesan"` → Creamy Mushroom Pasta
- `"eggs, spinach, cheese"` → Spinach and Cheese Omelet

## API Endpoints

- `GET /` - Main application page
- `POST /generate-recipe` - Generate recipe from ingredients
- `GET /health` - Health check endpoint

## Project Structure

```
recipe-preparation-agent/
├── server.js             # Main Express server
├── package.json          # Node.js dependencies
├── .env.example         # Environment variables template
└── public/
    ├── index.html       # Main HTML page
│   ├── js/
│   │   └── app.js       # Frontend JavaScript
│   └── css/
│       └── style.css    # Custom CSS styles
```

## Features in Detail

### AI-Powered Recipe Generation
- Uses IBM Granite LLM for intelligent recipe creation
- Considers ingredient combinations and cooking methods
- Provides creative and practical recipe suggestions

### Smart Formatting
- Automatically formats recipes for easy reading
- Organizes content into clear sections
- Highlights important information

### Responsive Design
- Works on desktop, tablet, and mobile devices
- Modern, clean interface
- Intuitive user experience

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your IBM Watson ML API key is correct
   - Check that your Watson ML service is active
   - Ensure your project ID is valid

2. **Recipe Generation Fails**
   - Check your internet connection
   - Verify IBM Cloud service status
   - Try with simpler ingredient combinations

3. **Styling Issues**
   - Ensure Tailwind CSS is loading properly
   - Check browser console for JavaScript errors
   - Clear browser cache

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Check the troubleshooting section
- Review IBM Watson ML documentation
- Create an issue in the repository

---

**Built with ❤️ using IBM Granite LLM and Flask**
