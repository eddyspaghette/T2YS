from frontend.schedule.models import Event
from predict_model.main import predict


def get_new_event(prompt):
    output = predict(prompt)
    Event.objects.create(name=output["name"], start_time=output["start_time"], end_time=output["end_time"])
