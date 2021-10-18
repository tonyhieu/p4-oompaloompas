onEvent("button1", "click", function(event) {
    console.log("button1 clicked!");
    var str = getText("text_input1");
    var i = 0;
    var out = 0;
    while ((i < str.length)) {
        if (str[i] == "a") {
            out = out + 1;
        } else if ((str[i] == "e")) {
            out = out + 1;
        } else if ((str[i] == "i")) {
            out = out + 1;
        } else if ((str[i] == "o")) {
            out = out + 1;
        } else if ((str[i] == "u")) {
            out = out + 1;
        }
        i = i + 1;
    }
    setText("label2", out);
});
