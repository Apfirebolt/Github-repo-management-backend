def handle_uploaded_file(f):
    with open('media/forum_videos/' + str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)