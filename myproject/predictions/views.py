from django.shortcuts import render
from .forms import PredictionForm
import pickle

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            numbers = form.cleaned_data['numbers']
            something = form.cleaned_data['something']
            
            # Make prediction
            input_data = [[numbers, something]]
            prediction = model.predict(input_data)
            
            return render(request, 'predictions/result.html', {'prediction': prediction[0]})
    else:
        form = PredictionForm()
    
    return render(request, 'predictions/predict.html', {'form': form})
