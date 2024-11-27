from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

def index(request):
	return render (request,'register.html')

def display (request):
	if request.method == "POST":
		Student_ID = request.POST.get('student_id')
		Roll_No = request.POST.get('roll_no')

		return render(request, 'display.html', {'Student_ID' : Student_ID, 'Roll_No' : Roll_No})

	else:
		return render(request, 'display.html')

#def display (request):
#	students = [
#		{'Student_ID' : 'Devaa', 'Roll_No' : 99},
#		{'Student_ID' : 'Manushi', 'Roll_No' : 100},
#		{'Student_ID' : 'Dev', 'Roll_No' : 101},
#	]
#	return render (request, 'display.html', {'students' : students})