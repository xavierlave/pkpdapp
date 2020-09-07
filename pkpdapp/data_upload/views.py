from django.shortcuts import render

from .forms import DataForm


# TODO: TO BE DELETED
def upload_file_view(request):
    # Create form
    form = DataForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        # Save form
        form.save()

        # Reset form
        form = DataForm(request.POST or None, request.FILES or None)

    context = {'form': form}

    return render(request, 'data_upload/upload.html', context)
