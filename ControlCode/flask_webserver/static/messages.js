{
    // * Create object on html subdirectory to register events on
    const eventSource = new EventSource('/alert-events');

    const messageBoxScroller = document.getElementById('messagesTextbox');
    const messageBox = document.getElementById('messageBoxContent');
    const clearButton = document.getElementById('clearTextboxButton');

    eventSource.onmessage = function(event) {
        // * Convert JSON text → JavaScript Object
        console.log(event);
        const jsonData = JSON.parse(event.data);

        messageBox.innerHTML += `\n<span>${jsonData.alert}</span>`;

        messageBoxScroller.scrollTop = messageBoxScroller.scrollHeight;
    }

    // let i = 1;
    // function addMessage () {
    //     // let currentHTML = messageBox.innerHTML;
    //     messageBox.innerHTML += `\n<span>text${i}</span>`; // + currentHTML;
    //     ++i;

    //     messageBoxScroller.scrollTop = messageBoxScroller.scrollHeight;
    // }

    // setInterval(addMessage, 3000);

    function clearMessages() {
        while(messageBox.firstChild){
            messageBox.removeChild(messageBox.firstChild);
        }
    }

    clearButton.addEventListener("mouseup", clearMessages)
    clearButton.addEventListener("touchend", clearMessages)
}