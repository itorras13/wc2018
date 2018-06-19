$(function() {
  $(".nav-link").on("click", function() {
    if ($(".navbar-toggler").css("display") != "none") {
      $(".navbar-toggler").trigger("click");
    }
  });
});

function filterNames() {
  var name = document.getElementById("standingsName").value;
  var body = document.getElementById("standingsBody");
  var rows = body.getElementsByTagName("tr");
  for (let idx = 0; idx < rows.length; idx++) {
    const row = rows[idx];
    const currName = row.getElementsByTagName("td")[1].id;
    if (name == null) {
      row.style.display = "none";
    } else if (currName.toLowerCase().includes(name.toLowerCase())) {
      row.style.display = "";
    } else {
      row.style.display = "none";
    }
  }
}
