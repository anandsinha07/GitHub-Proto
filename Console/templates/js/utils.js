<script type="text/javascript">
	var tabs = [];
	var tabspace = 0;
	function isNumericOrNot(str) {
	    var patt = new RegExp("[0-9]");
	    var res = patt.test(str);
	    return res;
	}
	function escapeDoubleQuotes(str) {
	  return str.replace(/\\([\s\S])|(")/g,"\\$1$2");
	}
	function escapeSingleQuotes(str) {
	  return str.replace(/\\([\s\S])|(')/g,"\\$1$2");
	}
	function show(p1, p2, type)
	{
	  $("#params"+type+""+p1).css("display", "block");
	  $("#params"+type+""+p2).css("display", "none");
	}

	function refresh()
	{
	  swal("This action will clear your code and all stored variables.\nDo you wish to continue?\n", {
	    buttons: {
	      cancel: "No",
	      ok: {
	        text: "Yes",
	        value: "confirm",
	      },
	    },
	    icon: "warning",
	    dangerMode:true,
	  })
	  .then((value) => {
	    switch (value) {
	       case "confirm":
	          $.post("../php/refresh.php",
	          {},
	          function(data, status){
	              if(status === "success") {
	                editor.selectAll();
	                editor.removeToLineEnd();
	                tabspace = 0;
	                tabs = [];

	                swal("Success","Refresh successful", "success");     
	              }
	              else {
	                swal("Something went wrong. Please try again later.", {icon:"warning",});
	              }
	          });
	        break;
	   
	      default:
	        swal("Refresh was cancelled by user!", {icon:"info",});
	        break;
	    }
	  });
	}

	function share() {
	  var user = firebase.auth().currentUser;
	  var email;
	  if (user != null) {
	    email = user.email;
	  }
	  $.post("../php/sendMail.php",
	  {
	    recipient: document.getElementById("modalEmail").value,
	    title: document.getElementById("modalTitle").value,
	    sender: email,
	    code: editor.getValue()
	  },
	  function(data, status){
	      if(status === "success") {
	        swal("Success","Code shared successfully", "success");     
	      }
	      else {
	        swal("Something went wrong. Please try again later.", {icon:"warning",});
	      }
	  });

	}

	function endBlock()
	{
	  if (tabs[tabs.length-1] !== "el") {
	    tabs.pop();
	    tabspace--;
	    if (tabspace === 0) {
	      document.getElementById("btn-endBlock").style.display = "none";
	    }
	    else {
	      if (tabs[tabs.length-1] ==='i') {
	        document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End If Block";
	      }
	      else if (tabs[tabs.length-1] === 'f') {
	        document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End For Block";
	      }
	      else if (tabs[tabs.length-1] === 'w') {
	        document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End While Block";
	      }
	      else if (tabs[tabs.length-1] === 'fun') {
	        document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End Function Definition";
	      }
	      else if (tabs[tabs.length-1] === 'class') {
	        document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End Class Definition";
	      }
	      else {
	        swal("Something went wrong!", {icon: "info",});
	      }
	    }
	  }
	  else {
	    swal("Cannot end elif without else!", {icon: "info"});
	  }
	}

	function indent(param)
	{
	  var t = "";
	  for (var i = 0; i < param; i++) {
	    t += "\t";
	  }
	  return t;
	}

	function updateIndent(ch, output)
	{
	  if (ch === 'i') {
	    tabs.push('i');
	    tabspace++;
	    document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End If Block";
	  }
	  else if (ch === 'el') {
	    if (tabs[tabs.length-1] === 'i' || tabs[tabs.length-1] === 'el') {
	      tabs.pop();
	      tabs.push('el');
	    }
	    else {
	      swal("'elif' block without 'if' block!", {icon: "warning",});
	      return;
	    }
	  }
	  else if (ch === 'e') {
	    if (tabs[tabs.length-1] === 'i' || tabs[tabs.length-1] === 'el') {
	      tabs.pop();
	      tabs.push('e');
	    }
	    else {
	      swal("'else' block without 'if' block!", {icon: "warning",});
	      return;
	    }
	  }
	  else if (ch === 'f') {
	    tabs.push('f');
	    tabspace++;
	    document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End For Block";
	  }
	  else if (ch === 'w') {
	    tabs.push('w');
	    tabspace++;
	    document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End While Block";
	  }
	  else if (ch === "fun") {
	  	tabs.push("fun");
	  	tabspace++;
	    document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End Function Definition";
	  }
	  else if (ch === "class") {
	  	tabs.push("class");
	  	tabspace++;
	    document.getElementById("btn-endBlock").innerHTML = "<i class='fas fa-square'></i>&nbsp;End Class Definition";
	  }
	  else {
	    swal("Something went wrong", {icon: "warning",});
	    return;
	  }
	  document.getElementById("btn-endBlock").style.display = "inline-block";
	  editor.insert(output);
	}

</script>
