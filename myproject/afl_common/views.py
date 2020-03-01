from django.shortcuts import render

################# Error Page ######################

def error_view(request):
	return render(request,'includes/404.html',status=404)

################# Generic page ###################

def generic(request):
	return render(request,'watch/generic.html')	

# def load_states(request):
#     country_id = request.GET.get('country')
#     states = State.objects.filter(country_id=country_id).order_by('name')
#     return render(request, 'includes/states_dropdown.html', {'states': states})	