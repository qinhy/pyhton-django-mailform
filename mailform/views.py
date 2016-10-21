from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import sendMail

def index(request):
	return HttpResponse('''Hello, world. You're at the mailform index. <a href="contact" class='btn btn-lg'>contact</a>''')
def contact(request):
	#return HttpResponse('''Hello, world. You're at the contact page. <a href="../" class='btn btn-lg'>index</a>''')
	template = loader.get_template('mailform/contact.html')
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
		if not request.POST.get('message', ''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if len(errors) == 0 :
			from_addr = 'ec2-user@example.com'
			to_addr = 'example@example.com'
			subject = request.POST['subject']
			body = request.POST['message']+'\n'+request.POST['email']
			encode = 'utf-8'
			msg = sendMail.create_msg(from_addr, to_addr, subject, body, encode) 
			sendMail.send_by_local(from_addr, to_addr, msg)
			return HttpResponse('Thank you, mailform has been submitted successfully.')
	context = {
		'errors': errors,
	}
	return HttpResponse(template.render(context, request))
