var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the crurrent tab

var inputs = [
  "a1h",
  "a1a",
  "a2h",
  "a2a",
  "a3h",
  "a3a",
  "a4h",
  "a4a",
  "a5h",
  "a5a",
  "a6h",
  "a6a",
  "b1h",
  "b1a",
  "b2h",
  "b2a",
  "b3h",
  "b3a",
  "b4h",
  "b4a",
  "b5h",
  "b5a",
  "b6h",
  "b6a",
  "c1h",
  "c1a",
  "c2h",
  "c2a",
  "c3h",
  "c3a",
  "c4h",
  "c4a",
  "c5h",
  "c5a",
  "c6h",
  "c6a",
  "d1h",
  "d1a",
  "d2h",
  "d2a",
  "d3h",
  "d3a",
  "d4h",
  "d4a",
  "d5h",
  "d5a",
  "d6h",
  "d6a",
  "e1h",
  "e1a",
  "e2h",
  "e2a",
  "e3h",
  "e3a",
  "e4h",
  "e4a",
  "e5h",
  "e5a",
  "e6h",
  "e6a",
  "f1h",
  "f1a",
  "f2h",
  "f2a",
  "f3h",
  "f3a",
  "f4h",
  "f4a",
  "f5h",
  "f5a",
  "f6h",
  "f6a",
  "g1h",
  "g1a",
  "g2h",
  "g2a",
  "g3h",
  "g3a",
  "g4h",
  "g4a",
  "g5h",
  "g5a",
  "g6h",
  "g6a",
  "h1h",
  "h1a",
  "h2h",
  "h2a",
  "h3h",
  "h3a",
  "h4h",
  "h4a",
  "h5h",
  "h5a",
  "h6h",
  "h6a"
];

var goals_per_team = {
  Egypt: { for: 0, against: 0 },
  Russia: { for: 0, against: 0 },
  "Saudi Arabia": { for: 0, against: 0 },
  Uruguay: { for: 0, against: 0 },
  Morocco: { for: 0, against: 0 },
  Iran: { for: 0, against: 0 },
  Portugal: { for: 0, against: 0 },
  Spain: { for: 0, against: 0 },
  France: { for: 0, against: 0 },
  Australia: { for: 0, against: 0 },
  Peru: { for: 0, against: 0 },
  Denmark: { for: 0, against: 0 },
  Argentina: { for: 0, against: 0 },
  Iceland: { for: 0, against: 0 },
  Croatia: { for: 0, against: 0 },
  Nigeria: { for: 0, against: 0 },
  Serbia: { for: 0, against: 0 },
  Brazil: { for: 0, against: 0 },
  "Costa Rica": { for: 0, against: 0 },
  Switzerland: { for: 0, against: 0 },
  Germany: { for: 0, against: 0 },
  Mexico: { for: 0, against: 0 },
  Sweden: { for: 0, against: 0 },
  "South Korea": { for: 0, against: 0 },
  Belgium: { for: 0, against: 0 },
  Panama: { for: 0, against: 0 },
  Tunisia: { for: 0, against: 0 },
  England: { for: 0, against: 0 },
  Colombia: { for: 0, against: 0 },
  Japan: { for: 0, against: 0 },
  Poland: { for: 0, against: 0 },
  Senegal: { for: 0, against: 0 }
};

var groupA = { Egypt: 0, Russia: 0, "Saudi Arabia": 0, Uruguay: 0 };
var groupB = { Iran: 0, Morocco: 0, Portugal: 0, Spain: 0 };
var groupC = { Australia: 0, Denmark: 0, France: 0, Peru: 0 };
var groupD = { Argentina: 0, Croatia: 0, Iceland: 0, Nigeria: 0 };
var groupE = { Brazil: 0, Switzerland: 0, "Costa Rica": 0, Serbia: 0 };
var groupF = { Germany: 0, "South Korea": 0, Mexico: 0, Sweden: 0 };
var groupG = { Belgium: 0, England: 0, Panama: 0, Tunisia: 0 };
var groupH = { Colombia: 0, Japan: 0, Poland: 0, Senegal: 0 };

var groups = {
  a: groupA,
  b: groupB,
  c: groupC,
  d: groupD,
  e: groupE,
  f: groupF,
  g: groupG,
  h: groupH
};

function showTab(n) {
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";

  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == x.length - 1) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }

  fixStepIndicator(n);
}

function nextPrev(n) {
  var x = document.getElementsByClassName("tab");

  if (n == 1 && !validateForm()) return false;

  x[currentTab].style.display = "none";
  if (currentTab === 1 && n == 1) {
    standings = getGroupStandings();
    updateGroupStandings(standings);
    updateRound16(standings);
  } else if (currentTab === 3 && n == 1) {
    updateQuarters();
  } else if (currentTab === 4 && n == 1) {
    updateSemis();
  } else if (currentTab === 5 && n == 1) {
    updateFinals();
  }

  currentTab = currentTab + n;
  if (currentTab >= x.length) {
    document.getElementById("regForm").submit();
    return false;
  }

  showTab(currentTab);
}

