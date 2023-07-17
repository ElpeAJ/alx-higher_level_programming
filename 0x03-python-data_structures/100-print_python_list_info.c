#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Print the size and memory
 * allocated for a list w/ elements types inclusive.
 * @p: A pointer 
 *
 **/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = 0, index = 0;

	list_size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	while (index < list_size)
	{
		printf("Element %ld: %s\n", index, Py_TYPE(PyList_GetItem(p, index))->tp_name);
		index++;
	}
}
