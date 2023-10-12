#include <Python.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 *
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	const char *type_name;
	int ob_size, allocated, idx;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;

	ob_size = var->ob_size;
	allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", ob_size);
	printf("[*] Allocated = %d\n", allocated);

	for (idx = 0; idx < ob_size; idx++)
	{
		type_name = list->ob_item[idx]->ob_type->tp_name;
		printf("Element %d: %s\n", idx, type_name);
		if (strcmp(type_name, "bytes") == 0)
			print_python_bytes(list->ob_item[idx]);
	}
}


/**
 * print_python_bytes - Prints basic info about Python byte objects.
 *
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char idx, ob_size;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  ob_size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		ob_size = 10;
	else
		ob_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", ob_size);
	for (idx = 0; idx < ob_size; idx++)
	{
		printf("%02hhx", bytes->ob_sval[idx]);
		if (idx == (ob_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
