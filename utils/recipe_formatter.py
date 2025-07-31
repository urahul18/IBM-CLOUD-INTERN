import re
from typing import Dict, List

class RecipeFormatter:
    """Utility class for formatting and parsing recipe content"""
    
    @staticmethod
    def parse_recipe_sections(recipe_text: str) -> Dict[str, str]:
        """Parse recipe text into structured sections"""
        sections = {
            'name': '',
            'prep_time': '',
            'cook_time': '',
            'servings': '',
            'ingredients': [],
            'instructions': [],
            'tips': [],
            'substitutions': []
        }
        
        lines = recipe_text.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Detect section headers
            lower_line = line.lower()
            if 'recipe name' in lower_line or line.startswith('Recipe:'):
                current_section = 'name'
            elif 'prep' in lower_line and 'time' in lower_line:
                current_section = 'prep_time'
            elif 'cook' in lower_line and 'time' in lower_line:
                current_section = 'cook_time'
            elif 'serving' in lower_line:
                current_section = 'servings'
            elif 'ingredient' in lower_line:
                current_section = 'ingredients'
            elif 'instruction' in lower_line or 'step' in lower_line:
                current_section = 'instructions'
            elif 'tip' in lower_line:
                current_section = 'tips'
            elif 'substitution' in lower_line:
                current_section = 'substitutions'
            else:
                # Add content to current section
                if current_section and line:
                    if current_section in ['ingredients', 'instructions', 'tips', 'substitutions']:
                        sections[current_section].append(line)
                    else:
                        sections[current_section] = line
        
        return sections
    
    @staticmethod
    def format_for_display(recipe_text: str) -> str:
        """Format recipe text for better display"""
        # Clean up the text
        recipe_text = re.sub(r'\n\s*\n', '\n\n', recipe_text)  # Remove extra blank lines
        recipe_text = re.sub(r'^\s+', '', recipe_text, flags=re.MULTILINE)  # Remove leading spaces
        
        return recipe_text
    
    @staticmethod
    def extract_cooking_time(recipe_text: str) -> Dict[str, str]:
        """Extract cooking times from recipe text"""
        times = {'prep_time': '', 'cook_time': '', 'total_time': ''}
        
        # Look for time patterns
        time_patterns = [
            r'prep(?:aration)?\s*time[:\s]*(\d+(?:\s*-\s*\d+)?\s*(?:min|minute|hour|hr)s?)',
            r'cook(?:ing)?\s*time[:\s]*(\d+(?:\s*-\s*\d+)?\s*(?:min|minute|hour|hr)s?)',
            r'total\s*time[:\s]*(\d+(?:\s*-\s*\d+)?\s*(?:min|minute|hour|hr)s?)'
        ]
        
        for i, pattern in enumerate(time_patterns):
            match = re.search(pattern, recipe_text, re.IGNORECASE)
            if match:
                time_keys = ['prep_time', 'cook_time', 'total_time']
                times[time_keys[i]] = match.group(1)
        
        return times
    
    @staticmethod
    def extract_servings(recipe_text: str) -> str:
        """Extract serving information from recipe text"""
        serving_patterns = [
            r'serves?\s*:?\s*(\d+(?:\s*-\s*\d+)?)',
            r'serving(?:s)?[:\s]*(\d+(?:\s*-\s*\d+)?)',
            r'yield[:\s]*(\d+(?:\s*-\s*\d+)?)'
        ]
        
        for pattern in serving_patterns:
            match = re.search(pattern, recipe_text, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return ''
    
    @staticmethod
    def validate_ingredients(ingredients: List[str]) -> List[str]:
        """Validate and clean ingredient list"""
        cleaned_ingredients = []
        
        for ingredient in ingredients:
            ingredient = ingredient.strip()
            if ingredient and len(ingredient) > 1:
                # Remove common prefixes
                ingredient = re.sub(r'^[-•*]\s*', '', ingredient)
                cleaned_ingredients.append(ingredient)
        
        return cleaned_ingredients
    
    @staticmethod
    def generate_recipe_summary(recipe_text: str) -> Dict[str, any]:
        """Generate a summary of the recipe"""
        formatter = RecipeFormatter()
        sections = formatter.parse_recipe_sections(recipe_text)
        times = formatter.extract_cooking_time(recipe_text)
        servings = formatter.extract_servings(recipe_text)
        
        return {
            'name': sections.get('name', 'Delicious Recipe'),
            'prep_time': times.get('prep_time', ''),
            'cook_time': times.get('cook_time', ''),
            'total_time': times.get('total_time', ''),
            'servings': servings,
            'ingredient_count': len(sections.get('ingredients', [])),
            'instruction_count': len(sections.get('instructions', [])),
            'has_tips': len(sections.get('tips', [])) > 0,
            'has_substitutions': len(sections.get('substitutions', [])) > 0
        }