function validateForm() {
  var x,
    y,
    i,
    valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].querySelectorAll("input,select");

  for (i = 0; i < y.length; i++) {
    if (y[i].value == "" || !y[i].checkValidity()) {
      y[i].className += " invalid";
      valid = false;
    } else {
      y[i].className = y[i].className.replace("invalid", "");
    }
  }

  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid;
}

function fixStepIndicator(n) {
  var i,
    x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }

  x[n].className += " active";
}

function getGroupStandings() {
  for (var i = 0; i < inputs.length; i += 2) {
    group = inputs[i][0];
    home = inputs[i];
    away = inputs[i + 1];

    home_score = parseInt($('input[name="' + home + '"]').val());
    home_team = $('label[for="' + home + '"]').text();

    away_score = parseInt($('input[name="' + away + '"]').val());
    away_team = $('label[for="' + away + '"]').text();

    goals_per_team[home_team].for += home_score;
    goals_per_team[away_team].for += away_score;
    goals_per_team[home_team].against += away_score;
    goals_per_team[away_team].against += home_score;

    if (home_score > away_score) {
      groups[group][home_team] += 3;
    } else if (home_score < away_score) {
      groups[group][away_team] += 3;
    } else {
      groups[group][home_team] += 1;
      groups[group][away_team] += 1;
    }
  }

  Object.keys(goals_per_team).forEach(team => {
    goals_per_team[team].diff =
      goals_per_team[team].for - goals_per_team[team].against;
  });

  var standings = {};
  var group_letters = ["a", "b", "c", "d", "e", "f", "g", "h"];

  group_letters.forEach(curr => {
    var currGroup = groups[curr];

    sorted = Object.keys(currGroup).sort(function(a, b) {
      return (
        currGroup[b] - currGroup[a] ||
        goals_per_team[b].diff - goals_per_team[a].diff ||
        goals_per_team[b].for - goals_per_team[a].for
      );
    });

    standings[curr + "1"] = sorted[0];
    standings[curr + "2"] = sorted[1];
  });

  console.log(standings);
  return standings;
}

function appendOptions(item, values) {
  $(item)
    .find("option")
    .remove()
    .end()
    .append(
      '<option disabled selected value style="display: none">Choose a Team</option>'
    );
  values.forEach(value => {
    $(item).append(
      $("<option></option>")
        .attr("value", value)
        .text(value)
    );
  });
}

function appendOption(item, value) {
  $("#" + item)
    .find("option")
    .remove();
  $("#" + item).append(
    $("<option></option>")
      .attr("value", value)
      .text(value)
  );
  $("input[name=" + item + "]").val(value);
}

function updateGroupStandings(standings) {
  appendOption("a1", standings.a1);
  appendOption("a2", standings.a2);
  appendOption("b1", standings.b1);
  appendOption("b2", standings.b2);
  appendOption("c1", standings.c1);
  appendOption("c2", standings.c2);
  appendOption("d1", standings.d1);
  appendOption("d2", standings.d2);
  appendOption("e1", standings.e1);
  appendOption("e2", standings.e2);
  appendOption("f1", standings.f1);
  appendOption("f2", standings.f2);
  appendOption("g1", standings.g1);
  appendOption("g2", standings.g2);
  appendOption("h1", standings.h1);
  appendOption("h2", standings.h2);
}

function updateRound16(standings) {
  appendOptions("#r1", [standings.a1, standings.b2]);
  appendOptions("#r2", [standings.c1, standings.d2]);
  appendOptions("#r3", [standings.e1, standings.f2]);
  appendOptions("#r4", [standings.g1, standings.h2]);
  appendOptions("#r5", [standings.b1, standings.a2]);
  appendOptions("#r6", [standings.d1, standings.c2]);
  appendOptions("#r7", [standings.f1, standings.e2]);
  appendOptions("#r8", [standings.h1, standings.g2]);
}

function getSelected(id) {
  return $(id)
    .children("option")
    .filter(":selected")
    .text();
}

function notSelected(id) {
  return $(id)
    .children("option")
    .filter(":not(:selected):not(:disabled)")
    .text();
}

function updateQuarters() {
  var r1 = getSelected("#r1");
  var r2 = getSelected("#r2");
  var r3 = getSelected("#r3");
  var r4 = getSelected("#r4");
  var r5 = getSelected("#r5");
  var r6 = getSelected("#r6");
  var r7 = getSelected("#r7");
  var r8 = getSelected("#r8");

  appendOptions("#q1", [r1, r2]);
  appendOptions("#q2", [r3, r4]);
  appendOptions("#q3", [r5, r6]);
  appendOptions("#q4", [r7, r8]);
}

function updateSemis() {
  var q1 = getSelected("#q1");
  var q2 = getSelected("#q2");
  var q3 = getSelected("#q3");
  var q4 = getSelected("#q4");

  appendOptions("#s1", [q1, q2]);
  appendOptions("#s2", [q3, q4]);
}

function updateFinals() {
  var s1 = getSelected("#s1");
  var s2 = getSelected("#s2");
  var t1 = notSelected("#s1");
  var t2 = notSelected("#s2");

  appendOptions("#final", [s1, s2]);
  appendOptions("#third", [t1, t2]);
}
