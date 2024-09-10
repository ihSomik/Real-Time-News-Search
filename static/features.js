document.addEventListener("DOMContentLoaded", function () {
    const voiceSearchBtn = document.getElementById('voiceSearchBtn');
    const queryInput = document.getElementById('query');
    const statusDiv = document.getElementById('status'); // Status indicator

    voiceSearchBtn.addEventListener('click', function () {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'en-US';
        recognition.start();

        statusDiv.innerHTML = "Listening...";
        voiceSearchBtn.innerText = "Listening...";

        recognition.onresult = function (event) {
            queryInput.value = event.results[0][0].transcript;
            statusDiv.innerHTML = "Searching...";
            document.forms[0].submit();
        };

        recognition.onend = function () {
            voiceSearchBtn.innerText = "🎙️ Voice Search";
            setTimeout(() => statusDiv.innerHTML = "", 2000); // Hide status after 2 seconds
        };
    });

    // Typing effect for the heading
    const heading = document.getElementById('searchHeading');
    let headingText = "Search For News";
    let index = 0;

    function typeHeading() {
        if (index < headingText.length) {
            heading.innerHTML += headingText.charAt(index);
            index++;
            setTimeout(typeHeading, 100);
        }
    }

    // Clear the heading before typing effect
    heading.innerHTML = "";
    typeHeading();
});
