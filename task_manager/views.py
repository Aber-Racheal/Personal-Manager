from django.shortcuts import render, redirect, get_object_or_404
# 'render' is used to display an HTML template in the web UI.
# 'redirect' is used to navigate the user to another page after an action is completed.

from .forms import CreateTask  
# This imports the 'CreateTask' form from forms.py, which is used to create and manage task input fields.

from .models import Task  
# This imports the 'Task' model from models.py, which defines the structure of the task data stored in the database.

from django.utils import timezone  
# This module provides timezone support, helping to work with timezone-aware date and time, useful for task timestamps.

from django.contrib import messages  
# This module allows sending temporary messages (e.g., success, error) to users after actions like form submission.

from datetime import timedelta

###The views file helps us define the logic/functionality of our application. It helps us interact with our database, make querries for 
#everything we need. 
#In this case we are using function based views, but we can also use class-based views

def CreatingTask(request):
#we take in a requesst as our parameter. This is because when a user says they want to create a task, that is definitely a request
#We then check that request type, is it a post? is it DELETE? etc. In this case its a POST 
    if request.method == 'POST':
#if its a POST, we then allow the user to create their task 
#we add the request.FILES since in the form, the user is also allowed to upload a file in this case an image.
#the CreateTask is a class in the forms.py file
        form = CreateTask(request.POST, request.FILES)
#so before we store the form data in our db, we have to check if it matches our predefined criteria in our models.py that is 
#we use the python in-built method called is_valid()           
        if form.is_valid():
#if the form is valid, we now go ahead to perform other checks that we didnot define in the db, such as ensuring a deadline is not set 
#an already past date.
            task_deadline = form.cleaned_data.get('task_deadline')
            if task_deadline <= timezone.now():
                messages.error(request, "Task deadline must be a valid future date")
                return redirect('CreatingTask')  # redirect back to the form
#if the form has passed the checks, we can now save the form data to our db with the save() function and then send the user to the page
#displaying the lists of tasks.
            form.save()
            return redirect('TaskList') 
#so if the user request is not a POST, then just let the form be displayed on the UI.    
    else:
        form = CreateTask()  #create an empty form for GET request   
    return render (request, 'create_task.html', {'form': form})

def DeleteTask(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        # Move task to trash (update is_in_trash field)
        task.is_in_trash = True
        task.save()

        messages.success(request, "Task moved to trash.")
        return redirect('TaskList')  # Redirect back to the task list
    
    return render(request, 'confirm_delete.html', {'task': task})
 
def TaskList(request): 
    tasks = Task.objects.filter(is_in_trash = False)  #fetch all tasks from the database
    current_time = timezone.now()
    # if Task.task_deadline == that day's date, then set the task status as deadline expired
    
    
    for task in tasks:
        if task.task_deadline:
            # Check if the task is overdue
            if task.task_deadline < current_time and task.task_status != 'complete':
                task.task_status = 'overdue'
                task.save()  # Save the updated status to the database
                messages.warning(request, f"Task '{task.task_title}' is overdue!")

            # Check if the task is approaching its deadline (within 5 days)
            elif task.task_deadline <= current_time + timedelta(days=5) and task.task_status != 'complete':
                messages.info(request, f"Reminder: Task '{task.task_title}' is due soon on {task.task_deadline.strftime('%Y-%m-%d')}.")
    return render(request, 'task_list.html', {'tasks': tasks})  #pass tasks to template
    
        
def TrashList(request):
    # Fetch all tasks that are in the trash
    tasks_in_trash = Task.objects.filter(is_in_trash=True)
    return render(request, 'trash_list.html', {'tasks': tasks_in_trash})
    
    
def RestoreTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_in_trash = False  # Restore task by setting is_in_trash to False
    task.save()
    messages.success(request, "Task restored.")
    return redirect('TrashList')  # Redirect to the Trash page

def DeletePermanently(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.success(request, "Task deleted permanently.")
    return redirect('TrashList')  # Redirect to the Trash page
    

def ViewTask(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'view_task.html', {'task': task})


def EditTask(request, id):
    task = get_object_or_404(Task, id=id)
    
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('ViewTask', id=task.id)  # Redirect to view the updated task
    else:
        form = CreateTask(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})


# def SendNotification(request, task_deadline):
#     if task_deadline < task_deadline-5 and task_deadline != or !> task_deadline:  timenow():
#         send a reminder to a suer, that their tak deadline is closing in this number of days