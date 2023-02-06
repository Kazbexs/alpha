import xml.etree.ElementTree as ET


# read for test
def read_xes():
    file = open("/Users/kazbexs/Documents/Project/kazbexs/flask-server/L1.xes", "rb")
    data = file.read()
    file.close()
    return data

#########################

def get_info_from_trace(trace):
    events = trace.findall("{http://www.xes-standard.org/}event")
    result = []
    for event in events:
        result.append(event[2].get('value'))

    return tuple(result)


def read_data(data):
    tree = ET.fromstring(data)

    traces = tree.findall("{http://www.xes-standard.org/}trace")

    log = []
    for trace in traces:
        events = get_info_from_trace(trace)
        log.append(events)

    return log
