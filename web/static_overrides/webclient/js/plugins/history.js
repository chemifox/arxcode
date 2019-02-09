/*
 *
 * Evennia Webclient Command History plugin
 *
 */
let history_plugin = (function () {

    // Manage history for input line
    var history_max = 21;
    var history = new Array();
    var history_pos = 0;

    history[0] = ''; // the very latest input is empty for new entry.

    //
    // move back in the history
    var back = function () {
        // step backwards in history stack
        history_pos = Math.min(++history_pos, history.length - 1);
        return history[history.length - 1 - history_pos];
    }

    //
    // move forward in the history
    var fwd = function () {
        // step forwards in history stack
        history_pos = Math.max(--history_pos, 0);
        return history[history.length - 1 - history_pos];
    };

    //
    // add a new history line
    var add = function (input) {
        // add a new entry to history, don't repeat latest
        if (input && input != history[history.length-2]) {
            if (history.length >= history_max) {
                history.shift(); // kill oldest entry
            }
            history[history.length-1] = input;
            history[history.length] = '';
        }
        // reset the position to the last history entry
        history_pos = 0;
    }

     var end = function () {
        // move to the end of the history stack
        history_pos = 0;
        return history[history.length -1];
    }

    var scratch = function (input) {
        // Put the input into the last history entry (which is normally empty)
        // without making the array larger as with add.
        // Allows for in-progress editing to be saved.
        history[history.length-1] = input;
    }


    // Public

    //
    // Handle up arrow and down arrow events.
    var onKeydown = function(event) {
        var code = event.which;
        var history_entry = null;
        var inputfield = $("#inputfield");

        if (code === 90 && event.ctrlKey) { // Arrow up
            history_entry = back();
        }
        else if (code === 89 && event.ctrlKey) { // Arrow down
            history_entry = fwd();
        }

    if (history_entry !== null) {
        // Doing a history navigation; replace the text in the input.
        inputfield.val(history_entry);
        event.preventDefault();
    }
    else {
        // Save the current contents of the input to the history scratch area.
        setTimeout(function () {
            // Need to wait until after the key-up to capture the value.
            input_history.scratch(inputfield.val());
            input_history.end();
        }, 0)
    }

    //
    // Listen for onSend lines to add to history
    var onSend = function (line) {
        add(line);
        return null; // we are not returning an altered input line
    }

    //
    // Init function
    var init = function () {
        console.log('History Plugin Initialized.');
    } 

    return {
        init: init,
        onKeydown: onKeydown,
        onSend: onSend,
        back: back,
        fwd: fwd,
        add: add,
        end: end,
        scratch: scratch
    }
}
plugin_handler.add('history', history_plugin);
