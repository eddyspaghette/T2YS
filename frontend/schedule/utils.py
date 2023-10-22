from .models import Event
from .predict_model.main import predict


def get_new_event(prompt):
    output = predict(prompt)

    if (output["name"] is None or output["start_time"] is None or output["end_time"] is None):
        return
        
    Event.objects.create(name=output["name"], start_time=output["start_time"], end_time=output["end_time"])
