

import struct


def bytesToScalar(data_bytes, sign='f', bytes_per_data=4):

    data = struct.unpack("{}{}".format(len(data_bytes) // bytes_per_data, sign), data_bytes)
    return data

def read(file, bytes_per_data=4, sign='f'):
    """Read binary data from file
    
    Arguments:
        file {file or str} -- File object or filepath
    
    Keyword Arguments:
        bytes_per_data {int} -- each element occupies how many bytes (default: {4})
        sign {str} -- indicates data type to extract (default: {'f'})
    
    Returns:
        data -- list of elements
    """

    file_need_close = False
    if isinstance(file, str):
        file = open(file, 'rb')
        file_need_close = True

    content = file.read()
    data = bytesToScalar(content, sign=sign, bytes_per_data=bytes_per_data)

    if file_need_close:
        file.close()
    
    return data



def scalarToBytes(data, sign='f'):
    
    if not isinstance(data, list or tuple):
        data = [data]
    if isinstance(data[0], int):
        sign = 'i'
    else:
        raise NotImplementedError("cannot recognize data-type [{}].".format(type(data[0])))
    
    data_bytes = struct.pack("{}{}".format(len(data), sign), *data)
    return data_bytes


def write(file, data):
    """Write data to file
    
    Arguments:
        file {file/str} -- File object or filepath
        data {scalar or list of scaler} -- data to be saved, only supported built-in scalar type
    """

    file_need_close = False
    if isinstance(file, str):
        file = open(file, 'wb+')
        file_need_close = True
    
    data_bytes = scalarToBytes(data)
    file.write(data_bytes)

    if file_need_close:
        file.close()
    
