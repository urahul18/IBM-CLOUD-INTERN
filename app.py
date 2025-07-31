import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ibm_watson_machine_learning import APIClient

# Load environment variables
load_dotenv()

app = Flask(__name__)

# IBM Watson ML configuration
wml_credentials = {
    "url": os.getenv("IBM_WATSON_ML_URL"),
    "apikey": os.getenv("IBM_WATSON_ML_API_KEY")
}

project_id = os.getenv("IBM_WATSON_ML_PROJECT_ID")

class RecipeAgent:
    def __init__(self):
        self.client = APIClient(wml_credentials)
        self.client.set.default_project(project_id)
        
    def generate_recipe(self, ingredients):
        """Generate a recipe using IBM Granite LLM"""
        
        # Create a detailed prompt for recipe generation
        prompt = f"""
        Create a detailed recipe using the following ingredients: {ingredients}

        Please provide:
        1. Recipe Name
        2. Preparation Time
        3. Cooking Time
        4. Servings
        5. Complete ingredient list with measurements
        6. Step-by-step cooking instructions
        7. Cooking tips and tricks
        8. Possible ingredient substitutions
        9. Nutritional highlights

        Format the response in a clear, easy-to-follow structure.
        """

        # Model parameters for IBM Granite
        model_params = {
            "decoding_method": "greedy",
            "max_new_tokens": 1000,
            "temperature": 0.7,
            "top_p": 0.9,
            "repetition_penalty": 1.1
        }

        try:
            # Generate text using IBM Granite model
            response = self.client.foundation_models.generate_text(
                model_id="ibm/granite-13b-chat-v2",
                prompt=prompt,
                params=model_params
            )
            
            return response
            
        except Exception as e:
            return f"Error generating recipe: {str(e)}"

# Initialize the recipe agent
recipe_agent = RecipeAgent()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    """Generate recipe from ingredients"""
    try:
        data = request.get_json()
        ingredients = data.get('ingredients', '')
        
        if not ingredients.strip():
            return jsonify({'error': 'Please provide ingredients'}), 400
        
        # Generate recipe using IBM Granite
        recipe = recipe_agent.generate_recipe(ingredients)
        
        return jsonify({
            'success': True,
            'recipe': recipe,
            'ingredients_used': ingredients
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'Recipe Preparation Agent'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)