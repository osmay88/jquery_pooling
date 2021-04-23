/// <reference path="../lib/jquery-3.6.0.js" />

$(() => {
    var count = 0;

    const logInput = (text) => {
        const baseText = $("#log-panel").val();
        $("#log-panel").val(baseText + "\n" + JSON.stringify(text));
    };

    const doPoll = (task_id) => {
        $.ajax('/pooling', {
            data: JSON.stringify({ task_id: task_id }),
            contentType: 'application/json',
            type: 'POST',
        }).then((response, statusText, xhr) => {
            if (response.status === "SUCCESS") {
                $("#submit_button").prop("disabled", false);
                logInput(response);
                logInput("==============> Pooling has finish <================")
                return;
            }
            logInput(response);
            setTimeout(doPoll, 5000, task_id);
        }).catch((error) => {
            $("#submit_button").prop("disabled", false);
            logInput(error);
        });
    };

    const submitData = (url, data) => {
        $.post({
            url,
            data,
        }).then((response) => {
            logInput("==============> Pooling has started <================");
            $("#submit_button").prop("disabled", true);
            doPoll(response.task_id);
        }).catch((error) => {
            console.log(error);
        });

    };

    $("#submit_button").on("click", (event) => {
        event.preventDefault();
        submitData("/", {});
    });
});
