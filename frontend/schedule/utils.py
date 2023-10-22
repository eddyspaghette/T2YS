from datetime import datetime

from .models import Event
from .predict_model.main import predict


def get_new_event(prompt):
    output = predict(prompt)

    if (output["name"] is None or output["start_time"] is None or output["end_time"] is None):
        return

    start_time = datetime.strptime("%Y-%m-%dT%H:%M:%S", output["start_time"])
    end_time = datetime.strptime("%Y-%m-%dT%H:%M:%S", output["end_time"])
        
    Event.objects.create(name=output["name"], start_time=start_time, end_time=end_time)
