import os


package_name = "{{ cookiecutter.project_slug }}"
*namespaces, base_name = package_name.split(".")

if namespaces:
    # We need to create the namespace directories and rename the inner directory
    directory = "src"
    existing_inner_directory = os.path.join("src", package_name)
    innermost_namespace_directory = os.path.join("src", *namespaces)
    os.mkdir(innermost_namespace_directory)
    # Rename the inner directory and move it into the last created directory
    os.rename(
        inner_directory,
        os.path.join(innermost_namespace_directory, base_name)
    )
