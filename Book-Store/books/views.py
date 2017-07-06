from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from books.models import Catalog

class ServerForm(ModelForm):
    class Meta:
        model = Catalog
        fields = ['name', 'slug', 'publisher','description','pub_date']

def server_list(request, template_name='books/server_list.html'):
    servers = Catalog.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

def server_create(request, template_name='books/server_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def server_update(request, pk, template_name='books/server_form.html'):
    server = get_object_or_404(Catalog, pk=pk)
    form = ServerForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def server_delete(request, pk, template_name='books/server_confirm_delete.html'):
    server = get_object_or_404(Catalog, pk=pk)    
    if request.method=='POST':
        server.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':server})
