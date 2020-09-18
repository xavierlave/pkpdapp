#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#


from django.shortcuts import render


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
