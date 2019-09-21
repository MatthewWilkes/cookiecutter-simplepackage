import os


package_name = "{{ cookiecutter.project_slug }}"
*namespaces, base_name = package_name.split(".")

if namespaces:
    # We need to create the namespace directories and rename the inner directory
    directory = "src"
    for namespace in namespaces:
        # Create a directory for each namespace in turn
        directory = os.path.join(directory, namespace)
        os.mkdir(directory)
    # Rename the inner directory and move it into the last created directory
    inner_directory = os.path.join("src", package_name)
    os.rename(inner_directory, os.path.join(directory, base_name))
