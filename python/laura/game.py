
def render_location(l_id, locations):
    current_location = locations[l_id]

    cl_name = current_location['name']
    cl_desc = current_location['description']
    cl_path = current_location['path']
    cl_avail = current_location['rooms']

    if cl_name.lower() == "bedroom":
        cl_name = "You are in your bedroom."

    if len(cl_avail) > 1:

    data = []
    data.append(cl_name)
    data.append(cl_desc)
    data.append(cl_path)
    data.append(cl_avail)
    return data

