#include <Python.h>

static PyObject* greet(PyObject* self, PyObject* args)
{
    const char* name;

    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;

    printf("Hello %s\n", name);

    Py_RETURN_NONE;
}

static PyMethodDef HelloMethods[] = {
    {"greet", greet, METH_VARARGS, "Greet somebody (in C)."},
    {NULL, NULL, 0, NULL}  /* Sentinel */
};

PyMODINIT_FUNC
inithello(void)
{
    (void) Py_InitModule("hello", HelloMethods);
}
