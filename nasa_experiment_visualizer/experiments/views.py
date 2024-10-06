# views.py
from django.shortcuts import render, redirect
from .models import Experiment  # Import the Experiment model



def graphs(request):
    # You can add logic here if needed
    return render(request, 'graphs.html')# Render the appropriate template

def form(request):
    return render(request, 'form.html')# Render the appropriate template


def results(request):
    # You can add logic here if needed
    return render(request, 'results.html')# Render the appropriate template

def result(request):
    # You can add logic here if needed
    return render(request, 'result.html')# Render the appropriate template

def evaluation(request):
    # You can add logic here if needed
    return render(request, 'evaluation.html')# Render the appropriate template

def experiment_create(request):
    if request.method == 'GET':
        return render(request, 'experiment_list.html')

    if request.method == 'POST':
        experiment_id = request.POST.get('experiment_id')  # Unique ID from the form
        experiment_title = request.POST.get('experiment_name')  # Name of the experiment
        experiment_file = request.FILES.get('experiment_file')  # Uploaded file

        try:
            # Ensure the correct keyword arguments are used
            experiment = Experiment(
                id=experiment_id,  # Set the unique ID
                title=experiment_title,  # Correctly set the title
                file=experiment_file  # Set the file
            )
            experiment.save()  # Save the experiment instance to the database
            if experiment_file.name == 'OSD-379.txt':
                return redirect('result')  # Redirect to result page if a.txt is uploaded
            elif experiment_file.name == 'OSD-665.txt':
                return redirect('results')  # Redirect to evaluation page if b.txt is uploaded
            else:
                return redirect('result')
        except Exception as e:
            print(f"Error creating experiment: {e}")  # Print the error for debugging
            return render(request, 'experiment_list.html')  # Render the form again on error

    return render(request, 'result.html')  # Render the form if GET request

