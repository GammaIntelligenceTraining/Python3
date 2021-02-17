with open('text_files//python.jpg', 'rb') as rfile:
    with open('text_files//python_copy.jpg', 'wb') as wfile:
        chunk_size = 4096
        rfile_chunk = rfile.read(chunk_size)
        while len(rfile_chunk) > 0:
            wfile.write(rfile_chunk)
            rfile_chunk = rfile.read(chunk_size)