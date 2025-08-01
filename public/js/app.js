class RecipeApp {
    constructor() {
        this.initializeElements();
        this.bindEvents();
    }

    initializeElements() {
        this.ingredientsInput = document.getElementById('ingredients');
        this.generateBtn = document.getElementById('generateBtn');
        this.enterBtn = document.getElementById('enterBtn');
        this.clearBtn = document.getElementById('clearBtn');
        this.copyBtn = document.getElementById('copyBtn');
        this.loading = document.getElementById('loading');
        this.recipeOutput = document.getElementById('recipeOutput');
        this.recipeContent = document.getElementById('recipeContent');
        this.usedIngredients = document.getElementById('usedIngredients');
        this.errorOutput = document.getElementById('errorOutput');
        this.errorMessage = document.getElementById('errorMessage');
    }

    bindEvents() {
        this.generateBtn.addEventListener('click', () => this.generateRecipe());
        this.enterBtn.addEventListener('click', () => this.generateRecipe());
        this.clearBtn.addEventListener('click', () => this.clearAll());
        this.copyBtn.addEventListener('click', () => this.copyRecipe());
        
        // Allow Enter key to generate recipe (Ctrl+Enter for new line)
        this.ingredientsInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.ctrlKey) {
                e.preventDefault();
                this.generateRecipe();
            }
        });
    }

    async generateRecipe() {
        const ingredients = this.ingredientsInput.value.trim();
        
        if (!ingredients) {
            this.showError('Please enter some ingredients first!');
            return;
        }

        this.showLoading();
        
        try {
            const response = await fetch('/generate-recipe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ingredients })
            });

            const data = await response.json();

            if (data.success || data.fallback) {
                this.showRecipe(data.recipe, data.ingredients_used);
                if (data.fallback) {
                    console.log('Using fallback recipe generation');
                }
            } else {
                this.showError(data.error || 'Failed to generate recipe');
            }
        } catch (error) {
            this.showError('Network error: ' + error.message);
        }
    }

    showLoading() {
        this.hideAllOutputs();
        this.loading.classList.remove('hidden');
        this.generateBtn.disabled = true;
        this.enterBtn.disabled = true;
        this.generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Generating...';
    }

    showRecipe(recipe, ingredients) {
        this.hideAllOutputs();
        this.recipeContent.innerHTML = this.formatRecipe(recipe);
        this.usedIngredients.textContent = ingredients;
        this.recipeOutput.classList.remove('hidden');
        this.resetGenerateButton();
    }

    showError(message) {
        this.hideAllOutputs();
        this.errorMessage.textContent = message;
        this.errorOutput.classList.remove('hidden');
        this.resetGenerateButton();
    }

    hideAllOutputs() {
        this.loading.classList.add('hidden');
        this.recipeOutput.classList.add('hidden');
        this.errorOutput.classList.add('hidden');
    }

    resetGenerateButton() {
        this.generateBtn.disabled = false;
        this.enterBtn.disabled = false;
        this.generateBtn.innerHTML = '<i class="fas fa-magic mr-2"></i>Generate Recipe';
    }

    formatRecipe(recipe) {
        // Convert plain text recipe to formatted HTML
        const lines = recipe.split('\n');
        let formattedHtml = '';
        let inList = false;

        for (let line of lines) {
            line = line.trim();
            if (!line) continue;

            // Check for headers (lines that end with : or are all caps)
            if (line.endsWith(':') || (line === line.toUpperCase() && line.length > 3)) {
                if (inList) {
                    formattedHtml += '</ol>';
                    inList = false;
                }
                formattedHtml += `<h3 class="text-xl font-semibold text-gray-800 mt-6 mb-3">${line}</h3>`;
            }
            // Check for numbered steps
            else if (/^\d+\./.test(line)) {
                if (!inList) {
                    formattedHtml += '<ol class="list-decimal list-inside space-y-2 ml-4">';
                    inList = true;
                }
                formattedHtml += `<li class="text-gray-700">${line.replace(/^\d+\.\s*/, '')}</li>`;
            }
            // Check for bullet points
            else if (line.startsWith('•') || line.startsWith('-') || line.startsWith('*')) {
                if (inList) {
                    formattedHtml += '</ol>';
                    inList = false;
                }
                formattedHtml += `<ul class="list-disc list-inside space-y-1 ml-4"><li class="text-gray-700">${line.substring(1).trim()}</li></ul>`;
            }
            // Regular paragraph
            else {
                if (inList) {
                    formattedHtml += '</ol>';
                    inList = false;
                }
                formattedHtml += `<p class="text-gray-700 mb-3">${line}</p>`;
            }
        }

        if (inList) {
            formattedHtml += '</ol>';
        }

        return formattedHtml;
    }

    clearAll() {
        this.ingredientsInput.value = '';
        this.hideAllOutputs();
        this.ingredientsInput.focus();
    }

    async copyRecipe() {
        const recipeText = this.recipeContent.innerText;
        
        try {
            await navigator.clipboard.writeText(recipeText);
            
            // Show success feedback
            const originalText = this.copyBtn.innerHTML;
            this.copyBtn.innerHTML = '<i class="fas fa-check mr-2"></i>Copied!';
            this.copyBtn.classList.remove('bg-blue-500', 'hover:bg-blue-600');
            this.copyBtn.classList.add('bg-green-500');
            
            setTimeout(() => {
                this.copyBtn.innerHTML = originalText;
                this.copyBtn.classList.remove('bg-green-500');
                this.copyBtn.classList.add('bg-blue-500', 'hover:bg-blue-600');
            }, 2000);
        } catch (error) {
            console.error('Failed to copy recipe:', error);
            alert('Failed to copy recipe to clipboard');
        }
    }
}

// Initialize the app when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new RecipeApp();
});