document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('inputForm');
    // const loading = document.getElementById('loading');

    form.addEventListener('submit', function () {
        // loading.style.display = 'block';
        event.preventDefault();
        var formData = $('#inputForm').serialize();
        console.log(formData);

        $.ajax({
            type: 'POST',
            url: '/postprompt/',
            data: formData,
            success: function (response) {
                // Handle the response (e.g., show a success message)
                console.log('Form submitted successfully');
            },
            error: function (xhr, status, error) {
                // Handle errors (e.g., show an error message)
                console.error('Error:', error);
            }
        });
        // setTimeout(function() {
        //   form.submit();
        // }, 3000);
    });

    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: [
            <!-- { -->
            <!--   "title": "Team Meeting", -->
            <!--   "start": "2023-10-21T10:00:00", -->
            <!--   "end": "2023-10-21T11:00:00" -->
            <!-- }, -->
            <!-- { -->
            <!--   "title": "Lunch Break", -->
            <!--   "start": "2023-10-21T12:30:00", -->
            <!--   "end": "2023-10-21T13:30:00" -->
            <!-- }, -->
        ]
    });
    document.getElementById('monthViewBtn').addEventListener('click', function () {
        calendar.changeView('dayGridMonth');
    });

    document.getElementById('weekViewBtn').addEventListener('click', function () {
        calendar.changeView('timeGridWeek');
    });

    const apiUrl = 'http://localhost:8000/getevents';
    calendar.on('dateClick', function (info) {
        fetch(apiUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json(); // Parse the response as JSON
            })
            .then(data => {

                // Remove existing event sources (clear the calendar)
                calendar.getEventSources().forEach(function (eventSource) {
                    eventSource.remove();
                });

                // Add the new event data as an event source
                calendar.addEventSource(data);

                // Render the updated calendar
                calendar.render();
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    });
    calendar.render();


});
