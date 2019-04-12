<script>

// Global Section
var vars = [];

var editor = ace.edit("code-area");
editor.setTheme("ace/theme/xcode");
document.getElementById('code-area').style.fontSize = '18px';
editor.session.setMode("ace/mode/python");

var script = "";
var it = "";
var developer = "";
var desc = "";
var n = "";
var idesc = "";
var opt = "";

//End Global Section

// Replaces all instances of the given substring.
String.prototype.replaceAll = function(strTarget, strSubString) {
    var strText = this;
    var intIndexOfMatch = strText.indexOf(strTarget);

    // Keep looping while an instance of the target string
    // still exists in the string.
    while (intIndexOfMatch != -1) {
        // Relace out the current instance.
        strText = strText.replace(strTarget, strSubString)

        // Get the index of any next matching substring.
        intIndexOfMatch = strText.indexOf(strTarget);
    }

    // Return the updated string with ALL the target strings
    // replaced out with the new substring.
    return (strText);
}

function getModule(id) {
    var url = "/program/api-mod/module/" + id + "/?username=root&api_key=4221de0b86f9076aa4f319bddc52362508b2dee4";
    $.get(url, function(data, status) {
        script = data.SubstitutedCode.split("%%%")[0];
        it = data.InputType.split(",");
        var front = generateCode(data);
        $(".modal #module-label").text(data.title);
        $(".modal #module-body").html(front);
        for (var i = vars.length - 1; i >= 0; i--) {
            $(".variables").html(
                $(".variables").html() + "<option value='" + vars[i] + "'>" + vars[i] + "</option>");
        };
    });

}

function generateCode(obj) {
    //GET object data
    developer = obj.developer;
    desc = obj.description;
    n = obj.NumberOfInputs;
    idesc = obj.InputDescription.split(",");
    opt = obj.Optional.split(",");

    // Render frontend
    var modal_body = "";

    for (var i = 0; i < n; i++) {
        if (it[i] === "0") {

            modal_body += "<label>" + idesc[i] + "</label><br>\n<input type='text' class='form-control' placeholder='" + idesc[i] + "' id='params" + i + "'>";
        } else if (it[i] === "1") {
            modal_body += "<label>" + idesc[i] + "</label><br>\n<select class='form-control variables' id='params" + i + "'><option value='' selected>Choose a variable...</option></select>";
        } else if (it[i] === "2") {
            modal_body += "\n<label>" + idesc[i] + "</label><br>\n"
            modal_body += "<div class='form-check form-check-inline'>\n<input class='form-check-input' type='radio' name='radioStore' onclick='show(1,2," + i + ");'>\n<label class='form-check-label'>Select Variable</label>\n</div><select class='form-control variables choice' id='params" + i + "1' name='params" + i + "'><option value='' selected>Choose a variable...</option></select><br>";
            modal_body += "<div class='form-check form-check-inline'>\n<input class='form-check-input' type='radio' name='radioStore' onclick='show(2,1," + i + ");'>\n<label class='form-check-label'>Enter String or number</label>\n</div><input type=text class='form-control choice' placeholder='" + idesc[i] + "' id='params" + i + "2' name='params" + i + "'><br>";
        } else if (it[i] === "3") {
            modal_body += "\n<label>" + idesc[i] + "</label><br>\n"
            modal_body += "<div class='form-check form-check-inline'>\n<input class='form-check-input' type='radio' name='radioStore' onclick='show(1,2," + i + ");'>\n<label class='form-check-label'>Select Variable</label>\n</div><select class='form-control variables choice' id='params" + i + "1' name='params" + i + "'><option value='' selected>Choose a variable...</option></select><br>";
            modal_body += "<div class='form-check form-check-inline'>\n<input class='form-check-input' type='radio' name='radioStore' onclick='show(2,1," + i + ");'>\n<label class='form-check-label'>Enter String or number</label>\n</div><input type=text class='form-control choice' placeholder='" + idesc[i] + "' id='params" + i + "2' name='params" + i + "'><br>";
            modal_body += "<select class='form-control' id='params" + i + "3'><option value='' selected>Choose an operator...</option></select>";
            modal_body += "<div class='form-check form-check-inline'>\n<input class='form-check-input' type='radio' name='radioStore' onclick='show(4,5," + i + ");'>\n<label class='form-check-label'>Select Variable</label>\n</div><select class='form-control variables choice' id='params" + i + "4' name='params" + i + "'><option value='' selected>Choose a variable...</option></select><br>";
            modal_body += "<div class='form-check form-check-inline'>\n<input class='form-check-input' type='radio' name='radioStore' onclick='show(5,4," + i + ");'>\n<label class='form-check-label'>Enter String or number</label>\n</div><input type=text class='form-control choice' placeholder='" + idesc[i] + "' id='params" + i + "5' name='params" + i + "'><br>";
        } else {}
    }

    modal_body += "<button class='btn btn-raised btn-bg-indigo' onclick='addCode();' data-dismiss='modal'><i class='fas fa-plus'></i>&nbsp;Add Code</button>";
    return modal_body;
}

// Create logic substitute params
function getParams(sc, it) {
    for (var i = 0; i < it.length; i++) {
        if (it[i] === "2") {
            var p;
            if (document.getElementById("params" + i + "1").value !== "") {
                p = document.getElementById("params" + i + "1").value;
            } else if (document.getElementById("params" + i + "2").value !== "") {
                p = document.getElementById("params" + i + "2").value;
                if (opt[i] === "1" && !isNumericOrNot(p)) {
                    p = escapeDoubleQuotes(p);
                    p = escapeSingleQuotes(p);
                    p = "\"" + p + "\"";
                }
            } else {
                if (opt[i] === 0)
                    p = "";
                else {
                    swal("Yikes!", idesc[i], "error");
                    return "";
                }
            }
        } else if (it[i] === "0") {
            if (document.getElementById("params" + i).value !== "") {
                p = document.getElementById("params" + i).value;
                if (opt[i] === "1" && !isNumericOrNot(p)) {
                    p = escapeDoubleQuotes(p);
                    p = escapeSingleQuotes(p);
                    p = "\"" + p + "\"";
                }
            } else {
                if (opt[i] === 0)
                    p = "";
                else {
                    swal("Yikes!", idesc[i], "error");
                    return "";
                }
            }
        }
        sc = sc.replaceAll("params[" + i + "]", p);
    }
    return sc;
}

function addCode() {
    editor.insert(getParams(script, it) + "\n");
}



</script>
