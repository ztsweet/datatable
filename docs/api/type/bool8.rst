
.. xattr:: datatable.Type.bool8
    :src: --

    The type of a column with boolean data.

    In a column of this type each data element is stored as 1 byte. NA values
    are also supported.

    The boolean type is considered numeric, where ``True`` is 1 and ``False``
    is 0.


    Examples
    --------
    >>> dt.Frame([True, False, None]).types
    [Type.bool8]
