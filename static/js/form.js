var currentTab = 1; // Current tab is set to be the first tab (0)
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
  Egypt: { goals_for: 0, goals_against: 0 },
  Russia: { goals_for: 0, goals_against: 0 },
  "Saudi Arabia": { goals_for: 0, goals_against: 0 },
  Uruguay: { goals_for: 0, goals_against: 0 },
  Morocco: { goals_for: 0, goals_against: 0 },
  Iran: { goals_for: 0, goals_against: 0 },
  Portugal: { goals_for: 0, goals_against: 0 },
  Spain: { goals_for: 0, goals_against: 0 },
  France: { goals_for: 0, goals_against: 0 },
  Australia: { goals_for: 0, goals_against: 0 },
  Peru: { goals_for: 0, goals_against: 0 },
  Denmark: { goals_for: 0, goals_against: 0 },
  Argentina: { goals_for: 0, goals_against: 0 },
  Iceland: { goals_for: 0, goals_against: 0 },
  Croatia: { goals_for: 0, goals_against: 0 },
  Nigeria: { goals_for: 0, goals_against: 0 },
  Serbia: { goals_for: 0, goals_against: 0 },
  Brazil: { goals_for: 0, goals_against: 0 },
  "Costa Rica": { goals_for: 0, goals_against: 0 },
  Switzerland: { goals_for: 0, goals_against: 0 },
  Germany: { goals_for: 0, goals_against: 0 },
  Mexico: { goals_for: 0, goals_against: 0 },
  Sweden: { goals_for: 0, goals_against: 0 },
  "South Korea": { goals_for: 0, goals_against: 0 },
  Belgium: { goals_for: 0, goals_against: 0 },
  Panama: { goals_for: 0, goals_against: 0 },
  Tunisia: { goals_for: 0, goals_against: 0 },
  England: { goals_for: 0, goals_against: 0 },
  Colombia: { goals_for: 0, goals_against: 0 },
  Japan: { goals_for: 0, goals_against: 0 },
  Poland: { goals_for: 0, goals_against: 0 },
  Senegal: { goals_for: 0, goals_against: 0 }
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
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
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
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n);
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (!validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  if (currentTab === 1) getGroupStandings();
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x,
    y,
    i,
    valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "" || !y[i].checkValidity()) {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    } else {
      y[i].className = y[i].className.replace("invalid", "");
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i,
    x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
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
    console.log(home_team);
    console.log(away_team);
    goals_per_team[home_team].goals_for += home_score;
    goals_per_team[away_team].goals_for += away_score;
    goals_per_team[home_team].goals_against += away_score;
    goals_per_team[away_team].goals_against += home_score;
    if (home_score > away_score) {
      groups[group][home_team] += 3;
    } else if (home_score < away_score) {
      groups[group][away_team] += 3;
    } else {
      groups[group][home_team] += 1;
      groups[group][away_team] += 1;
    }
  }
  console.log(goals_per_team);
  console.log(groups);
}
